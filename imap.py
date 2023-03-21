import imaplib
import email
import os
import human_detector_ia
import telegram


class ImapEmailDownloader:
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.server, self.port)
        self.connection.login(self.username, self.password)
        self.connection.select()

    def download_attachments_from_sender(self, sender):
        self.connect()
        _, messages = self.connection.search(None, f'FROM "{sender}"')
        for message_number in messages[0].split():
            _, msg = self.connection.fetch(message_number, "(RFC822)")
            email_message = email.message_from_bytes(msg[0][1])
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                filename = part.get_filename()
                if filename is not None:
                    buffered = part.get_payload(decode=True)
                    if (human_detector_ia.detect_human(filename, buffered)):
                        telegram.send_dvrimage(buffered)

                    # with open(filepath, 'wb') as f:
                    #   buffered=part.get_payload(decode=True)
                    #   f.write(buffered)
                    #   human_file_detector.detect_human(filename,buffered)
                    #   human_detector_ia.detect_human(filename,buffered)
            self.connection.store(message_number, '+FLAGS', '\\Deleted')
            # self.connection.uid('STORE',message_number, '+FLAGS', '(\\Deleted)')
        self.connection.expunge()
        self.connection.close()
        self.connection.logout()
