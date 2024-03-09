import requests
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(subject, body):
    sender_email = "dario.rossi17121999@email.com"
    receiver_email = "dario.rossi.1712@email.com"
    password = "callistoH2Osommersa"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def get_hash(url):
    response = requests.get(url)
    return hashlib.sha256(response.content).hexdigest()

def monitor_page(url):
    current_hash = get_hash(url)
    while True:
        new_hash = get_hash(url)
        if new_hash != current_hash:
            send_email("Pagina Aggiornata", f"La pagina {url} è stata aggiornata! \n Controlla subito!")
            current_hash = new_hash
        time.sleep(300)  # Controlla ogni 5 minuti

if __name__ == "__main__":
    url_to_monitor1 = "https://www.grappa.amsterdam/opportunities"
    url_to_monitor2 = "https://github.com/dariorossi36/dariorossi36"
    url_to_monitor3 = "https://inspirehep.net/jobs?sort=mostrecent&size=25&page=1&status=open&region=Europe&rank=PHD"
    monitor_page(url_to_monitor1)
    monitor_page(url_to_monitor2)
    monitor_page(url_to_monitor3)