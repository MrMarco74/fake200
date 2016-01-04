# fake200
fake200 is a small in python written webserver which main purpose is to answer this annoying tracking pixel requests.
It works best in combination with a self installed dns server which redirects all request to himself.

## Subtitle

More to come


## Featurelist

### Logging

* syslog
* level - facility (local 0 - 7)
* remote syslog server

### Content Delivery

1x1 Pixel Image for

* .png
* .gif
* .jpg
* .jpeg
* .svg

Empty File for

* .js
* .css

And last but not least

* Unknown file extension collector !


## Planned Features for later

* Different response for different requests. E.g. domain a wants to have a bigger empty pixel.
* Whiteliste of Domains for bypassing filtering
* HTTPS Support
    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
