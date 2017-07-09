from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_result():
   name = request.form['name']
   comment = request.form['comment']
   location = request.form['location']
   language = request.form['language']

   return render_template('result.html', named = name, dojo = location, languaged = language, commented = comment)

app.run(debug=True) # run our server
