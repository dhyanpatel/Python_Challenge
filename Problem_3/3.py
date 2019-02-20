url = "http://www.pythonchallenge.com/pc/def/{}.php"

with open("mess.txt") as mess:
    mess = mess.read()
    final = ""
    for pos in range(len(mess)):
        if mess[pos].islower():
            try:
                if (mess[pos - 3].isupper() and
                        mess[pos - 2].isupper() and
                        mess[pos - 1].isupper() and
                        mess[pos + 1].isupper() and
                        mess[pos + 2].isupper() and
                        mess[pos + 3].isupper() and
                        mess[pos - 4].islower() and
                        mess[pos + 4].islower()):
                    final += mess[pos]
            except IndexError:
                pass

    print(url.format(final))
