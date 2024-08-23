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
        "description": news_data.get("description"),
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
        st.error("Không thể lấy dữ liệu từ API")
        return []


# load from url image to image
def load_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None


# encoding the file
def read_file_with_encoding_detection(uploaded_file):
    encodings = ['utf-8', 'utf-16', 'latin-1']
    for encoding in encodings:
        try:
            return uploaded_file.read().decode(encoding)
        except UnicodeDecodeError:
            continue
    st.error(
        "Không thể đọc tệp này. Tệp có thể được mã hóa bằng định dạng không được hỗ trợ.")
    return None


def main():
    st.title("Text Summarization Web App")

    st.sidebar.header("Chọn chế độ đầu vào")
    input_type = st.sidebar.selectbox(
        "Chọn chế độ:", ("Upload file", "Nhập văn bản trực tiếp", "Xem tin tức"))

    # option upload file
    if input_type == "Upload file":
        uploaded_file = st.file_uploader(
            "Tải lên tệp văn bản", type=["txt", "pdf", "docx"])
        file_text = None

        if uploaded_file is not None:
            try:
                file_text = read_file_with_encoding_detection(uploaded_file)
                st.write("Văn bản từ tệp đã tải lên:")
                st.write(file_text)
            except UnicodeDecodeError:
                st.error("Không thể đọc tệp. Mã hóa không được hỗ trợ.")

        if file_text:
            if st.button("Tóm tắt"):
                summarized_text = summarize_text(file_text)
                st.write("Bản tóm tắt:")
                st.write(summarized_text)

    # option text
    elif input_type == "Nhập văn bản trực tiếp":
        user_input = st.text_area("Nhập văn bản cần tóm tắt", height=250)
        if st.button("Tóm tắt"):
            summarized_text = summarize_text(user_input)
            st.write("Bản tóm tắt:")
            st.write(summarized_text)

    # option news
    elif input_type == "Xem tin tức":
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
                    st.write("Hình ảnh không khả dụng")
                    st.subheader(article['title'])
                    st.write(f"Published at: {article['publishedAt']}")
                    st.markdown(f"[Read more]({article['url']})")
                    st.write("---")


if __name__ == "__main__":
    main()
