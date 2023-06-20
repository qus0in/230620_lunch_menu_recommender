# import numpy as np
# import streamlit as st

# def lunch_menu_recommendation(menu_list):
#     random_index = np.random.randint(0, len(menu_list))
#     return menu_list[random_index]

# def main():
#     st.title("점심 메뉴 추천기")
    
#     menu_list = st.text_area("점심 메뉴를 입력하세요 (한 줄에 하나의 메뉴):")
#     menu_list = menu_list.split('\n')
    
#     if st.button("추천받기"):
#         if len(menu_list) > 1:
#             recommended_menu = lunch_menu_recommendation(menu_list)
#             st.success(f"추천 메뉴: {recommended_menu}")
#         else:
#             st.error("메뉴를 두 개 이상 입력해주세요.")

# if __name__ == "__main__":
#     main()

# import numpy as np
# import streamlit as st

# def lunch_menu_recommendation(menu_list):
#     random_index = np.random.randint(0, len(menu_list))
#     return menu_list[random_index]

# def main():
#     st.title("점심 메뉴 추천기")
    
#     menu_list = st.text_area("점심 메뉴를 입력하세요 (한 줄에 하나의 메뉴):")
#     menu_list = menu_list.split('\n')
    
#     if st.button("추천받기"):
#         if len(menu_list) > 1:
#             recommended_menu = lunch_menu_recommendation(menu_list)
            
#             st.success("추천 메뉴")
#             st.write("---")
            
#             # 메뉴 리스트 시각화
#             st.subheader("점심 메뉴 리스트")
#             for menu in menu_list:
#                 st.write(menu)
                
#             st.write("---")
            
#             # 추천된 메뉴 카드 표시
#             st.subheader("추천된 메뉴")
#             st.info(recommended_menu)
#         else:
#             st.error("메뉴를 두 개 이상 입력해주세요.")

# if __name__ == "__main__":
#     main()

import requests
import numpy as np
import streamlit as st
from PIL import Image

def search_menu_image(menu):
    # 이미지 검색을 위한 코드
    # 이미지 URL이나 경로를 얻는 작업을 수행해야 함
    # 여기에서는 간단히 랜덤 이미지를 가져옴
    image_url = "https://via.placeholder.com/300"
    return image_url

def lunch_menu_recommendation(menu_list):
    random_index = np.random.randint(0, len(menu_list))
    return menu_list[random_index]

def main():
    st.title("점심 메뉴 추천기")
    
    menu_list = st.text_area("점심 메뉴를 입력하세요 (한 줄에 하나의 메뉴):")
    menu_list = menu_list.split('\n')
    
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
                image_url = search_menu_image(menu)
                image = Image.open(requests.get(image_url, stream=True).raw)
                st.image(image, caption=menu, width=300)
                
            st.write("---")
            
            # 추천된 메뉴 카드 표시
            st.subheader("추천된 메뉴")
            st.info(recommended_menu)
        else:
            st.error("메뉴를 두 개 이상 입력해주세요.")

if __name__ == "__main__":
    main()
