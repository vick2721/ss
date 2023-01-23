import streamlit as st
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt

start_date = st.date_input("選擇開始日期:", date.today() + timedelta(days=1))
end_date = st.date_input("選擇結束日期:", date.today() + timedelta(days=30))

# 創建模型選擇小部件
model_select = st.selectbox("選擇模型:", ["線性回歸", "決策樹", "隨機森林"])

# 訓練所選模型
if model_select == "線性回歸":
    reg = LinearRegression().fit(X_train, y_train)
elif model_select == "決策樹":streamlit hello
    reg = DecisionTreeRegressor().fit(X_train, y_train)
else:
    reg = RandomForestRegressor().fit(X_train, y_train)

# 使用所選模型對所選日期範圍進行預測
predicted_sales = reg.predict([[start_date.strftime("%Y-%m-%d")], [end_date.strftime("%Y-%m-%d")]])

# 顯示預測銷售額
st.write("所選日期範圍預測銷售額:", predicted_sales)

# 顯示評估指標
st.write("評估指標:")
st.write("R-squared:", reg.score(X_test, y_test))

# 允許用戶上傳自己的數據
uploaded_file = st.file_uploader("上傳您
uploaded_file = st.file_uploader("上傳您的數據:", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    # 使用所選模型對上傳的數據進行預測
    predicted_sales = reg.predict(data)
    st.write("上傳數據預測銷售額:",predicted_sales)

# 顯示實際銷售額和預測銷售額之間的比較
st.line_chart(pd.DataFrame({'實際銷售額': y_test, '預測銷售額': reg.predict(X_test)}))
                                 
                                 
