import requests
import streamlit as st
from PIL import Image
from io import BytesIO
from summarize_text import summarize_text


# summarize the news
def summarize_news(news_data):
    return {
        "urlToImage": news_data.get("urlToImage"),
        "title": news_data.get("title"),
        "description": summarize_text(news_data.get("description")),
        "publishedAt": news_data.get("publishedAt"),
        "url": news_data.get("url"),
    }


# fetch data from api news
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=40d48ff77f634e32941913f9f831c262"
    response = requests.get(url)
    if response.status_code == 200:
        news_list = response.json().get("articles")
        return [summarize_news(article) for article in news_list]
    else:
        st.error("Error can not fetch data")
        return []


# load from url image to image
def load_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None


# UI for news option
def function_news():
    news_articles = fetch_news()

    if news_articles:
        for article in news_articles:
            image_url = article['urlToImage']
            img = load_image_from_url(image_url)

            if img:
                st.image(img)
                st.subheader(article['title'])
                st.write(article['description'])
                st.write(f"Published at: {article['publishedAt']}")
                st.markdown(f"[Read more]({article['url']})")
                st.write("---")
            else:
                st.write("Image is invalid")
                st.subheader(article['title'])
                st.write(f"Published at: {article['publishedAt']}")
                st.markdown(f"[Read more]({article['url']})")
                st.write("---")
