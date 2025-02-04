import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

def analizar_pagina():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Por favor, ingrese una URL válida.")
        return
    
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        
        # Contar elementos de interés
        botones = len(driver.find_elements(By.TAG_NAME, "button"))
        campos_texto = len(driver.find_elements(By.TAG_NAME, "input"))
        dropdowns = len(driver.find_elements(By.TAG_NAME, "select"))
        
        # Obtener el HTML de la página
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        
        # Detectar año de publicación
        years = re.findall(r'\b(19\d{2}|20\d{2})\b', soup.text)
        year_published = min(years) if years else "No detectado"
        
        # Detectar lenguaje de programación
        language = "Desconocido"
        if "wp-content" in page_source:
            language = "WordPress (PHP)"
        elif "<script" in page_source:
            language = "JavaScript"
        elif ".aspx" in url:
            language = "ASP.NET"
        
        # Evaluar seguridad
        security = "Segura" if url.startswith("https") else "No segura"
        
        # Evaluar calidad del código
        script_tags = len(soup.find_all("script"))
        css_tags = len(soup.find_all("style"))
        quality = "Buena" if script_tags < 20 and css_tags < 20 else "Sobrecargada"
        
        resultado = (f"Botones: {botones}\nCampos de texto: {campos_texto}\nDropdowns: {dropdowns}\n"
                     f"Año de publicación: {year_published}\nLenguaje detectado: {language}\n"
                     f"Seguridad: {security}\nCalidad del código: {quality}")
        messagebox.showinfo("Análisis completado", resultado)
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo analizar la página: {str(e)}")
    
    finally:
        driver.quit()

# Interfaz gráfica
root = tk.Tk()
root.title("Analizador de Webs")
root.geometry("400x250")

tk.Label(root, text="Ingrese la URL a analizar:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Analizar", command=analizar_pagina).pack(pady=10)

root.mainloop()
