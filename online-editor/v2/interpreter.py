from flask import Flask
from flask_socketio import SocketIO, emit
import subprocess
import shlex
import threading
import queue

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Thread-safe queue to handle input/output of subprocess
io_queue = queue.Queue()


def execute_code(code):
  try:
    # Using Popen for subprocess to interact with stdin and stdout
    process = subprocess.Popen(shlex.split("python -c \"{}\"".format(code)),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    # Separate thread to handle output
    def process_output():
      while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
          break
        if output:
          socketio.emit('output', output.strip())
      rc = process.poll()
      socketio.emit('output', f'Process exited with code {rc}')

    threading.Thread(target=process_output).start()

    # Handling input from user
    while True:
      input_data = io_queue.get()
      if input_data == "__TERMINATE__":
        process.terminate()
        break
      process.stdin.write(input_data + '\n')
      process.stdin.flush()

  except Exception as e:
    socketio.emit('output', f'Error: {str(e)}')


@socketio.on('executeCode')
def handle_execute_code(data):
  code = data
  threading.Thread(target=execute_code, args=(code,)).start()


@socketio.on('continueExecution')
def handle_continue_execution(data):
  io_queue.put(data)


if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
