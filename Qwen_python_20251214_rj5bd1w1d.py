import requests

@app.route('/pedido/<int:pedido_id>/pagar', methods=['POST'])
@token_required
def pagar_pedido(current_user_id, pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    if pedido.usuario_id != current_user_id:
        return jsonify({'erro': 'Não autorizado'}), 403

    # Dados para o Pix
    data = {
        "transaction_amount": float(pedido.total),
        "description": f"Compra no {pedido.supermercado.nome}",
        "payment_method_id": "pix",
        "payer": {
            "email": "cliente@teste.com"  # ideal: buscar do usuário logado
        }
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('MERCADO_PAGO_ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.mercadopago.com/v1/payments",
        json=data,
        headers=headers
    )

    if response.status_code == 201:
        result = response.json()
        return jsonify({
            'qr_code': result['point_of_interaction']['transaction_data']['qr_code'],
            'qr_code_base64': result['point_of_interaction']['transaction_data']['qr_code_base64'],
            'status': result['status']
        })
    else:
        return jsonify({'erro': 'Falha ao gerar Pix', 'detalhes': response.json()}), 400