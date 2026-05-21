# Bank Marketing Campaign — Term Deposit Subscription Prediction

An AutoML project using PyCaret to predict whether a bank client will subscribe to a term deposit, based on marketing campaign call data.

---

## English

### About

This project applies automated machine learning (AutoML) via **PyCaret** to the Bank Marketing dataset. The goal is to classify whether a client will subscribe to a bank term deposit (`yes`/`no`) after a marketing campaign phone call. PyCaret automatically compares multiple classification algorithms and selects the best-performing model.

### Features

- Full AutoML pipeline with PyCaret 3.0.0
- Automated model comparison and selection
- Streamlit web app for interactive predictions
- Pre-trained best model included (`best_automl_model.pkl`)

### Dataset

**File:** `bank-additional-full.csv` (5.56 MB)

| Feature | Description |
|---|---|
| age | Client age |
| job | Type of job |
| marital | Marital status |
| education | Education level |
| contact | Contact communication type |
| duration | Last call duration (seconds) |
| campaign | Number of contacts during this campaign |
| pdays | Days since last contact |
| previous | Number of previous contacts |
| poutcome | Outcome of previous campaign |
| **y (target)** | Subscribed to term deposit? (yes/no) |

**Source:** [UCI ML Repository — Bank Marketing](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

### Model Architecture / Tech Stack

PyCaret automatically trains and evaluates multiple classifiers (Logistic Regression, Random Forest, XGBoost, LightGBM, etc.) and selects the best model based on cross-validation performance.

**Tech Stack:** Python · PyCaret 3.0.0 · Streamlit 1.35.0 · scikit-learn · pandas · NumPy · Matplotlib · Seaborn

### Results / Performance

The best AutoML model is saved as `best_automl_model.pkl`. Detailed metrics (Accuracy, AUC, Recall, Precision, F1) for all compared models are available in the notebook.

### How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> **Note:** Run the notebook first to regenerate `best_automl_model.pkl` if the file is missing.

### Requirements

```
pycaret==3.0.0
streamlit==1.35.0
scikit-learn
pandas
numpy
matplotlib
seaborn
```

---

## Türkçe

### Hakkında

Bu proje, Banka Pazarlama veri kümesine PyCaret aracılığıyla otomatik makine öğrenmesi (AutoML) uygular. Amaç, bir pazarlama kampanyası telefon görüşmesinin ardından müşterinin vadeli mevduata abone olup olmayacağını (`yes`/`no`) sınıflandırmaktır. PyCaret, birden fazla sınıflandırma algoritmasını otomatik olarak karşılaştırır ve en iyi performanslı modeli seçer.

### Özellikler

- PyCaret 3.0.0 ile tam AutoML işlem hattı
- Otomatik model karşılaştırma ve seçim
- Etkileşimli tahminler için Streamlit web uygulaması
- Önceden eğitilmiş en iyi model dahil (`best_automl_model.pkl`)

### Veri Seti

**Dosya:** `bank-additional-full.csv` (5,56 MB)

| Özellik | Açıklama |
|---|---|
| age | Müşteri yaşı |
| job | İş türü |
| marital | Medeni durum |
| education | Eğitim seviyesi |
| contact | İletişim türü |
| duration | Son arama süresi (saniye) |
| campaign | Bu kampanyada yapılan temas sayısı |
| pdays | Son temasın üzerinden geçen gün |
| previous | Önceki temas sayısı |
| poutcome | Önceki kampanyanın sonucu |
| **y (hedef)** | Vadeli mevduata abone oldu mu? (yes/no) |

**Kaynak:** [UCI ML Deposu — Banka Pazarlaması](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

### Model Mimarisi / Teknoloji Yığını

PyCaret, birden fazla sınıflandırıcıyı (Lojistik Regresyon, Random Forest, XGBoost, LightGBM vb.) otomatik olarak eğitir ve çapraz doğrulama performansına göre en iyi modeli seçer.

**Teknoloji Yığını:** Python · PyCaret 3.0.0 · Streamlit 1.35.0 · scikit-learn · pandas · NumPy · Matplotlib · Seaborn

### Sonuçlar / Performans

En iyi AutoML modeli `best_automl_model.pkl` olarak kaydedilir. Karşılaştırılan tüm modeller için detaylı metrikler (Accuracy, AUC, Recall, Precision, F1) notebook'ta mevcuttur.

### Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
streamlit run app.py
```

> **Not:** Dosya eksikse `best_automl_model.pkl`'yi yeniden oluşturmak için önce notebook'u çalıştırın.

### Gereksinimler

```
pycaret==3.0.0
streamlit==1.35.0
scikit-learn
pandas
numpy
matplotlib
seaborn
```
