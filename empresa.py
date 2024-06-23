from tkinter import *
from tkinter import messagebox
def buscar():
    buscarcodigo=codigo.get()
    for pos in range(len(acodigo)):
        if buscarcodigo==acodigo[pos]:
           producto.set(aproducto[pos])
           punit.set(apunit[pos])
    messagebox.showinfo("SISTEMA","Buscando producto")
def calcular():
    importe.set(cantidad.get()*punit.get())
    messagebox.showinfo("SISTEMA","REALIZANDO CALCULO...")

ventana=Tk()
ventana.title("LA TIENDITA DE DON PEPE")
ventana.geometry("600x400")
codigo=StringVar()
producto=StringVar()
cantidad=IntVar()
punit=IntVar()
importe=IntVar()
acodigo=[]
aproducto=[]
apunit=[]
acodigo.append("A001")
aproducto.append("Aceite Vegetal")
apunit.append(9)
acodigo.append("A002")
aproducto.append("Arrroz Costeño")
apunit.append(4)

lbltitulo=Label(ventana,text="SISTEMA ALMACEN").place(x=150,y=20)
lblcodigo=Label(ventana,text="Codigo: ").place(x=50,y=50)
lblproducto=Label(ventana,text="Producto: ").place(x=50,y=90)
lblcantidad=Label(ventana,text="Cantidad: ").place(x=50,y=130)
lblpunit=Label(ventana,text="Precio Unitario: ").place(x=50,y=170)
lblimporte=Label(ventana,text="Importe").place(x=50,y=210)


txtentry=Entry(ventana,textvariable=codigo).place(x=200,y=50)
txtprod=Entry(ventana,textvariable=producto).place(x=200,y=90)
txtcant=Entry(ventana,textvariable=cantidad).place(x=200,y=130)
txtpunit=Entry(ventana,textvariable=punit).place(x=200,y=170)
txtimporte=Entry(ventana,textvariable=importe).place(x=200,y=210)

btncalcular=Button(ventana,text="Calcular Venta",command=calcular).place(x=100,y=260)
btnbuscar=Button(ventana,text="Buscar Producto",command=buscar).place(x=350,y=50)

ventana.mainloop()
