import requests
import numpy as np
import streamlit as st
from PIL import Image

def search_menu_images(menu, client_id, client_secret, num_images=5):
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = {
        'query': menu,
        'display': num_images
    }
    api_url = 'https://openapi.naver.com/v1/search/image'
    response = requests.get(api_url, headers=headers, params=params).json()

    image_urls = []
    if 'items' in response:
        items = response['items']
        for item in items[:num_images]:
            image_url = item['link']
            image_urls.append(image_url)

    return image_urls

def lunch_menu_recommendation(menu_list):
    random_index = np.random.randint(0, len(menu_list))
    return menu_list[random_index]

def main():
    st.title("점심 메뉴 추천기")

    menu_list = st.text_area("점심 메뉴를 입력하세요 (한 줄에 하나의 메뉴):")
    menu_list = menu_list.split('\n')

    client_id = st.text_input("네이버 API Client ID:")
    client_secret = st.text_input("네이버 API Client Secret:")

    if st.button("추천받기"):
        if len(menu_list) > 1:
            recommended_menu = lunch_menu_recommendation(menu_list)

            st.success("추천 메뉴")
            st.write("---")

            # 메뉴 리스트 시각화 및 이미지 검색
            st.subheader("점심 메뉴 리스트")
            for menu in menu_list:
                st.write(menu)
                # 메뉴 이미지 검색 및 표시
                image_urls = search_menu_images(menu, client_id, client_secret, num_images=5)
                if image_urls:
                    image_columns = st.beta_columns(len(image_urls))
                    for i, image_url in enumerate(image_urls):
                        image = Image.open(requests.get(image_url, stream=True).raw)
                        with image_columns[i]:
                            st.image(image, caption=menu, width=300)

            st.write("---")

            # 추천된 메뉴 카드 표시
            st.subheader("추천된 메뉴")
            st.info(recommended_menu)
        else:
            st.error("메뉴를 두 개 이상 입력해주세요.")

if __name__ == "__main__":
    main()
