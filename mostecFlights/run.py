from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

# Calls the flask files for each page
from pages.index import apOnline, apOffline, uniqueDevices

from pages.graphs import ApOnlineLister, BokehPlotter

from pages.map import MapAnimations

from pages.mac_addresses import GraphManager
import numpy as np
import random

app = Flask(__name__)
api = Api(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = '6s08'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dome-crawler'
app.config['MYSQL_DATABASE_DB'] = '6s08'
app.config['MYSQL_DATABASE_HOST'] = 'domecrawl.us'
mysql.init_app(app)


# Handle GET requests to get the list of MACs
api.add_resource(ListManager, "/devices/list")

# Handle GET requests to set nicknames
api.add_resource(NicknameManager, "/devices/<string:from_mac>/set_nickname")

# Handle GET requests to get device locations
api.add_resource(LocationManager, "/devices/<string:from_mac>/set_location")

##########################
##                      ##
##    For index.html    ##
##                      ##
##########################

# ap online
api.add_resource(apOnline, "/ap_online/")
# ap offline
api.add_resource(apOffline, "/ap_offline/")
# unique devices
api.add_resource(uniqueDevices, "/unique_devices/")

# AP Online Lister
api.add_resource(ApOnlineLister, "/ap_in_keep_alive/")

# AP Bokeh Plotter
api.add_resource(BokehPlotter, "/plot/")

# AP Map Animations
api.add_resource(MapAnimations, "/map_animations/")

##########################
##                      ##
##  For mac_addresses   ##
##                      ##
##########################

api.add_resource(GraphManager, "/devices/<string:probe_mac>/create_graph")


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


@app.route("/")
def hello():
    return send_from_directory("static", "index.html")


@app.route('/update_markers/', methods=['GET'])
def time_post():

    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "SELECT `A`.`probe_mac`, `A`.`lat_location`, `A`.`long_location`, `A`.`signal_strength` FROM `mac_addresses` `A` WHERE `A`.`probe_mac` IN( SELECT `probe_mac` FROM ( SELECT `probe_mac`, COUNT(DISTINCT `from_mac`) AS `a` FROM `mac_addresses` GROUP BY `probe_mac` ) AS `b` WHERE `a` > 1 ) AND `A`.`timestamp` BETWEEN(DATE_SUB(NOW(), INTERVAL 5 MINUTE)) AND NOW() ORDER BY `timestamp` DESC"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.commit()
    except Exception as e:
        return {"message": "an unknown error occured"}

    coord_list = []

    for item in data:
        try:
            distance = (4 ** ((-45 - int(item[3])) / 25.0)) / 1000.0
            r_earth = 6378
            x_offset, y_offset = pol2cart(
                distance, np.random.uniform(low=0.0, high=360.0))
            new_latitude = float(item[1]) + \
                (y_offset / r_earth) * (180 / np.pi)
            new_longitude = float(item[2]) + (x_offset / r_earth) * \
                (180 / np.pi) / cos(float(item[2]) * np.pi / 180)
            coord_list.append({"lat": new_latitude, "lng": new_longitude})
        except Exception as e:
            print e

    # print(coord_list)

    return jsonify({'coord_list': coord_list})


@app.route("/<path:path>")
def open_file(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4999, threaded=True)
