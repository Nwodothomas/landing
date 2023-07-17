from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doc/')
def view_documentation():
    return render_template('doc/doc.html')

if __name__ == '__main__':
    app.run(debug=True)
