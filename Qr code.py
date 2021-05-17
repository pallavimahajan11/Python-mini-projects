import pyqrcode
import png
from pyqrcode import QRCode
#string which reprsent the qr code
p="https://www.youtube.com/channel/ehgfiuikgig"

#generate the qr code

url=pyqrcode.create(p)
url.svg("mycyoutube channel.svg",scale=8)
