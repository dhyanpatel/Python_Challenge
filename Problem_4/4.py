import requests

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

url = "http://www.pythonchallenge.com/pc/def/{}"
currentURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
nothing = "12345"

final = []


for i in range(400):
    request = requests.get(currentURL.format(nothing))
    nothing = request.text[24:]
    if not isInt(nothing):
        final.append(url.format(request.text))
        print("Anomaly found at " + str(i))
        continue
    if(i % 25 == 0):
        print("Currently at " + str(i))

for i in final:
    if requests.get(i).status_code == 200:
        print(i)
