from flask import Flask, request, jsonify

app = Flask(__name__)
# Esta lista actuará como memoria temporal en la nube
bandeja_mensajes = []

# El iPhone enviará los SMS aquí
@app.route('/sms', methods=['POST'])
def recibir_sms():
    datos = request.json
    bandeja_mensajes.append(datos)
    return "Mensaje guardado en la nube", 200

# Tu PC entrará aquí a revisar si hay mensajes nuevos
@app.route('/obtener', methods=['GET'])
def entregar_sms():
    global bandeja_mensajes
    # Copiamos los mensajes y vaciamos la bandeja para no enviarlos duplicados
    mensajes_nuevos = bandeja_mensajes.copy()
    bandeja_mensajes.clear()
    return jsonify(mensajes_nuevos), 200

if __name__ == '__main__':
    app.run(port=5000)