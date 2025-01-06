# 文件顶部定义所需列名
required_columns = ['T Stage', 'N Stage', 'M Stage', 'Tumor Size', 'Grade']

def main():
    st.title("Breast Cancer Survival Prediction")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # 读取 CSV 文件
        try:
            df = pd.read_csv(uploaded_file)
            
            # 检查缺失列
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                st.error(f"Missing required columns: {', '.join(missing_columns)}")
            else:
                st.success("File successfully uploaded and all required columns are present.")
                st.write("Preview of your data:")
                st.dataframe(df.head())  # 显示文件前几行
            
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.sidebar.subheader("Sample File Format")
        st.sidebar.write("Your CSV file should contain the following columns:")
        for col in required_columns:
            st.sidebar.write(f"- {col}")

if __name__ == "__main__":
    main()
