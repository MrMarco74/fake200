#!/usr/bin/python

# Response with a HTTP 204
# http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all

import SimpleHTTPServer, SocketServer
import urlparse

PORT = 8001

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):

		# Parse query data & params to find out what was passed
		headers = self.headers
		print headers['Host']
		parsedParams = urlparse.urlparse(self.path)
		queryParsed = urlparse.parse_qs(parsedParams.query)

		# request is either for a file to be served up or our test
		self.processMyRequest(queryParsed)

	def processMyRequest(self, query):

		self.send_response(200)
		self.send_header('Content-Type', 'image/gif')
		self.end_headers()

		self.wfile.write(pixel.tobytes)
		#self.wfile.write("<html><body>Nothing to see here</body></html>")
		self.wfile.close()



httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()