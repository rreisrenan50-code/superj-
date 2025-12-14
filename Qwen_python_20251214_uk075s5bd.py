from math import radians, sin, cos, sqrt, atan2

def distancia(lat1, lon1, lat2, lon2):
    R = 6371.0  # raio da Terra em km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

@app.route('/supermercados/proximos')
def supermercados_proximos():
    lat = float(request.args.get('lat', -23.55))
    lng = float(request.args.get('lng', -46.63))
    todos = Supermercado.query.filter(Supermercado.latitude.isnot(None)).all()
    ordenados = sorted(todos, key=lambda s: distancia(lat, lng, s.latitude, s.longitude))
    return jsonify([{
        'id': s.id,
        'nome': s.nome,
        'endereco': s.endereco,
        'distancia_km': round(distancia(lat, lng, s.latitude, s.longitude), 2)
    } for s in ordenados[:5]])