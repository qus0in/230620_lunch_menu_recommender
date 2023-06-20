import numpy as np
import streamlit as st

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
            st.success(f"추천 메뉴: {recommended_menu}")
        else:
            st.error("메뉴를 두 개 이상 입력해주세요.")

if __name__ == "__main__":
    main()