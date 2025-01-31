import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def analizar_pagina():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Por favor, ingrese una URL válida.")
        return
    
    # Si la URL no tiene protocolo, agregar "https://"
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    # Configuración de Selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Para ejecutar sin abrir el navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        
        # Contar elementos de interés
        botones = len(driver.find_elements(By.TAG_NAME, "button"))
        campos_texto = len(driver.find_elements(By.TAG_NAME, "input"))
        dropdowns = len(driver.find_elements(By.TAG_NAME, "select"))
        
        resultado = f"Botones: {botones}\nCampos de texto: {campos_texto}\nDropdowns: {dropdowns}"
        messagebox.showinfo("Análisis completado", resultado)
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo analizar la página: {str(e)}")
    
    finally:
        driver.quit()

# Interfaz gráfica
root = tk.Tk()
root.title("Analizador de Webs")
root.geometry("400x200")

tk.Label(root, text="Ingrese la URL a analizar:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Analizar", command=analizar_pagina).pack(pady=10)

root.mainloop()
