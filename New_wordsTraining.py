import pygame
import random
import threading
import gtts
import os
import tempfile

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    print(f"Audio file {file} finished playing.")
    os.remove(file)

def speak_word(word):
    """ 生成并播放单词语音 """
    slow_word = " ".join(word)  # Add spaces between letters (e.g., "h e l l o")
    tts = gtts.gTTS(f"{word}. {slow_word}. {word}", lang='en', slow=True)
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        audio_file = tmp_file.name
        tts.save(audio_file)

    # 让音频播放在单独的线程中进行，避免阻塞 input
    thread = threading.Thread(target=play_audio, args=(audio_file,))
    thread.start()

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))

# 使用支持音标的字体（例如 NotoSans 或其他）
font_path = "NotoSansCJK-Regular.ttc"  # 支持汉字的字体
phonetic_font_path = "NotoSans-Regular-2.ttf"  # 支持音标的字体
font = pygame.font.Font(font_path, 50)  # 用于汉字和英文单词
score_font = pygame.font.Font(font_path, 30)
phonetic_font = pygame.font.Font(phonetic_font_path, 30)  # 用于音标
translation_font = pygame.font.Font(font_path, 20)  # 用于翻译的小字体

# 定义颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

import json

# 打开并读取 JSON 文件
with open("ENG.json", "r", encoding="utf-8") as f:
    words_with_phonetics_and_translations = json.load(f)  # 读取 JSON 并转换为字典

word_speed = 3  # 降低文字的滚动速度

# 游戏主循环
running = True
word_pos = screen_height-100  # 设置初始位置从屏幕底部开始
current_word = random.choice(list(words_with_phonetics_and_translations.keys()))  # 随机选择单词
speak_word(current_word)
current_input = ""  # 玩家输入的内容
current_direction = None

# 统计正确和错误的次数
correct_count = 0
wrong_count = 0

# 函数：检查文字是否超出屏幕宽度，并进行换行处理
def wrap_text(text, font, max_width):
    lines = []
    current_line = []
    current_line_width = 0

    # 将单词分割并逐个添加到当前行，直到行宽超过最大宽度
    for word in text.split():
        word_width, _ = font.size(word)
        if current_line_width + word_width <= max_width:
            current_line.append(word)
            current_line_width += word_width + font.size(' ')[0]  # 考虑单词之间的空格
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_line_width = word_width

    if current_line:
        lines.append(" ".join(current_line))

    return lines

# 函数：处理翻译部分的换行
def wrap_translation(text, font, max_width):
    lines = []
    current_line = []
    current_line_width = 0

    # 将每个字符逐个添加到当前行，直到行宽超过最大宽度
    for char in text:
        char_width, _ = font.size(char)  # 获取每个字符的宽度
        if current_line_width + char_width <= max_width:
            current_line.append(char)
            current_line_width += char_width  # 仅考虑字符宽度
        else:
            lines.append("".join(current_line))  # 换行
            current_line = [char]
            current_line_width = char_width

    if current_line:
        lines.append("".join(current_line))

    return lines

# Fireworks effect
def display_fireworks():
    """ 显示烟花效果 """
    firework_particles = []
    for _ in range(50):  # 创建50个烟花粒子
        particle = {
            'x': random.randint(screen_width - 100, screen_width - 50),
            'y': random.randint(50, 150),
            'color': random.choice([RED, YELLOW, BLUE, WHITE]),
            'size': random.randint(2, 6),
            'speed': random.uniform(1.0, 3.0)
        }
        firework_particles.append(particle)

    # 启动烟花动画
    for _ in range(30):  # 动画更新30次
        screen.fill(BLACK)  # 每次绘制新的背景

        for particle in firework_particles:
            particle['y'] -= particle['speed']
            pygame.draw.circle(screen, particle['color'], (particle['x'], particle['y']), particle['size'])

        pygame.display.flip()
        pygame.time.delay(50)  # 延迟，控制动画速度

# 游戏循环
while running:
    screen.fill(BLACK)
    # 获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]  # 删除最后一个字符
            elif event.key == pygame.K_RETURN:  # 按回车键检查拼写是否正确
                if current_input == current_word:
                    correct_count += 1  # 增加正确计数
                    display_fireworks()  # 显示烟花
                    word_pos = screen_height  # 重新从底部开始
                    current_word = random.choice(list(words_with_phonetics_and_translations.keys()))
                    speak_word(current_word)
                else:
                    wrong_count += 1  # 增加错误计数
                current_input = ""  # 重置输入框
            else:
                current_input += event.unicode  # 输入字符

    # 获取单词的渲染文本并进行换行处理
    wrapped_text = wrap_text(current_word, font, screen_width - 20)  # 留出边距
    y_offset = word_pos
    for line in wrapped_text:
        text_surface = font.render(line, True, RED)
        text_width, text_height = text_surface.get_size()
        text_x = (screen_width - text_width) // 2  # 计算居中的X坐标
        screen.blit(text_surface, (text_x, y_offset))
        y_offset += text_height  # 下移y坐标，显示下一行

    # 获取玩家输入的渲染文本
    input_surface = font.render(current_input, True, RED)
    input_width, input_height = input_surface.get_size()
    input_x = (screen_width - input_width) // 2  # 计算居中的X坐标
    input_y = screen_height - 440  # 设置Y坐标
    screen.blit(input_surface, (input_x, input_y))

    # 获取翻译部分的换行渲染文本
    translation_text = words_with_phonetics_and_translations[current_word]["translation"]
    wrapped_translation = wrap_translation(translation_text, translation_font, screen_width - 20)  # 留出边距
    translation_y = screen_height - 300  # 设置初始Y坐标
    for line in wrapped_translation:
        translation_surface = translation_font.render(line, True, WHITE)
        translation_width, translation_height = translation_surface.get_size()
        translation_x = (screen_width - translation_width) // 2  # 计算居中的X坐标
        screen.blit(translation_surface, (translation_x, translation_y))
        translation_y += translation_height  # 下移Y坐标，显示下一行

    # 获取音标的渲染文本
    phonetic_surface = phonetic_font.render(words_with_phonetics_and_translations[current_word]["phonetic"], True, WHITE)
    phonetic_width, phonetic_height = phonetic_surface.get_size()
    phonetic_x = (screen_width - phonetic_width) // 2  # 计算居中的X坐标
    phonetic_y = screen_height - 350  # 设置Y坐标
    screen.blit(phonetic_surface, (phonetic_x, phonetic_y))

    # 文字下移
    word_pos -= word_speed  # 让文字从下往上滚动
    if word_pos < -text_height:
        word_pos = screen_height-100  # 如果文字滚出屏幕，就从底部重新开始
        current_word = random.choice(list(words_with_phonetics_and_translations.keys()))
        speak_word(current_word)

    # 显示得分和错误统计
    correct_text = score_font.render(f"Correct: {correct_count}", True, WHITE)
    wrong_text = score_font.render(f"Wrong: {wrong_count}", True, RED)

    # 获取得分和错误统计的渲染文本并居中显示
    correct_width, correct_height = correct_text.get_size()
    correct_x = (screen_width - correct_width) // 2
    screen.blit(correct_text, (correct_x, 10))

    wrong_width, wrong_height = wrong_text.get_size()
    wrong_x = (screen_width - wrong_width) // 2
    screen.blit(wrong_text, (wrong_x, 40))

    # 更新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # 设置帧率

# 退出游戏
pygame.quit()
