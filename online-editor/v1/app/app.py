from flask import Flask, request, abort
from flask_cors import CORS
import subprocess
import base64
import ast

app = Flask(__name__)
CORS(app)

# ALLOWED_ORIGIN = 'https://mywebsite.com'


# @app.before_request
# def check_origin():
#  if request.headers.get('Origin') != ALLOWED_ORIGIN:
#    abort(403)


# Prevent malicious code such as module installations
def contains_install_commands(code):
  keywords = ['pip', 'install', 'sys.executable', 'subprocess', 'os.system', 'Popen']
  try:
    parsed_code = ast.parse(code)
    for node in ast.walk(parsed_code):
      if isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id in keywords:
        return True
      if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
        for n in node.names:
          if n.name in ['os', 'subprocess']:
            return True
  except SyntaxError:
    return True
  return False


# The Flask App
@app.route('/run', methods=['POST'])
def run_code():
  encoded_code = request.json['code']
  try:
    decoded_code = base64.b64decode(encoded_code).decode('utf-8')

    # Security check for installation commands
    if contains_install_commands(decoded_code):
      return {'error': 'Installation of packages is not allowed'}, 403

    # Proceed with code execution if the check passes
    output = subprocess.run(['python', '-c', decoded_code], capture_output=True, text=True, timeout=5)
    if output.returncode != 0:
      return {'output': output.stdout, 'error': output.stderr}, 200
    return {'output': output.stdout}, 200

  except (base64.binascii.Error, UnicodeDecodeError) as e:
    return {'error': 'Invalid input: Unable to decode base64 string.'}, 400
  except subprocess.TimeoutExpired:
    return {'error': 'Execution Timeout: Code took longer than 5 seconds to execute.'}, 408
  except subprocess.SubprocessError as e:
    return {'error': f'Subprocess error: {str(e)}'}, 500
  except Exception as e:
    return {'error': f'Unknown error: {str(e)}'}, 500


# For now allow traffic from all hosts and set debugging on

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
