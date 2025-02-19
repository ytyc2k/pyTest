<?php
$urls = [
    "https://www.google.com",
    "https://www.baidu.com",
    "http://glant.cn"
];
?>
<!DOCTYPE html>
<html>
<head>
    <title>每5秒打开一个新网站</title>
</head>
<body>
    <button onclick="startOpening()">开始打开网站</button>

    <script>
        var urls = <?php echo json_encode($urls); ?>; // 将 PHP 数组转换为 JavaScript 数组
        var index = 0;

        function openNextSite() {
            if (index < urls.length) {
                window.open(urls[index], "_blank");
                index++;
            } else {
                clearInterval(interval); // 所有网站都打开后停止
            }
        }

        function startOpening() {
            index = 0; // 重置索引
            interval = setInterval(openNextSite, 5000); // 每 5 秒打开一个
        }
    </script>
</body>
</html>
