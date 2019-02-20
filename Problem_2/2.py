url = "http://www.pythonchallenge.com/pc/def/{}.html"

with open("mess.txt") as mess:
    mess = list(mess.read())
    values = {}
    for symbol in mess:
        if symbol in values:
            values[symbol]+=1
        else:
            values[symbol] = 1
    final = ""
    for key in values:
        if values[key] == 1:
            final += key
    print(url.format(final))