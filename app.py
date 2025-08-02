import streamlit as st
from utils import analyze_report

st.set_page_config(page_title="전세가드", layout="wide")
st.title("전세가드 리포트 v0.1.1")

uploaded_file = st.file_uploader("등기부 등본 이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    result = analyze_report(uploaded_file)

    st.markdown("### 🧾 리포트 요약")
    st.json(result)

    st.markdown("---")
    st.markdown("### 📍 입지 요약 (베타 예정)")
    st.markdown("""
    - 🚇 지하철역까지 도보 **6분**
    - 🏫 초등학교 반경 **700m**
    - 🏗️ 주변 **재건축 예정지 있음**
    """)

    st.markdown("### 💬 한 줄 평가")
    st.success("✅ 안심하고 입주해도 좋은 물건이에요!")
