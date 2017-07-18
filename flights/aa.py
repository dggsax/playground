import csv
import datetime
import json
import logging
import os
import pprint
import requests
import sys
import time
import threading

# Set up a logger
logging.basicConfig(level=logging.DEBUG, # The level that we want it to Debug.
                    format='[%(levelname)s] (%(threadName) - 10s) %(message)s')

def worker():
	logging.debug('Beginning to grab information')
	try:
		while True:
			info = steal()
			processInfo(info)
			time.sleep(5)
	except:
		logging.debug('Failed')

def processInfo(response):
	flightNumberInfo = str(response['Response']['flightInfo']['flightNumberInfo'])
	hSpeed = str(response['Response']['flightInfo']['hspeed'])
	vSpeed = str(response['Response']['flightInfo']['vspeed'])
	altitude = str(response['Response']['flightInfo']['altitude'])
	localTime = str(response['Response']['flightInfo']['localTime'])
	longitude = str(response['Response']['flightInfo']['longitude'])
	latitude = str(response['Response']['flightInfo']['latitude'])
	logging.debug("Info for Flight: " + flightNumberInfo +
		". Speed: " + hSpeed +
		". Altitude: " + altitude +
		". Time: " + localTime +
		". Latitude: " + latitude +
		". Longitude: " + longitude +"")
	logInfo(flightNumberInfo, hSpeed, vSpeed, localTime, altitude, latitude, longitude)

def logInfo(flight,hSpeed,vSpeed,time,alt,lat,lon):
        # Don't forget to update flight number for the csv file.
	with open('docs/aa1806.csv','a') as file:
		writer = csv.writer(file)
		currentTime = str(datetime.datetime.now())
		information = [currentTime,flight,hSpeed,vSpeed,time,alt,lat,lon]
		logging.debug(information)
		writer.writerow(information)

def steal():
	url = '''curl 'http://airborne.gogoinflight.com/abp/ws/absServices/statusTray?' -H 'Cookie: MYSESSIONID=E86093540205ED9DBF757F14921E65AC; testCookieName=testCookieName; JSESSIONID=902D149E0BD3DF4ACF149C546EA7ECCB.33; fxCookie=902D149E0BD3DF4ACF149C546EA7ECCB.33; video=true; HMAuserName=null; GG_VE_STATUS=true; s_cc=true; _sdsat_Access Technology=2KU; _sdsat_Flight Region Code=DOM; counterSDI=3; s_fid=1A05F9C635E7BC02-0C9A5A4105358245; s_vi=[CS]v1|2CAF44D8851D07FE-400001628000494C[CE]' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8,an;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: */*' -H 'Referer: http://airborne.gogoinflight.com/gbp/splash.do?execution=e2s1' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed'''
	response = os.popen(url).read()
	loaded = json.loads(response)
	return loaded

# Where the ma(in)gic happens
def main():
	# Make the thread
	flight = threading.Thread(name="Gonzo's Flight", target=worker)
	# Start the thread
	flight.start()

if __name__ == '__main__':
	main()

'''
CURL COMMAND FOR AA(insert number here)
curl 'http://airborne.gogoinflight.com/abp/ws/absServices/statusTray?'
	-H 'Cookie: testCookieName=testCookieName;
	JSESSIONID=A6E5A79491B9EB89EAFEB1B569F5F9B8.37;
	fxCookie=A6E5A79491B9EB89EAFEB1B569F5F9B8.37;
	video=true;
	HMAuserName=null;
	GG_VE_STATUS=true;
	s_cc=true;
	_sdsat_Access Technology=ATG4;
	_sdsat_Flight Region Code=DOM;
	counterSDI=2;
	s_fid=1A05F9C635E7BC02-0C9A5A4105358245;
	s_vi=[CS]v1|2CAF44D8851D07FE-400001628000494C[CE]'
	-H 'Accept-Encoding: gzip, deflate'
	-H 'Accept-Language: en-US,en;q=0.8,an;q=0.6'
	-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
	-H 'Accept: */*' -H 'Referer: http://airborne.gogoinflight.com/gbp/splash.do?execution=e1s1'
	-H 'X-Requested-With: XMLHttpRequest'
	-H 'Connection: keep-alive' --compressed

CURL COMMAND FOR AA1806
'''
