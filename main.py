from time import sleep
from imap import ImapEmailDownloader


#downloader = Pop3EmailDownloader('pop.gmail.com', 995, 'dvrnotificacaoimagem@gmail.com', 'Gaia1979gm@')
#downloader.download_attachments_from_sender('gaialber@gmail.com', 'email_received')

while True:
    downloader = ImapEmailDownloader('imap.gmail.com', 993, 'dvrnotificacaoimagem@gmail.com', 'hureajgcekarpytx')
    downloader.download_attachments_from_sender('gaia.walber@gmail.com', 'email_received')
    sleep(120)