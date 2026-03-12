from sklearn.datasets import fetch_kddcup99
import pandas as pd

# 데이터 자동 다운로드 (10% 샘플)
print("데이터 다운로드 중...")
data = fetch_kddcup99(subset='10percent', as_frame=True)

df = data.frame
print("shape:", df.shape)
print(df.head())
print(df['labels'].value_counts())