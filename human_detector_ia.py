import cv2
import os
import numpy as np


# Baixe um modelo pré-treinado para detecção de objetos. Por exemplo, você pode baixar o modelo "YOLOv3" para detecção de objetos da biblioteca Darknet:
# wget https://pjreddie.com/media/files/yolov3.weights
# pip install opencv-python

def detect_human(file_name,buffer):
    # Carrega o modelo YOLOv3
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    # Define as classes que o modelo pode detectar
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Configurações do modelo
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1]
                     for i in net.getUnconnectedOutLayers()]

    # Define a cor para cada classe detectada
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Carrega o buffer de imagem
    nparr = np.frombuffer(buffer, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Redimensiona a imagem para que tenha um tamanho compatível com o modelo
    blob = cv2.dnn.blobFromImage(
        img, 0.00392, (416, 416), swapRB=True, crop=False)

    # Passa a imagem pelo modelo para detectar objetos
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Processa as detecções e desenha as caixas delimitadoras na imagem
    conf_threshold = 0.5
    nms_threshold = 0.4
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold and classes[class_id] == "person":
                center_x = int(detection[0] * img.shape[1])
                center_y = int(detection[1] * img.shape[0])
                w = int(detection[2] * img.shape[1])
                h = int(detection[3] * img.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Salva a imagem detectada na pasta "detectados" ou exibe a mensagem "Não detectado"
    if len(boxes) > 0:
        os.makedirs("detectados", exist_ok=True)
        for i in range(len(boxes)):
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        #cv2.imwrite(f"email_detected_ia/{file_name}", img)
        return True
        
    else:
        return False
        #print("Não detectado")


def detect_human_video(buffer):
    # Carrega o modelo YOLOv3
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    # Define as classes que o modelo pode detectar
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Configurações do modelo
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Define a cor para cada classe detectada
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Carrega o buffer de vídeo
    nparr = np.frombuffer(buffer, np.uint8)
    cap = cv2.VideoCapture()
    cap.open("pipe:.mp4")
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    out = cv2.VideoWriter("detectados/output.avi", fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    # Processa cada frame do vídeo
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Redimensiona o frame para que tenha um tamanho compatível com o modelo
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)

        # Passa o frame pelo modelo para detectar objetos
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Processa as detecções e desenha as caixas delimitadoras no frame
        conf_threshold = 0.5
        nms_threshold = 0.4
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > conf_threshold and classes[class_id] == "person":
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # Salva o frame detectado na pasta "detectados" ou exibe a mensagem "Não detectado"
        if len(boxes) > 0:
            for i in range(len(boxes)):
                box = boxes[i]
                x = box[0]
                y = box[1]
                w = box[2]
                h = box[3]
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            out.write(frame)
        else:
            out.write(frame)

    cap.release()
    out.release()




#with open("email_received/ch01_20230227_205404_E.jpg", "rb") as f:
#    buffer = f.read()

#detect_human(buffer)

