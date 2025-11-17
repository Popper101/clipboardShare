from flask import Flask, render_template
import pyperclip

app = Flask(__name__)

@app.route('/copy')
def copy_page():
    # Read clipboard data from the server
    clipboard_data = pyperclip.paste()
    return render_template('copy.html', clipboard_data=clipboard_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7878, debug=True)
