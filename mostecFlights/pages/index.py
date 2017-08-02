from flask import Flask, current_app, jsonify
from flaskext.mysql import MySQL
from flask_restful import reqparse, Resource

import datetime
import logging

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'dangonzo@172.21.0.237'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gonzodb'
app.config['MYSQL_DATABASE_DB'] = 'dangonzo+edu'
app.config['MYSQL_DATABASE_HOST'] = 'sql.mit.edu'
mysql.init_app(app)

class test(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT * FROM 'mostec_flights_2017'"

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.commit()
            cursor.close()
        except Exception as e:
            logging.error(e)
            cursor.close()
            return {"message": "bad stuff happened"}

