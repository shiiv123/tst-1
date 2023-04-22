from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def index():
  flash("what's your name?")
  return render_template('home.html')
  
@app.route("/greet", methods=["POST", "GET"])
def greet():
  flash("Hi " + str(request.form['name_input']) + ", greet to see it")
  return render_template('home.html')

if __name__ == "__main__" :
  app.run(host='0.0.0.0', debug=True)