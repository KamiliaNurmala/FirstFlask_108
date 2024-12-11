from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name');
    age = request.form.get('age');
    return f"<h2>Hello, {name}!</h2><p>Umur kamu sekarang {age}</p>"

if __name__ == '__main__':
    app.run(debug=True)
