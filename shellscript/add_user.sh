cd ~/smartlock
sudo systemctl stop smartlock.service
python add_user.py
sudo systemctl start smartlock.service
