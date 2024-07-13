import pyqrcode

def gen_qr_code(qrdata):
    qr = pyqrcode.create(qrdata)
    qr.png('QRTest.png', scale=7)

if __name__ == "__main__":
    gen_qr_code("MY QR")