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
    msg_txt = '''
        Dear user,
        Thank you for registering on the CapitalOne Capstone Website.
        We need you to confirm your email. Here is a <a href="{{SITE_URL}}/account/confirm/?user={{user}}&key={{key}}"> Confirmation Link </a>.
        Here is your temporary password: {{password}}
        Thank you for registering!
        '''
    try:    
        confirmation_key = user.confirmation_key
        msg_html = render_to_string('email/confirmation.html', {'SITE_URL': settings.SITE_URL, 'user': user.email, 'key' : confirmation_key, 'password' : user.password})
        return send_mail('Confirmation email',msg_txt,'daniyar.yeralin@gmail.com',[user.email],html_message=msg_html,)
    except:
        confirmation_key = user.add_unconfirmed_email(user.email)
        msg_html = render_to_string('email/confirmation.html', {'SITE_URL': settings.SITE_URL, 'user': user.email, 'key' : confirmation_key, 'password' : user.password})
        return send_mail('Confirmation email',msg_txt,'daniyar.yeralin@gmail.com',[user.email],html_message=msg_html,)