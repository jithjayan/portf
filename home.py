from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect('data.db')
try:
    con.execute("create table msg(name text,email email,msg text)")
except:
    pass
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template ("index.html")

@app.route('/submit-contact',methods=['GET','POST'])
def submit_contact():

    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        msg=request.form.get('msg')
        print(name,email,msg)
        con=sqlite3.connect('data.db')
        con.execute("insert into msg(name,email,msg)values(?,?,?)",(name,email,msg))
        con.commit()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)