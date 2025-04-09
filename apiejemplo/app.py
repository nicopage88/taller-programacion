import requests
import os

# Definir la URL base de la API de TheCatAPI
url = "https://api.thecatapi.com/v1/images/search"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()
    # Obtener la URL de la imagen
    image_url = data[0]['url']

    # Crear un archivo HTML con la imagen y explicación
    html_content = f"""
    <html>
    <head>
        <title>Usando TheCatAPI</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 20px;
            }}
            h1 {{
                color: #4CAF50;
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
        <h1>Bienvenido a la API de TheCatAPI</h1>
        <p>Esta es una imagen aleatoria de un gato obtenida de la API de TheCatAPI. La API devuelve imágenes de gatos en formato JSON que puedes utilizar en tus aplicaciones.</p>
        
        <div class="image-container">
            <h2>Imagen de un gato:</h2>
            <img src="{image_url}" alt="Gato Aleatorio">
        </div>

        <h2>¿Cómo utilizar la API?</h2>
        <p>La API de TheCatAPI permite obtener imágenes de gatos en diferentes formatos. Para usarla, debes realizar una solicitud HTTP y acceder a los datos JSON que te devuelven.</p>

        <div class="code-example">
            <strong>Código de ejemplo en Python:</strong>

            <pre>
import requests

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    image_url = data[0]['url']
    print(f"Imagen de gato: {image_url}")
else:
    print("Error al obtener la imagen.")
            </pre>
        </div>

        <h2>Parámetros de consulta disponibles</h2>
        <ul>
            <li><strong>limit</strong>: Número de imágenes que deseas obtener (por defecto es 1).</li>
            <li><strong>order</strong>: Orden de las imágenes (RAND para aleatorio, DESC o ASC para fechas).</li>
            <li><strong>has_breeds</strong>: Filtrar imágenes por gatos con información de raza (0 o 1).</li>
            <li><strong>breed_ids</strong>: Filtro de imágenes por raza (por ejemplo, <code>beng</code>, <code>abys</code>).</li>
        </ul>
    </body>
    </html>
    """

    # Guardar el contenido en un archivo HTML
    file_path = os.path.join(os.getcwd(), "cat_api_example.html")
    with open(file_path, "w") as file:
        file.write(html_content)

    print(f"Archivo HTML generado con éxito: {file_path}")
else:
    print("Error al obtener los datos de la API:", response.status_code)
