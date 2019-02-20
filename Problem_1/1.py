url = "http://www.pythonchallenge.com/pc/def/{}.html"

original = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

for letter in original:
    if(letter==' '):
        print(' ', end='')
        continue
    print(chr(ord(letter)+2), end="")

print("\nAnswer Below:")

final = ""
new = list("map")
for letter in new:
    final += chr(ord(letter) + 2)
print(url.format(final))