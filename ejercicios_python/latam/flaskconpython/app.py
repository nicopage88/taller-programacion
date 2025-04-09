from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite solicitudes de diferentes orígenes (React)

# Datos de ejemplo para enviar a React
products = [
    {"id": 1, "name": "Laptop", "price": 1000, "category": "Electronics"},
    {"id": 2, "name": "Shoes", "price": 50, "category": "Clothing"},
    {"id": 3, "name": "Smartphone", "price": 500, "category": "Electronics"},
    {"id": 4, "name": "Watch", "price": 150, "category": "Accessories"},
    {"id": 5, "name": "Backpack", "price": 80, "category": "Accessories"}
]

# Ruta para obtener los productos
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
