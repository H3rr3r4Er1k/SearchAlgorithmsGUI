import tkinter as tk
from tkinter import messagebox
import random
from vector import quicksort


def generar_nombres_aleatorios(nombres_entry):
    nombres = ["Ana", "Juan", "María", "Pedro", "Luis", "Laura", "Carlos", "Sofía", "David", "Mónica"]
    random.shuffle(nombres)
    for i, nombre_entry in enumerate(nombres_entry):
        nombre_entry.delete(0, tk.END)
        nombre_entry.insert(tk.END, nombres[i])


def mostrar_vector(nombres_entry, vector_label):
    vector = [nombre.get() for nombre in nombres_entry]
    vector_label.configure(text="Vector: " + ", ".join(vector))


def ordenar_vector(nombres_entry, vector_ordenado_label):
    vector = [nombre.get() for nombre in nombres_entry]
    vector_ordenado = quicksort(vector)
    vector_ordenado_label.configure(text="Vector Ordenado: " + ", ".join(vector_ordenado))


def buscar_elemento(nombres_entry, elemento_busqueda_entry, tipo_busqueda_var):
    elemento = elemento_busqueda_entry.get()
    tipo_busqueda = tipo_busqueda_var.get()

    vector = [nombre.get() for nombre in nombres_entry]
    if tipo_busqueda == "Búsqueda Lineal":
        for i in range(len(vector)):
            if vector[i] == elemento:
                messagebox.showinfo("Resultado", f"Se encontró el elemento '{elemento}' en la posición {i+1}.")
                return
        messagebox.showinfo("Resultado", f"No se encontró el elemento '{elemento}'.")
    elif tipo_busqueda == "Búsqueda Binaria":
        vector_ordenado = quicksort(vector)
        left = 0
        right = len(vector_ordenado) - 1
        while left <= right:
            mid = (left + right) // 2
            if vector_ordenado[mid] == elemento:
                messagebox.showinfo("Resultado", f"Se encontró el elemento '{elemento}' en la posición {mid+1}.")
                return
            elif vector_ordenado[mid] < elemento:
                left = mid + 1
            else:
                right = mid - 1
        messagebox.showinfo("Resultado", f"No se encontró el elemento '{elemento}'.")
    elif tipo_busqueda == "Búsqueda Hash":
        hash_table = {}
        for i, nombre in enumerate(vector):
            hash_table[nombre] = i
        if elemento in hash_table:
            messagebox.showinfo("Resultado", f"Se encontró el elemento '{elemento}' en la posición {hash_table[elemento]+1}.")
        else:
            messagebox.showinfo("Resultado", f"No se encontró el elemento '{elemento}'.")
