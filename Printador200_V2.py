import PySimpleGUI as sg                
import time
import pyscreenshot as ImageGrab
import os
#Interface grafica com pysimplegui:
layout = [
            [sg.Text("Printador 2000")],
            [sg.Text('Nome.JPG:'), sg.Input(key="name_f",size=(10,1))],
            [sg.Button('Print'),sg.Button('Sair')]]        
#Variaveis:
window = sg.Window('P2000', layout)
directoryPath =('/home/pi/Desktop/Prints/')
#Funcao de print:
def Tirar_Print():
    imagem = ImageGrab.grab()    
    imagem.save("/home/pi/Desktop/Prints/{}.jpg".format(n_fotos),"jpeg") 
#checador de existencia de pasta:
def checkFile():
    if os.path.isdir(directoryPath) == False:
        os.makedirs(directoryPath)
#laço de repetição principal:   
while True:
    events,values = window.read()
    if events == 'Print':
        window.hide()
        time.sleep(1)
        n_fotos = values["name_f"]
        checkFile()
        Tirar_Print()
        time.sleep(1)
        window.un_hide()
        events,values = ('','')
    elif events == sg.WINDOW_CLOSED or events == 'Sair':
        break
window.close()        

