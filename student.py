from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'suvendu'
app.config['MYSQL_PASSWORD'] = 'suvendu123'
app.config['MYSQL_DB'] = 'student_enroll_system'

mysql = MySQL(app)


@app.route('/all', methods=['GET'])
def get_all():
    cur = mysql.connection.cursor()
    cur.execute('SELECT *FROM student')
    result = cur.fetchall()
    return jsonify(result)


@app.route('/add', methods=['POST'])
def create():
    STUDENT_NAME = request.json['STUDENT_NAME']
    STUDENT_EMAIL = request.json['STUDENT_EMAIL']
    STUDENT_MOBILE = request.json['STUDENT_MOBILE']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO student (STUDENT_NAME, STUDENT_EMAIL, STUDENT_MOBILE) VALUES (%s,%s,%s)',
                (STUDENT_NAME, STUDENT_EMAIL, STUDENT_MOBILE))
    mysql.connection.commit()
    return jsonify({'message':'add successfully'})

@app.route('/update/<int:ROLL_NO>',methods=['PUT'])
def update(ROLL_NO):
    STUDENT_NAME = request.json['STUDENT_NAME']
    STUDENT_EMAIL = request.json['STUDENT_EMAIL']
    STUDENT_MOBILE = request.json['STUDENT_MOBILE']
    cur = mysql.connection.cursor()
    cur.execute('UPDATE student SET STUDENT_NAME = %s, STUDENT_EMAIL = %s, STUDENT_MOBILE = %s WHERE ROLL_NO = %s',
                (ROLL_NO,STUDENT_NAME, STUDENT_EMAIL, STUDENT_MOBILE))
    mysql.connection.commit()
    return jsonify({'message':'update successfully'})


@app.route('/delete/<int:ROLL_NO>', methods=['DELETE'])
def delete(ROLL_NO):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM student WHERE ROLL_NO = %s', (ROLL_NO,))
    mysql.connection.commit()
    return jsonify({'message': ' deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)
