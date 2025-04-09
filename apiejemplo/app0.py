import requests

url = "https://randomfox.ca/floof/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    image_url = data['image']
    print(f"Imagen de zorro: https://randomfox.ca/images/44.jpg")
else:
    print("Error al obtener la imagen.")