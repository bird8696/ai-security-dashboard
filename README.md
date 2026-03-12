# 🛡️ AI Security Threat Detection Dashboard

> KDD Cup 99 네트워크 데이터셋 기반의 보안 위협 탐지 대시보드  
> Random Forest + Claude API를 활용한 AI 자동 분석 리포트 생성

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![Claude API](https://img.shields.io/badge/Claude-API-blueviolet?style=flat-square)

---

## 📌 프로젝트 개요

네트워크 트래픽 데이터를 머신러닝 모델로 분석하여 **정상 트래픽과 공격 트래픽을 자동으로 탐지**하고,  
탐지 결과를 시각화 대시보드로 제공합니다.  
Claude API를 연동하여 탐지된 위협에 대한 **한국어 보안 분석 리포트를 자동 생성**합니다.

---

## 🖥️ 주요 기능

| 기능                   | 설명                                                   |
| ---------------------- | ------------------------------------------------------ |
| 📊 공격 유형 분포 차트 | 데이터셋 내 공격 유형별 건수 시각화                    |
| 🔍 탐지 결과 테이블    | 실제 vs 예측 결과 비교                                 |
| 📈 혼동 행렬           | 모델 성능 시각화 (Confusion Matrix)                    |
| 🤖 AI 리포트 생성      | Claude API 기반 한국어 위협 분석 및 권고사항 자동 생성 |

---

## 🏗️ 기술 스택

- **언어**: Python 3.11
- **ML**: Scikit-learn (Random Forest)
- **대시보드**: Streamlit
- **시각화**: Matplotlib, Seaborn
- **AI 연동**: Anthropic Claude API
- **데이터셋**: KDD Cup 99 (10% 샘플)

---

## ⚙️ 실행 방법

### 1. 레포지토리 클론

```bash
git clone https://github.com/bird8696/ai-security-dashboard.git
cd ai-security-dashboard
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv --without-pip
source venv/Scripts/activate  # Windows (Git Bash)
# source venv/bin/activate    # Mac/Linux

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정

프로젝트 루트에 `.env` 파일 생성 후 API 키 입력

```
ANTHROPIC_API_KEY=your_api_key_here
```

### 5. 실행

```bash
streamlit run app.py
```

---

## 📁 프로젝트 구조

```
ai-security-dashboard/
├── app.py              # 메인 Streamlit 앱
├── requirements.txt    # 패키지 목록
├── .env                # API 키 (Git 미포함)
├── .gitignore
└── README.md
```

---

## 📊 모델 성능

| 지표      | 점수 |
| --------- | ---- |
| Accuracy  | 100% |
| Precision | 1.00 |
| Recall    | 1.00 |
| F1-Score  | 1.00 |

> KDD Cup 99는 클린한 벤치마크 데이터셋으로 높은 성능이 나타납니다.  
> 실제 환경에서는 더 복잡한 전처리와 튜닝이 필요합니다.

---

## 🚀 향후 개선 계획

- [ ] 직접 트래픽 데이터 업로드 기능
- [ ] 공격 유형 다중 분류 (이진 → 멀티클래스)
- [ ] 탐지 결과 PDF 리포트 다운로드
- [ ] 실시간 탐지 시뮬레이션

---

## 👤 개발자

**bird8696** · [GitHub](https://github.com/bird8696)
