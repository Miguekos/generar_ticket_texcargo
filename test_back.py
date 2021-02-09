# import win32api
# import win32print
# from glob import glob
# import tempfile
#
# printText = """
# asdasd
# asdasd
# asdasd
# asdasd
# asdasd
# """
# print(printText)
# filename = tempfile.mktemp(".txt")
# open(filename, "w").write(printText)
# print(win32print.GetDefaultPrinter())
# # Bellow is call to print text from your_widget_name textbox
# win32api.ShellExecute(0,"printto", filename, '"%s"' % "Canon G3010 series", ".", 0)



# import win32api
# import win32print
#
# name = win32print.GetDefaultPrinter()
# print(name)
#
# #printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}
# printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}
# handle = win32print.OpenPrinter(name, printdefaults)
#
# level = 2
# attributes = win32print.GetPrinter(handle, level)
#
# print("Old Duplex = %d" % attributes["pDevMode"].Duplex)
#
# #attributes["pDevMode"].Duplex = 1    # no flip
# #attributes["pDevMode"].Duplex = 2    # flip up
# attributes["pDevMode"].Duplex = 3    # flip over
#
# ## "SetPrinter" fails because of "Access is denied."
# ## But the attribute "Duplex" is set correctly
# try:
#     win32print.SetPrinter(handle, level, attributes, 0)
# except:
#     print ("win32print.SetPrinter: set 'Duplex'")
#
# res = win32api.ShellExecute(0, "print", "test.pdf", None, ".", 0)
#
# win32print.ClosePrinter(handle)


########################

import win32ui
import win32api
import win32print
import win32con
#
# str1 = \
# """
#         TexCargo.cl
#   Numero de orden: 33321
#
# Fecha de envio: 2021-01-31
# Comuna:         Olivos
# Destinatario:   Villa Sol
# Direccion:      Mz B Lt 7
# Tlfn:           965778450
# Remitente:      Miguel Rodriguez
# Tipo de Servicio:
# Valor:
# El cliente acepta todos los
# terminos y condiciones
# publicados en nuestra pagina
# www.texcargo.cl/condiciones
#
# """
#
# #str1 = str1 + str1 + str1 + str1  # test height of text area
#
# hDC = win32ui.CreateDC()
# print(win32print.GetDefaultPrinter())  # test
# hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
# hDC.StartDoc("Test doc")
# hDC.StartPage()
# hDC.SetMapMode(win32con.MM_TWIPS)
#
# # draws text within a box (assume about 1400 dots per inch for typical HP printer)
# ulc_x = 1000    # give a left margin
# ulc_y = -1000   # give a top margin
# lrc_x = 11500   # width of text area-margin, close to right edge of page
# lrc_y = -15000  # height of text area-margin, close to bottom of the page
# hDC.DrawText(str1, (ulc_x, ulc_y, lrc_x, lrc_y), win32con.DT_LEFT)
#
# hDC.EndPage()
# hDC.EndDoc()

import os
import subprocess
import sys
#
# ruta = os.getcwd()
# # ruta = "{}{} {}".format(ruta, "\GSPRINT\gsprint.exe", "27392.pdf")
# ruta = "{}{} {} {} {} {} {} {}".format(ruta, "\GHOSTSCRIPT\\bin\\gswin32c.exe" , "-sDEVICE=mswinpr2", "-dBATCH" , "-dNOPAUSE","-dFitPage", "-sOutputFile='Canon G3010 series'", "27392.pdf")
# print(ruta)


GHOSTSCRIPT_PATH = "{}\\GHOSTSCRIPT\\bin\\gswin32.exe".format(os.getcwd())
GSPRINT_PATH = "{}\\GSPRINT\\gsprint.exe".format(os.getcwd())

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "27392.pdf"', '.', 0)
# args = " .\\GHOSTSCRIPT\\bin\\gswin32c"
# "-sDEVICE=mswinpr2 "
# "-dBATCH "
# "-dNOPAUSE "
# "-dFitPage "
# "-sOutputFile='%printer%myPrinterName' "
# ghostscript = args + os.path.join(os.getcwd(), "comprobante.pdf")
# subprocess.call(ruta, shell=True)
# ruta = os.getcwd()
# # ruta = "{}{} {}".format(ruta, "\GSPRINT\gsprint.exe", "27392.pdf")
# ruta = "{}{}".format(ruta, "\GSPRINT\gsprint.exe")
# file = "27392.pdf"
# print(ruta)
# win32api.ShellExecute(0, 'open', ruta, '-printer {}'.format('"%s"' % "Canon G3010 series") + file, '.', 0)
# subprocess.call(r"{}".format(ruta), shell=True)
# p = subprocess.Popen([ruta, "27392.pdf"],
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = p.communicate()
# print (stdout)
# print (stderr)



import win32print
import win32ui
from PIL import Image, ImageWin
#
# PHYSICALWIDTH = 110
# PHYSICALHEIGHT = 111
#
# printer_name = win32print.GetDefaultPrinter()
# file_name = "logo.png"
#
# hDC = win32ui.CreateDC ()
# hDC.CreatePrinterDC (printer_name)
# printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
#
# bmp = Image.open (file_name)
# if bmp.size[0] < bmp.size[1]:
#   bmp = bmp.rotate (90)
#
# hDC.StartDoc (file_name)
# hDC.StartPage ()
#
# dib = ImageWin.Dib (bmp)
# dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1]))
#
# hDC.EndPage ()
# hDC.EndDoc ()
# hDC.DeleteDC ()

# import os
# if os.name== 'nt':
#   import win32print
# import win32api
# printerName = win32print.GetDefaultPrinter()
# printer = win32print.OpenPrinter(printerName)
# printerValues = win32print.GetPrinter(printer,2)
# dir(printerValues['pDevMode'])
#
# win32api.ShellExecute(0,'print','requeriments.txt',None,'.',0)
