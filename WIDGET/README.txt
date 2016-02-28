###############################################################################
# WIDGET Directory
# Questions?  Contact Keith <keithmiller@umass.edu>
###############################################################################
#
# This directory is for:
# - Widget Source code
# - Widget Docs
# - Example code for the widget
#
#
# The Subdirectory HARDWARE_DOCS is for:
# - Docs and Research for the widget hardware design
#
#  To Update Widget:
#   - sudo bash update
#
#  How to make a fresh BeagleBone
#    1) Boot the MITRE Image
#    2) Run `date -s "24 FEB 2016 18:00:00"`
#    3) Run `openssl req -x509 -newkey rsa:2048 -days 100 -nodes -subj "/C=US/ST=Massachusetts/L=Amherst/O=UMass/CN=www.umass.edu"\
#            -keyout /etc/ssl/certs/key.pem -out /etc/ssl/certs/cert.pem`
#    4) Copy all AVRChip.py, Logger.py, ServerConnection.py, and widget_client.py to /usr/local/bin
#    5) chmod +x all of those files
#    6) Copy the program_avr.sh to /etc/systemd/system
#    7) Create a file called first-boot.txt in /etc/
#    8) Install fail2ban and edit /etc/fail2ban/jail.conf by changing the line in the SSH section to false
#    9) Do any tpm stuff that i haven't figured out yet - look at TPMREADME.md in the repo
