from tkinter import *
from tkinter import messagebox
import os.path
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


root=Tk()
root.attributes("-fullscreen", True)
root.title("Healthy & Tasty")

root.iconbitmap("logo.ico")
root.geometry("1366x768")
root.config(bg="light goldenrod")

miFrame=Frame(root, width=1366, height=768,bg="light goldenrod")
miFrame.pack(expand=True)

if os.path.isfile("users.txt"):
    pass
else:
    diccionarioUsuarios={}
    dicUsers=open("users.txt","w")
    dicUsers.close()

diccionarioUsuarios={}
dicUsers=open("users.txt","r")
usersInformation=dicUsers.read()
dicUsers.close()

listaUsuarios=usersInformation.split()

for i in listaUsuarios:
    nUser=i.split(":")
    diccionarioUsuarios[nUser[0]]=nUser[1]
#--------------------------------------------REGISTRO-------------------------------------------------------------
def registro():
    root.withdraw()
    rootreg=Toplevel()
    rootreg.attributes("-fullscreen", True)
    rootreg.title("Healthy & Tasty - Registro")

    rootreg.iconbitmap("logo.ico")
    rootreg.geometry("1366x768")
    rootreg.config(bg="light goldenrod")
    
    miFramereg=Frame(rootreg, width=1366, height=768,bg="light goldenrod")
    miFramereg.pack(expand=True)
    
    textoUsuario=Label(miFramereg, text="Usuario: ",bg="light goldenrod",fg="black")
    textoUsuario.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuario=Entry(miFramereg)
    cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)

    passwordLabel=Label(miFramereg, text="Clave: ",bg="light goldenrod",fg="black")
    passwordLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroPassword=Entry(miFramereg)
    cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")
    
    def inforeg():
        messagebox.showinfo("Registro", "Has registrado tus datos correctamente")
    def userinuse():
        messagebox.showwarning("Error", "El usuario ingresado ya se encuentra registrado")
    def errorlenuser():
        messagebox.showwarning("Error", "El nombre de usuario debe contener 4 letras como minimo")
    def passworderror():
        messagebox.showwarning("Error", "La clave debe contener al menos un numero y una letra")
    def MenuR():
        rootreg.destroy()
        root.deiconify()
    def registroa1():
        cLetrasU=0
        cNumeros=0
        cLetras=0
        a1=cuadroUsuario.get()
        print(a1)
        b1=cuadroPassword.get()
        print(b1)
        aa1=a1.lower()
        for i in aa1:
            if i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="o" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" or i=="u" or i=="v" or i=="w" or i=="x" or i=="y" or i=="z":
                cLetrasU=cLetrasU+1
        ba1=b1.lower()
        for i in ba1:
            if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
                cNumeros=cNumeros+1
            elif i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="o" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" or i=="u" or i=="v" or i=="w" or i=="x" or i=="y" or i=="z":
                cLetras=cLetras+1
        if cLetrasU<4:
            errorlenuser()
        elif a1 in diccionarioUsuarios:
            userinuse()
        elif cNumeros<1 or cLetras<1:
            passworderror()
        else:
            dicUsers=open("users.txt","a")
            dicUsers.write(a1+":"+b1+"\n")
            dicUsers.close()
            inforeg()
            rootreg.destroy()
            root.deiconify()
    
    botonRegistroa1=Button(miFramereg,bg="green4",fg="white",text="Registrarse", command=registroa1)
    botonRegistroa1.grid(row=2, column=0, padx=10, pady=10)
    
    botonMenuR=Button(miFramereg,bg="green4",fg="white",text="Volver al Menu", command=MenuR)
    botonMenuR.grid(row=2, column=1, padx=10, pady=10)
#---------------------------------FIN REGISTRO------------------------------------
#------------------------------------INICIO------------------------------------------
def inicio():
    root.withdraw()
    rootStart=Toplevel()
    rootStart.attributes("-fullscreen", True)
    rootStart.title("Healthy & Tasty - Inicio de Sesion")

    rootStart.iconbitmap("logo.ico")
    rootStart.geometry("1366x768")
    rootStart.config(bg="light goldenrod")
    
    miFrameStart=Frame(rootStart, width=1366, height=768,bg="light goldenrod")
    miFrameStart.pack(expand=True)
    
    textoUsuarioS=Label(miFrameStart, text="Usuario: ",bg="light goldenrod",fg="black")
    textoUsuarioS.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroUsuarioS=Entry(miFrameStart)
    cuadroUsuarioS.grid(row=0, column=1, padx=10, pady=10)

    passwordLabelS=Label(miFrameStart, text="Clave: ",bg="light goldenrod",fg="black")
    passwordLabelS.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    cuadroPasswordS=Entry(miFrameStart)
    cuadroPasswordS.grid(row=1, column=1, padx=10, pady=10)
    cuadroPasswordS.config(show="*")
        
    def infoStart():
        messagebox.showinfo("Inicio de Sesion", "Has ingresado correctamente")
    def errorlenuserS():
        messagebox.showwarning("Error", "No se encontro el nombre de usuario")
    def passworderrorS():
        messagebox.showwarning("Error", "Clave erronea")
    def MenuS():
        rootStart.destroy()
        root.deiconify()
    def documento():
        info_1= open(""+usuario+".txt","r")
        info_2=info_1.read()
        info_1.close()
    def registroa1S():
        diccionarioUsuarios={}
        dicUsers=open("users.txt","r")
        usersInformation=dicUsers.read()
        dicUsers.close()
            
        listaUsuarios=usersInformation.split()

        for i in listaUsuarios:
            nUser=i.split(":")
            diccionarioUsuarios[nUser[0]]=nUser[1]        
        
        a1S=cuadroUsuarioS.get()
        print(a1S)
        b1S=cuadroPasswordS.get()
        print(b1S)
        
        if a1S not in diccionarioUsuarios:
            errorlenuserS()
        else:
            pass
        b1SV=diccionarioUsuarios[a1S]
        print(b1SV)
        
        if b1S!=b1SV:
            passworderrorS()
#---------------------------------PREGUNTAS1---------------------------------
        
        else:
            
            infoStart()
            rootStart.destroy()
            rootAns=Toplevel()
            rootAns.attributes("-fullscreen", True)
            rootAns.title("Healthy & Tasty - Perfil")
    
            rootAns.iconbitmap("logo.ico")
            rootAns.geometry("1366x768")
            rootAns.config(bg="light goldenrod")
    
            miFrameAns=Frame(rootAns, width=1366, height=768,bg="light goldenrod")
            miFrameAns.pack(expand=True)
    
            varEdad=IntVar()
            varPeso=IntVar()
            varEstatura=IntVar()
            varOpcionb1=IntVar()
            varOpcionb2=IntVar()
    
            textoEdad=Label(miFrameAns,bg="light goldenrod",fg="black",text="1. Que edad tienes?(numero): ").grid(row=0,column=0,sticky=W)
            cuadroEdad=Entry(miFrameAns,textvariable=varEdad)
            cuadroEdad.grid(row=4,column=0,pady=10)
    
            textoPeso=Label(miFrameAns,bg="light goldenrod",fg="black",text="2.Cuanto pesas?(kg): ").grid(row=5,column=0,sticky=W)
            cuadroPeso=Entry(miFrameAns,textvariable=varPeso)
            cuadroPeso.grid(row=7,column=0,pady=10)
    
            textoEstatura=Label(miFrameAns,bg="light goldenrod",fg="black",text="3. Cuanto mides?(en cm): ").grid(row=8,column=0,sticky=W)
            cuadroEstatura=Entry(miFrameAns,textvariable=varEstatura)
            cuadroEstatura.grid(row=11,column=0,pady=10)
    
            textoEnfermedad=Label(miFrameAns,bg="light goldenrod",fg="black",text="5. Sufres de alguna enfermedad alimeticia(Diabetes, Bulimia,Hipoglicemia, etc)?: ").grid(row=8,column=1,columnspan=2,sticky=W)
            Radiobutton(miFrameAns,indicatoron=0,bg="green4",fg="white",text="Si", variable=varOpcionb2, value=1).grid(row=9,column=3,sticky=S,pady=10)
            Radiobutton(miFrameAns,indicatoron=0,bg="green4",fg="white",text="No", variable=varOpcionb2, value=2).grid(row=10,column=3,sticky=N,pady=10)
    
            textoTipo=Label(miFrameAns,bg="light goldenrod",fg="black",text="4. Que tipo de somatotipo posees?: ").grid(row=0,column=1,columnspan=2,sticky=W)
            imagen1=PhotoImage(file="somatotipomod.PNG")
            imagenpuesta1=Label(miFrameAns,image=imagen1).grid(row=1,column=1,columnspan=2,rowspan=7,sticky=N,padx=20)
            imagen2=PhotoImage(file="Edad.PNG")
            imagenpuesta2=Label(miFrameAns,image=imagen2).grid(row=1,column=0,rowspan=3,padx=20)
            imagen3=PhotoImage(file="Peso.PNG")
            imagenpuesta3=Label(miFrameAns,image=imagen3).grid(row=6,column=0)
            imagen4=PhotoImage(file="Altura1.PNG")
            imagenpuesta4=Label(miFrameAns,image=imagen4).grid(row=9,column=0,rowspan=2)
            imagen5=PhotoImage(file="Enfermedad.PNG")
            imagenpuesta5=Label(miFrameAns,image=imagen5).grid(row=9,column=1,columnspan=2,rowspan=2)
            Radiobutton(miFrameAns,indicatoron=0,bg="green4",fg="white",text="Endomorfo", variable=varOpcionb1, value=1).grid(row=1,column=3,sticky=S)
            Radiobutton(miFrameAns,indicatoron=0,bg="green4",fg="white",text="Ectomorfo", variable=varOpcionb1, value=2).grid(row=2,column=3,padx=20)
            Radiobutton(miFrameAns,indicatoron=0,bg="green4",fg="white",text="Mesomorfo", variable=varOpcionb1, value=3).grid(row=3,column=3,sticky=N)
            def erroredad():
                messagebox.showwarning("Error", "Debes ingresar una edad valida")
            def erroropeso():
                messagebox.showwarning("Error", "Debes ingresar un peso valido")
            def errorestatura():
                messagebox.showwarning("Error", "Debes ingresar una estatura valida")
            def errortipoc():
                messagebox.showwarning("Error", "Debe seleccionar tu tipo de cuerpo")
            def errorenfermedad():
                messagebox.showwarning("Error", "Debe seleccionar si padeces una enfermedad")
            def MenuAns1():
                rootAns.destroy()
                root.deiconify() 
            def ejecutarAns1():
                e1=varEdad.get()
                print(e1)
                if e1>16 and e1<64:
                    edad=str(e1)
                    pass
                else:
                    e1=4
                    erroredad()
                e2=varPeso.get()
                print(e2)
                if e2>30 and e2<500:
                    peso=str(e2)
                    pass
                else:
                    e2=4
                    erroropeso()
                e3=varEstatura.get()
                print(e3)
                if e3>130 and e3<210:
                    estatura=str(e3)
                    pass
                else:
                    e3=4
                    errorestatura()
                
                e4=varOpcionb1.get()
                if e4==1:
                    somatotipo=str(e4)
                elif e4==2:
                    somatotipo=str(e4)
                elif e4==3:
                    somatotipo=str(e4)
                else:
                    e4=4
                    errortipoc()
                e5=varOpcionb2.get()
                if e5==1:
                    enfermedad=str(e5)
                elif e5==2:
                    enfermedad=str(e5)
                else:
                    e5=4
                    errorenfermedad()
                    
                if e1==4 or e2==4 or e3==4 or e4==4 or e5==4:
                    pass
#--------------------------------------PREGUNTAS2-------------------------------------------------------------------
                else:
                    rootAns.destroy()
                    rootAns2=Toplevel()
                    rootAns2.attributes("-fullscreen", True)
                    rootAns2.title("Healthy & Tasty")
                    rootAns2.config(bg="light goldenrod")
        
                    rootAns2.iconbitmap("logo.ico")
                    rootAns2.geometry("1366x768")
                    rootAns2.config(bg="light goldenrod")
        
                    miFrameAns2=Frame(rootAns2,width=1366,height=768,bg="light goldenrod")
                    miFrameAns2.pack()
        
                    varObjetivo=IntVar()
                    varEjercicio=IntVar()
                    varEmot=IntVar()
                    varI1=IntVar()
                    varI2=IntVar()
                    varI3=IntVar()
                    varI4=IntVar()
            
                    Label(miFrameAns2,bg="light goldenrod",fg="black",text="6. objetivo: ").grid(row=0,column=0,sticky=W,columnspan=2)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Bajar de peso", variable=varObjetivo, value=1).grid(row=1,column=0,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Ganar masa muscular", variable=varObjetivo, value=2).grid(row=2,column=0,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Tonificar", variable=varObjetivo, value=3).grid(row=3, column=0,sticky=W,columnspan=2,pady=10)
                    label=Label(miFrameAns2)
        
                    Label(miFrameAns2,bg="light goldenrod",fg="black",text="7. Cuantas veces haces ejercicio?: ").grid(row=0,column=2,sticky=W,columnspan=2)
        
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="De 0 a 3 veces por semana", variable=varEjercicio, value=1).grid(row=1,column=2,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="De 4 a 6 veces por semana", variable=varEjercicio, value=2).grid(row=2,column=2,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Mas de 6 veces por semana", variable=varEjercicio, value=3).grid(row=3,column=2,sticky=W,columnspan=2,pady=10)
        
                    imagena1=PhotoImage(file="Diapositiva1.PNG")
                    imagena2=PhotoImage(file="Diapositiva2.PNG")
                    imagena3=PhotoImage(file="Diapositiva3.PNG")
                    imagena4=PhotoImage(file="Diapositiva4.PNG")
                    imagenpuestaa1=Label(miFrameAns2,image=imagena1).grid(row=5,column=0,columnspan=2)
                    imagenpuestaa2=Label(miFrameAns2,image=imagena2).grid(row=5,column=2,columnspan=2)
                    imagenpuestaa3=Label(miFrameAns2,image=imagena3).grid(row=5,column=4,columnspan=2)
                    imagenpuestaa4=Label(miFrameAns2,image=imagena4).grid(row=7,column=1,columnspan=2)
            
                    textoUsuario=Label(miFrameAns2,bg="light goldenrod",fg="black",text="9.Que porcentaje de los siguiente elementos consume: ")
                    textoUsuario.grid(row=4,column=0,sticky=W,padx=10,pady=10,columnspan=6)
        
                    cuadroImga1=Entry(miFrameAns2, textvariable=varI1)
                    cuadroImga1.grid(row=6,column=0,pady=10,columnspan=2)
        
                    cuadroImga2=Entry(miFrameAns2, textvariable=varI2)
                    cuadroImga2.grid(row=6,column=2,pady=10,columnspan=2)
        
                    cuadroImga3=Entry(miFrameAns2, textvariable=varI3)
                    cuadroImga3.grid(row=6,column=4,pady=10,columnspan=2)
        
                    cuadroImga4=Entry(miFrameAns2, textvariable=varI4)
                    cuadroImga4.grid(row=8,column=1,pady=10,columnspan=2)
        
                    textoRecordatorio=Label(miFrameAns2, text="*Recuerde que la suma de los porcentajes\nde los alimentos debe ser igual a 100",bg="light goldenrod",fg="black")
                    textoRecordatorio.grid(row=7,column=3,columnspan=2)
        
                    textoEmot=Label(miFrameAns2,bg="light goldenrod",fg="black",text="8. Ante situaciones emocionales usted: ")
                    textoEmot.grid(row=0,column=4,sticky=W,pady=10,columnspan=2)
        
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Come mas", variable=varEmot, value=1).grid(row=1,column=4,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Come menos", variable=varEmot, value=2).grid(row=2,column=4,sticky=W,columnspan=2,pady=10)
                    Radiobutton(miFrameAns2,indicatoron=0,bg="green4",fg="white",text="Come la misma cantidad", variable=varEmot, value=3).grid(row=3,column=4,sticky=W,columnspan=2,pady=10)
        
                    def errorporcentaje():
                        messagebox.showwarning("Error", "La suma de los porcentajes del consumo de alimentos deben ser igual a 100%")
            
                    def errorobjincomp():
                        messagebox.showwarning("Error", "Debe seleccionar su objetivo")
        
                    def errorrutincompleto():
                        messagebox.showwarning("Error", "Debe seleccionar la frecuencia con la que hace ejercicio")
        
                    def erroreaincompleto():
                        messagebox.showwarning("Error", "Debe seleccionar el comportamiento en situaciones emocionales")
                    def MenuAns2():
                        rootAns2.destroy()
                        root.deiconify()    
                    def ejecutarAns2():
                        c0=0
                        c1=varI1.get()
                        c2=varI2.get()
                        c3=varI3.get()
                        c4=varI4.get()
                        if c1+c2+c3+c4==100:
                            print("Bien")
                        else:
                            c0=4
                            errorporcentaje()
                        c5=varObjetivo.get()
                        if c5==1:
                            print("Bajar peso")
                        elif c5==2:
                            print("Ganar masa muscular")
                        elif c5==3:
                            print("Tonificar")
                        else:
                            c5=4
                            errorobjincomp()
                        c6=varEjercicio.get()
                        if c6==1:
                            print("0 a 3 veces por semana")
                        elif c6==2:
                            print("4 a 6 veces por semana")
                        elif c6==3:
                            print("Mas veces por semana")
                        else:
                            c6=4
                            errorrutincompleto()
                        c7=varEmot.get()
                        if c7==1:
                            print("Come mas")
                        elif c7==2:
                            print("Come menos")  
                        elif c7==3:
                            print("Ninguno")
                        else:
                            c7=4
                            erroreaincompleto()
                        if c0==4 or c5==4 or c6==4 or c7==4:
                            pass
                        else:
                            rootAns2.destroy()
                            rootRes=Toplevel()
                            rootRes.attributes("-fullscreen", True)
                            rootRes.title("Healthy & Tasty")
                    
                            rootRes.iconbitmap("logo.ico")
                            rootRes.geometry("1366x768")
                            rootRes.config(bg="light goldenrod")
                            
                            miFrameRes=Frame(rootRes, width=1366, height=768,bg="light goldenrod")
                            miFrameRes.pack()
                                                   
                            IMC=10000*(int(e2)/(int(e3)*int(e3)))  
                            print(IMC)
                            users=open(""+a1S+".txt","w")
                            users.close()
                            users= open (""+a1S+".txt","a")
                            users.write("Su IMC es: "+str(IMC)+"\n")
                            users.close()
                            textoResW=Label(miFrameRes,bg="light goldenrod",fg="black",font="Verdana",text="Gracias por tu tiempo, este es tu resultado:",)
                            textoResW.grid(row=0,column=0,columnspan=2,pady=20)
                            imcmsgres="Su IMC es "+str(IMC)+":"
                            textoRes=Label(miFrameRes,bg="light goldenrod",fg="black",text=imcmsgres)
                            textoRes.grid(row=1,column=0,padx=10)
                            if e1>=16 and e1<=18:
                                if IMC<17.75:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>25.5:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                            
                            if e1>=19 and e1<=24:
                                if IMC<19:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                
                            if e1>=25 and e1<=34:
                                if IMC<20:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>25:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                
                            if e1>=35 and e1<=44:
                                if IMC<21:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>26:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                
                            if e1>=45 and e1<=54:
                                if IMC<22:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>27:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                
                            if e1>=55 and e1<=64:
                                if IMC<23:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>28:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                
                            if e1>=65:
                                if IMC<24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en desnutrición.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en desnutrición."
                
                                if IMC>29:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Debería consultar a un especialista. Usted puede estar en sobrepeso.\n")
                                    users.close()
                                    anaIMC="Debería consultar a un especialista. Usted puede estar en sobrepeso."
                
                                elif IMC>=19 and IMC<=24:
                                    users= open (""+a1S+".txt","a",encoding='utf-8')
                                    users.write("Usted tiene un peso balanceado acorde a su altura.\n")
                                    users.close()
                                    anaIMC="Usted tiene un peso balanceado acorde a su altura."
                            
                            textoanaIMC=Label(miFrameRes,text=anaIMC,bg="light goldenrod",fg="black")
                            textoanaIMC.grid(row=1,column=1,pady=10)
                            
                            if e4==1:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Endomorfo:\n \nSe le recomienda según su somatotipo debe realizar un tipo de entrenamiento en el cual prevalezca el cardio sin dejar ejercicios de pesas.\nAdemás para estos ejercicios de pesas se recomienda que estén enfocadas en conseguir la tonificación.\nSe recomienda: Ejecutar series con repeticiones moderadas a altas (de ocho a quince)y mantener períodos de descanso cortos entre ejercicios. \n Mantener un ritmo cardíaco elevando durante la mayor parte de una sesión.\n \n ")
                                users.close()
                                somati="Endomorfo: "
                                soma="Se le recomienda según su somatotipo realizar un tipo de entrenamiento en el cual prevalezca el\ncardio  sin  dejar ejercicios de  pesas. Además, para  estos ejercicios de pesas se recomienda que\nestén  enfocadas  en conseguir  la tonificación. Se  recomienda:  Ejecutar series con  repeticiones\nmoderadas  a altas (de ocho a quince) y  mantener períodos de descanso cortos entre ejercicios.\nMantener un ritmo cardíaco elevando durante la mayor parte de una sesión."
                            if e4==2:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Ectomorfo:\n \nSe le recomienda según su somatotipo debe realizar un tipo de entrenamiento que sea breve y de alta intensidad, debe enfocar su trabajo en los grandes grupos musculares.\nAdemás enfoca el ejercicio en el trabajo de fuerza más que en el cardio.\nSe recomienda: Descansar más tiempo entre series para ralentizar el entrenamiento. \n Usar pesas más pesadas ​​para hacer menos repeticiones (cuatro a ocho). \n")
                                users.close()
                                somati="Ectomorfo: "
                                soma="Se le recomienda según su somatotipo realizar un tipo de entrenamiento que sea breve y de alta\nintensidad,  debe  enfocar  su  trabajo  en  los  grandes  grupos  musculares. Además,  enfocar  el\nejercicio  en  el  trabajo  de fuerza  más que  en el cardio. Se recomienda: Descansar más tiempo\nentre  series  para  ralentizar  el  entrenamiento.  Usar  pesas   más   pesadas  ​​para  hacer  menos\nrepeticiones (cuatro a ocho)."
                            if e4==3:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Mesomorfo:\n \nSe le recomienda según su somatotipo debe realizar un tipo de entrenamiento en el cual maneje una proporción entre el cardio y fuerza para mantener el cuerpo.\nSe recomienda: Entrenamiento de pesas través de un esquema de repeticiones amplio (de 3 a 12 repeticiones).\nComplementar con intervalos de cardio de alta intensidad. \n")
                                users.close()
                                somati="Mesomorfo: "
                                soma="Se le recomienda según su somatotipo  realizar un tipo de  entrenamiento en el cual maneje una\nproporción  entre el  cardio y fuerza para mantener el cuerpo. Se recomienda: Entrenamiento de\npesas a  través  de un  esquema  de repeticiones amplio (de 3 a 12 repeticiones). Complementar\ncon intervalos de cardio de alta intensidad."                           
                            textosomati=Label(miFrameRes, text=somati,bg="light goldenrod",fg="black")
                            textosomati.grid(row=2,column=0,padx=10)
                            textosoma=Label(miFrameRes,text=soma,bg="light goldenrod",fg="black")
                            textosoma.grid(row=2,column=1,pady=10)
                   
                            if c5==1:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Bajar de peso:\n \nDisminuya la cantidad de grasa de los alimentos, ya que estas son la mayor fuente de calorías en las comidas. Además de ser difíciles de quemar.\nReduzca las raciones de los alimentos, ya que el objetivo es consumir menos calorías al día Evite las bebidas alcohólicas , pues, además de las calorías vacías que aporta, abre el apetito y hace que te entren unas ganas repentinas de comer compulsivamente alimentos calóricos.\nRealice ejercicio físico diario dentro de sus posibilidades, para quemar las grasas acumuladas y mantener tu cuerpo saludable.\nTome un vaso de agua antes de cada comida. El agua aumenta metabolismo hasta 30% por un periodo de una hora - una hora y medio, así ayudando quemar más calorías. Además se sentirán más llenos así comiendo menos calorías.\nEl consumo de azúcar agregado está directamente relacionado a obesidad y diabetes, por esto debes evitarlo.\nReduce  el consumo de los carbohidratos ya que estos se almacenan como grasa y son difíciles de quemar.\nRespetar las horas de sueño, aproximadamente entre 8 a 10 horas.\n \n")
                                users.close()
                                Objti="Bajar de peso: "
                                Obj="Disminuya la cantidad de grasa de los alimentos, ya que estas son la mayor fuente de calorías en\nlas comidas, además de  ser difíciles de quemar. Reduzca las  raciones de los alimentos, ya que el\nobjetivo  es consumir  menos calorías  al día. Evite las bebidas  alcohólicas , pues, además  de las\ncalorías  vacías que aporta, abre el apetito y hace que te entren unas ganas repentinas de comer\ncompulsivamente  alimentos calóricos. Realice  ejercicio físico diario dentro de sus posibilidades,\npara  quemar  las  grasas  acumuladas  y mantener  tu cuerpo  saludable. Tome  un vaso  de agua\nantes  de cada  comida, el agua  aumenta  metabolismo hasta 30% por un periodo de una hora a\nuna  hora  y  medio ,  ayudando  así  a  quemar  más  calorías ,  además,  se  sentirán  más  llenos\ncomiendo  menos  calorías.  El  consumo  de azúcar  agregado  está  directamente  relacionado a\nobesidad  y diabetes, por  esto  debes  evitarlo. Reduce  el consumo  de los carbohidratos ya que\nestos  se  almacenan   como grasa  y  son  difíciles  de  quemar .   Respetar  las  horas  de  sueño ,\naproximadamente entre 8 a 10 horas."
                            elif c5==2:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Ganar masa muscular:\n \nPara aumentar nuestra masa muscular de forma efectiva necesitamos un superávit calórico de entre unas 500 a 1000 calorías diarias.\nNo saltarse las comidas, ya que el objetivo es aumentar la porción de calorías al día.\nEs importante consumir frecuentemente proteína en cada comida para mantener un aporte óptimo de aminoácidos en sangre y mantener los músculos bien alimentados.\nConsumir grasas buenas\nMantente bien hidratado durante los entrenamientos, esto es  muy importante ya que evita la pérdida de apetito. Además de esto, mantenerse bien hidratado mejora la calidad de los entrenamientos.\nConsumir por lo menos 2 frutas por día, ya que estas brindan carbohidratos naturales y proporcionan energía.\nEvita azúcares y alimentos procesados ya que estos carbohidratos y grasas se almacenan y son difíciles de quemar. Además estos pueden generar enfermedades como diabetes o problemas como el colesterol. Lo cual puede alterar el equilibrio de tu cuerpo.\n \n")
                                users.close()
                                Objti="Ganar masa muscular: "
                                Obj="Para  aumentar nuestra masa  muscular de forma  efectiva necesitamos  un superávit calórico de\nentre unas 500 a 1000 calorías diarias. No saltarse las comidas, ya que el objetivo es aumentar la\nporción  de  calorías  al  día. Es  importante  consumir  frecuentemente  proteína en cada comida\npara  mantener  un  aporte  óptimo  de  aminoácidos  en  sangre  y  mantener  los músculos bien\nalimentados.  Consumir  grasas  buenas. Mantente  bien  hidratado  durante los entrenamientos,\nesto  es  muy  importante  ya que  evita la  pérdida de apetito, además de esto, mejora la calidad\nde   los   entrenamientos .  Consumir   por   lo   menos  2  frutas  por  día , ya  que  estas   brindan\ncarbohidratos  naturales  y  proporcionan energía. Evita  azúcares y alimentos procesados ya que\nestos  carbohidratos  y grasas  se almacenan  y son  difíciles  de quemar,  además,  estos  pueden\ngenerar  enfermedades  como  diabetes o  problemas como  el  colesterol, lo  cual  puede alterar\nel equilibrio de tu cuerpo."
                            elif c5==3:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Tonificar:\nDetermina tus necesidades calóricas diarias. Deberás restarle unas quinientas (500) calorías diarias para perder peso de forma gradual y saludable.\nEvita siempre bajar de peso de forma rápida. Ya que esto puede hacer que se pierda el músculo magro\nAsegúrate de que tu metabolismo se mantenga acelerado. Es recomendable es hacer pequeñas comidas cada cuatro horas.\nEvita al máximo el consumo de grasas saturadas y calorías vacías como las que aportan las bebidas alcohólicas. Siempre mantén un 30% de esas calorías diarias en forma de proteínas.\nConsume las proteínas junto con una porción de carbohidratos del tipo saludable como los cereales integrales, vegetales. Ten en cuenta que las carnes deben ser magras y de preferencia blancas como pescado, pavo o pollo.\n \n ")
                                users.close()
                                Objti="Tonificar: "
                                Obj="Determina  tus  necesidades  calóricas  diarias. Deberás  restarle  unas  quinientas  (500)  calorías\ndiarias  para  perder  peso  de forma  gradual y  saludable. Evita  siempre bajar de peso de forma\nrápida ,  ya  que  esto  puede  hacer  que  se  pierda  el  músculo  magro  .  Asegúrate  de  que  tu\nmetabolismo  se mantenga acelerado. Es recomendable es hacer pequeñas comidas cada cuatro\nhoras.  Evita  al máximo  el consumo  de grasas  saturadas y calorías vacías como las que aportan\nlas bebidas  alcohólicas. Siempre  mantén un 30% de esas calorías diarias en forma de proteínas.\nConsume  las  proteínas  junto  con  una  porción  de  carbohidratos  del  tipo saludable como los\ncereales  integrales,  vegetales. Ten  en  cuenta que las carnes deben ser magras y de preferencia\nblancas como pescado, pavo o pollo."
                            textoObjetivoti=Label(miFrameRes, text=Objti,bg="light goldenrod",fg="black")
                            textoObjetivoti.grid(row=3,column=0,padx=10)
                            textoObjetivo=Label(miFrameRes, text=Obj,bg="light goldenrod",fg="black")
                            textoObjetivo.grid(row=3,column=1,pady=10)
                            if c6==1:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Entrenas de 0 a 3 veces por semana:\nDeberías incrementar el ejercicio que haces por semana ya que en estos tiempos de cuarentena, se está la mayor parte del tiempo quieto y sedentario.\n \n ")
                                users.close()
                                Ejcti="Entrenas de 0 a 3 veces por semana: "
                                Ejc="Deberías incrementar el ejercicio que haces por semana ya que, en\nestos  tiempos  de  cuarentena,  se está la mayor  parte del  tiempo\nquieto y sedentario."
                            elif c6==2:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Entrenas de 4 a 6 veces por semana:\n \nEstás haciendo el ejercicio suficiente para mantener tu cuerpo en forma durante la cuarentena, sigue así.\n \n")
                                users.close()
                                Ejcti="Entrenas de 4 a 6 veces por semana: "
                                Ejc="Estás  haciendo  el ejercicio  suficiente para mantener tu cuerpo en\nforma durante la cuarentena, sigue así."
                            elif c6==3:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("Entrenas más de 6 veces por semana:\nExcelente, muy buen trabajo, no pierdes la costumbre a pesar de la cuarentena.")
                                users.close()
                                Ejcti="Entrenas más de 6 veces por semana: "
                                Ejc="Excelente,  muy  buen  trabajo, no pierdes la costumbre a pesar de\nla cuarentena."
                            textoEjercicioti=Label(miFrameRes, text=Ejcti,bg="light goldenrod",fg="black")
                            textoEjercicioti.grid(row=4,column=0,padx=10)
                            textoEjercicio=Label(miFrameRes, text=Ejc,bg="light goldenrod",fg="black",)
                            textoEjercicio.grid(row=4,column=1,pady=10)
                            if c7==1:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("\n \n Es normal que las personas suelan tener situaciones de ansiedad, por ende se debería tener en mente unas opciones saludables para esos momentos\nTe recomendamos que antes situaciones emocionales mantengas la calma y si persiste intenta comer alimentos como:\nchocolate amargo o maní\nmanzana verde\ntomar aromáticas o té\nsin descuidar las cantidades de estas\nSi persiste deberías consultar a un médico.")
                                users.close()
                                Emtresti="Consejo: "
                                Emtres="Es normal que las personas suelan tener  situaciones de ansiedad, por ende, se debería tener en\nmente unas opciones saludables para  esos momentos. Te recomendamos que antes situaciones\nemocionales mantengas la calma y si  persiste intenta comer alimentos como: chocolate amargo\no maní, manzana verde, tomar aromáticas o té (sin descuidar las cantidades de estas), si persiste\ndeberías consultar a un médico."
                            elif c7==2:
                                users= open (""+a1S+".txt","a",encoding='utf-8')
                                users.write("\n \n Es normal que las personas suelan tener situaciones de ansiedad, por ende se debería tener en mente unas opciones saludables para esos momentos.\nDebes tener siempre en mente que tu cuerpo necesita comer todas las comidas del día, por lo que no puedes descuidar ninguna de ellas.\nEn caso de que persista, consultar a un médico.")
                                users.close()    
                                Emtresti="Consejo: "
                                Emtres="Es normal que las personas suelan tener  situaciones de ansiedad, por ende, se debería tener en\nmente  unas opciones  saludables para esos  momentos. Debes tener  siempre en  mente que tu\ncuerpo  necesita  comer  todas las  comidas del día, por  lo que no  puedes descuidar ninguna de\nellas, en caso de que persista debes consultar a un médico."
                            elif c7==3:
                                Emtresti=" "
                                Emtres=" "
                                                         
                            textoEmotti=Label(miFrameRes, text=Emtresti,bg="light goldenrod",fg="black")
                            textoEmotti.grid(row=5,column=0,padx=10)
                            textoEmot=Label(miFrameRes, text=Emtres,bg="light goldenrod",fg="black")
                            textoEmot.grid(row=5,column=1,pady=10)
                            textoEmotti=Label(miFrameRes, text="Ingresa tu correo para recibir tu rutina: ",bg="light goldenrod",fg="black")
                            textoEmotti.grid(row=6,column=0,padx=10)
                            varEmail=StringVar()
                            cuadroemail=Entry(miFrameRes, textvariable=varEmail)
                            cuadroemail.grid(row=6,column=1,pady=10,columnspan=2)
                                                                                    
                            def enviarcorreo():
                                em=varEmail.get()
                                info_1=open(a1S+".txt","r")
                                info_2=info_1.read()
                                info_1.close()
                                msg=MIMEMultipart()
                                message=(info_2)
                                password="Hytpy123."
                                msg['From']="healthyandtasty.registro@gmail.com"
                                msg['To']=em
                                msg['Subject']="Rutina"

                                msg.attach(MIMEText(message, 'plain'))

                                server = smtplib.SMTP('smtp.gmail.com: 587')
                                server.starttls()

                                server.login(msg['From'], password)

                                server.sendmail(msg['From'], msg['To'], msg.as_string())
                                server.quit()
                                messagebox.showinfo("Informacion","Correo enviado exitosamente")
                                
                                
                            def MenuRes():
                                rootRes.destroy()
                                root.deiconify()
                                
                            botonEmail=Button(miFrameRes,bg="green4",fg="white",text="Enviar al correo", command=enviarcorreo)
                            botonEmail.grid(row=7,column=0,columnspan=2,pady=20)
                            botonMenuRes=Button(miFrameRes,bg="green4",fg="white",text="Volver al Menu", command=MenuRes)
                            botonMenuRes.grid(row=7,column=1,columnspan=2,pady=20)
                            
#-------------------------------VENTANA RESULTADO---------------------------
                    botonIngAns1=Button(miFrameAns2,bg="green4",fg="white",text="Ingresar datos", command=ejecutarAns2)
                    botonIngAns1.grid(row=9,column=2,pady=10)
                    botonMenuAns2=Button(miFrameAns2,bg="green4",fg="white",text="Volver al Menu", command=MenuAns2)
                    botonMenuAns2.grid(row=9,column=3,pady=10)
            
                    rootAns2.mainloop()
#-------------------------------------FIN PREGUNTAS2----------------------------------------------            
            botonIngresoAns1=Button(miFrameAns,bg="green4",fg="white",text="Siguiente", command=ejecutarAns1)
            botonIngresoAns1.grid(row=11,column=1)
            botonMenuAns1=Button(miFrameAns,bg="green4",fg="white",text="Volver al Menu", command=MenuAns1)
            botonMenuAns1.grid(row=11,column=2)
            rootAns.mainloop()
#-------------------------------------FIN PREGUNTAS 1---------------------------------    
    botonRegistroa1S=Button(miFrameStart,bg="green4",fg="white",text="Iniciar Sesion", command=registroa1S)
    botonRegistroa1S.grid(row=2, column=0, padx=10, pady=10)
    botonMenuS=Button(miFrameStart,bg="green4",fg="white",text="Volver al Menu", command=MenuS)
    botonMenuS.grid(row=2, column=1, padx=10, pady=10)
    
    rootStart.mainloop()

#/////////////////////////////////////////FIN INICIO/////////////////////////////////////////
botonRegistro=Button(miFrame, text="Registrarse", bg="green4", width=20, height=8, fg="white", font="Verdana", command=registro)
botonRegistro.grid(row=0, column=0, padx=10, pady=10)

botonIngreso=Button(miFrame, text="Ingresar", bg="green4", width=20, height=8, fg="white", font="Verdana", command=inicio)
botonIngreso.grid(row=1, column=0, padx=10, pady=10)

botonSalir=Button(miFrame, text="Salir", bg="green4", width=20, height=8, fg="white", font="Verdana", command=root.destroy)
botonSalir.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()