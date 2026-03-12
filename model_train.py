from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

print("데이터 로딩 중...")
data = fetch_kddcup99(percent10=True, as_frame=True)
df = data.frame

# 라벨 정리 - 정상(0) vs 공격(1) 이진분류
df['labels'] = df['labels'].str.decode('utf-8')
df['is_attack'] = df['labels'].apply(lambda x: 0 if x == 'normal.' else 1)

# 범주형 컬럼 인코딩
df['protocol_type'] = df['protocol_type'].str.decode('utf-8')
df['service'] = df['service'].str.decode('utf-8')
df['flag'] = df['flag'].str.decode('utf-8')
df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])

# 피처 / 라벨 분리
X = df.drop(['labels', 'is_attack'], axis=1)
y = df['is_attack']

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("모델 학습 중...")
model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

print("평가 결과:")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['정상', '공격']))
