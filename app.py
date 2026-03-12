import anthropic
import os
from dotenv import load_dotenv
from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

load_dotenv()

st.title("🛡️ 보안 위협 탐지 대시보드")

@st.cache_data
def load_and_train():
    data = fetch_kddcup99(percent10=True, as_frame=True)
    df = data.frame
    df['labels'] = df['labels'].str.decode('utf-8')
    df['is_attack'] = df['labels'].apply(lambda x: 0 if x == 'normal.' else 1)
    df['protocol_type'] = df['protocol_type'].str.decode('utf-8')
    df['service'] = df['service'].str.decode('utf-8')
    df['flag'] = df['flag'].str.decode('utf-8')
    df_encoded = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])
    X = df_encoded.drop(['labels', 'is_attack'], axis=1)
    y = df_encoded['is_attack']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    return df, model, X_test, y_test

with st.spinner("모델 학습 중..."):
    df, model, X_test, y_test = load_and_train()

st.success("모델 준비 완료!")

st.subheader("공격 유형 분포")
attack_counts = df['labels'].value_counts().reset_index()
attack_counts.columns = ['공격 유형', '건수']
st.bar_chart(attack_counts.set_index('공격 유형'))

st.subheader("탐지 결과 샘플")
y_pred = model.predict(X_test)
result_df = pd.DataFrame({
    '실제': ['정상' if v == 0 else '공격' for v in y_test[:50]],
    '예측': ['정상' if v == 0 else '공격' for v in y_pred[:50]]
})
st.dataframe(result_df)

st.subheader("혼동 행렬")
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', ax=ax,
            xticklabels=['정상', '공격'],
            yticklabels=['정상', '공격'])
ax.set_xlabel('예측')
ax.set_ylabel('실제')
st.pyplot(fig)

st.subheader("AI 위협 분석")

top_attacks = df[df['labels'] != 'normal.']['labels'].value_counts().head(3).index.tolist()

if st.button("AI 리포트 생성"):
    with st.spinner("분석 중..."):
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        prompt = f"""
        네트워크 침입 탐지 분석 결과:
        - 전체 샘플 수: {len(df)}
        - 정상 트래픽: {len(df[df['labels'] == 'normal.'])}
        - 공격 트래픽: {len(df[df['labels'] != 'normal.'])}
        - 상위 3개 공격 유형: {', '.join(top_attacks)}

        반드시 한국어로 3~4문장으로 보안 위협 요약과 권고사항을 작성해줘.
        """

        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(message.content[0].text)