from flask import Flask, jsonify
import pymysql

host = "testing.cmabfri96m3t.us-west-2.rds.amazonaws.com"
user = "suvendu"
password = "suvendu@13972684"
dbname = "next_v3_pum_dashboard"

app = Flask(__name__)


def get_connection():
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=dbname,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# client wise user wise course details ..
@app.route('/course', methods=['GET'])
def course_details():
    sql = """SELECT * FROM client_wise_user_wise_course_details"""
    connection = get_connection()
    result = None
    with connection.cursor() as cursor:
        # Read a single record
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


@app.route('/course/<int:CLIENT_ID>', methods=['GET'])
def course_details_id(CLIENT_ID):
    sql = """SELECT * FROM client_wise_user_wise_course_details WHERE CLIENT_ID=%s """
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql, CLIENT_ID)
        result = cursor.fetchall()
        return result


# client wise user wise event details..
@app.route('/events', methods=['GET'])
def events_details():
    sql = "SELECT * FROM client_wise_user_wise_event_details"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


@app.route('/events/<int:CLIENT_ID>', methods=['GET'])
def events_details_by_client_id(CLIENT_ID):
    sql = "SELECT * FROM client_wise_user_wise_event_details WHERE CLIENT_ID=%s"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql, CLIENT_ID)
        result = cursor.fetchall()
        return result


# client wise user wise journey details  ...
@app.route('/journey', methods=['GET'])
def journey_details():
    sql = "SELECT * FROM client_wise_user_wise_journey_details"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


@app.route('/journey/<int:CLIENT_ID>')
def journey_details_by_client_id(CLIENT_ID):
    sql = "SELECT * FROM client_wise_user_wise_journey_details WHERE CLIENT_ID=%s"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql, CLIENT_ID)
        result = cursor.fetchall()
        return result


@app.route('/tool', methods=['GET'])
def tool_package_details():
    sql = "SELECT * FROM client_wise_user_wise_tool_package_details"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


@app.route('/tool/<int:CLIENT_ID>', methods=['GET'])
def tool_package_details_by_client_id(CLIENT_ID):
    sql = "SELECT * FROM client_wise_user_wise_tool_package_details WHERE CLIENT_ID=%s"
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(sql, CLIENT_ID)
        result = cursor.fetchall()
        return result


if __name__ == "__main__":
    app.run(debug=True)
