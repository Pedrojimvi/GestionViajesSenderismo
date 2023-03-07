"""Los objetos que se usarán serán los siguientes:

- La ventana tendrá un título en la parte superior que diga “Agencia de Viajes”.
- Una etiqueta (Label) que indique “Viajes de Senderismo”
- Un logo de la empresa como imagen en la ventana
- 4 Radiobutton para seleccionar la excursión que desea realizar el cliente: Monte Abantos,
La Pedriza, Las dehesas de Cercedilla y La Cabrera-Pico de la Miel.
- 8 Checkbutton para poder elegir los accesorios que llevarán a la excursión: Mochila,
Linterna, GPS, Mapa, Prismáticos, Cantimplora, Botiquín y Crema Solar.

- Unas etiquetas para indicar el contenido que debe tener los cuadros de texto.
- Unos cuadros de texto para introducir los datos del excursionista: Nombre, Apellidos,
Dirección y Teléfono.
- Un Combobox que contenga los nombres de las poblaciones de los posibles excursionistas
para que se seleccione aquella de donde es un excursionista determinado: Madrid,
Alcobendas, San Sebastián de los Reyes, Algete, Pozuelo, Las Rozas, Majadahonda, Móstoles,
Alcorcón, Boadilla del Monte y Villaviciosa de Odón.
- Un cuadro de lista o Listbox.
- Un botón que introduzca todos los datos de un excursionista en el cuadro de lista o Listbox.
En este Listbox se irán agregando los datos de todos los excursionistas que se vayan dando
de alta. """

from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Agencia de Viajes")
ventana.geometry("800x800")

# Etiqueta
etiqueta = Label(ventana, text="Viajes de Senderismo")
etiqueta.config()
etiqueta.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Logo
logo = PhotoImage(file="viajes.png")
logo_label = Label(ventana, image=logo)
logo_label.config(width=200, height=200)
logo_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

# Radiobutton
excursion = StringVar()
excursion.set("")

monte_abantos = Radiobutton(ventana, text="Monte Abantos", variable=excursion, value="Monte Abantos")
monte_abantos.grid(row=1, column=0, padx=10, pady=10)

la_pedriza = Radiobutton(ventana, text="La Pedriza", variable=excursion, value="La Pedriza")
la_pedriza.grid(row=1, column=1, padx=10, pady=10)

las_dehesas = Radiobutton(ventana, text="Las dehesas de Cercedilla", variable=excursion,
                          value="Las dehesas de Cercedilla")
las_dehesas.grid(row=1, column=2, padx=10, pady=10)

la_cabrera = Radiobutton(ventana, text="La Cabrera-Pico de la Miel", variable=excursion,
                         value="La Cabrera-Pico de la Miel")
la_cabrera.grid(row=1, column=3, padx=10, pady=10)

# Checkbutton
mochila_accesorio = StringVar()
linterna_accesorio = StringVar()
gps_accesorio = StringVar()
mapa_accesorio = StringVar()
prismaticos_accesorio = StringVar()
cantimplora_accesorio = StringVar()
botiquin_accesorio = StringVar()
crema_solar_accesorio = StringVar()

lista_accesorios = [("Mochila", mochila_accesorio), ("Linterna", linterna_accesorio), ("GPS", gps_accesorio), ("Mapa", mapa_accesorio), ("Prismáticos", prismaticos_accesorio), ("Cantimplora", cantimplora_accesorio), ("Botiquín", botiquin_accesorio), ("Crema Solar", crema_solar_accesorio)]


mochila = Checkbutton(ventana, text="Mochila", variable=mochila_accesorio, onvalue="Mochila", offvalue="")
mochila.grid(row=2, column=0, padx=10, pady=10)

linterna = Checkbutton(ventana, text="Linterna", variable=linterna_accesorio, onvalue="Linterna", offvalue="")
linterna.grid(row=2, column=1, padx=10, pady=10)

gps = Checkbutton(ventana, text="GPS", variable=gps_accesorio, onvalue="GPS", offvalue="")
gps.grid(row=2, column=2, padx=10, pady=10)

mapa = Checkbutton(ventana, text="Mapa", variable=mapa_accesorio, onvalue="Mapa", offvalue="")
mapa.grid(row=2, column=3, padx=10, pady=10)

prismaticos = Checkbutton(ventana, text="Prismáticos", variable=prismaticos_accesorio, onvalue="Prismáticos", offvalue="")
prismaticos.grid(row=3, column=0, padx=10, pady=10)

cantimplora = Checkbutton(ventana, text="Cantimplora", variable=cantimplora_accesorio, onvalue="Cantimplora", offvalue="")
cantimplora.grid(row=3, column=1, padx=10, pady=10)

botiquin = Checkbutton(ventana, text="Botiquín", variable=botiquin_accesorio, onvalue="Botiquín", offvalue="")
botiquin.grid(row=3, column=2, padx=10, pady=10)

crema_solar = Checkbutton(ventana, text="Crema Solar", variable=crema_solar_accesorio, onvalue="Crema Solar", offvalue="")
crema_solar.grid(row=3, column=3, padx=10, pady=10)

# Etiquetas
nombre_label = Label(ventana, text="Nombre")
nombre_label.grid(row=4, column=0, padx=10, pady=10)

apellidos_label = Label(ventana, text="Apellidos")
apellidos_label.grid(row=4, column=1, padx=10, pady=10)

direccion_label = Label(ventana, text="Dirección")
direccion_label.grid(row=4, column=2, padx=10, pady=10)

telefono_label = Label(ventana, text="Teléfono")
telefono_label.grid(row=4, column=3, padx=10, pady=10)

# Cuadros de texto
nombre = Entry(ventana)
nombre.grid(row=5, column=0, padx=10, pady=10)

apellidos = Entry(ventana)
apellidos.grid(row=5, column=1, padx=10, pady=10)

direccion = Entry(ventana)
direccion.grid(row=5, column=2, padx=10, pady=10)

telefono = Entry(ventana)
telefono.grid(row=5, column=3, padx=10, pady=10)

# Combobox
poblacion = ttk.Combobox(ventana)
poblacion["values"] = (
    "Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles",
    "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón")
poblacion.grid(row=6, column=0, padx=10, pady=10)

# Listbox
lista = Listbox(ventana)
lista.grid(row=7, column=0, columnspan=4, padx=10, pady=10)


# Botón
def agregar():
    lista.insert(END, nombre.get())
    lista.insert(END, apellidos.get())
    lista.insert(END, direccion.get())
    lista.insert(END, telefono.get())
    lista.insert(END, poblacion.get())
    lista.insert(END, excursion.get())
    for texto, variable in lista_accesorios:
        if variable.get():
            lista.insert(END, variable.get())
    lista.insert(END, "---------------------")


boton = Button(ventana, text="Agregar", command=agregar)
boton.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

ventana.mainloop()
