import os

# 1. 讀取文字設定
txt_path = 'character.txt'
content = "Google Diva V3"
if os.path.exists(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\n', '<br>')

# 2. 升級版 HTML 模板：加入合成引擎
html_template = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diva Cloud Synthesis</title>
    <style>
        body {{ background: #0b0e14; color: #0ef; text-align: center; font-family: 'Courier New', monospace; }}
        .console {{ border: 2px solid #0ef; padding: 20px; display: inline-block; margin-top: 30px; border-radius: 10px; background: rgba(0,0,0,0.8); box-shadow: 0 0 15px #0ef; }}
        img {{ width: 180px; filter: drop-shadow(0 0 10px #0ef); margin-bottom: 15px; cursor: pointer; }}
        input {{ background: #000; border: 1px solid #0ef; color: #0ef; padding: 10px; width: 80%; margin: 10px 0; }}
        button {{ background: #0ef; color: #000; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; }}
        .log {{ font-size: 0.8em; color: #555; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="console">
        <h1>DIVA SYNTHESIS SYSTEM</h1>
        <img src="image.png" id="avatar">
        <div id="info" style="font-size:0.9em;">{content}</div>
        
        <input type="text" id="voiceInput" placeholder="輸入日文字符 (如: あいう)">
        <br>
        <button onclick="synthesize()">執行雲端合成</button>
        
        <div class="log" id="status">系統就緒...</div>
    </div>

    <script>
        async function synthesize() {{
            const input = document.getElementById('voiceInput').value;
            const status = document.getElementById('status');
            const avatar = document.getElementById('avatar');
            
            // 將輸入拆解成單個字符
            const chars = input.split('');
            status.innerText = "正在從雲端抓取零件...";
            
            for (let char of chars) {{
                try {{
                    // 這裡會自動對應妳 GitHub 上的 .wav 檔案
                    const audio = new Audio(encodeURIComponent(char) + '.wav');
                    avatar.style.transform = "scale(1.1)";
                    status.innerText = "正在播放: " + char;
                    
                    await new Promise((resolve) => {{
                        audio.onended = resolve;
                        audio.onerror = () => {{
                            console.log("找不到音訊: " + char);
                            resolve(); // 跳過找不到的音檔
                        }};
                        audio.play();
                    }});
                    avatar.style.transform = "scale(1.0)";
                }} catch (e) {{ console.error(e); }}
            }}
            status.innerText = "合成任務完成。";
        }}
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("✅ 雲端合成版轉換完成！")
