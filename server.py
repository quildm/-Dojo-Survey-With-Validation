from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_result():
  name = request.form['name']
  comment = request.form['comment']
  location = request.form['location']
  language = request.form['language']
  
  if len(request.form['name']) < 1:
    flash("Name field cannot be blank!")
  elif len(request.form['name']) > 120:
    flash("Too long!")
  else:
    flash("You are winner!")

  if len(request.form['comment']) < 1:
    flash('Comment cannot be blank', 'commentError')
  if len(request.form['comment']) > 120:
    flash('Comment is too long, no one will read this', 'commentError')

  return render_template('result.html', named = name, dojo = location, languaged = language, commented = comment)

app.run(debug=True) # run our server

