# Llama a esta función para enviar correos electrónicos en un hilo separado
import threading
from app import *
from flask_mail import Message
from app.modules.utils import processCorreo
import requests

def enviar_factura_correo_asincrono(cedula, subject, html):
    with app.app_context():
        correo = requests.post('https://digital.utp.ac.pa:8080/estudiantes/cedula-a-correo', json={'cedula': cedula}).text
        correo = processCorreo(correo)
        msg = Message()
        msg.subject = subject
        msg.recipients = [correo]
        msg.html = html
        # Envía el correo
        mail.send(msg)
        
def enviar_factura_correo(cedula, subject, html):
    thread = threading.Thread(target=enviar_factura_correo_asincrono, args=(cedula, subject, html))
    thread.start()