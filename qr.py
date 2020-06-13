import pyqrcode
url=pyqrcode.create("https://github.com/Saishashidhar66")
url.svg('uca-url.svg',scale=8)
print(url.terminal(quiet_zone=1))