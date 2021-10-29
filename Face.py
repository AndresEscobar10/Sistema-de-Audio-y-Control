from time import sleep
import cv2
import pyautogui
import voiceSynthesizer as voz

# Load the cascade
face_cascade = cv2.CascadeClassifier('Rostro2.xml')
# To capture video from webcam
cap = cv2.VideoCapture(1)
#Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

global Cnt
global PromX
global PromY
global Bandera
global VectorX
global VectorY

Cnt = 0
PromX = 0
PromY = 0
Bandera = 0
VectorX = [640, 640, 640, 640, 640]
VectorY = [400, 400, 400, 400, 400]

voz.hablar("iniciando reconocimiento facial")
while True:
    #sistema de reconocimiento facial
    # Read the frame
    _, img = cap.read()
    # Restart the flag
    Bandera = 0
    # Horizontal flip
    img = cv2.flip(img, 1)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, cv2.CASCADE_FIND_BIGGEST_OBJECT, 5, (80,80))
    # Draw the rectangle around the face
    
    if (len(faces) > 0):

        for (x, y, w, h) in faces:

            if (Bandera == 0):

                Bandera = 1

                posX = x + (w/2)
                posY = y + (h/2)

                if (Cnt < 15):
                    Cnt+=1
                    PromX = PromX + posX
                    PromY = PromY + posY

                elif (Cnt == 15):
                    PromX = (int)(PromX / 15)
                    PromY = (int)(PromY / 15)
                    Cnt+=1

                elif (Cnt > 15):
                    #Calcula la posicion del mouse en el eje X (640 es la mitad de la resolución de la pantalla)
                    if (posX - 160 >= 0): 
                        MouseX = 640 + (int)(((posX - 160)/20) * 640)
                    else: 
                        MouseX = 640 - (int)(((160 - posX)/20) * 640)

                    #Calcula la posicion del mouse en el eje Y (400 es la mitad d ela resolución de la pantalla)
                    if (posY - 120 >= 0):
                        MouseY = 400 + (int)(((posY - 120)/20) * 400)
                    else: 
                        MouseY = 400 - (int)(((120 - posY)/20) * 400)

                    #cv2.rectangle(img, (PromX-(w/2), PromY-(h/2)), (PromX+(w/2), PromY+(h/2)), (255, 0, 0), 2)
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

                    #Filtro Media Movil de Orden 5
                    VectorX[0] = VectorX[1]
                    VectorX[1] = VectorX[2]
                    VectorX[2] = VectorX[3]
                    VectorX[3] = VectorX[4]
                    VectorX[4] = MouseX
                    MouseX = (int)((VectorX[0]+VectorX[1]+VectorX[2]+VectorX[3]+VectorX[4]) / 5)

                    VectorY[0] = VectorY[1]
                    VectorY[1] = VectorY[2]
                    VectorY[2] = VectorY[3]
                    VectorY[3] = VectorY[4]
                    VectorY[4] = MouseY
                    MouseY = (int)((VectorY[0]+VectorY[1]+VectorY[2]+VectorY[3]+VectorY[4]) / 5)

                    #Limites y bordes par amover el cursor
                    if (MouseX >= 1350): 
                        MouseX = 1350
                    
                    if (MouseY >= 766):  
                        MouseY = 766
                    
                    if (MouseX <= 3): 
                        MouseX = 3
                    
                    if (MouseY <= 3): 
                        MouseY = 3 

                    #Mover el mouse
                    pyautogui.moveTo(MouseX, MouseY)

                    #Aqui va la comparacion para los bordes del scroll 
                    if (MouseX > 40 and MouseX < 1341 and MouseY > 50 and MouseY < 200):
                        pyautogui.scroll(15)

                    if (MouseX > 40 and MouseX < 1341 and MouseY > 600 and MouseY < 700):
                        pyautogui.scroll(-15)
    else:
        #Cuando no hay rostros, reinicia, 
        if (len(faces) == 0):
            Cnt = 0
            PromX = 0
            PromY = 0
            VectorX = [640, 640, 640, 640, 640]
            VectorY = [400, 400, 400, 400, 400]

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()