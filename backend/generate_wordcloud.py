def generate_wordcloud():
    import requests
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import os
    from datetime import datetime

    # APIキーを取得
    API_KEY = os.getenv("NEWSAPI_KEY")
    print("🔑 API_KEY:", "存在します" if API_KEY else "None")

    # API URL とパラメータ
    URL = 'https://newsapi.org/v2/top-headlines'
    PARAMS = {
        'country': 'us',
        'category': 'technology',
        'pageSize': 100,
        'apiKey': API_KEY,
    }

    # ニュースを取得
    try:
        response = requests.get(URL, params=PARAMS)
        data = response.json()
        print("📦 APIレスポンス status:", data.get("status"))
    except Exception as e:
        print(f"❌ APIリクエスト失敗: {e}")
        return

    # 記事がなければ終了
    if 'articles' not in data:
        print(f"⚠️ 'articles' が存在しません: {data.get('message')}")
        return

    # タイトルを連結してテキストに
    text_data = ' '.join(article['title'] for article in data['articles'] if article.get('title'))
    if not text_data:
        print("⚠️ 有効な記事タイトルが見つかりません")
        return

    # ワードクラウド生成
    try:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
    except Exception as e:
        print(f"❌ ワードクラウド生成失敗: {e}")
        return

    # 出力ディレクトリとパス作成
    today = datetime.now().strftime("%Y%m%d")
    output_dir = os.path.join("backend", "data", today)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "wordcloud.png")

    # 画像として保存
    try:
        wordcloud.to_file(output_path)
        print(f"✅ ワードクラウド画像生成成功: {output_path}")
    except Exception as e:
        print(f"❌ ワードクラウド画像保存失敗: {e}")
        return

    # 正常終了ログ
    print("✅ generate_wordcloud.py の処理が完了しました")