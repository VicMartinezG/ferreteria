from tkinter import *
from tkinter import messagebox
def buscar():
    buscararticulo=articulo.get()
    for pos in range(len(aarticulo)):
        if buscararticulo==aarticulo[pos]:
           producto.set(aproducto[pos])
           punit.set(apunit[pos])
    messagebox.showinfo("SISTEMA","BUSCANDO PRODUCTO...")
        
def calcular():
    importe.set(cantidad.get()*punit.get())
    messagebox.showinfo("SISTEMA","CALCULANDO...")

    
ventana=Tk()
ventana.title("FERRETODO")
ventana.geometry("600x400")

producto=StringVar()
articulo=StringVar()
cantidad=IntVar()
punit=DoubleVar()
importe=IntVar()

aarticulo=[]
aproducto=[]
apunit=[]
aarticulo.append("001")
aproducto.append("ARENA X M3")
apunit.append(3.5)
aarticulo.append("002")
aproducto.append("CEMENTO BOLSA")
apunit.append(10)
aarticulo.append("003")
aproducto.append("FIERRO 1/4")
apunit.append(1.5)
aarticulo.append("004")
aproducto.append("TUBOS DE PVC")
apunit.append(1.2)
aarticulo.append("005")
aproducto.append("PEGAMENTOS")
apunit.append(16)
aarticulo.append("006")
aproducto.append("WINCHA")
apunit.append(18.5)
aarticulo.append("007")
aproducto.append("CABLES COBRE X METROS")
apunit.append(18.5)
aarticulo.append("008")
aproducto.append("PIEDRA CHANCADA")
apunit.append(18.5)
aarticulo.append("009")
aproducto.append("DESTORNILLADOR")
apunit.append(18.5)
aarticulo.append("010")
aproducto.append("ALICATE")
apunit.append(18.5)

lbltitulo=Label(ventana,text="STOCK DE MATERIALES").place(x=150,y=20)
lblarticulo=Label(ventana,text="Codigo: ").place(x=50,y=50)
lblproducto=Label(ventana,text="Producto: ").place(x=50,y=90)
lblcantidad=Label(ventana,text="Cantidad: ").place(x=50,y=130)
lblpunit=Label(ventana,text="Precio Unitario: ").place(x=50,y=170)
lblimporte=Label(ventana,text="Importe total: ").place(x=50,y=210)


txtentry=Entry(ventana,textvariable=articulo).place(x=200,y=50)
txtprod=Entry(ventana,textvariable=producto).place(x=200,y=90)
txtcant=Entry(ventana,textvariable=cantidad).place(x=200,y=130)
txtpunit=Entry(ventana,textvariable=punit).place(x=200,y=170)
txtimporte=Entry(ventana,textvariable=importe).place(x=200,y=210)

btncalcular=Button(ventana,text="Añadir Venta",command=calcular).place(x=100,y=260)
btnbuscar=Button(ventana,text="Buscar Producto",command=buscar).place(x=350,y=50)

ventana.mainloop()
