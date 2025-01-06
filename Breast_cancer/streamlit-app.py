import streamlit as st
import pandas as pd

# 标准化列名
required_columns = ['t stage', 'n stage', 'm stage', 'tumor size', 'grade']

def main():
    st.title("Breast Cancer Survival Prediction")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
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
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.sidebar.subheader("Sample File Format")
        st.sidebar.write("Your CSV file should contain the following columns:")
        for col in required_columns:
            st.sidebar.write(f"- {col}")

if __name__ == "__main__":
    main()

