import pyautogui as controlTecladoyMouse
import subprocess
import os


def buscar(texto):
    subprocess.call(
        ['google-chrome', 'www.google.com/search?q={0}'.format(texto)])


def cerrarVentana():
    controlTecladoyMouse.hotkey('alt', 'f4')

  
def scrollDown():
    controlTecladoyMouse.scroll(-10)
    # controlTecladoyMouse.press('j')


def scrollUp():
    controlTecladoyMouse.scroll(10)
    # controlTecladoyMouse.press('k')


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

def llamada():
    controlTecladoyMouse.moveTo(x= +1211,y= 56, duration=.5)
    controlTecladoyMouse.click()
def colgarLLamada():
    controlTecladoyMouse.moveTo(x= +1316,y= 71, duration=.5)
    controlTecladoyMouse.click()

def videoLLamada():
    controlTecladoyMouse.moveTo(x= 1159,y= 57, duration=.5)
    controlTecladoyMouse.click()
def colgarVideoLLamada():
    controlTecladoyMouse.moveTo(x= +1231,y= 309, duration=.5)
    controlTecladoyMouse.click()
def Verfoto():
    controlTecladoyMouse.moveTo(x= 567,y= 95, duration=.5)
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
#no esta funcionando    
def borrar():
    controlTecladoyMouse.hotkey('ctrl', 'shift','d')
#no esta funcionando
def borrarTexto():
    controlTecladoyMouse.hotkey('backspace')
#no esta funcionando
def borrarTodo():
    controlTecladoyMouse.hotkey('ctrl', 'a')    
    controlTecladoyMouse.hotkey('backspace')

def maximizar():
    controlTecladoyMouse.getWindowsWithTitle("Whastapp")[0].maximize()


def replace(texto):
    texto.replace("á","a")
    texto.replace("é","e")
    texto.replace("í","i")
    texto.replace("ó","o")
    texto.replace("ú","u")
    return texto
