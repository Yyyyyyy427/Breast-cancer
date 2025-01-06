from joblib import load

# 加载模型
xgb_model = load('breast_cancer_xgb_model.joblib')
print("Model loaded successfully!")

# 测试模型
# 确保测试数据 (X_test) 格式正确
sample_data = X_test.iloc[:5]  # 选择测试集的前5行作为样本
predictions = xgb_model.predict(sample_data)

print("Predictions for sample data:")
print(predictions)
