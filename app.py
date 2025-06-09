import pandas as pd
import streamlit as st
import joblib

# Load model dan dict label_encoders
model = joblib.load("model.joblib")
label_encoders = joblib.load("preprocessor.joblib")  # dict: {'region_code': le1, 'model': le2, ...}

def run_app():
    st.title('🚗 Vehicle Insurance Fraud Predictor')

    # Form input
    with st.form("insurance_form"):
        st.subheader("Input Informasi Penting Kendaraan & Policyholder")

        col1, col2 = st.columns(2)
        with col1:
            subscription_length = float(st.number_input("Subscription Length", value=9.3))
            customer_age = int(st.number_input("Customer Age", value=41))
            vehicle_age = float(st.number_input("Vehicle Age", value=1.2))
            region_density = int(st.number_input("Region Density", value=8794))
            region_code = st.selectbox("Region Code", options=label_encoders['region_code'].classes_.tolist())

        with col2:
            length = int(st.number_input("Vehicle Length", value=4300))
            width = int(st.number_input("Vehicle Width", value=1790))
            gross_weight = int(st.number_input("Gross Weight", value=1720))
            model_val = st.selectbox("Model", options=label_encoders['model'].classes_.tolist())
            max_power = st.selectbox("Max Power", options=label_encoders['max_power'].classes_.tolist())

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Buat DataFrame mentah
        input_df = pd.DataFrame([{
            "subscription_length": subscription_length,
            "customer_age": customer_age,
            "vehicle_age": vehicle_age,
            "region_density": region_density,
            "region_code": region_code,
            "length": length,
            "model": model_val,
            "width": width,
            "gross_weight": gross_weight,
            "max_power": max_power
        }])

        # Encode kolom kategorikal
        for col in ['region_code', 'model', 'max_power']:
            le = label_encoders[col]
            if input_df[col][0] not in le.classes_:
                st.error(f"Nilai '{input_df[col][0]}' tidak valid untuk kolom '{col}'")
                return
            input_df[col] = le.transform([input_df[col][0]])

        with st.expander("Lihat Data Input"):
            st.dataframe(input_df)

        # Prediksi
        prediction = model.predict(input_df)

        # Output
        if prediction[0] == 1:
            st.success("🚨 Prediksi: Terdapat potensi **klaim asuransi**.")
        else:
            st.success("✅ Prediksi: Tidak ada indikasi klaim asuransi.")

if __name__ == '__main__':
    run_app()
