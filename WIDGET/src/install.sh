#Run this after pulling
CERT = "/etc/ssl/certs/cert.pem"
KEY = "/etc/ssl/certs/key.pem"

if [ -e $CERT ] && [ -e $KEY ];then
  echo "Certs already exist"
else
  echo "Creating New Certs"
  openssl req -x509 -newkey rsa:2048 -keyout /etc/ssl/certs/key.pem -out /etc/ssl/certs/cert.pem -days 100
fi

sudo cp widget_client.py /usr/local/bin
sudo chmod +x /usr/local/bin/widget_client.py
sudo systemctl daemon-reload
sudo systemctl enable widget-client.service
sudo systemctl start widget-client.service
echo "Done updating widget."
