# generate_wordcloud.py

def generate_wordcloud():
    import requests
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import os
    from datetime import datetime

    API_KEY = os.getenv("NEWSAPI_KEY")
    print("🔑 API_KEY:", API_KEY)

    URL = 'https://newsapi.org/v2/top-headlines'
    PARAMS = {
        'country': 'us',
        'category': 'technology',
        'pageSize': 100,
        'apiKey': API_KEY,
    }

    response = requests.get(URL, params=PARAMS)
    data = response.json()
    print("📦 APIレスポンス:", data)

    if 'articles' not in data:
        print(f"⚠️ 'articles' が空、または存在しません。status: {data.get('status')} message: {data.get('message')}")
        return

    text_data = ' '.join(article['title'] for article in data['articles'] if article.get('title'))

    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=None).generate(text_data)

    today = datetime.now().strftime("%Y%m%d")
    output_dir = f"data/{today}"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "wordcloud.png")
    wordcloud.to_file(output_path)
    print(f"✅ ワードクラウド画像生成: {output_path}")