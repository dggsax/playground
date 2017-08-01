from flask import Flask, current_app, jsonify
from flaskext.mysql import MySQL
from flask_restful import reqparse, Resource

import datetime
import logging

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = '6s08'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dome-crawler'
app.config['MYSQL_DATABASE_DB'] = '6s08'
app.config['MYSQL_DATABASE_HOST'] = 'domecrawl.us'
mysql.init_app(app)

class apOnline(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT count(*) FROM `keep_alive` WHERE last_alive > DATE_SUB(NOW(),INTERVAL 30 MINUTE)"

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.commit()
            cursor.close()
        except Exception as e:
            logging.error(e)
            cursor.close()
            return {"message": "an unknown error occured, check the server"}, 500

        logging.info("Just collected number of devices online!")
        cursor.close()
        return jsonify(data[0][0])

class apOffline(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT count(*) FROM `keep_alive` WHERE last_alive < DATE_SUB(NOW(),INTERVAL 30 MINUTE)"

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.commit()
            cursor.close()
        except Exception as e:
            logging.error(e)
            cursor.close()
            return {"message": "an unknown error occured"}, 500

        logging.info("Just collected number of devices offline!")
        cursor.close()
        return jsonify(data[0][0])

class uniqueDevices(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        # sql = "INSERT INTO mac_addresses (timestamp, from_mac, probe_mac, signal_strength) VALUES "
        # sql = "SELECT COUNT(*) FROM `mac_addresses` WHERE `timestamp` > last_moved"
        sql = "SELECT COUNT(*) FROM (SELECT `probe_mac`, COUNT(DISTINCT `from_mac`) AS `a` FROM `mac_addresses` WHERE `timestamp` > `last_moved` GROUP BY `probe_mac`) AS `b` WHERE `a` > 1"

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.commit()
            cursor.close()
        except Exception as e:
            logging.error(e)
            cursor.close()
            return {"message": "an unknown error occured"}, 500

        logging.info("Just collected number of unique devices!")
        return jsonify(data[0][0])
