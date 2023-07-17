from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        content = file.read()
    return render_template_string(content)

@app.route('/docs/')
def view_documentation():
    with open('docs/doc.html', 'r') as file:
        content = file.read()
    return render_template_string(content)

if __name__ == '__main__':
    app.run(debug=True)
