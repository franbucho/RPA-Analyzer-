Aquí tienes el archivo `README` en inglés y español para tu proyecto:

---

# Web Analyzer (Analizador de Páginas Web)

## Description / Descripción

This script allows you to analyze a webpage and retrieve various data points, such as the number of buttons, text fields, dropdowns, the publication year, programming language used, page security, and the quality of the code based on the number of scripts and CSS styles.

Este script te permite analizar una página web y obtener diversos puntos de datos, como el número de botones, campos de texto, dropdowns, el año de publicación, el lenguaje de programación utilizado, la seguridad de la página y la calidad del código basado en la cantidad de scripts y estilos CSS.

## Features / Características

- **Number of Buttons, Text Fields, and Dropdowns**  
- **Publication Year Detection**  
- **Programming Language Detection**  
- **Page Security (HTTP vs HTTPS)**  
- **Code Quality (based on scripts and CSS)**

- **Número de botones, campos de texto y dropdowns**  
- **Detección del año de publicación**  
- **Detección del lenguaje de programación**  
- **Seguridad de la página (HTTP vs HTTPS)**  
- **Calidad del código (basada en los scripts y CSS)**

## Requirements / Requisitos

- Python 3.x
- Selenium
- BeautifulSoup (bs4)
- WebDriver Manager
- ChromeDriver (or another supported browser driver)

- Python 3.x
- Selenium
- BeautifulSoup (bs4)
- WebDriver Manager
- ChromeDriver (u otro controlador de navegador compatible)

### Installation / Instalación

To run this script, you need to install the required Python libraries. You can install them using `pip`:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

Para ejecutar este script, necesitas instalar las bibliotecas de Python necesarias. Puedes instalarlas usando `pip`:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

### How to Use / Cómo Usar

1. Run the script by executing it in your Python environment.
2. Enter the URL of the webpage you want to analyze.
3. Click the "Analyze" button to start the analysis.
4. The results will appear in a pop-up window showing:
   - The number of buttons, text fields, and dropdowns.
   - The publication year detected.
   - The programming language detected.
   - The security of the page (HTTP or HTTPS).
   - The quality of the code based on the number of scripts and CSS.

1. Ejecuta el script en tu entorno de Python.
2. Ingresa la URL de la página web que deseas analizar.
3. Haz clic en el botón "Analizar" para comenzar el análisis.
4. Los resultados aparecerán en una ventana emergente mostrando:
   - El número de botones, campos de texto y dropdowns.
   - El año de publicación detectado.
   - El lenguaje de programación detectado.
   - La seguridad de la página (HTTP o HTTPS).
   - La calidad del código basado en la cantidad de scripts y CSS.

### Example / Ejemplo

1. Open the script and enter `https://example.com` in the input field.
2. After clicking "Analyze", a pop-up will show the analysis results for that page.

1. Abre el script e ingresa `https://example.com` en el campo de entrada.
2. Después de hacer clic en "Analizar", aparecerá una ventana emergente con los resultados del análisis para esa página.

## License / Licencia

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Listo! Ahora tienes un `README` que cubre tanto la versión en inglés como en español del proyecto. Si necesitas algún ajuste, no dudes en decírmelo.