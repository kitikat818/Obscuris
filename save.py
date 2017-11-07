import requests
url = "http://wheeloffortunesolutions.com/spinid.html"
r = requests.get(url)
text = r.text
saveFile = open('spinid.txt','w')
saveFile.write(text)
saveFile.close()

