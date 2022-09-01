from flask import Flask,render_template,request,jsonify
import mysql.connector
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/student_data',methods=['POST'])
def student_data():
    s_name=request.form['student_name']
    s_roll_no=request.form['student_roll_no']
    s_sub1=request.form['student_sub1']
    s_sub2=request.form['student_sub2']
    s_sub3=request.form['student_sub3']

    print(f'Student Name = {s_name}')

    conn = mysql.connector.connect(host = 'localhost',database = 'may7',
                                        user = 'root',
                                        password = 'Yogesh@1996')

    cursor = conn.cursor()

    query = 'insert into student (name,roll_no,sub1,sub2,sub3) values(%s,%s,%s,%s,%s)'
    data = (s_name,s_roll_no,s_sub1,s_sub2,s_sub3)

    cursor.execute(query,data)

    conn.commit()
    conn.close()

    return jsonify(s_name,s_roll_no,s_sub1,s_sub2,s_sub3)

if __name__== '__main__':
    app.run(debug=True)