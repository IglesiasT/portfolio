from flask import Flask, render_template

app = Flask(__name__)
#el video de mundo python es muy bueno guiarme con eso
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about-me')
def about_me():
    return render_template("about-me.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
