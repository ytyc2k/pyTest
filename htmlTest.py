import webbrowser

html_content = """\
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python 生成的网页</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>欢迎来到 Python 生成的网页</h1>
        <p>这是一个简单的示例页面，由 Python 生成 HTML 代码。</p>
        <p>发货尽快释放空间是否</p>
    </div>
</body>
</html>
"""

# 将 HTML 内容写入文件
file_path = "generated_page.html"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# 在浏览器中打开生成的网页
webbrowser.open(file_path)
