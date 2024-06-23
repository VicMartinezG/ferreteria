from tkinter import *
from tkinter import messagebox
def buscar():
    buscarcodigo=codigo.get()
    for pos in range(len(acodigo)):
        if buscarcodigo==acodigo[pos]:
           producto.set(aproducto[pos])
           punit.set(apunit[pos])
    messagebox.showinfo("SISTEMA","Producto añadido...")
def calcular():
    importe.set(cantidad.get()*punit.get())
    messagebox.showinfo("SISTEMA","REALIZANDO CALCULO...")

ventana=Tk()
ventana.title("FARMACIA SU SALUD")
ventana.geometry("600x400")
codigo=StringVar()
producto=StringVar()
cantidad=IntVar()
punit=DoubleVar()
importe=IntVar()
acodigo=[]
aproducto=[]
apunit=[]
acodigo.append("001")
aproducto.append("PANADOL ANTIGRIPAL")
apunit.append(3.5)
acodigo.append("002")
aproducto.append("ALCOHOL 1LT")
apunit.append(10)
acodigo.append("003")
aproducto.append("IBUPROFENO")
apunit.append(1.5)
acodigo.append("004")
aproducto.append("PARACETAMOL")
apunit.append(1.2)
acodigo.append("005")
aproducto.append("PAÑALES")
apunit.append(16)
acodigo.append("006")
aproducto.append("JARABE VICK")
apunit.append(18.5)
lbltitulo=Label(ventana,text="STOCK DE MEDICAMENTOS").place(x=150,y=20)
lblcodigo=Label(ventana,text="Codigo: ").place(x=50,y=50)
lblproducto=Label(ventana,text="Producto: ").place(x=50,y=90)
lblcantidad=Label(ventana,text="Cantidad: ").place(x=50,y=130)
lblpunit=Label(ventana,text="Precio Unitario: ").place(x=50,y=170)
lblimporte=Label(ventana,text="Importe total: ").place(x=50,y=210)


txtentry=Entry(ventana,textvariable=codigo).place(x=200,y=50)
txtprod=Entry(ventana,textvariable=producto).place(x=200,y=90)
txtcant=Entry(ventana,textvariable=cantidad).place(x=200,y=130)
txtpunit=Entry(ventana,textvariable=punit).place(x=200,y=170)
txtimporte=Entry(ventana,textvariable=importe).place(x=200,y=210)

btncalcular=Button(ventana,text="Añadir Venta",command=calcular).place(x=100,y=260)
btnbuscar=Button(ventana,text="Buscar Producto",command=buscar).place(x=350,y=50)

ventana.mainloop()
