import smtplib
from email.message import EmailMessage

def enviar_mensagem(mensagem_texto: str,
                    sender: str,
                    assunto: str,
                    senha_pass_sv: str,
                    destinatario: str):

    print("Iniciando Envio..")
    print(f"Destinatário: {destinatario}")
    
    mensagem = EmailMessage()
    mensagem.set_content(mensagem_texto)
    mensagem['Subject'] = assunto
    mensagem['From'] = sender
    mensagem['To'] = destinatario

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender, senha_pass_sv)
    s.send_message(mensagem)
    s.quit()