import sys
from generate_wordcloud import generate_wordcloud

generate_wordcloud()

def batch():
    print("▶️ バッチ処理開始")
    generate_wordcloud()
    print("✅ バッチ処理完了")

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "batch":
        batch()
    else:
        print("使い方: python main.py batch")