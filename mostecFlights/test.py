from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

# Calls the flask files for each page
from pages.index import test

app = Flask(__name__)
api = Api(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'dangonzo'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rer42kir'
app.config['MYSQL_DATABASE_DB'] = 'dangonzo+edu'
app.config['MYSQL_DATABASE_HOST'] = 'sql.mit.edu'
mysql.init_app(app)


##########################
##                      ##
##    For index.html    ##
##                      ##
##########################

# test
api.add_resource(test, "/test/")

@app.route("/")
def hello():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def open_file(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, threaded=True)
