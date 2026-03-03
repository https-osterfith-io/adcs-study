# 檔案名稱：test_gpu.py
import torch

def check_gpu():
    print("=== GPU 狀態測試 ===")
    
    # 檢查 CUDA 是否可用
    is_gpu_available = torch.cuda.is_available()
    print(f"1. GPU 是否可用: {is_gpu_available}")
    
    if is_gpu_available:
        # 取得 GPU 數量
        gpu_count = torch.cuda.device_count()
        print(f"2. 偵測到的 GPU 數量: {gpu_count} 張")
        
        # 取得第一張 GPU 的名稱
        gpu_name = torch.cuda.get_device_name(0)
        print(f"3. GPU 型號: {gpu_name}")
        
        # 測試一個小運算，確認 GPU 真的能跑
        print("4. 正在進行張量 (Tensor) 運算測試...")
        x = torch.rand(5, 5).cuda() # 把數據丟到 GPU
        y = torch.rand(5, 5).cuda()
        z = x + y
        print("   -> 運算成功！你的 GPU 準備好上工了！")
    else:
        print("\n[警告] 系統沒有偵測到 GPU，目前只能使用 CPU 運算。")
        print("請檢查：1. 機器是否真的有 GPU？ 2. 顯示卡驅動與 CUDA 是否正確安裝？")

if __name__ == "__main__":
    check_gpu()