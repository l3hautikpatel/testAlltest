import requests
import requests
import json

reqUrl = "http://www.cloudinverter.net/dist/server/api/CodeIgniter/index.php/Senergytec/web/v2/Inverterapi/MemberMonitor"
headersList = {
 "Accept": "application/json",
 "Accept-Encoding": "gzip, deflate",
 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuY2xvdWRpbnZlcnRlci5uZXQiLCJhdWQiOiJ3d3cuY2xvdWRpbnZlcnRlci5uZXQiLCJpYXQiOjE2NzI2NTEzNTIsIm5iZiI6MTY3MjY1MTM1MiwiZXhwIjoxNzAzNzU1MzUyLCJkYXRhIjp7Ik1lbWJlckF1dG9JRCI6bnVsbH19.5N3w5p5Dn9RHSfZYjBZ52FsaCUSzmU2zlvNq_C2NIG4",
 "Content-Type": "application/json" 
}
payload = json.dumps({
  "MemberAutoID": "78958",
  "language": "en-US",
  "sign": "6NwdXFZoKQ9kW9JggrjOTaQo67lO7THKnGyXC8q86+cIOErS9Lj5fABnV4JUny0fQPOVIooVEEmw1HAN3m+zIycztYzC4pgHdWnGvh5y+CY="
})
x = json.loads(requests.request("POST", reqUrl, data=payload,  headers=headersList).text)

redLight = x['AllLight']['red']
greenLight = x['AllLight']['Green']
greyLight = x['AllLight']['gray']
yellowLight = x['AllLight']['yellow']
earnToday = x ['EToday']/1000
earnTotal = x ['ETotal']/1000
wattNow = x['CurrPac']/1000
Htotal = x['Htotal']
name = x['MemberID']
Light = "Green"
if greyLight == 1 :
  Light = "Grey"
if yellowLight == 1:
  Light = "Yellow"
if redLight == 1:
  Light = "Red"
print (name , "      " , wattNow , "        "  )
print (greenLight , "           " , redLight , "      " , yellowLight , "      " , greyLight , "      "   )
print (earnToday , "           " , earnTotal , "      " ,  Htotal ,"          " )

if redLight == 0 :
  MSG = "<b> YOUR TODAY READING IS </b>\n\nName :- "+name+"\nToday gen :- "+str(earnToday)+"\nTotal gen :- "+str(earnTotal)+"\ncurrent watts :-"+str(wattNow)+"\n LIGHT :- " + Light +" \nJSK"
  reqUrl = "https://api.telegram.org/bot5809721521:AAEwgAO1VdOrfNIlIEgOXSn7S0e0mX-nR9E/sendMessage?chat_id=700678109&text="+MSG+"&parse_mode=HTML"
  headersList = {
   "Accept": "*/*",
   "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
  }
  payload = ""
  response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
  print(response.text)
  
  reqUrl = "https://api.telegram.org/bot5809721521:AAEwgAO1VdOrfNIlIEgOXSn7S0e0mX-nR9E/sendMessage?chat_id=700678109&text="+MSG+"&parse_mode=HTML"
  headersList = {
   "Accept": "*/*",
   "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
  }
  payload = ""
  response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
  print(response.text)

if redLight == 0 :
  MSG = "<b> Your solar system have a problem please cheack manually </b>\n\nName :- "+name+"\nToday gen :- "+str(earnToday)+"\nTotal gen :- "+str(earnTotal)+"\ncurrent watts :-"+str(wattNow)+"\n JSK"
  reqUrl = "https://api.telegram.org/bot5809721521:AAEwgAO1VdOrfNIlIEgOXSn7S0e0mX-nR9E/sendMessage?chat_id=700678109&text="+MSG+"&parse_mode=HTML"
  headersList = {
   "Accept": "*/*",
   "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
  }
  payload = ""
  response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
  print(response.text)
  
  reqUrl = "https://api.telegram.org/bot5809721521:AAEwgAO1VdOrfNIlIEgOXSn7S0e0mX-nR9E/sendMessage?chat_id=700678109&text="+MSG+"&parse_mode=HTML"
  headersList = {
   "Accept": "*/*",
   "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
  }
  payload = ""
  response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
  print(response.text)
  
