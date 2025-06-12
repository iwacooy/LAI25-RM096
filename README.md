
# 🛡️ Clainsure – Deteksi Penipuan Klaim Asuransi Menggunakan Machine Learning

Proyek ini bertujuan untuk membantu perusahaan asuransi dalam mendeteksi klaim asuransi kendaraan yang berpotensi penipuan (fraud) dengan memanfaatkan algoritma machine learning. Sistem ini dilatih menggunakan data historis dan diimplementasikan dalam aplikasi interaktif berbasis Streamlit.
---

## ⚙️ Teknologi yang Digunakan

- Python 3.x  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Streamlit  
- Imbalanced-learn (SMOTE)  
- Anaconda (environment management)

---

## 🔍 Proses dan Tahapan yang Dilakukan

Proyek ini dibangun melalui beberapa tahapan utama, yang mencakup:

### 📊 1. **Eksplorasi dan Manipulasi Data**
- Menggunakan **pandas** dan **numpy** untuk membaca dan memproses dataset klaim asuransi.
- Menganalisis distribusi data menggunakan `Counter` dan visualisasi data.

### 📈 2. **Visualisasi Data**
- Menggunakan **matplotlib** dan **seaborn** untuk membuat grafik distribusi, korelasi, dan heatmap untuk mendukung pemahaman terhadap pola data.


### ⚙️ 3. **Pra-Pemrosesan Data**
- Melakukan encoding data kategorikal menggunakan **LabelEncoder**.
- Membagi dataset menjadi data latih dan data uji dengan **train_test_split**.
- Mengatasi ketidakseimbangan kelas dengan teknik oversampling **SMOTE** dari imbalanced-learn.

### 🤖 4. **Pelatihan Model Machine Learning**
Mengimplementasikan berbagai model klasifikasi:
- Random Forest
- Logistic Regression
- Decision Tree
- Naive Bayes (GaussianNB dan MultinomialNB)
- K-Nearest Neighbors
- Support Vector Machine (SVM)
- AdaBoost, Bagging, Extra Trees, Gradient Boosting, dan XGBoost
- Voting Classifier untuk ensemble learning

### 🧪 5. **Evaluasi Model**
- Menggunakan metrik evaluasi seperti:
  - Accuracy
  - Precision
  - Recall
  - Confusion Matrix
  - Classification Report

### 💾 6. **Penyimpanan Model**
- Menyimpan model terbaik menggunakan **joblib** untuk digunakan pada aplikasi Streamlit.

---

## 📦 Setup Environment (Menggunakan Anaconda)

Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal:

### 1. Clone Repository
```bash
git clone https://github.com/iwacooy/LAI25-RM096.git
```

### 2. Masuk ke Folder Proyek
```bash
cd LAI25-RM096
```

### 3. Buat Environment Virtual dengan Anaconda
```bash
conda env create -f capstone.yml
```

### 4. Aktifkan Environment
```bash
conda activate capstone
```

### 5. Jalankan Aplikasi Streamlit
```bash
streamlit run app.py
```

---

## 📁 Struktur Folder
```
LAI25-RM096/
├── data.csv            # Dataset klaim asuransi
├── Capstone.ipynb      # Notebook eksplorasi dan training model
├── .joblib             # Model machine learning yang telah disimpan
├── app.py              # Aplikasi utama berbasis Streamlit
├── capstone.yml        # File environment untuk Anaconda
└── README.md           # Dokumentasi proyek
```

## 🎯 Tujuan Akhir

Dengan proyek ini, kami berharap:

- Perusahaan asuransi dapat mendeteksi klaim palsu secara lebih cepat dan efisien.  
- Mengurangi kerugian finansial akibat penipuan.  
- Meningkatkan akurasi keputusan tim investigasi asuransi.

---

## 📌 Catatan

- Proyek ini dikembangkan untuk keperluan edukatif (Capstone Project).  
- Dataset dan model dapat disesuaikan lebih lanjut untuk kebutuhan produksi riil.

---

## 🚀 Coba Aplikasinya

Untuk mencoba aplikasi deteksi penipuan klaim asuransi secara langsung, kunjungi:

🔗 [capstone-clainsure.streamlit.app](https://capstone-clainsure.streamlit.app/)



