from config import SMTP_SERVER
import smtplib, ssl
from config import *



def _combine_subject_and_body(subject: str, body: str) -> str:
    return f'Subject: {subject}\n\n{body}'

def send_mail(subject, body, do_print=True, debug=False):
    context = ssl.create_default_context()
    content = _combine_subject_and_body(subject, body)
    if do_print:
        print("SENDING CONTENT: \n\n")
        print(content)
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context, local_hostname="foobarbaz") as server:
        if debug: server.set_debuglevel(2)
        server.login(SEND_FROM, PASSWORD)
        server.sendmail(SEND_FROM, SEND_TO, content.encode('utf-8'))
