#!/usr/bin/python3

# Response with a HTTP 204
# http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all

import sys
import http.server
import configparser
import ssl
import time
import logging
import logging.handlers
import socket

VERSION = "0.1"
COPYRIGHT = "Copyright 2015 - 2016 - Bumbl3b33 / CiscoBob"



class SmallWebserverHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		# Parse query data & params to find out what was passed
		headers = self.headers
		#print("Headers: %s" % headers['Host'])

		# request is either for a file to be served up or our test
		self.processrequest("asd")

	def processrequest(self, query):
		self.send_response(200)
		self.send_header('Content-Type', 'image/gif')
		self.end_headers()
		# self.wfile.write(pixel.tobytes)
		#self.wfile.write("<html><body>Nothing to see here</body></html>")



def set_up_logging(config):
	slserver = config['logging']['syslog_server']
	slport = int(config['logging']['syslog_port'])
	slname = config['logging']['syslog_name']
	sltype = config['logging']['syslog_type']
	slfacility = config['logging']['syslog_facility']
	sllevel = config['logging']['syslog_level']

	if sltype == 'TCP':
		slsock=socket.SOCK_STREAM
	else:
		slsock=socket.SOCK_DGRAM

	syslog = logging.handlers.SysLogHandler(address=(slserver, slport), facility=slfacility, socktype=slsock)
	syslog.setLevel(logging.DEBUG)
	syslog.setFormatter(logging.Formatter('%(pathname)s [%(process)d]: %(levelname)s %(message)s'))

	logger = logging.getLogger()
	logger.addHandler(syslog)

	return logger



# ***************************************************************
#
# ***************************************************************

def main(argv):
	config = configparser.ConfigParser()
	config.read("fake200.cfg")
	wsbind = config['webserver']['bind']
	wsport = int(config['webserver']['port'])
	wscertfile = config['webserver']['certfile']

	logger = set_up_logging(config)

	logger.debug ('Test')

	server_address = (wsbind, wsport)
	httpd = http.server.HTTPServer(server_address, SmallWebserverHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile=wscertfile, ssl_version=ssl.PROTOCOL_TLSv1_2)

	print("serving at port %s" % wsport)

	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass

	httpd.server_close()
	print(time.asctime(), "serving stops")



# ***************************************************************
# Single point of entry - Let us jump directly to the main part
# ***************************************************************

if __name__ == "__main__":
	main(sys.argv)
	sys.exit(0)

	# EOF
