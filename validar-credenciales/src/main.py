import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

user = os.getenv("APP_USER")
password = os.getenv("APP_PASSWORD")


def get_user_password():
    user = entry_user.get()
    password = entry_password.get()
    if user == "sebastian1416" and password == "jfEtL4IM0BNDdtQY":
        label_inicio1.config(text=f"Bienvenido usuario", fg="green")
    else:
        label_inicio1.config(text=f"Credenciales incorrectas", fg="red")
    

ventana = tk.Tk()
ventana.title("Validar Contraseñas")
ventana.geometry("300x300")

label_user = tk.Label(ventana, text="Ingrese su usuario")
label_user.pack()

entry_user = tk.Entry(ventana)
entry_user.pack()

label_password = tk.Label(ventana, text="Ingrese su contraseña")
label_password.pack()

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()

button = tk.Button(ventana, text="Ingresar", command=get_user_password)
button.pack()

label_inicio1 = tk.Label(text="")
label_inicio1.pack()

ventana.mainloop()

 
   