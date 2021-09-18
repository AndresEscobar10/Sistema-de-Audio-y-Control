import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print('Width: %i px, Height: %i px' % (screen_width, screen_height))

pant = 408
pant2 = screen_width

calculo = pant/pant2
print(calculo)

adaptador = calculo*screen_width
print(adaptador)












