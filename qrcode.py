                                 #### FIRST METHOD FOR QR CODE####
# python3 -m pip install pyqrcode in cmd
# python3 -m pip install pypng in cmd

# import pyqrcode
# import png
# from pyqrcode import QRCode

# url = 'www.shiksha.com/online-courses/articles' 
# url = pyqrcode.create(url)

# url.svg('qr.svg',)
# url.png('qr.png', scale = 8) //Scale to magnify
 
                                 #### SECOND METHOD FOR QR CODE####

# generating qrcode
# with scaling and white blocks border around it
# and with different bg color
import segno

qrcode = segno.make_qr("paste link in ' ' and text in doubleqt for QR ")
qrcode.save(
    "newqr.png",
    scale = 8,
    border = 3,
    #light = "lightblue",  #--it changes the bg color of whole qrcode
    #dark  = "darkblue", #--it changes color of only blocks of qrcode
    quiet_zone = "pink", #--it changes color of white blocks around qrcode
    #data_dark/data_light = "<color>" #--it changes color only of black/white data stored blocks  
)
