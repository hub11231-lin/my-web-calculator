
import streamlit as st

st.set_page_config(page_title="我的網頁計算機")

st.title("我的 Python 網頁計算機")
st.write("請輸入兩個數字，選擇運算方式。")

a = st.number_input("第一個數字", value=10.0)
b = st.number_input("第二個數字", value=5.0)

op = st.selectbox(
    "運算方式",
    ["加法 (+)", "減法 (-)", "乘法 (*)", "除法 (/)"]
)

if st.button("開始計算"):
    if op == "加法 (+)":
        result = a + b
    elif op == "減法 (-)":
        result = a - b
    elif op == "乘法 (*)":
        result = a * b
    elif b == 0:
        st.error("除數不能為 0")
        st.stop()
    else:
        result = a / b

    st.success(f"計算結果：{result}")
