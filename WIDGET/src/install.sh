sudo cp widget_client.py /usr/local/bin
sudo chmod +x /usr/local/bin/widget_client.py
sudo systemctl daemon-reload
sudo systemctl enable widget-client.service
sudo systemctl start widget-client.service
echo "Done updating widget."
