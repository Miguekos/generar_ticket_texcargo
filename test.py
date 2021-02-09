import win32ui
import win32api
import win32print
import win32con
import os
import subprocess
import sys

from flask import Flask
app = Flask(__name__)

app.route('/print', methods=['GET'])
def hello_world():
    # GHOSTSCRIPT_PATH = "{}\\GHOSTSCRIPT\\bin\\gswin32.exe".format(os.getcwd())
    # GSPRINT_PATH = "{}\\GSPRINT\\gsprint.exe".format(os.getcwd())
    #
    # # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
    # currentprinter = win32print.GetDefaultPrinter()
    # print(currentprinter)
    #
    # win32api.ShellExecute(0, 'open', GSPRINT_PATH,
    #                       '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "27392.pdf"', '.',
    #                       0)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)