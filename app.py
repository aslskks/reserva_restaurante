from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Lista de reservas de restaurantes (por simplicidad, se almacenan en una lista en memoria).
reservas = []

# Función para registrar solicitudes en el archivo de registro (log.txt).
def registrar_solicitud(solicitud):
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as archivo_log:
        archivo_log.write(f"{fecha_hora_actual} - {solicitud}\n")

@app.route('/')
def index():
    return render_template('index.html', reservas=reservas)

@app.route('/agregar_reserva', methods=['POST'])
def agregar_reserva():
    nombre_cliente = request.form['nombre_cliente']
    fecha = request.form['fecha']
    hora = request.form['hora']
    num_personas = request.form['num_personas']

    # Agregar la reserva a la lista (en una aplicación real, deberías usar una base de datos).
    reservas.append({'nombre_cliente': nombre_cliente, 'fecha': fecha, 'hora': hora, 'num_personas': num_personas})

    # Registrar la solicitud en el archivo de registro.
    solicitud = f"Reserva de {nombre_cliente} para el {fecha} a las {hora} para {num_personas} personas."
    registrar_solicitud(solicitud)

    return redirect(url_for('index'))

if __name__ == '__main__':
    # Iniciar el servidor de desarrollo.
    app.run(debug=True)
