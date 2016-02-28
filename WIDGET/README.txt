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
#    4) Copy cert.pem and put it in the Docker Server image file widget_cert.pem, take the the server cert in the docker image called keys/cert.pem
#       and add it to /etc/ssl/certs/server_cert.pem
#    5) Copy all AVRChip.py, Logger.py, ServerConnection.py, and widget_client.py to /usr/local/bin
#    6) chmod +x all of those files
#    7) Copy the program_avr.sh to /etc/systemd/system
#    8) Create a file called first-boot.txt in /etc/
#    9) Install fail2ban and edit /etc/fail2ban/jail.conf by changing the line in the SSH section to false
#    10) Do any tpm stuff that i haven't figured out yet - look at TPMREADME.md in the repo
#
#
#  How to take the image of whats on BBB3
#
#  1) ssh into the image
#  2) do the fail2ban stuff up there ^^^
#  3) create the first-boot file from up there ^^^
#  4) Take the image (look at mitres faq for the command)
#  5) AFTER you take the image and BEFORE you exit the ssh session, change the line in fail2ban back to true in case
      you want to log back in in the future.
