from doctest import debug

from flask import Flask, render_template, make_response, request, send_from_directory
from flask_socketio import SocketIO
import pdfkit
import socketio
import pytz
from flask_cors import CORS
from datetime import datetime
import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
import win32ui
import win32api
import win32print
import win32con
import os
import subprocess
import sys

app = Flask(__name__)

# cors = CORS()
# cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

# socketio = SocketIO(app)
sio = socketio.Client()

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


# @app.route('/api/imprimirticketpdf', methods=['POST'])
def main(data):
    try:
        lima = pytz.timezone('America/Lima')
        li_time = datetime.now(lima)
        _json = data
        _json['registro']['registro'] = int(_json['registro']['registro'])
        _json['registro']['created_at'] = "{}".format(_json['registro']['created_at'])
        id = _json['id']
        imagen = qrcode.make("{}".format(id))
        archivo_imagen = open(app.config['PDF_FOLDER'] + '{}.png'.format(_json['registro']['registro']), 'wb')
        imagen.save(archivo_imagen)
        archivo_imagen.close()
        pdffile = '{}fileserver/{}.pdf'.format(os.getcwd(), _json['registro']['registro'])
        rendered = render_template('test2.html', json=_json,
                                   qr="http://127.0.0.1:5454/fileserver/tickets/{}.png".format(
                                       _json['registro']['registro']))
        pdfkit.from_string(rendered, pdffile, options=options, configuration=config)
        GHOSTSCRIPT_PATH = "{}\\GHOSTSCRIPT\\bin\\gswin32.exe".format(os.getcwd())
        GSPRINT_PATH = "{}\\GSPRINT\\gsprint.exe".format(os.getcwd())

        # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
        # currentprinter = win32print.GetDefaultPrinter()
        currentprinter = "Canon G3010 series"
        print(currentprinter)

        win32api.ShellExecute(0, 'open', GSPRINT_PATH,
                              '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "{}"'.format(
                                  pdffile),
                              '.', 0)
        return {
            "codRes": "00",
            "message": "Se envio a imprimir correctalemte"
        }
    except NameError:
        # print(NameError)
        return {
            "codRes": "99",
            "message": "Error controlado"
        }


# @sio.event
# def message(data):
#     print('I received a message! ->', data)

@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def message(data):
    print('message received with ', data)
    main(data)
    sio.emit('my response', {'response': 'my response'})


sio.connect('http://localhost:7667')
sio.wait()
