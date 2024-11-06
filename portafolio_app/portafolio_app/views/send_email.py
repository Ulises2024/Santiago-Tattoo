import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from django.http import HttpResponse

def send_email(request):
    nombre = request.POST.get('nombre')
    email_receptor = request.POST.get('email_receptor')
    mensaje = request.POST.get('mensaje')
    # El resto de tu código de envío de correo
    return HttpResponse("Correo enviado exitosamente.")
