
from flask import Flask, render_template, request, redirect, url_for, session
import random
from elementos import elementos

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesario para manejar sesiones

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        if not nombre.startswith(('Dr.', 'Dra.')):
            error = "¡Debes ingresar un nombre válido que comience con Dr. o Dra.!"
            return render_template('index.html', error=error)
        session['nombre'] = nombre
        return redirect(url_for('modo'))
    return render_template('index.html')

@app.route('/modo', methods=['GET', 'POST'])
def modo():
    if request.method == 'POST':
        modo = int(request.form['modo'])
        session['modo'] = modo
        return redirect(url_for('jugar'))
    return render_template('modo.html')

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if 'pregunta' not in session:
        elemento = random.choice(list(elementos.items()))
        session['elemento'] = elemento
        session['intentos'] = 0

        num_atomico, (nombres, simbolo) = elemento
        modo = session['modo']
        if modo == 1:
            session['pregunta'] = f"¿Cuál es el número atómico de {nombres[0]} ({simbolo})?"
            session['respuesta'] = str(num_atomico)
        elif modo == 2:
            session['pregunta'] = f"¿Cuál es el nombre del elemento con número atómico {num_atomico} y símbolo {simbolo}?"
            session['respuesta'] = nombres[0].lower()
        else:
            session['pregunta'] = f"¿Cuál es el símbolo del elemento {nombres[0]} con número atómico {num_atomico}?"
            session['respuesta'] = simbolo.lower()

    if request.method == 'POST':
        guess = request.form['respuesta'].strip().lower()
        session['intentos'] += 1
        if guess == session['respuesta']:
            correcto = True
            return render_template('resultado.html', correcto=correcto, nombre=session['nombre'])
        elif session['intentos'] >= 5:
            correcto = False
            return render_template('resultado.html', correcto=correcto, nombre=session['nombre'],
                                   respuesta_correcta=session['respuesta'])
        else:
            error = f"Incorrecto. Intento {session['intentos']}/5. Intenta de nuevo."
            return render_template('jugar.html', pregunta=session['pregunta'], error=error)

    return render_template('jugar.html', pregunta=session['pregunta'])

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
