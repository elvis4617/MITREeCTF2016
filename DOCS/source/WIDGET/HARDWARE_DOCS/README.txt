###############################################################################
# HARDWARE Docs Directory
# Questions?  Contact Keith <keithmiller@umass.edu>
###############################################################################
#
# This directory is for:
# - Documentation and Research for the widget hardware design

TPM Installation and Encription:

Installation:


Connect BeagleBone Black to Internet by:

https://elementztechblog.wordpress.com/2014/12/22/sharing-internet-using-network-over-usb-in-beaglebone-black/

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ethtool
sudo apt-get install tpm-tools

after install tpm-tools use following command to test to see if tpm is running:

tpm_version
tpm_selftest (should return 0000)

and if encounter error or failure, do tcsd to start the tpm

before take ownership of tpm chips, sudo halt the beaglebone black and restart completely:

tpm_takeownership -l debug

use following command to see PCR status (security boot)：

cat /sys/class/misc/tpm0/device/pcrs

Seal and unseal file:

tpm_sealdata -i hashlet-1.1.0.tar.gz -o sealed -l debug
tpm_unsealdata -i sealed -o zzz.tar.gz -l debug


Change owner password and Srk Password:

tpm_changeownerauth -o
tpm_changeownerauth -s

Current BBB #3 Tpm password:

Owner: 8888
Srk: nb666