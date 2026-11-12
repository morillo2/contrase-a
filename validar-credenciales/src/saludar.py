import tkinter as tk

def saludar_usuario():
    name = entrada.get()
    label_saludo.config(text=f"Saludos {name}!!!")
    
ventana = tk.Tk()
ventana.title("Aprendiendo Tkinter")
ventana.geometry("300x300")

label = tk.Label(ventana, text="Inserta tu nombre:", font=("Arial", 20))
label.pack()

entrada = tk.Entry(ventana,)
entrada.pack()

boton = tk.Button(ventana, text="Capturar", command=saludar_usuario, font=("Arial", 10))
boton.pack()
label_saludo = tk.Label(text="")
label_saludo.pack()

ventana.mainloop()
