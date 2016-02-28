###############################################################################
# SERVER Directory
# Questions?  Contact Keith <keithmiller@umass.edu>
###############################################################################
#
# This directory is for:
# - Server Source code
# - Server Docs
# - Example code for the server
#
#
#  To start the server:
#   - Be on a Unix System
#   - sudo bash start-server
#
#  Making the server from scratch:
#     1) Copy our repo
#     2) Run `openssl req -x509 -newkey rsa:2048 -days 100 -nodes -subj "/C=US/ST=Massachusetts/L=Amherst/O=UMass/CN=www.umass.edu"\
#            -keyout keys/key.pem -out keys/cert.pem` from the door_app directory
#     3) copy /etc/ssl/certs/cert.pem from the widget to keys/widget_cert.pem.
#     4) copy keys/cert.pem on the server into this file on the widget : /etc/ssl/certs/server_cert.pem
#     5) Thats it
#
#
#
