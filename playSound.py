import os
import time
import pygame
from gtts import gTTS
from collections import deque

MAX_FILES = 5  # 最多保留 5 个语音文件
FILENAME_PREFIX = "output"
file_queue = deque()  # 用于存储文件的队列（先进先出）

def generate_speech_file(text):
    """生成新的语音文件"""
    file_index = len(file_queue) + 1
    filename = f"{FILENAME_PREFIX}_{file_index}.mp3"

    tts = gTTS(text=text, lang="en")  # 设置为英语
    tts.save(filename)
    print(f"Generated speech file: {filename}")

    file_queue.append(filename)  # 记录新文件
    return filename

def play_audio(filename):
    """使用 pygame 播放音频"""
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # 等待播放完成
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()  # 释放音频文件，防止占用

def play_and_manage_files(filename):
    """播放语音文件，播放完成后删除最旧的文件"""
    if os.path.exists(filename):
        print(f"Playing {filename} ...")
        play_audio(filename)  # 播放语音

    # 确保文件队列不会超过 MAX_FILES
    if len(file_queue) > MAX_FILES:
        old_file = file_queue.popleft()  # 获取最旧的文件
        if os.path.exists(old_file):
            os.remove(old_file)  # 删除最旧的文件
            print(f"Deleted old file: {old_file}")

# 示例循环调用（英文单词）
text_list = [
    "apple",  # apple
    "banana",  # banana
    "cherry",  # cherry
    "date",  # date
    "elderberry",  # elderberry
    "fig",  # fig
    "grape"  # grape
]

for text in text_list:
    new_file = generate_speech_file(text)  # 生成新语音文件
    play_and_manage_files(new_file)  # 播放语音并管理文件
