import pandas as pd
import streamlit as st
import joblib

# Load model dan dict label_encoders
model = joblib.load("model.joblib")
label_encoders = joblib.load("preprocessor.joblib") 
feature_order = joblib.load("feature_columns.joblib")  # urutan kolom saat training

def run_app():
    st.title('🚗 Vehicle Insurance Fraud Predictor')

    # Form input
    with st.form("insurance_form"):
        st.subheader("Input Informasi Penting Kendaraan & Policyholder")

        col1, col2 = st.columns(2)
        with col1:
            subscription_length = st.slider("Subscription Length", min_value=0.0, max_value=14.0, value=9.3)
            customer_age = st.slider("Customer Age", min_value=35, max_value=75, value=41)
            vehicle_age = st.slider("Vehicle Age", min_value=0.0, max_value=20.0, value=1.2)
            region_density = st.slider("Region Density", min_value=290, max_value=73430, value=8794)
            region_code = st.selectbox("Region Code", options=label_encoders['region_code'].classes_.tolist())

        with col2:
            length = st.slider("Vehicle Length", min_value=3445, max_value=4300, value=4300)
            displacement = st.slider("Displacement", min_value=796, max_value=1498, value=1497)
            gross_weight = st.slider("Gross Weight", min_value=1051, max_value=1720, value=1720)
            model_val = st.selectbox("Model", options=label_encoders['model'].classes_.tolist())
            max_power = st.slider("Max Power (bhp)", min_value=40.36, max_value=118.36, value=113.45)

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Buat DataFrame mentah
        input_df = pd.DataFrame([{
            "subscription_length": subscription_length,
            "customer_age": customer_age,
            "vehicle_age": vehicle_age,
            "region_density": region_density,
            "region_code": region_code,
            "model": model_val,
            "length": length,
            "gross_weight": gross_weight,
            "displacement": displacement,
            "max_power": max_power
        }])

        # Encode kolom kategorikal
        for col in ['region_code', 'model']:
            le = label_encoders[col]
            if input_df[col][0] not in le.classes_:
                st.error(f"Nilai '{input_df[col][0]}' tidak valid untuk kolom '{col}'")
                return
            input_df[col] = le.transform([input_df[col][0]])

        # Pastikan urutan kolom sesuai dengan saat training
        input_df = input_df.reindex(columns=feature_order)

        with st.expander("Lihat Data Input"):
            st.dataframe(input_df)

        # Prediksi
        prediction = model.predict(input_df)

        # Output
        if prediction[0] == 1:
            st.markdown(
            """
            <div style="padding: 1rem; border-radius: 10px; background-color: #ffe6e6; color: #a94442; border: 1px solid #f5c6cb;">
                <h3 style="margin-top: 0;">🚨 Klaim Asuransi Terdeteksi!</h3>
                <p><strong>Status:</strong> Sistem memprediksi adanya potensi <b>klaim asuransi</b>. Harap dilakukan verifikasi lebih lanjut.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(
            """
            <div style="padding: 1rem; border-radius: 10px; background-color: #e6ffed; color: #155724; border: 1px solid #c3e6cb;">
                <h3 style="margin-top: 0;">✅ Aman Tanpa Klaim</h3>
                <p><strong>Status:</strong> Tidak ada indikasi klaim asuransi dari data yang dimasukkan.</p>
            </div>
            """, unsafe_allow_html=True)


if __name__ == '__main__':
    run_app()
