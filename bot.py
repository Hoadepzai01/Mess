import sys
import os
from main.patcute import *
from main.pat import *
from main import *

print("""
╔══════════════════════════════════════════╗
║   COPYRIGHT X AUTHOR: LỒN CON ĐĨ MẸ MÀY  ║
╚══════════════════════════════════════════╝
""")

try:
    pat.check_license()
except Exception as e:
    print(f"[!] Lỗi: {str(e)}")
    sys.exit(1)

try:
    patcute.main()
except Exception as e:
    print(f"[!] Lỗi: {str(e)}")
finally:
    input("Nhấn Enter để thoát...")

if __name__ == "__main__":
    pass