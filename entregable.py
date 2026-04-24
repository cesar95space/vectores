import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import os

# --- FUNCIÓN GLOBAL PARA GUARDAR EXCEL ---
def guardar_en_excel(nombre_archivo, datos):
    try:
        df = pd.DataFrame(datos)
        df.to_excel(nombre_archivo, index=False)
        messagebox.showinfo("UTE - Reporte", f"Archivo generado con éxito:\n{nombre_archivo}")
    except Exception as e:
        messagebox.showerror("Error de Excel", "Asegúrate de tener instalada la librería: pip install openpyxl")

# --- VENTANA PARA NOTAS (EJERCICIOS 1, 2 Y 3) ---
def ventana_notas(ventana_padre, titulo, es_decimal, cant_fija=0):
    nombre = entry_nombre.get().strip()
    materia = entry_materia.get().strip()
    
    if not nombre or not materia:
        return messagebox.showwarning("Faltan Datos", "Por favor ingresa Nombre y Asignatura en el menú principal.")

    ventana_padre.withdraw()
    top = tk.Toplevel()
    top.title(titulo)
    top.geometry("400x550")
    top.configure(bg="white")
    
    lista_notas = []

    tk.Label(top, text=f"ASIGNATURA: {materia.upper()}", font=("Arial", 9, "bold"), bg="white", fg="#2e7d32").pack(pady=5)
    tk.Label(top, text=titulo, font=("Arial", 12, "bold"), bg="white").pack(pady=10)
    
    tk.Label(top, text="¿Cuántas notas registrará?", bg="white").pack()
    ent_cant = tk.Entry(top)
    if cant_fija > 0:
        ent_cant.insert(0, str(cant_fija))
        ent_cant.config(state="disabled")
    ent_cant.pack(pady=5)

    tk.Label(top, text="Ingrese la nota (0.0 - 5.0):", bg="white").pack(pady=5)
    ent_nota = tk.Entry(top, font=("Arial", 12))
    ent_nota.pack(pady=5)
    
    lbl_contador = tk.Label(top, text="Notas capturadas: 0", bg="white", fg="blue")
    lbl_contador.pack(pady=10)

    def guardar_nota():
        try:
            limite = int(ent_cant.get())
            valor = float(ent_nota.get()) if es_decimal else int(ent_nota.get())
            
            if 0 <= valor <= 5:
                lista_notas.append(valor)
                ent_nota.delete(0, tk.END)
                ent_cant.config(state="disabled")
                lbl_contador.config(text=f"Notas capturadas: {len(lista_notas)} de {limite}")
                
                if len(lista_notas) >= limite:
                    promedio = sum(lista_notas) / len(lista_notas)
                    datos_excel = {
                        "Estudiante": [nombre],
                        "Asignatura": [materia],
                        "Notas": [str(lista_notas)],
                        "Promedio Final": [round(promedio, 2)]
                    }
                    guardar_en_excel(f"Notas_{materia}_{titulo}.xlsx", datos_excel)
                    top.destroy()
                    ventana_padre.deiconify()
            else:
                messagebox.showwarning("Rango", "La nota debe estar entre 0 y 5.")
        except:
            messagebox.showerror("Dato Inválido", "Ingresa un número válido.")

    tk.Button(top, text="Guardar Nota", command=guardar_nota, bg="#2e7d32", fg="white", width=20).pack(pady=10)
    tk.Button(top, text="← Volver al Menú", command=lambda:[top.destroy(), ventana_padre.deiconify()], bg="#d32f2f", fg="white", width=20).pack(pady=5)

# --- EJERCICIO 4: NOMBRES Y EDADES ---
def iniciar_ejercicio_4(ventana_padre):
    ventana_padre.withdraw()
    top = tk.Toplevel()
    top.title("Ejercicio 4 - UTE")
    top.geometry("400x550")
    top.configure(bg="white")
    
    registros = []

    tk.Label(top, text="REGISTRO DE ESTUDIANTES Y EDADES", font=("Arial", 11, "bold"), bg="white", fg="#1976d2").pack(pady=15)

    tk.Label(top, text="Nombre Completo:", bg="white").pack()
    enom = tk.Entry(top, width=30)
    enom.pack(pady=5)

    tk.Label(top, text="Edad:", bg="white").pack()
    eedad = tk.Entry(top, width=30)
    eedad.pack(pady=5)

    lbl_visor = tk.Label(top, text="Aún no hay registros", bg="white", fg="grey")
    lbl_visor.pack(pady=15)

    def agregar():
        n = enom.get().strip()
        e = eedad.get().strip()
        if n and e:
            registros.append({"Nombre": n, "Edad": e})
            enom.delete(0, tk.END)
            eedad.delete(0, tk.END)
            texto = "\n".join([f"{r['Nombre']} ({r['Edad']} años)" for r in registros[-5:]])
            lbl_visor.config(text=texto, fg="black")
        else:
            messagebox.showwarning("Faltan datos", "Escribe nombre y edad.")

    def finalizar():
        if registros:
            guardar_en_excel("Registro_Edades_Ejer4.xlsx", registros)
        top.destroy()
        ventana_padre.deiconify()

    tk.Button(top, text="Agregar Estudiante", command=agregar, bg="#1976d2", fg="white", width=20).pack(pady=5)
    tk.Button(top, text="Finalizar y Exportar", command=finalizar, bg="#2e7d32", fg="white", width=20).pack(pady=5)
    tk.Button(top, text="← Volver al Menú", command=lambda:[top.destroy(), ventana_padre.deiconify()], bg="#d32f2f", fg="white", width=20).pack(pady=5)

# --- EJERCICIO 5: SUMA DE MATRICES 2x2 ---
def iniciar_ejercicio_5(ventana_padre):
    ventana_padre.withdraw()
    top = tk.Toplevel()
    top.title("Ejercicio 5 - Matrices")
    top.geometry("450x450")
    top.configure(bg="white")
    
    tk.Label(top, text="INGRESE VALORES PARA MATRICES 2x2", font=("Arial", 11, "bold"), bg="white", fg="#8e24aa").pack(pady=10)
    
    frame_m = tk.Frame(top, bg="white")
    frame_m.pack(pady=10)

    # Entradas Matriz A
    tk.Label(frame_m, text="Matriz A", bg="white", font=("Arial", 9, "bold")).grid(row=0, column=0, columnspan=2)
    a11 = tk.Entry(frame_m, width=5); a11.grid(row=1, column=0, padx=5, pady=5)
    a12 = tk.Entry(frame_m, width=5); a12.grid(row=1, column=1, padx=5, pady=5)
    a21 = tk.Entry(frame_m, width=5); a21.grid(row=2, column=0, padx=5, pady=5)
    a22 = tk.Entry(frame_m, width=5); a22.grid(row=2, column=1, padx=5, pady=5)

    # Entradas Matriz B
    tk.Label(frame_m, text="Matriz B", bg="white", font=("Arial", 9, "bold")).grid(row=0, column=2, columnspan=2)
    b11 = tk.Entry(frame_m, width=5); b11.grid(row=1, column=2, padx=5, pady=5)
    b12 = tk.Entry(frame_m, width=5); b12.grid(row=1, column=3, padx=5, pady=5)
    b21 = tk.Entry(frame_m, width=5); b21.grid(row=2, column=2, padx=5, pady=5)
    b22 = tk.Entry(frame_m, width=5); b22.grid(row=2, column=3, padx=5, pady=5)

    def calcular():
        try:
            mA = [[int(a11.get()), int(a12.get())], [int(a21.get()), int(a22.get())]]
            mB = [[int(b11.get()), int(b12.get())], [int(b21.get()), int(b22.get())]]
            res = [[mA[i][j] + mB[i][j] for j in range(2)] for i in range(2)]
            
            resultado_str = f"SUMA RESULTANTE:\n\n[{res[0][0]}]  [{res[0][1]}]\n[{res[1][0]}]  [{res[1][1]}]"
            messagebox.showinfo("Cálculo Realizado", resultado_str)
            
            datos_excel = {"Fila 1": res[0], "Fila 2": res[1]}
            guardar_en_excel("Suma_Matrices_Ejer5.xlsx", datos_excel)
            top.destroy()
            ventana_padre.deiconify()
        except:
            messagebox.showerror("Error", "Ingrese números enteros en todos los campos.")

    tk.Button(top, text="Realizar Sumatoria", command=calcular, bg="#8e24aa", fg="white", width=25).pack(pady=15)
    tk.Button(top, text="← Volver al Menú", command=lambda:[top.destroy(), ventana_padre.deiconify()], bg="#d32f2f", fg="white", width=25).pack()

# --- EJERCICIO 6: TABLA DE MULTIPLICAR ---
def iniciar_ejercicio_6(ventana_padre):
    ventana_padre.withdraw()
    top = tk.Toplevel()
    top.title("Ejercicio 6 - Tablas")
    top.geometry("400x500")
    top.configure(bg="white")
    
    tk.Label(top, text="TABLA DE MULTIPLICAR (MATRICES)", font=("Arial", 11, "bold"), bg="white", fg="#fb8c00").pack(pady=15)
    tk.Label(top, text="Número base para la tabla:", bg="white").pack()
    ent_num = tk.Entry(top, font=("Arial", 12), width=10)
    ent_num.pack(pady=10)

    def generar():
        try:
            n = int(ent_num.get())
            # Se usan vectores (matrices de una columna)
            numeros = [[i] for i in range(1, 11)]
            resultados = [[n * r[0]] for r in numeros]
            
            formato_tabla = "\n".join([f"{n} x {i+1} = {resultados[i][0]}" for i in range(10)])
            messagebox.showinfo(f"Tabla del {n}", formato_tabla)
            
            datos_excel = {
                "Multiplicando": [n]*10,
                "Multiplicador": [x[0] for x in numeros],
                "Resultado": [r[0] for r in resultados]
            }
            guardar_en_excel(f"Tabla_Multiplicar_{n}.xlsx", datos_excel)
            top.destroy()
            ventana_padre.deiconify()
        except:
            messagebox.showerror("Error", "Ingresa un número entero válido.")

    tk.Button(top, text="Generar Tabla y Excel", command=generar, bg="#fb8c00", fg="white", width=25).pack(pady=15)
    tk.Button(top, text="← Volver al Menú", command=lambda:[top.destroy(), ventana_padre.deiconify()], bg="#d32f2f", fg="white", width=25).pack()

# --- MENÚ PRINCIPAL ---
def main():
    global entry_nombre, entry_materia
    root = tk.Tk()
    root.title("UTE - Gestión Académica")
    root.geometry("550x850")
    root.configure(bg="white")

    # --- CARGA DEL LOGO (logo.png) ---
    archivo_logo = "logo.png"
    
    if os.path.exists(archivo_logo):
        try:
            img = Image.open(archivo_logo)
            img = img.resize((150, 200), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(img)
            lbl_logo = tk.Label(root, image=foto, bg="white")
            lbl_logo.image = foto
            lbl_logo.pack(pady=10)
        except Exception as e:
            print(f"Error cargando imagen: {e}")
    else:
        tk.Label(root, text="[ ESCUDO UTE ]", font=("Arial", 14, "bold"), fg="#1b5e20", bg="white").pack(pady=20)

    tk.Label(root, text="UNIVERSIDAD TECNOLÓGICA DEL EJE", font=("Arial", 14, "bold"), bg="white", fg="#1b5e20").pack()
    
    f_datos = tk.LabelFrame(root, text=" Información del Estudiante ", bg="white", font=("Arial", 9, "bold"), padx=10, pady=10)
    f_datos.pack(pady=15)
    
    tk.Label(f_datos, text="Nombre Completo:", bg="white").grid(row=0, column=0, sticky="e", pady=2)
    entry_nombre = tk.Entry(f_datos, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=2)
    
    tk.Label(f_datos, text="Asignatura:", bg="white").grid(row=1, column=0, sticky="e", pady=2)
    entry_materia = tk.Entry(f_datos, width=30)
    entry_materia.grid(row=1, column=1, padx=5, pady=2)

    tk.Label(root, text="Seleccione el Ejercicio:", font=("Arial", 10), bg="white").pack(pady=5)

    estilo = {"width": 40, "height": 2, "fg": "white", "font": ("Arial", 9, "bold")}
    
    tk.Button(root, text="EJERCICIO 1 (6 Notas - Enteros)", bg="#2e7d32", **estilo, 
              command=lambda: ventana_notas(root, "Ejercicio 1", False, 6)).pack(pady=4)
    
    tk.Button(root, text="EJERCICIO 2 (Variable - Enteros)", bg="#388e3c", **estilo, 
              command=lambda: ventana_notas(root, "Ejercicio 2", False)).pack(pady=4)
    
    tk.Button(root, text="EJERCICIO 3 (Variable - Decimales)", bg="#ef6c00", **estilo, 
              command=lambda: ventana_notas(root, "Ejercicio 3", True)).pack(pady=4)
    
    tk.Button(root, text="EJERCICIO 4 (Registro de Edades)", bg="#1976d2", **estilo, 
              command=lambda: iniciar_ejercicio_4(root)).pack(pady=4)
    
    tk.Button(root, text="EJERCICIO 5 (Sumatoria de Matrices 2x2)", bg="#8e24aa", **estilo, 
              command=lambda: iniciar_ejercicio_5(root)).pack(pady=4)
              
    tk.Button(root, text="EJERCICIO 6 (Tabla de Multiplicar)", bg="#fb8c00", **estilo, 
              command=lambda: iniciar_ejercicio_6(root)).pack(pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()