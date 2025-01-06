import streamlit as st
import pandas as pd
from joblib import load

# 加载模型
model = load('breast_cancer_rf_model.joblib')

# 必需的列名
required_columns = ['t stage', 'n stage', 'm stage', 'tumor size', 'grade']

def main():
    st.title("Breast Cancer Survival Prediction")
    
    # 文件上传
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # 读取文件
            df = pd.read_csv(uploaded_file)
            
            # 标准化列名
            df.columns = df.columns.str.strip().str.lower()
            
            # 检查缺失列
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                st.error(f"Missing required columns: {', '.join(missing_columns)}")
            else:
                st.success("File successfully uploaded and all required columns are present.")
                st.write("Preview of your data:")
                st.dataframe(df.head())
                
                # 预测
                X = df[required_columns]
                predictions = model.predict(X)
                df['Prediction'] = predictions.map({0: 'Alive', 1: 'Dead'})
                
                # 显示结果
                st.write("Prediction Results:")
                st.dataframe(df[['Prediction']])
        except Exception as e:
            st.error(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()
