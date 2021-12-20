#JUAN RIVERA VARGAS
import cv2
import numpy as np
import matplotlib.pyplot as plt

###########################################INGRESA EL NOMBRE DE TU IMAGEN EN LA VARIABLE NOMBRE
############################################TAMBIEN DEBES PONER SU EXTENSION

nombre='tablero4.png'
img1 = cv2.imread(nombre,0)
img2 = cv2.imread(nombre)

#### TABLERO DE LETRAS
letras='A B C D E F G H'.split()
numeros='8 7 6 5 4 3 2 1'.split()
tablero=[]
for numero in numeros:
  fila=[]
  for letra in letras:
    fila.append(letra + numero)
  tablero.append(fila)

tablero = np.array(tablero)

ancho=img1.shape[1]
alto=img1.shape[0]

######################################Encuentra la arista izquierda y la superior del tablero
arista_izquierda=0
arista_superior=0
out=0
for c in range(ancho):
  for r in range(alto):
    #print(img1[r,c])
    if img1[r,c] != 0:

      arista_izquierda=c
      arista_superior=r
      out=1
      break
  if out==1:
    break



#########################################encuentra la arista inferior y derecha
arista_derecha=0
arista_inferior=0
out=0
for c in range(ancho,0,-1):
  for r in range(alto,0,-1):
    #print(img1[r,c])
    if img1[r-1,c-1] != 0:

      arista_derecha=c-1
      arista_inferior=r-1
      out=1
      break
  if out==1:
    break


########################################Encuentra las coordenadas x de cada fila del tablero
coordenadasx=[]
#dibujar lineas que atraviesan el tablero
l=37
for i in range(8):
  coordenadasx.append(l + arista_izquierda)
  if i%2==0:
    l=l+75
  else:
    l=l+74


###########################################Encuentra las coordenadas y de cada fila del tablero
coordenadasy=[]
h=38
for i in range(8):
  coordenadasy.append(arista_superior + h)
  if i%2==0:
    h=h+75
  else:
    h=h+74



#####################################################Cuenta las fichas y dibuja los circulos y letras
tonos_de_gris=[]

blancas=0
negras=0

letra=0
font = cv2.FONT_ITALIC
for i in coordenadasx:
  numero=0

  for j in coordenadasy:

    tono=img1[j,i]
    tonos_de_gris.append(tono)

    if tono <= 204+5 and tono >= 204-10:
      blancas=blancas+1
      cv2.circle(img2,(i,j),36,(238,197,72),4)
      #texto
      cv2.putText(img2,tablero[numero, letra],(i-21,j+10),font,1,(248,118,22),2,cv2.LINE_AA)

    elif tono <= 53+20 and tono >= 53-20:
      negras=negras+1
      cv2.circle(img2,(i,j),36,(0,255,0),4)
      #texto
      cv2.putText(img2,tablero[numero, letra],(i-21,j+10),font,1,(0,255,0),2,cv2.LINE_AA)
      
    numero += 1
  letra += 1

###################################################Se imprime el total de fichas
cadena_blancas='Fichas blancas: ' + str(blancas)
cv2.putText(img2,cadena_blancas,(arista_izquierda - 20,arista_superior - 15),font,1,(248,118,22),2,cv2.LINE_AA)

cadena_negras='Fichas cafes: ' + str(negras)
cv2.putText(img2,cadena_negras,(arista_izquierda - 20,arista_inferior + 45),font,1,(0,255,0),2,cv2.LINE_AA)



#########################################################SE IMPRIME EL TABLERO
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.title('Tablero ' + nombre[7])
plt.xticks([]),plt.yticks([])
plt.show()

