from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Configurar opciones de Chrome
options = Options()
options.headless = False  # Si deseas ver el navegador en acción, ponlo en False

# Inicializar el WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL de los libros
libros_url = "https://biblioteca.sgdls.cl/biblioteca/Libros"

# Navegar a la página
driver.get(libros_url)

# Esperar unos segundos para que la página cargue completamente
sleep(5)  # Espera 5 segundos o ajusta según sea necesario

# Verificar si la tabla existe
try:
    table = driver.find_element(By.ID, 'tblLibros')
    rows = table.find_elements(By.TAG_NAME, 'tr')[1:]  # Ignorar la primera fila (encabezado)
    
    # Extraer los datos de cada fila
    libros_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > 0:
            libro = {
                'id': cells[0].text.strip(),
                'titulo': cells[1].text.strip(),
                'cantidad': cells[2].text.strip(),
                'autor': cells[3].text.strip(),
                'editorial': cells[4].text.strip(),
                'materia': cells[5].text.strip(),
                'foto': cells[6].find_element(By.TAG_NAME, 'img').get_attribute('src').strip(),
                'descripcion': cells[7].text.strip(),
                'estado': cells[8].text.strip(),
            }
            libros_data.append(libro)

    # Mostrar los datos extraídos
    for libro in libros_data:
        print(libro)

except Exception as e:
    print(f"Error: {e}")

# Cerrar el navegador
driver.quit()
