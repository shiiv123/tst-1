from flask import Flask, render_template

app = Flask(__name__)
Jobs = [
  {'id': 1,
   'title': 'data anlyst',
   'location': 'bangalore',
   'salary': 120000
  },
   {'id': 2,
   'title': 'data scientist',
   'location': 'pune'
  },
 {'id': 3,
   'title': 'financial anlyst',
   'location': 'delhi'
  }
]

@app.route("/")
def hello_world():
 
  return render_template('home.html',jobs =Jobs, company = 'shiv')

if __name__ == "__main__" :
  app.run(host='0.0.0.0', debug=True)