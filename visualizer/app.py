# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import traceback
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json['code']
    try:
        # Redirect stdout to capture output
        old_stdout = sys.stdout
        sys.stdout = buffer = StringIO()

        # Execute the code
        exec(code)

        # Restore stdout
        sys.stdout = old_stdout
        output = buffer.getvalue()
    except Exception as e:
        output = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
    return jsonify({'output': output})

if __name__ == '__main__':
    from io import StringIO  # Import here to avoid affecting the global namespace
    app.run(debug=True)
