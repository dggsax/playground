st login: Tue Aug  1 09:27:31 on ttys001
dhcp-18-111-71-142:~ gonzo$ cd Documents/projects/arealytics/
dhcp-18-111-71-142:arealytics gonzo$ clea
-bash: clea: command not found
dhcp-18-111-71-142:arealytics gonzo$ clear
dhcp-18-111-71-142:arealytics gonzo$ ls
README.md       client          iOS         lib         pip-selfcheck.json  update_function
bin         data_science        include         media           server          website
dhcp-18-111-71-142:arealytics gonzo$ cd website/
dhcp-18-111-71-142:website gonzo$ clear


from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from math import cos

# Calls iphone shit
from ios_manager import ListManager, NicknameManager, LocationManager

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
6 lines yanked
