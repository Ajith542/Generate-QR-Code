from flask import Flask,request
import util

app = Flask(__name__)

@app.route('/gen_qr_code', methods=['GET','POST'])
def gen_qr_code():
    qrd = request.form['qrdata']
    util.gen_qr_code(qrd)
    return '', 204

if __name__ == "__main__":
    print("Starting Flask Server for QR Code Generator")
    app.run()