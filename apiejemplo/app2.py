import requests
import os

# Definir la URL base de la API de RandomFox
url = "https://randomfox.ca/floof/"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()
    # Obtener la URL de la imagen
    # image_url = data['image']
    # Obtener el enlace para más información
    # fox_link = data['link']
    image_url = "https://randomfox.ca/images/44.jpg"
    fox_link = "https://randomfox.ca/?i=44"


    # Crear un archivo HTML con la imagen y explicación
    html_content = f"""
    <html>
    <head>
        <title>Usando la API de RandomFox</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 20px;
            }}
            h1 {{
                color: #ff6600;
            }}
            p {{
                font-size: 16px;
            }}
            .image-container {{
                text-align: center;
                margin-top: 20px;
            }}
            img {{
                max-width: 80%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}
            .code-example {{
                background-color: #f1f1f1;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-family: monospace;
                margin-top: 20px;
                white-space: pre-wrap;
            }}
        </style>
    </head>
    <body>
        <h1>Bienvenido a la API de RandomFox</h1>
        <p>Esta es una imagen aleatoria de un zorro obtenida de la API de RandomFox. La API devuelve imágenes de zorros en formato JSON que puedes utilizar en tus aplicaciones.</p>
        
        <div class="image-container">
            <h2>Imagen de un zorro:</h2>
            <img src="{image_url}" alt="Zorro Aleatorio">
        </div>

        <h2>¿Cómo utilizar la API?</h2>
        <p>La API de RandomFox permite obtener imágenes de zorros en diferentes formatos. Para usarla, debes realizar una solicitud HTTP y acceder a los datos JSON que te devuelven.</p>

        <div class="code-example">
            <strong>Código de ejemplo en Python:</strong>

            <pre>
import requests

url = "https://randomfox.ca/floof/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    image_url = data['image']
    print(f"Imagen de zorro: {image_url}")
else:
    print("Error al obtener la imagen.")
            </pre>
        </div>

        <h2>Enlace para más información:</h2>
        <p>Para obtener más imágenes de zorros, visita <a href="{fox_link}" target="_blank">este enlace</a>.</p>
    </body>
    </html>
    """

    # Guardar el contenido en un archivo HTML
    file_path = os.path.join(os.getcwd(), "fox_api_example.html")
    with open(file_path, "w") as file:
        file.write(html_content)

    print(f"Archivo HTML generado con éxito: {file_path}")
else:
    print("Error al obtener los datos de la API:", response.status_code)