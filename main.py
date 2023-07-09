import tkinter as tk
from gui import *
from vector import *


# Crear la ventana
ventana = tk.Tk()
ventana.title("Programa con GUI")
ventana.geometry("800x500")
ventana.configure(bg="white")

# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_screenwidth()
alto_ventana = ventana.winfo_screenheight()
x = (ancho_ventana - 800) // 2
y = (alto_ventana - 500) // 2
ventana.geometry(f"800x500+{x}+{y}")

# Crear y centrar el marco
marco = tk.Frame(ventana)
marco.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear etiquetas y campos de entrada
tamanio_label = tk.Label(marco, text="Tamaño del vector:")
tamanio_label.grid(row=0, column=0, pady=5)
tamanio_entry = tk.Entry(marco)
tamanio_entry.grid(row=0, column=1, pady=5)

nombres_label = tk.Label(marco, text="Nombres:")
nombres_label.grid(row=1, column=0, pady=5)

nombres_entry = []
# ...
nombres_entry = []
for i in range(5):
    nombre_entry = tk.Entry(marco)
    nombre_entry.grid(row=i+1, column=1, pady=2)
    nombres_entry.append(nombre_entry)
# ...


# Botón para generar nombres aleatorios
generar_nombres_button = tk.Button(marco, text="Generar Nombres Aleatorios", command=lambda: generar_nombres_aleatorios(nombres_entry))
generar_nombres_button.grid(row=6, column=0, columnspan=2, pady=5)

elemento_busqueda_label = tk.Label(marco, text="Elemento a buscar:")
elemento_busqueda_label.grid(row=7, column=0, pady=5)
elemento_busqueda_entry = tk.Entry(marco)
elemento_busqueda_entry.grid(row=7, column=1, pady=5)

# Crear botones
mostrar_vector_button = tk.Button(marco, text="Mostrar Vector", command=lambda: mostrar_vector(nombres_entry, vector_label))
mostrar_vector_button.grid(row=8, column=0, pady=5)

ordenar_vector_button = tk.Button(marco, text="Ordenar Vector", command=lambda: ordenar_vector(nombres_entry, vector_ordenado_label))
ordenar_vector_button.grid(row=8, column=1, pady=5)

tipo_busqueda_var = tk.StringVar()
tipo_busqueda_var.set("Búsqueda Lineal")

tipo_busqueda_label = tk.Label(marco, text="Tipo de búsqueda:")
tipo_busqueda_label.grid(row=9, column=0, pady=5)

tipo_busqueda_menu = tk.OptionMenu(marco, tipo_busqueda_var, "Búsqueda Lineal", "Búsqueda Binaria", "Búsqueda Hash")
tipo_busqueda_menu.grid(row=9, column=1, pady=5)

buscar_elemento_button = tk.Button(marco, text="Buscar Elemento", command=lambda: buscar_elemento(nombres_entry, elemento_busqueda_entry, tipo_busqueda_var))
buscar_elemento_button.grid(row=10, column=0, columnspan=2, pady=5)

vector_label = tk.Label(marco, text="Vector:")
vector_label.grid(row=11, column=0, columnspan=2, pady=5)

vector_ordenado_label = tk.Label(marco, text="Vector Ordenado:")
vector_ordenado_label.grid(row=12, column=0, columnspan=2, pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
