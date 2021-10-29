#control de teclado y mouse 
import pyautogui as controlTecladoyMouse
import os
import subprocess

def buscar(texto):
    subprocess.call(
        ['google-chrome', 'www.google.com/search?q={0}'.format(texto)])


def cerrarVentana():
    controlTecladoyMouse.hotkey('alt', 'f4')

def acercar():
    controlTecladoyMouse.hotkey('ctrl', '+')


def alejar():
    controlTecladoyMouse.hotkey('ctrl', '-')


def nuevo():
    controlTecladoyMouse.hotkey('ctrl', 'n')

def foto():
    controlTecladoyMouse.hotkey('ctrl', 'p')

def enter():
    controlTecladoyMouse.hotkey('enter')

def siguienteChat():
    controlTecladoyMouse.hotkey('ctrl', 'tab')

def buscarChat():
    controlTecladoyMouse.hotkey('ctrl', 'f')

def anteriorChat():
    controlTecladoyMouse.hotkey('ctrl', 'shift', 'tab')


def escribir(texto):
    texto = replace(texto)
    controlTecladoyMouse.typewrite(texto)


def minimizar():
    controlTecladoyMouse.hotkey('win', 'm')


def restaurar():
    controlTecladoyMouse.getWindowsWithTitle("Whastapp")[0].maximize()
    #controlTecladoyMouse.hotkey('win', 'shift', 'm')

def abrir():   
    os.system('WhatsApp.exe')
    
def archivarChat():
    controlTecladoyMouse.hotkey('ctrl','shift','e')

def crearGrupo():
    controlTecladoyMouse.hotkey('ctrl','shift','n')

def silenciarChat():
    controlTecladoyMouse.hotkey('ctrl','shift','m')

def buscarTextoChat():
    controlTecladoyMouse.hotkey('ctrl','shift','f')

#movimientos del mouse 
def hacerclik():
    controlTecladoyMouse.click()
def hacerDobleclik():
    controlTecladoyMouse.doubleClick()
def hacerclikDerecho():
    controlTecladoyMouse.rightClick()
def hacerclikizquierdo():
    controlTecladoyMouse.leftClick()
def scrollDown():
    controlTecladoyMouse.scroll(-15)
def scrollUp():
    controlTecladoyMouse.scroll(15)
        
def llamada():
    controlTecladoyMouse.moveTo(x= +1211,y= 56, duration=.5)
    controlTecladoyMouse.click()

def colgarLLamada():
    controlTecladoyMouse.moveTo(x= +1316,y= 70, duration=.5)
    controlTecladoyMouse.click()

def videoLLamada():
    controlTecladoyMouse.moveTo(x= 1160,y= 56, duration=.5)
    controlTecladoyMouse.click()

def colgarVideoLLamada():
    controlTecladoyMouse.moveTo(x= +1230,y= 3010, duration=.5)
    controlTecladoyMouse.click()


def Verfoto():
    controlTecladoyMouse.moveTo(x= 442,y= 48, duration=.5)
    controlTecladoyMouse.click()

def cerrarVerFoto():
    controlTecladoyMouse.moveTo(x= 992,y= 59, duration=.5)
    controlTecladoyMouse.click()

def microfono():
    controlTecladoyMouse.moveTo(x= 1336,y= 731, duration=.5)
    controlTecladoyMouse.click()

def cancelarAudio ():
    controlTecladoyMouse.moveTo(x= 1161,y= 731, duration=.5)
    controlTecladoyMouse.click()
    
def marcarMensaje():
    controlTecladoyMouse.hotkey('ctrl','shift','u')

def escape():
    controlTecladoyMouse.press('esc')

def borrarTexto():
    controlTecladoyMouse.hotkey('backspace')

def eliminarChat():
    controlTecladoyMouse.hotkey('ctrl', 'shift', 'd') 
    controlTecladoyMouse.moveTo(x= 780,y= 426, duration=1)
    controlTecladoyMouse.click()   

def maximizar():
    controlTecladoyMouse.getWindowsWithTitle("Whastapp")[0].maximize()

def fijarChat():
    controlTecladoyMouse.hotkey('ctrl','shift','p')

def replace(texto):
    texto.replace("á","a")
    texto.replace("é","e")
    texto.replace("í","i")
    texto.replace("ó","o")
    texto.replace("ú","u")
    return texto
