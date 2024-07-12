import os
import sys

# 獲取 my_project/src 的路徑
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 將 src 路徑添加到 sys.path
sys.path.append(src_path)

# 現在使用絕對導入
from utils.math import add

# 使用導入的函數
result = add(5, 3)
print(f"5 + 3 = {result}")