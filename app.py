from doctest import debug

from flask import Flask, render_template, make_response, request, send_from_directory
# from flask_socketio import SocketIO
import pdfkit
# import socketio
import pytz
from flask_cors import CORS
from datetime import datetime
import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
import os
import subprocess
import sys

app = Flask(__name__)

cors = CORS()
cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

# socketio = SocketIO(app)
# sio = socketio.Client()

# socketio = SocketIO(app, cors_allowed_origins="*")

app.config['PDF_FOLDER'] = 'fileserver/'
app.config['TEMPLATE_FOLDER'] = 'templates/'
app.config['STATIC'] = 'static/'


@app.route('/reporte/static/<filename>')
def uploaded_file_static(filename):
    return send_from_directory(app.config['STATIC'],
                               filename)


global options, config
path_wkthmltopdf = 'wkhtmltox/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
options = {
    # 'page-size': 'A4',
    # 'dpi': 300,
    # 'disable-smart-shrinking': '',
    'margin-top': '0.2in',
    'margin-right': '0.0in',
    # 'margin-bottom': '0.3in',
    'margin-left': '0.0in',
    'margin-bottom': '0.3in',
    # 'encoding': "UTF-8",
    # 'footer-right': '[page] de [topage]',
    # 'custom-header': [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'quiet': '',
    # 'cookie': [
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    # 'no-outline': None
}


@app.route('/fileserver/tickets/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['PDF_FOLDER'],
                               filename)


@app.route('/api/imprimirticketpdf', methods=['POST'])
def index():
    try:
        print("iniciando proceso...")
        lima = pytz.timezone('America/Lima')
        li_time = datetime.now(lima)
        _json = request.json
        print("1")
        _json['registro']['registro'] = int(_json['registro']['registro'])
        print("2")
        _json['registro']['created_at'] = "{}".format(_json['registro']['created_at'])
        print("3")
        pdffile = app.config['PDF_FOLDER'] + '{}.pdf'.format(_json['registro']['registro'])
        print("4")
        rendered = render_template('test2.html', json=_json)
        print("5")
        pdfkit.from_string(rendered, pdffile, options=options) if os.name != "nt" else pdfkit.from_string(
            rendered, pdffile, options=options, configuration=config)
        print("6")
        return {
            "codRes": "00",
            "message": "http://95.111.235.214:4545/fileserver/tickets/{}.pdf".format(_json['registro']['registro'])
            # "message": "http://127.0.0.1:4545/fileserver/tickets/{}.pdf".format(_json['registro']['registro'])
        }
    except NameError:
        # print(NameError)
        return {
            "codRes": "99",
            "message": "Error controlado"
        }


if __name__ == '__main__':
    app.run(debug=True, port=4545, host="0.0.0.0")
    # socketio.run(app, debug=True, port=5454, host="0.0.0.0")
