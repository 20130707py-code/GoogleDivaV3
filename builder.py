import os

# 1. 讀取妳的 txt 設定檔
txt_path = 'character.txt'
if not os.path.exists(txt_path):
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write("角色名稱: Google Diva\n設定內容: 這是來自 txt 的自動轉換版本")

with open(txt_path, 'r', encoding='utf-8') as f:
    content = f.read().replace('\n', '<br>')

# 2. 定義 HTML 模板 (把 txt 內容塞進去)
html_template = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Diva 自動生成版</title>
    <style>
        body {{ background: #1a1a1a; color: white; text-align: center; font-family: sans-serif; }}
        .card {{ background: #333; padding: 20px; border-radius: 15px; display: inline-block; margin-top: 50px; border: 2px solid #0ef; }}
        img {{ width: 200px; border-radius: 10px; cursor: pointer; }}
        .content {{ text-align: left; margin-top: 20px; color: #0ef; font-size: 1.1em; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Diva 系統啟動</h1>
        <img src="image.png" onclick="new Audio('あ.wav').play()">
        <div class="content">
            <strong>從檔案讀取的設定：</strong><br>
            {content}
        </div>
        <p style="font-size: 0.8em; color: #888;">(點擊圖片播放語音序列)</p>
    </div>
</body>
</html>
"""

# 3. 輸出成 HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("✅ 轉換完成！已根據 character.txt 更新 index.html")
