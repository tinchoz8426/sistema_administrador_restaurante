from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import datetime
import pywhatkit

# Funciones
def reset():
    reciept_entry.delete(1.0, END)
    e_pollo.set("0")
    e_pizza.set("0")
    e_hamburgesa.set("0")
    e_ensalada.set("0")
    e_papas_fritas.set("0")
    e_sopa.set("0")
    e_sanguche.set("0")
    e_asado.set("0")
    e_tacos.set("0")

    e_gaseosa.set("0")
    e_agua_mineral.set("0")
    e_vino.set("0")
    e_cerveza.set("0")
    e_licuado.set("0")
    e_jugo.set("0")
    e_limonada.set("0")
    e_bebida_energetica.set("0")
    e_cafe.set("0")

    e_helado.set("0")
    e_flan.set("0")
    e_torta.set("0")
    e_pastafrola.set("0")
    e_cheesecake.set("0")
    e_trufas.set("0")
    e_budin.set("0")
    e_rosquillas.set("0")
    e_frutas.set("0")    

    pollo_entry.config(state=DISABLED)
    pizza_entry.config(state=DISABLED)
    hamburgesa_entry.config(state=DISABLED)
    ensalada_entry.config(state=DISABLED)
    papas_fritas_entry.config(state=DISABLED)
    sopa_entry.config(state=DISABLED)
    sanguche_entry.config(state=DISABLED)
    asado_entry.config(state=DISABLED)
    tacos_entry.config(state=DISABLED)

    gaseosa_entry.config(state=DISABLED)    
    agua_mineral_entry.config(state=DISABLED)
    vino_entry.config(state=DISABLED)
    cerveza_entry.config(state=DISABLED)
    licuado_entry.config(state=DISABLED)
    jugo_entry.config(state=DISABLED)
    limonada_entry.config(state=DISABLED)
    bebida_energetica_entry.config(state=DISABLED)
    cafe_entry.config(state=DISABLED)

    helado_entry.config(state=DISABLED)
    flan_entry.config(state=DISABLED)
    torta_entry.config(state=DISABLED)
    pastafrola_entry.config(state=DISABLED)
    cheesecake_entry.config(state=DISABLED)
    trufas_entry.config(state=DISABLED)
    budin_entry.config(state=DISABLED)
    rosquillas_entry.config(state=DISABLED)
    frutas_entry.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    cost_of_food_var.set("")
    cost_of_drink_var.set("")
    cost_of_cake_var.set("")
    subtotal_var.set("")
    tax_var.set("")
    total_var.set("")

def send():
    if reciept_entry.get(1.0, END) == "\n":
        messagebox.showerror("Error", "No has cargado un pedido.")
    else:
        def send_message():
            message = text_area.get(1.0, END)
            number = number_field.get()
            now = datetime.datetime.now()
            pywhatkit.sendwhatmsg(number, message, now.hour, now.minute + 1)

        root2 = Toplevel()

        root2.title("Enviar cuenta")
        root2.config(bg="grey")
        root2.geometry("485x650+50+50")
        root2.resizable(height=0, width=0)

        logo_image = PhotoImage(file="sending.png")
        label = Label(root2, image=logo_image, bg="grey")
        label.pack()

        number_label = Label(root2, text="Numero de celular", font=('arial', 19, 'bold'), bg="grey", fg="white")
        number_label.pack(pady=4)

        number_field = Entry(root2, font=('arial', 19, 'bold'), bd=3, width=24)
        number_field.pack(pady=4)

        bill_label = Label(root2, text="Detalles de la cuenta", font=('arial', 19, 'bold'), bg="grey", fg="white")
        bill_label.pack(pady=4)

        text_area = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=10)
        text_area.pack(pady=4)
        text_area.insert(END, "Recibo: " + "\t\t" + bill_number + "\t\t       " + date + "\n")

        if cost_of_food_var.get() != "0 ARS":
            text_area.insert(END, f"Costo de la comida\t\t\t{price_of_food} ARS\n")
        if cost_of_drink_var.get() != "0 ARS":
            text_area.insert(END, f"Costo de la bebida\t\t\t{price_of_drink} ARS\n")
        if cost_of_cake_var.get() != "0 ARS":
            text_area.insert(END, f"Costo del postre\t\t\t{price_of_cake} ARS\n")

        text_area.insert(END, f"Subtotal:\t\t\t{subtotal_items} ARS\n")
        text_area.insert(END, f"Impuesto:\t\t\t{50} ARS\n")
        text_area.insert(END, f"Total:\t\t\t{total_items} ARS\n")

        send_button = Button(root2, text="Enviar", font=('arial', 19, 'bold'), command=send_message)
        send_button.pack(pady=4)

        root2.mainloop()

def save():
    if reciept_entry.get(1.0, END) == "\n":
        messagebox.showerror("Error", "Recibo vacio")
    else:
        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if url == None:
            pass
        else:
            bill_data = reciept_entry.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo("Información", "¡Tu cuenta ha sido guardada!")

def receipt():
    global bill_number, date

    if cost_of_food_var.get() != '' or cost_of_drink_var.get() != '' or cost_of_cake_var.get() != '':
        reciept_entry.delete(1.0, END)
        x = random.randint(100, 10000)
        bill_number = "Cuenta: " + str(x)
        date = time.strftime("%d/%m/%y")
        reciept_entry.insert(END, "Recibo: " + "\t\t" + bill_number + "\t\t       " + date + "\n")
        reciept_entry.insert(END, "********************************************************************\n")
        reciept_entry.insert(END, "Items:\t\t Costo (ARS):\n")
        reciept_entry.insert(END, "********************************************************************\n")

        if e_pollo.get() !="0":
            reciept_entry.insert(END, f"Pollo\t\t\t{int(e_pollo.get())*500} ARS\n")
        if e_pizza.get() !="0":
            reciept_entry.insert(END, f"Pizza\t\t\t{int(e_pizza.get())*400} ARS\n")
        if e_hamburgesa.get() !="0":
            reciept_entry.insert(END, f"Hamburguesa\t\t\t{int(e_hamburgesa.get())*350} ARS\n")
        if e_ensalada.get() !="0":
            reciept_entry.insert(END, f"Ensalada\t\t\t{int(e_ensalada.get())*200} ARS\n")
        if e_papas_fritas.get() !="0":
            reciept_entry.insert(END, f"Papas fritas\t\t\t{int(e_papas_fritas.get())*250} ARS\n")
        if e_sopa.get() !="0":
            reciept_entry.insert(END, f"Sopa\t\t\t{int(e_sopa.get())*150} ARS\n")
        if e_sanguche.get() !="0":
            reciept_entry.insert(END, f"Sánguche\t\t\t{int(e_sanguche.get())*200} ARS\n")
        if e_asado.get() !="0":
            reciept_entry.insert(END, f"Asado\t\t\t{int(e_asado.get())*600} ARS\n")
        if e_tacos.get() !="0":
            reciept_entry.insert(END, f"Tacos\t\t\t{int(e_tacos.get())*150} ARS\n")

        if e_gaseosa.get() !="0":
            reciept_entry.insert(END, f"Gaseosa\t\t\t{int(e_gaseosa.get())*500} ARS\n")
        if e_agua_mineral.get() !="0":
            reciept_entry.insert(END, f"Agua mineral\t\t\t{int(e_agua_mineral.get())*400} ARS\n")
        if e_vino.get() !="0":
            reciept_entry.insert(END, f"Vino\t\t\t{int(e_vino.get())*350} ARS\n")    
        if e_cerveza.get() !="0":
            reciept_entry.insert(END, f"Cerveza\t\t\t{int(e_cerveza.get())*200} ARS\n")    
        if e_licuado.get() !="0":
            reciept_entry.insert(END, f"Licuado\t\t\t{int(e_licuado.get())*250} ARS\n")  
        if e_jugo.get() !="0":
            reciept_entry.insert(END, f"Jugo\t\t\t{int(e_jugo.get())*150} ARS\n")  
        if e_limonada.get() !="0":
            reciept_entry.insert(END, f"Limonada\t\t\t{int(e_limonada.get())*200} ARS\n")  
        if e_bebida_energetica.get() !="0":
            reciept_entry.insert(END, f"Bebida energetica\t\t\t{int(e_bebida_energetica.get())*600} ARS\n")  
        if e_cafe.get() !="0":
            reciept_entry.insert(END, f"Café\t\t\t{int(e_cafe.get())*150} ARS\n")  

        if e_helado.get() !="0":
            reciept_entry.insert(END, f"Helado\t\t\t{int(e_helado.get())*500} ARS\n")  
        if e_flan.get() !="0":
            reciept_entry.insert(END, f"Flan\t\t\t{int(e_flan.get())*400} ARS\n")  
        if e_torta.get() !="0":
            reciept_entry.insert(END, f"Torta\t\t\t{int(e_torta.get())*350} ARS\n")  
        if e_pastafrola.get() !="0":
            reciept_entry.insert(END, f"Pastafrola\t\t\t{int(e_pastafrola.get())*200} ARS\n")
        if e_cheesecake.get() !="0":
            reciept_entry.insert(END, f"Cheesecake\t\t\t{int(e_cheesecake.get())*250} ARS\n")
        if e_trufas.get() !="0":
            reciept_entry.insert(END, f"Trufas\t\t\t{int(e_trufas.get())*150} ARS\n")   
        if e_budin.get() !="0":
            reciept_entry.insert(END, f"Budin\t\t\t{int(e_budin.get())*200} ARS\n")   
        if e_rosquillas.get() !="0":
            reciept_entry.insert(END, f"Rosquillas\t\t\t{int(e_rosquillas.get())*600} ARS\n")  
        if e_frutas.get() !="0":
            reciept_entry.insert(END, f"Frutas\t\t\t{int(e_frutas.get())*150} ARS\n")  

        reciept_entry.insert(END, "********************************************************************\n")

        if cost_of_food_var.get() != "0 ARS":
            reciept_entry.insert(END, f"Costo de la comida\t\t\t{price_of_food} ARS\n")
        if cost_of_drink_var.get() != "0 ARS":
            reciept_entry.insert(END, f"Costo de la bebida\t\t\t{price_of_drink} ARS\n")
        if cost_of_cake_var.get() != "0 ARS":
            reciept_entry.insert(END, f"Costo del postre\t\t\t{price_of_cake} ARS\n")

        reciept_entry.insert(END, "********************************************************************\n")

        reciept_entry.insert(END, f"Subtotal:\t\t\t{subtotal_items} ARS\n")
        reciept_entry.insert(END, f"Impuesto:\t\t\t{50} ARS\n")
        reciept_entry.insert(END, f"Total:\t\t\t{total_items} ARS\n")
    else:
        messagebox.showerror('Error','No ha seleccionado ningun item.')

def total_cost():
    global price_of_food, price_of_drink, price_of_cake, subtotal_items, receipt, total_items

    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1 = int(e_pollo.get())
        item2 = int(e_pizza.get())
        item3 = int(e_hamburgesa.get())
        item4 = int(e_ensalada.get())
        item5 = int(e_papas_fritas.get())
        item6 = int(e_sopa.get())
        item7 = int(e_sanguche.get())
        item8 = int(e_asado.get())
        item9 = int(e_tacos.get())

        item10 = int(e_gaseosa.get())
        item11 = int(e_agua_mineral.get())
        item12 = int(e_vino.get())
        item13 = int(e_cerveza.get())
        item14 = int(e_licuado.get())
        item15 = int(e_jugo.get())
        item16 = int(e_limonada.get())
        item17 = int(e_bebida_energetica.get())
        item18 = int(e_cafe.get())

        item19 = int(e_helado.get())
        item20 = int(e_flan.get())
        item21 = int(e_torta.get())
        item22 = int(e_pastafrola.get())
        item23 = int(e_cheesecake.get())
        item24 = int(e_trufas.get())
        item25 = int(e_budin.get())
        item26 = int(e_rosquillas.get())
        item27 = int(e_frutas.get())

        price_of_food = (item1*500) + (item2*400) + (item3*350) + (item4*200) + (item5*250) + (item6*150) + (item7*200) + (item8*600) + (item9*150)
        price_of_drink = (item10*500) + (item11*400) + (item12*350) + (item13*200) + (item14*250) + (item15*150) + (item16*200) + (item17*600) + (item18*150)
        price_of_cake = (item19*500) + (item20*400) + (item21*350) + (item22*200) + (item23*250) + (item24*150) + (item25*200) + (item26*600) + (item27*150)

        cost_of_food_var.set(str(price_of_food) + " ARS")
        cost_of_drink_var.set(str(price_of_drink) + " ARS")
        cost_of_cake_var.set(str(price_of_cake) + " ARS")

        subtotal_items = price_of_food + price_of_drink + price_of_cake
        subtotal_var.set(str(subtotal_items) + " ARS")

        tax_var.set("50 ARS")

        total_items = subtotal_items + 50
        total_var.set(str(total_items) + " ARS")
    else:
        messagebox.showerror("Error", "No ha seleccionado ningun item.")

def pollo():
    if var1.get()==1:
        pollo_entry.config(state=NORMAL)
        pollo_entry.delete(0, END)
        pollo_entry.focus()
    else:
        pollo_entry.config(state=DISABLED)
        e_pollo.set("0")

def pizza():
    if var2.get()==1:
        pizza_entry.config(state=NORMAL)
        pizza_entry.delete(0, END)
        pizza_entry.focus()
    else:
        pizza_entry.config(state=DISABLED)
        e_pizza.set("0")

def hamburguesa():
    if var3.get()==1:
        hamburgesa_entry.config(state=NORMAL)
        hamburgesa_entry.delete(0, END)
        hamburgesa_entry.focus()
    else:
        hamburgesa_entry.config(state=DISABLED)
        e_hamburgesa.set("0")

def ensalada():
    if var4.get()==1:
        ensalada_entry.config(state=NORMAL)
        ensalada_entry.delete(0, END)
        ensalada_entry.focus()
    else:
        ensalada_entry.config(state=DISABLED)
        e_ensalada.set("0")

def papas_fritas():
    if var5.get()==1:
        papas_fritas_entry.config(state=NORMAL)
        papas_fritas_entry.delete(0, END)
        papas_fritas_entry.focus()
    else:
        papas_fritas_entry.config(state=DISABLED)
        e_papas_fritas.set("0")

def sopa():
    if var6.get()==1:
        sopa_entry.config(state=NORMAL)
        sopa_entry.delete(0, END)
        sopa_entry.focus()
    else:
        sopa_entry.config(state=DISABLED)
        e_sopa.set("0")

def sanguche():
    if var7.get()==1:
        sanguche_entry.config(state=NORMAL)
        sanguche_entry.delete(0, END)
        sanguche_entry.focus()
    else:
        sanguche_entry.config(state=DISABLED)
        e_sanguche.set("0")

def asado():
    if var8.get()==1:
        asado_entry.config(state=NORMAL)
        asado_entry.delete(0, END)
        asado_entry.focus()
    else:
        asado_entry.config(state=DISABLED)
        e_asado.set("0")

def tacos():
    if var9.get()==1:
        tacos_entry.config(state=NORMAL)
        tacos_entry.delete(0, END)
        tacos_entry.focus()
    else:
        tacos_entry.config(state=DISABLED)
        e_tacos.set("0")

def gaseosa():
    if var10.get()==1:
        gaseosa_entry.config(state=NORMAL)
        gaseosa_entry.delete(0, END)
        gaseosa_entry.focus()
    else:
        gaseosa_entry.config(state=DISABLED)
        e_gaseosa.set("0")

def agua_mineral():
    if var11.get()==1:
        agua_mineral_entry.config(state=NORMAL)
        agua_mineral_entry.delete(0, END)
        agua_mineral_entry.focus()
    else:
        agua_mineral_entry.config(state=DISABLED)
        e_agua_mineral.set("0")

def vino():
    if var12.get()==1:
        vino_entry.config(state=NORMAL)
        vino_entry.delete(0, END)
        vino_entry.focus()
    else:
        vino_entry.config(state=DISABLED)
        e_vino.set("0")

def cerveza():
    if var13.get()==1:
        cerveza_entry.config(state=NORMAL)
        cerveza_entry.delete(0, END)
        cerveza_entry.focus()
    else:
        cerveza_entry.config(state=DISABLED)
        e_cerveza.set("0")

def licuado():
    if var14.get()==1:
        licuado_entry.config(state=NORMAL)
        licuado_entry.delete(0, END)
        licuado_entry.focus()
    else:
        licuado_entry.config(state=DISABLED)
        e_licuado.set("0")

def jugo():
    if var15.get()==1:
        jugo_entry.config(state=NORMAL)
        jugo_entry.delete(0, END)
        jugo_entry.focus()
    else:
        jugo_entry.config(state=DISABLED)
        e_jugo.set("0")

def limonada():
    if var16.get()==1:
        limonada_entry.config(state=NORMAL)
        limonada_entry.delete(0, END)
        limonada_entry.focus()
    else:
        limonada_entry.config(state=DISABLED)
        e_limonada.set("0")

def bebida_energetica():
    if var17.get()==1:
        bebida_energetica_entry.config(state=NORMAL)
        bebida_energetica_entry.delete(0, END)
        bebida_energetica_entry.focus()
    else:
        bebida_energetica_entry.config(state=DISABLED)
        e_bebida_energetica.set("0")

def cafe():
    if var18.get()==1:
        cafe_entry.config(state=NORMAL)
        cafe_entry.delete(0, END)
        cafe_entry.focus()
    else:
        cafe_entry.config(state=DISABLED)
        e_cafe.set("0")

def helado():
    if var19.get()==1:
        helado_entry.config(state=NORMAL)
        helado_entry.delete(0, END)
        helado_entry.focus()
    else:
        helado_entry.config(state=DISABLED)
        e_helado.set("0")

def flan():
    if var20.get()==1:
        flan_entry.config(state=NORMAL)
        flan_entry.delete(0, END)
        flan_entry.focus()
    else:
        flan_entry.config(state=DISABLED)
        e_flan.set("0")

def torta():
    if var21.get()==1:
        torta_entry.config(state=NORMAL)
        torta_entry.delete(0, END)
        torta_entry.focus()
    else:
        torta_entry.config(state=DISABLED)
        e_torta.set("0")

def pastafrola():
    if var22.get()==1:
        pastafrola_entry.config(state=NORMAL)
        pastafrola_entry.delete(0, END)
        pastafrola_entry.focus()
    else:
        pastafrola_entry.config(state=DISABLED)
        e_pastafrola.set("0")

def cheesecake():
    if var23.get()==1:
        cheesecake_entry.config(state=NORMAL)
        cheesecake_entry.delete(0, END)
        cheesecake_entry.focus()
    else:
        cheesecake_entry.config(state=DISABLED)
        e_cheesecake.set("0")

def trufas():
    if var24.get()==1:
        trufas_entry.config(state=NORMAL)
        trufas_entry.delete(0, END)
        trufas_entry.focus()
    else:
        trufas_entry.config(state=DISABLED)
        e_trufas.set("0")

def budin():
    if var25.get()==1:
        budin_entry.config(state=NORMAL)
        budin_entry.delete(0, END)
        budin_entry.focus()
    else:
        budin_entry.config(state=DISABLED)
        e_budin.set("0")

def rosquillas():
    if var26.get()==1:
        rosquillas_entry.config(state=NORMAL)
        rosquillas_entry.delete(0, END)
        rosquillas_entry.focus()
    else:
        rosquillas_entry.config(state=DISABLED)
        e_rosquillas.set("0")

def frutas():
    if var27.get()==1:
        frutas_entry.config(state=NORMAL)
        frutas_entry.delete(0, END)
        frutas_entry.focus()
    else:
        frutas_entry.config(state=DISABLED)
        e_frutas.set("0")


root = Tk()

root.geometry("1400x700+0+0") # Tamaño y posicion de la ventana

root.resizable(height=0, width=0) # Para agrandar la ventana, tambien se le puede pasar (0, 0)

root.title("Administración de Restaurante") # Agrega el titulo en la barra de la ventana

root.config(bg="grey") # Para poner el color de fondo
# root.configure(bg="red") # Otra opción para poner el color de fondo

# Frame de TITULO
top_frame = Frame(root, bd=10, relief=GROOVE, bg="grey") # relief es para el borde del frame: Tenemos --> flat, groove, raised, ridge, solid, or sunken, si no ponemos este parametro quedara en flat
top_frame.pack(side=TOP)

label_title = Label(top_frame, text="Restaurante EL ELEGANTE", font=('arial', 30, 'bold'), bg="grey", width=49) # Creamos un label y pasamos parametros
label_title.grid(row=0, column=0)

# Frame de MENU
menu_frame = Frame(root, bd=10, relief=GROOVE)
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=4, relief=GROOVE)
cost_frame.pack(side=BOTTOM)

# Frame de COMIDAS
food_frame = LabelFrame(menu_frame, text="Comidas", font=('arial', 19, 'bold'), bd=10, relief=GROOVE)
food_frame.pack(side=LEFT)

# Frame de BEBIDAS
drinks_frame = LabelFrame(menu_frame, text="Bebidas", font=('arial', 19, 'bold'), bd=10, relief=GROOVE)
drinks_frame.pack(side=LEFT)

# Frame de POSTRES
cakes_frame = LabelFrame(menu_frame, text="Postres", font=('arial', 19, 'bold'), bd=10, relief=GROOVE)
cakes_frame.pack(side=LEFT)


# Frame de la derecha
right_frame = Frame(root, bd=10, relief=GROOVE)
right_frame.pack(side=RIGHT)

# Frame de CALCULADORA
calculator_frame = Frame(right_frame, bd=1, relief=GROOVE)
calculator_frame.pack()

# Frame de RECIBO
reciept_frame = Frame(right_frame, bd=4, relief=GROOVE)
reciept_frame.pack()

# Frame de BOTONES
buttons_frame = Frame(right_frame, bd=3, relief=GROOVE)
buttons_frame.pack()


# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_pollo = StringVar()
e_pizza = StringVar()
e_hamburgesa = StringVar()
e_ensalada = StringVar()
e_papas_fritas = StringVar()
e_sopa = StringVar()
e_sanguche = StringVar()
e_asado = StringVar()
e_tacos = StringVar()

e_gaseosa = StringVar()
e_agua_mineral = StringVar()
e_vino = StringVar()
e_cerveza = StringVar()
e_licuado = StringVar()
e_jugo = StringVar()
e_limonada = StringVar()
e_bebida_energetica = StringVar()
e_cafe = StringVar()

e_helado = StringVar()
e_flan = StringVar()
e_torta = StringVar()
e_pastafrola = StringVar()
e_cheesecake = StringVar()
e_trufas = StringVar()
e_budin = StringVar()
e_rosquillas = StringVar()
e_frutas = StringVar()

cost_of_food_var = StringVar()
cost_of_drink_var = StringVar()
cost_of_cake_var = StringVar()
subtotal_var = StringVar()
tax_var = StringVar()
total_var = StringVar()

e_pollo.set("0")
e_pizza.set("0")
e_hamburgesa.set("0")
e_ensalada.set("0")
e_papas_fritas.set("0")
e_sopa.set("0")
e_sanguche.set("0")
e_asado.set("0")
e_tacos.set("0")

e_gaseosa.set("0")
e_agua_mineral.set("0")
e_vino.set("0")
e_cerveza.set("0")
e_licuado.set("0")
e_jugo.set("0")
e_limonada.set("0")
e_bebida_energetica.set("0")
e_cafe.set("0")

e_helado.set("0")
e_flan.set("0")
e_torta.set("0")
e_pastafrola.set("0")
e_cheesecake.set("0")
e_trufas.set("0")
e_budin.set("0")
e_rosquillas.set("0")
e_frutas.set("0")

# COMIDAS
pollo = Checkbutton(food_frame, text="Pollo", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var1, command=pollo)
pollo.grid(row=0, column=0, sticky=W)

pizza = Checkbutton(food_frame, text="Pizza", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var2, command=pizza)
pizza.grid(row=1, column=0, sticky=W)

hamburgesa = Checkbutton(food_frame, text="Hamburguesa", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var3,command=hamburguesa)
hamburgesa.grid(row=2, column=0, sticky=W)

ensalada = Checkbutton(food_frame, text="Ensalada", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var4, command=ensalada)
ensalada.grid(row=3, column=0, sticky=W)

papas_fritas = Checkbutton(food_frame, text="Papas fritas", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var5, command=papas_fritas)
papas_fritas.grid(row=4, column=0, sticky=W)

sopa = Checkbutton(food_frame, text="Sopa", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var6, command=sopa)
sopa.grid(row=5, column=0, sticky=W)

sanguche = Checkbutton(food_frame, text="Sánguche", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var7, command=sanguche)
sanguche.grid(row=6, column=0, sticky=W)

asado = Checkbutton(food_frame, text="Asado", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var8, command=asado)
asado.grid(row=7, column=0, sticky=W)

tacos = Checkbutton(food_frame, text="Tacos", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var9, command=tacos)
tacos.grid(row=8, column=0, sticky=W)

# Campo de entrada para COMIDAS
pollo_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_pollo)
pollo_entry.grid(row=0, column=1)

pizza_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_pizza)
pizza_entry.grid(row=1, column=1)

hamburgesa_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_hamburgesa)
hamburgesa_entry.grid(row=2, column=1)

ensalada_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_ensalada)
ensalada_entry.grid(row=3, column=1)

papas_fritas_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_papas_fritas)
papas_fritas_entry.grid(row=4, column=1)

sopa_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_sopa)
sopa_entry.grid(row=5, column=1)

sanguche_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_sanguche)
sanguche_entry.grid(row=6, column=1)

asado_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_asado)
asado_entry.grid(row=7, column=1)

tacos_entry = Entry(food_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_tacos)
tacos_entry.grid(row=8, column=1)


# BEBIDAS
gaseosa = Checkbutton(drinks_frame, text="Gaseosa", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var10, command=gaseosa)
gaseosa.grid(row=0, column=0, sticky=W)

agua_mineral = Checkbutton(drinks_frame, text="Agua mineral", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var11, command=agua_mineral)
agua_mineral.grid(row=1, column=0, sticky=W)

vino = Checkbutton(drinks_frame, text="Vino", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var12, command=vino)
vino.grid(row=2, column=0, sticky=W)

cerveza = Checkbutton(drinks_frame, text="Cerveza", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var13, command=cerveza)
cerveza.grid(row=3, column=0, sticky=W)

licuado = Checkbutton(drinks_frame, text="Licuado", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var14, command=licuado)
licuado.grid(row=4, column=0, sticky=W)

jugo = Checkbutton(drinks_frame, text="Jugo", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var15, command=jugo)
jugo.grid(row=5, column=0, sticky=W)

limonada = Checkbutton(drinks_frame, text="Limonada", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var16, command=limonada)
limonada.grid(row=6, column=0, sticky=W)

bebida_energetica = Checkbutton(drinks_frame, text="Bebida energetica", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var17, command=bebida_energetica)
bebida_energetica.grid(row=7, column=0, sticky=W)

cafe = Checkbutton(drinks_frame, text="Cafe", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var18, command=cafe)
cafe.grid(row=8, column=0, sticky=W)

# Campo de entrada para BEBIDAS
gaseosa_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_gaseosa)
gaseosa_entry.grid(row=0, column=1)

agua_mineral_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_agua_mineral)
agua_mineral_entry.grid(row=1, column=1)

vino_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_vino)
vino_entry.grid(row=2, column=1)

cerveza_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_cerveza)
cerveza_entry.grid(row=3, column=1)

licuado_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_licuado)
licuado_entry.grid(row=4, column=1)

jugo_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_jugo)
jugo_entry.grid(row=5, column=1)

limonada_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_limonada)
limonada_entry.grid(row=6, column=1)

bebida_energetica_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_bebida_energetica)
bebida_energetica_entry.grid(row=7, column=1)

cafe_entry = Entry(drinks_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_cafe)
cafe_entry.grid(row=8, column=1)


# POSTRES
helado = Checkbutton(cakes_frame, text="Helado", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var19, command=helado)
helado.grid(row=0, column=0, sticky=W)

flan = Checkbutton(cakes_frame, text="Flan", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var20, command=flan)
flan.grid(row=1, column=0, sticky=W)

torta = Checkbutton(cakes_frame, text="Torta", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var21, command=torta)
torta.grid(row=2, column=0, sticky=W)

pastafrola = Checkbutton(cakes_frame, text="Pastafrola", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var22, command=pastafrola)
pastafrola.grid(row=3, column=0, sticky=W)

cheesecake = Checkbutton(cakes_frame, text="Cheesecake", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var23, command=cheesecake)
cheesecake.grid(row=4, column=0, sticky=W)

trufas = Checkbutton(cakes_frame, text="Trufas", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var24, command=trufas)
trufas.grid(row=5, column=0, sticky=W)

budin = Checkbutton(cakes_frame, text="Budin", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var25, command=budin)
budin.grid(row=6, column=0, sticky=W)

rosquillas = Checkbutton(cakes_frame, text="Rosquillas", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var26, command=rosquillas)
rosquillas.grid(row=7, column=0, sticky=W)

frutas = Checkbutton(cakes_frame, text="Frutas", font=('arial', 19, 'bold'), onvalue = 1, offvalue = 0, variable=var27, command=frutas)
frutas.grid(row=8, column=0, sticky=W)

# Campo de entrada para POSTRES
helado_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_helado)
helado_entry.grid(row=0, column=1)

flan_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_flan)
flan_entry.grid(row=1, column=1)

torta_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_torta)
torta_entry.grid(row=2, column=1)

pastafrola_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_pastafrola)
pastafrola_entry.grid(row=3, column=1)

cheesecake_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_cheesecake)
cheesecake_entry.grid(row=4, column=1)

trufas_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_trufas)
trufas_entry.grid(row=5, column=1)

budin_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_budin)
budin_entry.grid(row=6, column=1)

rosquillas_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_rosquillas)
rosquillas_entry.grid(row=7, column=1)

frutas_entry = Entry(cakes_frame, font=('arial', 19, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_frutas)
frutas_entry.grid(row=8, column=1)


# Labels y campo de entradas de COSTO
label_cost_of_food = Label(cost_frame, text="Costo de la comida", font=('arial', 17, 'bold'))
label_cost_of_food.grid(row=0, column=0)

cost_of_food_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=cost_of_food_var)
cost_of_food_entry.grid(row=0, column=1)

label_cost_of_drink = Label(cost_frame, text="Costo de la bebida", font=('arial', 17, 'bold'))
label_cost_of_drink.grid(row=1, column=0)

cost_of_drink_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=cost_of_drink_var)
cost_of_drink_entry.grid(row=1, column=1)

label_cost_of_cake = Label(cost_frame, text="Costo del postre", font=('arial', 17, 'bold'))
label_cost_of_cake.grid(row=2, column=0)

cost_of_cake_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=cost_of_cake_var)
cost_of_cake_entry.grid(row=2, column=1)

label_subtotal = Label(cost_frame, text="Subtotal", font=('arial', 17, 'bold'))
label_subtotal.grid(row=0, column=2)

subtotal_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=subtotal_var)
subtotal_entry.grid(row=0, column=3, padx=10, pady=5)

label_tax = Label(cost_frame, text="Impuesto", font=('arial', 17, 'bold'))
label_tax.grid(row=1, column=2)

tax_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=tax_var)
tax_entry.grid(row=1, column=3, padx=10, pady=5)

label_total = Label(cost_frame, text="Total", font=('arial', 17, 'bold'))
label_total.grid(row=2, column=2)

total_entry = Entry(cost_frame, font=('arial', 19, 'bold'), bd=5, state='readonly', textvariable=total_var)
total_entry.grid(row=2, column=3, padx=10, pady=5)


# Botones
button_total = Button(buttons_frame, text="Total", font=('arial', 12, 'bold'), bd=3, padx=6, command=total_cost)
button_total.grid(row=0, column=0)

button_receipt = Button(buttons_frame, text="Recibo", font=('arial', 12, 'bold'), bd=3, padx=6, command=receipt)
button_receipt.grid(row=0, column=1)

button_save = Button(buttons_frame, text="Guardar", font=('arial', 12, 'bold'), bd=3, padx=6, command=save)
button_save.grid(row=0, column=2)

button_send = Button(buttons_frame, text="Enviar", font=('arial', 12, 'bold'), bd=3, padx=6, command=send)
button_send.grid(row=0, column=3)

button_reset = Button(buttons_frame, text="Reiniciar", font=('arial', 12, 'bold'), bd=3, padx=6, command=reset)
button_reset.grid(row=0, column=4)


# Area de texto para RECIBO
reciept_entry = Text(reciept_frame, font=('arial', 12, 'bold'), bd=3, width=46, height=14)
reciept_entry.grid(row=0, column=0)

# Calculadora
operator = ""

def button_click(numbers):
    global operator
    operator = operator + numbers
    calculator_field.delete(0, END)
    calculator_field.insert(END, operator)
    
def clear():
    global operator
    operator = ""
    calculator_field.delete(0, END)

def answer():
    global operator
    result = eval(operator) 
    calculator_field.delete(0, END)
    calculator_field.insert(0, result)

calculator_field = Entry(calculator_frame, font=('arial', 12, 'bold'), width=40, bd=3)
calculator_field.grid(row=0, column=0, columnspan=4)

button7 = Button(calculator_frame, text="7", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("7"))
button7.grid(row=1, column=0)

button8 = Button(calculator_frame, text="8", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("8"))
button8.grid(row=1, column=1)

button9 = Button(calculator_frame, text="9", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("9"))
button9.grid(row=1, column=2)

button_sum = Button(calculator_frame, text="+", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("+"))
button_sum.grid(row=1, column=3)

button4 = Button(calculator_frame, text="4", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("4"))
button4.grid(row=2, column=0)

button5 = Button(calculator_frame, text="5", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("5"))
button5.grid(row=2, column=1)

button6 = Button(calculator_frame, text="6", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("6"))
button6.grid(row=2, column=2)

button_men = Button(calculator_frame, text="-", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("-"))
button_men.grid(row=2, column=3)

button1 = Button(calculator_frame, text="1", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("1"))
button1.grid(row=3, column=0)

button2 = Button(calculator_frame, text="2", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("2"))
button2.grid(row=3, column=1)

button3 = Button(calculator_frame, text="3", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("3"))
button3.grid(row=3, column=2)

button_mul = Button(calculator_frame, text="*", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("*"))
button_mul.grid(row=3, column=3)

button_ans = Button(calculator_frame, text="Res", font=('arial', 12, 'bold'), bd=5, width=5, command=answer)
button_ans.grid(row=4, column=0)

button_clear = Button(calculator_frame, text="Borrar", font=('arial', 12, 'bold'), bd=5, width=5, command=clear)
button_clear.grid(row=4, column=1)

button0 = Button(calculator_frame, text="0", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("0"))
button0.grid(row=4, column=2)

button_inv = Button(calculator_frame, text="/", font=('arial', 12, 'bold'), bd=5, width=5, command=lambda:button_click("/"))
button_inv.grid(row=4, column=3)

# Bucle principal del programa
root.mainloop()