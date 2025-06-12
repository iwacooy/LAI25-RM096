
# 🛡️ Clainsure – Deteksi Penipuan Klaim Asuransi Menggunakan Machine Learning

Proyek ini bertujuan untuk membantu perusahaan asuransi dalam mendeteksi klaim asuransi kendaraan yang berpotensi penipuan (fraud) dengan memanfaatkan algoritma machine learning. Sistem ini dilatih menggunakan data historis dan diimplementasikan dalam aplikasi interaktif berbasis Streamlit.

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

---

## 🧠 Model yang Digunakan
Beberapa model klasifikasi yang digunakan dalam proyek ini:

- Random Forest  
- Logistic Regression  
- Decision Tree  
- Naive Bayes  
- Support Vector Machine (SVM)  
- K-Nearest Neighbor (KNN)  
- AdaBoost  
- Gradient Boosting  

Model terbaik dipilih berdasarkan hasil evaluasi menggunakan metrik:
- Recall
- Confusion Matrix

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

