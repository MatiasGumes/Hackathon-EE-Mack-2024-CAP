#criptografia da pasta
from cryptography.fernet import Fernet 
import os 

# Função para gerar uma chave de criptografia 
def gerar_chave(): 
    return Fernet.generate_key()

# Função para criptografar uma pasta 
def criptografar_pasta(caminho_pasta, chave): 
    fernet = Fernet(chave) 
    for root, _, files in os.walk(caminho_pasta): 
        for file in files: 
            caminho_arquivo = os.path.join(root, file) 
            with open(caminho_arquivo, 'rb') as f: 
                dados = f.read() 
            dados_criptografados = fernet.encrypt(dados) 
            with open(caminho_arquivo + '.encrypted', 'wb') as f: 
                f.write(dados_criptografados) 
            os.remove(caminho_arquivo) 

# Função para descriptografar uma pasta 
def descriptografar_pasta(caminho_pasta, chave): 
    fernet = Fernet(chave) 
    for root, _, files in os.walk(caminho_pasta): 
        for file in files: 
            if file.endswith('.encrypted'): 
                caminho_arquivo = os.path.join(root, file) 
                with open(caminho_arquivo, 'rb') as f: 
                    dados_criptografados = f.read() 
                dados_descriptografados = fernet.decrypt(dados_criptografados) 
                with open(caminho_arquivo[:-10], 'wb') as f: 
                    f.write(dados_descriptografados) 
                os.remove(caminho_arquivo)  

if __name__ == "__main__": 
    # Defina o caminho para a pasta que deseja criptografar/descriptografar 
    caminho_pasta = "C:\Base_dados" 
    # Gere uma chave de criptografia 
    chave = gerar_chave() 
    print("chave:", chave)
    # Criptografar a pasta 
    criptografar_pasta(caminho_pasta, chave) 
    # Descriptografar a pasta 
    descriptografar_pasta(caminho_pasta, chave) 

#acessar a pasta
import os 
 # Define o caminho para a pasta de imagens 
folder_path = "C:\Base_dados" 
# Lista todos os arquivos na pasta 
image_files = os.listdir(folder_path) 
# Exibe os nomes dos arquivos 
for file in image_files: 
    print(file) 

#diferenciação rosto foto x rosto real + captura de rosto real
import cv2
import threading

# Load Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Global variables for status and frame
status = ""
frame = None

# Function to process frames and detect eye movement
def process_frame():
    global frame, status

    while True:
        if frame is not None:
            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Loop through each detected face
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                # Detect eyes in the face region
                eyes = eye_cascade.detectMultiScale(roi_gray)
                
                # Check if eyes are detected
                if len(eyes) < 2:
                    status = "Photo"
                else:
                    status = "Real Face"
                    cv2.imwrite('temp_frame.jpg', frame)
                
                # Display status on the frame
                cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Draw rectangle around the face and eyes
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

            # Display the resulting frame
            cv2.imshow('Eye Movement Tracking', frame)

            # Clear the frame to release the lock
            frame = None

            # mandar o python esperar um pouquinho -> de um jeito inteligente\
            tecla = cv2.waitKey(2)
            # mandar ele parar o código se eu clicar no ESC\n",
            if tecla == 27:
                break
# Start capturing video from the default camera
video_capture = cv2.VideoCapture(0)

# Start the thread for processing frames
thread = threading.Thread(target=process_frame)
thread.daemon = True
thread.start()

while True:
    # Capture frame-by-frame
    ret, new_frame = video_capture.read()

    if ret:
        frame = new_frame
    # mandar o python esperar um pouquinho -> de um jeito inteligente\
    tecla = cv2.waitKey(2)
    # mandar ele parar o código se eu clicar no ESC\n",
    if tecla == 27:
        break
# Liberar recursos e fechar a janela

video_capture.release()

cv2.destroyAllWindows()

#reconhecimento facial (comparação da captura de rosto real com banco de dados)
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
if status == "Photo":
    print("NÃO É POSSÍVEL REALIZAR O RECONHECIMENTO")
else:
    for file in image_files:
        # Define o caminho completo para o arquivo de imagem 
        image_path = os.path.join(folder_path, file) 
        # Lê a imagem 
        image = cv2.imread(image_path) 
        #definir caminho para frame da webcam
        temp_frame_path = "temp_frame.jpg"
        img_frame = cv2.imread(temp_frame_path)
        #reconhecimento = autenticação
        resultado = DeepFace.verify(image_path, temp_frame_path)
        verificacao = resultado["verified"]
        if verificacao:
          print("Comparando")
          plt.imshow(image[:,:,::-1])
          plt.show()
          print("Com")
          plt.imshow(img_frame[:, :, ::-1])
          plt.show()
          break
    if verificacao:
      print("ROSTO IDENTIFICADO")
    else:
        print("ROSTO NÃO IDENTIFICADO")