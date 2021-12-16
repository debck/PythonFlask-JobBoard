from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
<<<<<<< HEAD
	return render_template('index.html')
=======
  return render_template('index.html')
>>>>>>> origin/module2-solution
