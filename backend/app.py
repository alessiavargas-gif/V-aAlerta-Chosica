from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

alertas_chosica = [
    {
        "id": 1,
        "zona": "Quebrada Quirio - Carretera Central (Km 34)",
        "estado": "PRECAUCIÓN",
        "mensaje": "Incremento de caudal reportado por vecinos.",
        "hora": "12:30 PM"
    },
    {
        "id": 2,
        "zona": "Quebrada Pedregal - Chosica",
        "estado": "DESPEJADA",
        "mensaje": "Tránsito fluido sin novedades.",
        "hora": "12:45 PM"
    }
]

@app.route('/api/alertas', methods=['GET'])
def obtener_alertas():
    return jsonify(alertas_chosica)

@app.route('/api/reportar-gesto', methods=['POST'])
def reportar_gesto():
    datos = request.json
    zona = datos.get("zona", "Carretera Central - Tramo Chosica")
    tipo_gesto = datos.get("gesto", "Mano Abierta (Alerta de Huaico)")
    
    nueva_alerta = {
        "id": len(alertas_chosica) + 1,
        "zona": zona,
        "estado": "BLOQUEADA",
        "mensaje": f"¡ALERTA GESTUAL! Reporte ciudadano activado mediante: {tipo_gesto}",
        "hora": datetime.now().strftime("%I:%M %p")
    }
    
    alertas_chosica.insert(0, nueva_alerta)
    return jsonify({"status": "ok", "alerta": nueva_alerta}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
