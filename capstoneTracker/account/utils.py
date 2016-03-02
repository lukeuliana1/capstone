import os, random, string
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

def generate_temp_password():   
    length = 7
    chars = string.ascii_letters + string.digits
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars) for i in range(length))

def send_confirmation_email(user):
    try:    
        confirmation_key = user.confirmation_key
    except:
        confirmation_key = user.add_unconfirmed_email(user.email)
    msg_txt=render_to_string('email/confirmation.txt', {'SITE_URL': settings.SITE_URL, 'user': user.email, 'key' : confirmation_key})
    msg_html = render_to_string('email/confirmation.html', {'SITE_URL': settings.SITE_URL, 'user': user.email, 'key' : confirmation_key})
    return send_mail('Confirmation email',msg_txt,'daniyar.yeralin@gmail.com',[user.email],html_message=msg_html,)