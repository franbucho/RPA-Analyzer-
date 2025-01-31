# Web Analyzer / Analizador de Webs

## English

This project is a Python tool that analyzes the complexity of automating a web page by identifying the number of buttons, text fields, and dropdowns present on the page.

### Requirements

Before running the script, make sure you have installed the following dependencies:

```bash
pip install selenium webdriver-manager tkinter
```

### Usage

1. Run the `analizador_webs.py` script.
2. Enter the URL of the page to be analyzed in the text box.
3. Click the "Analyze" button.
4. A message will display the number of buttons, text fields, and dropdowns detected on the page.

### Features

- **Simple graphical interface** using `tkinter`.
- **Automatic page analysis** with Selenium.
- **URL correction**: If the user enters a URL without `http://` or `https://`, the program automatically adds it.
- **Headless mode** (`headless`): The analysis is performed without opening a browser window.

### Considerations

- This script uses Google Chrome as the default browser.
- If an error occurs while loading the page, an error message will be displayed with the cause of the issue.

### Author
Francisco Villahermosa

---

## Español

Este proyecto es una herramienta en Python que permite analizar la complejidad de automatización de una página web, identificando la cantidad de botones, campos de escritura y dropdowns presentes en la página.

### Requisitos

Antes de ejecutar el script, asegúrese de tener instaladas las siguientes dependencias:

```bash
pip install selenium webdriver-manager tkinter
```

### Uso

1. Ejecute el script `analizador_webs.py`.
2. Ingrese la URL de la página a analizar en la caja de texto.
3. Haga clic en el botón "Analizar".
4. Se mostrará un mensaje con el número de botones, campos de texto y dropdowns detectados en la página.

### Funcionalidades

- **Interfaz gráfica simple** con `tkinter`.
- **Análisis automático de la página** con Selenium.
- **Corrección de URL**: Si el usuario ingresa una URL sin `http://` o `https://`, el programa lo agrega automáticamente.
- **Modo sin cabeza** (`headless`): El análisis se realiza sin abrir una ventana del navegador.

### Consideraciones

- Este script utiliza Google Chrome como navegador predeterminado.
- Si se encuentra un error al cargar la página, se mostrará un mensaje de error con la causa del problema.

### Autor
Francisco Villahermosa

