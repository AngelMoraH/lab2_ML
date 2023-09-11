clases = ["Apple Braeburn","Apricot","Banana","Cherry","Clementine","Lemon","Mango","Orange","Papaya","Pineapple"]

import os

def contar_archivos(carpeta):
  sub_carpetas = os.listdir(carpeta)
  archivos = []
  for sub_carpeta in sub_carpetas:
    sub_carpeta = carpeta + sub_carpeta
    archivos += os.listdir(sub_carpeta)
  print(archivos)
  return len(archivos), archivos


carpeta = "train/"
cantidad_archivos, data = contar_archivos(carpeta)

# train 80%
# validation 10%
# test 10%



print(cantidad_archivos)

