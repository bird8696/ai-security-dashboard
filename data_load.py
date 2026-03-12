from sklearn.datasets import fetch_kddcup99
import pandas as pd

print("데이터 다운로드 중...")
data = fetch_kddcup99(percent10=True, as_frame=True)

df = data.frame
print("shape:", df.shape)
print(df.head())
print(df['labels'].value_counts())
