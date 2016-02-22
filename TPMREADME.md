After connecting via SSH:

Make sure to have internet on the BeagleBone:
https://elementztechblog.wordpress.com/2014/12/22/sharing-internet-using-network-over-usb-in-beaglebone-black/

To Install the TPM-Tool: 

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ethtool
sudo apt-get install tpm-tools

sudo halt and fully shutdown

Reconnect via SSH: 

tcsd // -- This starts the tcsd daemon
use tpm_version to make sure you can talk to the TPM

tpm_takeownership -l debug // -- This takes the ownership of the TPM after setting the  owner's password and srk password

To Seal Files:
tpm_sealdata -i [filename] -o [output file name] -l debug
tpm_unsealdata -i [filename] -o [output] -l debug -z

