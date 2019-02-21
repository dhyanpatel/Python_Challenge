from zipfile import ZipFile

url = "http://www.pythonchallenge.com/pc/def/{}.html"

nothing = "90052"

with ZipFile('./channel.zip', 'r') as z:
    while True:
        try:
            with z.open("{}.txt".format(nothing)) as f:
                nothing = f.read()[16:].decode('utf-8')
                print(z.getinfo(f.name).comment.decode('utf-8'), end="")
        except KeyError:
            break


#This reveals the key is oxygen
final = "oxygen"

print(url.format(final))