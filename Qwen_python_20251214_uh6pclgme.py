from firebase_admin import messaging, initialize_app, credentials

# Inicialize Firebase (coloque seu arquivo serviceAccountKey.json na raiz)
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)

def enviar_notificacao_entregador(mensagem):
    # Suponha que você tenha um token FCM de um entregador disponível
    entregador_fcm_token = "TOKEN_FCM_DO_ENTREGADOR"  # vindo do banco

    message = messaging.Message(
        notification=messaging.Notification(
            title="Novo Pedido!",
            body=mensagem
        ),
        token=entregador_fcm_token
    )
    messaging.send(message)