# import the required library
import cv2
import os
import shutil

pasta_imagens = "/home/kaique/boundbox/tolabel/"

f = open("grountruth.txt", "a")
top_left_corner=[]
bottom_right_corner=[]

fglobal = 0
fprox = 0

# of the points clicked on the image
def click_event(event, x, y, flags, params):

    #print(cv2.EVENT_FLAG_LBUTTON)
    global fglobal
    global fprox
    global top_left_corner, bottom_right_corner
    imgCopy = img.copy()

    if event == cv2.EVENT_MOUSEMOVE:

         cv2.line(imgCopy, (x, y+500), (x, y-500), (0, 0, 255), 1)
         cv2.line(imgCopy, (x+500, y), (x-500, y), (0, 0, 255), 1)

         if (fglobal == 1):
            cv2.rectangle(imgCopy, top_left_corner[0], (x, top_left_corner[0][1] + (x - top_left_corner[0][0]) ), (0,255,0),2,8)

         cv2.imshow('Point Coordinates', imgCopy)

    if event == cv2.EVENT_LBUTTONDOWN:

        fglobal = 1
        top_left_corner = [(x,y)]

    if event == cv2.EVENT_LBUTTONUP:
        fglobal = 0
        fprox = 1
        bottom_right_corner = [(x,y)]
        yQuadrado = top_left_corner[0][1] + (x - top_left_corner[0][0])

        cv2.rectangle(img, top_left_corner[0], (x, yQuadrado ), (0,255,0),2,8)
        cv2.imshow('Point Coordinates', img)
         
        f.write(str(x) + ";" + str(yQuadrado) + ";" )
 
# create a window
cv2.namedWindow('Point Coordinates')

i = 0

lista_arquivos = sorted(os.listdir(pasta_imagens), key=lambda x: int(x), reverse=False)

#ini = input("Começar de qual imagem? ")
#inicio = int(ini) -1


for arquivo in os.listdir(pasta_imagens):
    print(len(lista_arquivos))
    i = i+ 1
    f.write(arquivo + ";")
    img = cv2.imread(pasta_imagens + arquivo)
    cv2.imshow('Point Coordinates',img)
    cv2.setMouseCallback('Point Coordinates', click_event)
    k = 0

    texto = "inflamavel = i\noxidante = o\nambiental = a\nplaca laranja = l\ntipo nao definido = n\nma qualidade = x"

    y_start = 150
    y_increment = 40

    while True:
        for i, line in enumerate(texto.split('\n')):
            y = y_start + i*y_increment
            cv2.putText(img, line, (100,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,255,0), 2)
            cv2.imshow('Point Coordinates',img)
        print("Desenhe o retangulo na placa \n")

        k = cv2.waitKey(0)
        if k == 8: m = "backspace"
        else: m = chr(k)

        labeledPAth = "/home/kaique/boundbox/rotuladas/"

# inflamavel = 1
# oxidante = 2
# ambiental = 3
# placa laranja = 4
# tipo nao definido = n
# má qualidade = x

        match m:

            case 'i':
                f.write("1\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "inflamavel/" + arquivo)
                break

            case 'o':
                f.write("2\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "oxidante/" + arquivo)
                break
            
            case 'a':
                f.write("3\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "ambiental/" + arquivo)
                break
            
            case 'l':
                f.write("4\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "laranja/" + arquivo)
                break
        
            case 'n':
                f.write("?\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "indefinido/" + arquivo)
                break

            case 'x':
                f.write("MQ\n")
                shutil.move(pasta_imagens + arquivo, labeledPAth + "qualidade/" + arquivo)
                break

            case 'q':
                f.close()
                cv2.destroyAllWindows()
                exit()

            case 'backspace':
                f.write("refazer\n")
                break
            
f.close()
cv2.destroyAllWindows()