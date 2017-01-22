# sendsms
SMS sender
##import urllib.parse
##import urllib.request
##import json
#phone = input("Enter receiver's number: ")
#msg = input("Enter the message to send: ")
import http.client, urllib.parse
phone="xxxxxxxxxxx"
msg="your mesage"
headers = {  "X-Mashape-Key" : "obtain key from mashape" }
data = urllib.parse.urlencode(headers)
data = data.encode('utf-8')
url = "https://freesms8.p.mashape.com/index.php?msg="+msg+"&phone="+phone+"&pwd=your passwd &uid=user id:443"
print(url)


conn = http.client.HTTPConnection(url)
conn.request("POST",headers)
response = conn.getresponse()
print(response)

