
import streamlit as st
from utils import analyze_report

st.set_page_config(page_title="전세가드", layout="wide")

st.title("🏠 전세가드 리포트 v0.1")

uploaded_file = st.file_uploader("등기부 등본 이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    result = analyze_report(uploaded_file)
    st.write("### 📄 리포트 요약", result)
