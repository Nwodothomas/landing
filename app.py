from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs/')
def view_documentation():
    return render_template('docs/doc.html')

if __name__ == '__main__':
    app.run(debug=True)
