""" Duarte Silva Julio Daniel, 16-05-2023
Prueba: realizar un Login para registro de una página. """

from tkinter import * # Se importan las librerías de Tkinter y Os para el desarrollo del código.
import os

def window_init(): # Definición de la ventana inicial.
    global window_p # Ventana principal.
    color_pestana = "gainsboro"
    window_p = Tk()
    window_p.title(" - Login - ") #Título de la ventana de Login
    window_p.geometry("300x250") #Se establecen las simensiones de la ventana.
    Label(text="Bienvenid@", bg = "lightseagreen", width = "300", height = "2", font = ("Times New Roman", 12)).pack() # Se establece un subtitulo para la ventana con un color de fondo, altura, anchura y fuente.
    Label(text="").pack()
    Button(text="Login / Acceder", height = "2", width = "30", bg = color_pestana, command = login).pack() # Se establece el boton de "Login" con una altura, una anchura y un fondo para la opción, además de "command" con la función que ejecutarán. 
    Label (text="").pack() 
    Button(text="Sing Up / Registrarse", height = "2", width = "30", bg = color_pestana, command = registro).pack()
    Label (text="").pack()
    window_p.mainloop()
    
def registro():
    global window_regis
    window_regis = Toplevel(window_p)
    window_regis.title("Sing Up / Registro")
    window_regis.geometry("400x350")
    
    global nombre
    global apellido 
    global username
    global email
    global password
    global entry_name
    global entry_lname
    global entry_user
    global entry_email
    global entry_pass
    
    nombre = StringVar()
    apellido = StringVar()
    username = StringVar()
    email = StringVar()
    password = StringVar ()
        
    Label(window_regis, text = "Introduce tus datos", bg = "lightseagreen").pack()
    Label(window_regis, text = "").pack()
    
    etiqueta_user = Label(window_regis, text = "Username * ")
    etiqueta_user.pack()
    entry_user = Entry(window_regis, textvariable = username)
    entry_user.pack()
    
    etiqueta_name = Label(window_regis, text = "Nombre * ")
    etiqueta_name.pack()
    entry_name = Entry(window_regis, textvariable = nombre)
    entry_name.pack()
    
    etiqueta_lname = Label(window_regis, text = "Apellido * ")
    etiqueta_lname.pack()
    entry_lname = Entry(window_regis, textvariable = apellido)
    entry_lname.pack()
    
    etiqueta_email = Label(window_regis, text = "Email * ")
    etiqueta_email.pack()
    entry_email = Entry(window_regis, textvariable = email)
    entry_email.pack()
    
    etiqueta_pass = Label(window_regis, text = "Contraseña * ")
    etiqueta_pass.pack()
    entry_pass = Entry(window_regis, textvariable = password, show = '*')
    entry_pass.pack()
    
    Label(window_regis, text = "").pack()
    Button(window_regis, text = "Registrate", width = 10, height = 1, bg = "lightseagreen", command = registro_user).pack()

def registro_user():
    name_info = nombre.get()
    lname_info = apellido.get()
    email_info = email.get()
    user_info = username.get()
    pass_info = password.get()
    
    file = open(user_info, "w")
    file.write(user_info + "\n")
    file.write(name_info + "\n")
    file.write(lname_info + "\n")
    file.write(email_info + "\n")
    file.write(pass_info)
    file.close()
    
    entry_user.delete(0, END)
    entry_name.delete(0, END)
    entry_lname.delete(0,END)
    entry_email.delete(0,END)
    entry_pass.delete(0, END)
    
    Label(window_regis, text="¡Enhorabuena! \n Te has registrado con éxito.", fg="green", font=("Times New Roman", 10)).pack()

def login():
    global window_login
    window_login = Toplevel(window_p)
    window_login.title("Iniciar Sesión")
    window_login.geometry("300x250")
    Label(window_login, text = "Introduce tu username y contraeña: ").pack()
    Label(window_login, text = "").pack()
    
    global v_user
    global v_password
    
    v_user = StringVar()
    v_password = StringVar()
    
    global entry_login_user
    global entry_login_pass
    
    Label(window_login, text = "Username * ").pack()
    entry_login_user = Entry(window_login, textvariable = v_user)
    entry_login_user.pack()
    
    Label(window_login, text = "").pack()
    
    Label(window_login, text = "Contraseña * ").pack()
    entry_login_pass = Entry(window_login, textvariable = v_password)
    entry_login_pass.pack()
    
    Label(window_login, text = "").pack()
    
    Button(window_login, text = "Login", width = 10, height = 1, bg = "lightseagreen", command = v_login).pack()

def v_login():
    user1 = v_user.get()
    password1 = v_password.get()
    
    entry_login_user.delete(0, END)
    entry_login_pass.delete(0, END)
    
    list_files = os.listdir()#
    if user1 in list_files:
        file1 = open(user1, "r")
        verifica = file1.read().splitlines()
        if password1 in verifica:
            exito_login()
        
        else:
            fail_password()
    
    else:
        fail_user()
        
def exito_login():
    global window_exito
    window_exito = Toplevel(window_login)
    window_exito.title(" <3 Bienvenid@ de nuevo <3 ")
    window_exito.geometry("275x50")
    
    Label(window_exito, text = "Inicio de sesión exitoso, bienvenid@", fg = "green", font = ("Times New Roman", 13)).pack()
    
    Button(window_exito, text = "OK", command=delete_exito_login).pack()
        
def fail_user():
    global window_fail_user
    window_fail_user = Toplevel(window_login)
    window_fail_user.title("Oh no...")
    window_fail_user.geometry("400x100")
    
    Label(window_fail_user, text = "Usuario no encontrado, corrobora los datos ingresados.", fg = "red").pack()
    
    Button(window_fail_user, text = "OK", command = delete_fail_user).pack()
    
def fail_password():
    global window_fail_pass
    window_fail_pass = Toplevel(window_login)
    window_fail_pass.title("Oh no...")
    window_fail_pass.geometry("400x100")
    
    Label(window_fail_pass, text = "Contraseña incorrecta, corrobora los datos ingresados.", fg = "red").pack()
    
    Button(window_fail_pass, text = "OK", command = delete_fail_pass).pack()
    
def delete_exito_login():
    window_exito.destroy()
    
def delete_fail_user():
    window_fail_user.destroy()
    
def delete_fail_pass():
    window_fail_pass.destroy()
    
window_init()
    
    
    
    
    