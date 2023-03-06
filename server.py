from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/submit_data', methods=['POST'])
def submit_data():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['fav_framework'] = request.form['fav_framework']
    session['desired_field'] = request.form['desired_field']
    session['desired_job'] = request.form['desired_job']
    session['comments'] = request.form['comments']
    print(request.form)
    return redirect('/show')   

@app.route('/show')
def display_data():
    return render_template('result.html') 

if __name__ == "__main__":
    app.run(debug=True,port=5001)