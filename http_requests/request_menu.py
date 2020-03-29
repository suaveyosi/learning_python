# to use this we have to install requests
# virtualenv .env -p python3
# source .env/bin/activate
# pip3 install requests
import requests
my_request = requests.get("http://go.codeschool.com/spamvanmenu")
# Parse the request to json
menu_list=my_request.json()
print(menu_list)
print("Today's menu")
for item in menu_list:
    print("{}: {}: {}".format(item['name'],item['desc'],item['price']))

