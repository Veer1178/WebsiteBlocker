import time
from datetime import datetime as dt
hosts_temp = r"C:\Users\TamimNur\Desktop\WebsiteBlocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,00):
        print("Working Hours")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_lis
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
else:
print("Fun Hours")
time.sleep(5)
