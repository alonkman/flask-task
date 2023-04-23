from flask import Flask, render_template


api = Flask(__name__)

@api.route("/")
def home():
    return render_template('index.html')

@api.route("/about.html")
def about():
    return render_template('about.html')

@api.route("/contact.html")
def contact():
    return render_template('contact.html')


if __name__=="__main__" :
    api.run(debug=True)
