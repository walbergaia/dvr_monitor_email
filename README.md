# dvr_monitor_email

Fiz esse código em uma necessidade rápida que tive, onde meu DVR intelbras antigo, não detecta pessoas, somente avisa em caso de movimento com a foto via e-mail ou ftp. Nem todo movimento é um pessoa, então eu precisava saber quando alguém pulava o muro e ser notificado na hora via Telegram para eu pegar meu porrete.

1º Configurei primeiramente meu DVR para enviar as notificações de DM (Detecção de Movimento) com foto para um email xxxxx@gmail.com
2º Fiz esse código para ir no e-mail do GMAIL (Configurei a caixa para imap é mais rápido) pegar todas as fotos tiradas pelo DVR e analisar uma a uma
3º Ao analisar utilizando um modelo de detecção de objetos, filtrei "person" é claro, na detecção de um ser uma pessoa, enviar para um grupo no Telegram a foto.


Vou tentar melhorar, mas espero que possa ajudar alguém.

Utilizei o modelo (ele é bem menor é sem grana para hospedar, usei o https://www.pythonanywhere.com/):
yolov4-tiny.cfg
yolov4-tiny.weights

o bom é utilizar o completo:
yolov4.cfg
yolov4.weights




