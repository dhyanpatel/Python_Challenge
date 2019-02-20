import pickle, requests
from pprint import pprint

pickle_file = "http://www.pythonchallenge.com/pc/def/banner.p"
url = "http://www.pythonchallenge.com/pc/def/{}.html"

request = requests.get(pickle_file)

newFile = pickle.loads(request.content)

for x in newFile:
    for y in x:
        for i in range(y[1]):
            print(y[0], end="")
    print()

# ASCII reveals the answer is channel
final = "channel"

print(url.format(final))