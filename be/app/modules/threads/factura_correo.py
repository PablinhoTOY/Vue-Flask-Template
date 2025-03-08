# Llama a esta función para enviar correos electrónicos en un hilo separado
import threading
from app import *
from flask_mail import Message
from app.modules.utils import processCorreo
import requests

def enviar_correo_asincrono(correo, subject, html):
    with app.app_context():
        msg = Message()
        msg.subject = subject
        msg.recipients = [correo]
        msg.html = html
        # Envía el correo
        mail.send(msg)
        
def enviar_correo(correo, subject, html):
    thread = threading.Thread(target=enviar_correo_asincrono, args=(correo, subject, html))
    thread.start()