1. Edit _config.py
2. Rename _config.py to config.py
3. Run send_mail.py

crontab task:
* * * * * /home/user/hamilton_pool_availability/send_mail.py >> /home/user/hamilton_pool_availability/log.txt 2>&1
