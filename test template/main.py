from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import pathlib

app = FastAPI(title="ADCS Monitor API")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    """
    根目錄路由：讀取並回傳 index.html 的內容
    """
    html_path = pathlib.Path(__file__).parent / "index.html"
    try:
        html_content = html_path.read_text(encoding="utf-8")
        return html_content
    except FileNotFoundError:
        return "找不到 index.html 檔案，請確保它與 main.py 在同一個資料夾下。"

@app.get("/api/telemetry")
async def get_telemetry_data():
    """
    API 路由：回傳模擬的 ADCS 遙測數據
    （之後可以換成讀取真實感測器或硬體的數據）
    """
    return {
        "roll": random.uniform(-5.0, 5.0),
        "pitch": random.uniform(-5.0, 5.0),
        "yaw": random.uniform(0.0, 360.0),
        "status": "online"
    }

if __name__ == "__main__":
    import uvicorn
    # 執行 Uvicorn 伺服器，預設綁定 127.0.0.1:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
