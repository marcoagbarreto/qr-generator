from flask import Flask, render_template, request
import qrcode
import cv2
import json
import base64
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', image_data=None)


@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text', None)
    json_file = request.files.get('json_file', None)

    if text:
        image_data = create_qr(text)
        return render_template('index.html', image_data=image_data)
    elif json_file:
        if json_file.filename == '':
            return 'Please select a JSON file to upload'
        json_data = json.loads(json_file.read())
        image_data = create_qr(json.dumps(json_data))
        return render_template('index.html', image_data=image_data)
    else:
        return render_template('index.html', decoded_data="No file or text found")


@app.route('/decode', methods=['POST'])
def decode():
    qr_file = request.files['qr_file']
    qr_file.save(qr_file.filename)
    img = cv2.imread(qr_file.filename)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    qr_decoder = cv2.QRCodeDetector()
    decoded_data, bbox, _ = qr_decoder.detectAndDecode(img)
    if decoded_data:
        return render_template('index.html', decoded_data=decoded_data)
    else:
        return render_template('index.html', decoded_data="No QR code found")


def create_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # save the image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    # encode the image data
    image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Production
    # app.run(debug=True)  # Development

