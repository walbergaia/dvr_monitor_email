import json
from time import sleep
from imap import ImapEmailDownloader

# Lendo as configurações a partir do arquivo JSON
with open('configdetector.json', 'r') as f:
    config = json.load(f)

while True:
    # Usando as configurações lidas do arquivo JSON
    email_config = config['email']
    downloader = ImapEmailDownloader(email_config['server'], email_config['port'], email_config['username'], email_config['password'])
    downloader.download_attachments_from_sender(email_config['sender'])
    sleep(email_config['interval'])