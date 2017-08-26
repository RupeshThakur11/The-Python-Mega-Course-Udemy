import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print(1)
	else:
		print("Fun hours")
	time.sleep(1)
