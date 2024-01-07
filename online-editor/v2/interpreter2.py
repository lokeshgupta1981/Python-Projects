from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
  return render_template('index.html')


clients = {}


def run_script(code, sid):

  print(code)
  process = subprocess.Popen(['python', '-u', '-c', code],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             text=True, bufsize=1)
  clients[sid] = process

  output = ""
  while True:
    char = process.stdout.read(1)
    if char == '' and process.poll() is not None:
      break
    if char != '\n':
      output += char
    else:
      socketio.emit('output', {'data': output}, room=sid)
      output = ""

  if output:
    print(output)
    socketio.emit('output', {'data': output}, room=sid)

  process.stdout.close()
  del clients[sid]


@socketio.on('execute_code')
def handle_execute_code(json):
  sid = request.sid
  threading.Thread(target=run_script, args=(json['code'], sid)).start()


@socketio.on('send_input')
def handle_input(json):
  sid = request.sid
  if sid in clients:
    clients[sid].stdin.write(json['data'] + '\n')
    clients[sid].stdin.flush()


@socketio.on('disconnect')
def handle_disconnect():
  sid = request.sid
  if sid in clients and clients[sid].poll() is None:
    clients[sid].terminate()


if __name__ == '__main__':
  socketio.run(app, debug=True, host='0.0.0.0', allow_unsafe_werkzeug=True)
