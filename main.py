from moviepy.video.io.VideoFileClip import VideoFileClip
import cv2
import os

# Função para cortar o vídeo, se necessário
def cortar_video(input_path, output_path, inicio, fim):
    video = VideoFileClip(input_path)
    novo_video = video.subclip(inicio, fim)
    novo_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    video.close()

# Função para separar o frames do vídeo 
def extract_frames(video_path, output_folder, step):
    cap = cv2.VideoCapture(video_path)    
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)    
    for i in range(0, total_frames, step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i) 
        ret, frame = cap.read() 
        if not ret:
            break
        frame_filename = os.path.join(output_folder, f"frame_{i}.jpg")
        cv2.imwrite(frame_filename, frame)
    cap.release()


if __name__ == "__main__":
    input_path = input("Digite o caminho do vídeo de entrada: ")
    resposta = input("Deseja cortar o vídeo? (S/N): ").upper()
    if resposta == "S":
        #input_path = input("Digite o caminho do vídeo de entrada: ")
        output_path = input("Digite o caminho para salvar o novo vídeo: ")
        inicio = float(input("Digite o instante de início (em segundos): "))
        fim = float(input("Digite o instante de fim (em segundos): "))
        cortar_video(input_path, output_path, inicio, fim)
        print("Vídeo cortado e salvo com sucesso!")
    elif resposta == "N":
        print("Processo de corte do vídeo cancelado.")
        output_path = input_path
    else:
        print("Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não.")
    
    video_path = output_path
    output_folder = input("Digite o caminho para salvar os frames: ")    
    step = int(input('Defina o passo dos frames: '))   
    extract_frames(video_path, output_folder, step)
    print("Frames separados com sucesso!")




