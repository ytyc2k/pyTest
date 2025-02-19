import os
import gtts
import pygame
import threading
import time

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    os.remove(file)

def speak_word(word):
    """ 生成并播放单词语音 """
    slow_word = " ".join(word)  # Add spaces between letters (e.g., "h e l l o")
    tts = gtts.gTTS(f"{word}. {slow_word}. {word}", lang='en', slow=True)  
    # tts = gtts.gTTS(word, lang='en',slow=True)
    audio_file = "word.mp3"
    tts.save(audio_file)

    # 让音频播放在单独的线程中进行，避免阻塞 input
    thread = threading.Thread(target=play_audio, args=(audio_file,))
    thread.start()

if __name__ == "__main__":
    while True:
        word = input("请输入要发声的英文单词（输入 'exit' 退出）： ")
        if word.lower() == "exit":
            break
        speak_word(word)
