import streamlit as st
import pandas as pd
import joblib

# Judul
st.header("Fraud Detection pada Klaim Asuransi Kendaraan")

# Penginputan Informasi Demografi Policyholder
st.subheader("Input Informasi Demografi Policyholder")
# customer_age, segment
col1, col2 = st.columns(2)
with col1:
    customer_age = int(st.number_input(label="Customer Age", value=41))
with col2:
    segment = st.selectbox(
        label="Segment",
        options=["C2", "C1", "A", "B2", "B1", "Utility"],
        index=0,
    )
# region_code, region_density
col1, col2 = st.columns(2)
with col1:
    region_code = st.selectbox(
        label="Region Code",
        options=[
            "C8",
            "C2",
            "C10",
            "C13",
            "C7",
            "C5",
            "C3",
            "C19",
            "C9",
            "C15",
            "C6",
            "C11",
            "C1",
            "C14",
            "C17",
            "C12",
            "C4",
            "C21",
            "C16",
            "C18",
            "C22",
            "C20",
        ],
        index=0,
    )
with col2:
    region_density = int(st.number_input(label="Region Density", value=8794))

# Penginputan Informasi Insurance Policy
st.subheader("Input Informasi Insurance Policy")
# subscription_length, ncap_rating, is_ecw
col1, col2, col3 = st.columns(3)
with col1:
    subscription_length = float(st.number_input(label="Subscription Length", value=9.3))
with col2:
    ncap_rating = int(st.number_input(label="NCAP Rating", value=3))
with col3:
    is_ecw = st.selectbox(
        label="Is Engineered Collision Warranty (ECW)?",
        options=["Yes", "No"],
        index=0,
    )

# Penginputan Informasi Umum Kendaraan
st.subheader("Input Informasi Umum Kendaraan")
# model, is_driver_seat_height_adjustable
col1, col2 = st.columns(2)
with col1:
    model = st.selectbox(
        label="Model",
        options=["M4", "M9", "M1", "M5", "M7", "M6", "M8", "M3", "M2", "M10", "M11"],
        index=0,
    )
with col2:
    is_driver_seat_height_adjustable = st.selectbox(
        label="Is Driver Seat Height Adjustable?",
        options=["Yes", "No"],
        index=0,
    )
# transmission_type, steering_type, turning_radius
col1, col2, col3 = st.columns(3)
with col1:
    transmission_type = st.selectbox(
        label="Transmission Type",
        options=["Automatic", "Manual"],
        index=0,
    )
with col2:
    steering_type = st.selectbox(
        label="Steering Type",
        options=["Power", "Electric", "Manual"],
        index=0,
    )
with col3:
    turning_radius = float(st.number_input(label="Turning Radius", value=5.2))
# length, width, gross_weight
col1, col2, col3 = st.columns(3)
with col1:
    length = int(st.number_input(label="Length", value=4300))
with col2:
    width = int(st.number_input(label="Width", value=1790))
with col3:
    gross_weight = int(st.number_input(label="Gross Weight", value=1720))

# Penginputan Informasi Mesin Kendaraan
st.subheader("Input Informasi Mesin Kendaraan")
# engine_type, fuel_type
col1, col2 = st.columns(2)
with col1:
    engine_type = st.selectbox(
        label="Engine Type",
        options=[
            "1.5 L U2 CRDi",
            "i-DTEC",
            "F8D Petrol Engine",
            "1.5 Turbocharged Revotorq",
            "1.2 L K Series Engine",
            "K Series Dual jet",
            "K10C",
            "1.0 SCe",
            "1.2 L K12N Dualjet",
            "G12B",
            "1.5 Turbocharged Revotron",
        ],
        index=0,
    )
with col2:
    fuel_type = st.selectbox(
        label="Fuel Type",
        options=["Diesel", "CNG", "Petrol"],
        index=0,
    )
# vehicle_age, displacement, cylinder
col1, col2, col3 = st.columns(3)
with col1:
    vehicle_age = float(st.number_input(label="Vehicle Age", value=1.2))
with col2:
    displacement = int(st.number_input(label="Displacement", value=1493))
with col3:
    cylinder = int(st.number_input(label="Cylinder", value=4))
# max_torque, max_power
col1, col2 = st.columns(2)
with col1:
    max_torque = st.selectbox(
        label="Max Torque",
        options=[
            "250Nm@2750rpm",
            "200Nm@1750rpm",
            "60Nm@3500rpm",
            "200Nm@3000rpm",
            "113Nm@4400rpm",
            "82.1Nm@3400rpm",
            "91Nm@4250rpm",
            "85Nm@3000rpm",
            "170Nm@4000rpm",
        ],
        index=0,
    )
with col2:
    max_power = st.selectbox(
        label="Max Power",
        options=[
            "113.45bhp@4000rpm",
            "97.89bhp@3600rpm",
            "40.36bhp@6000rpm",
            "88.77bhp@4000rpm",
            "88.50bhp@6000rpm",
            "55.92bhp@5300rpm",
            "67.06bhp@5500rpm",
            "61.68bhp@6000rpm",
            "118.36bhp@5500rpm",
        ],
        index=0,
    )

# Penginputan Informasi Keselamatan dan Keamanan Kendaraan
st.subheader("Input Informasi Keselamatan dan Keamanan Kendaraan")
# is_esc, is_adjustable_steering, is_power_steering
col1, col2, col3 = st.columns(3)
with col1:
    is_esc = st.selectbox(
        label="Is Electronic Stability Control (ESC)?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_adjustable_steering = st.selectbox(
        label="Is Adjustable Steering?",
        options=["Yes", "No"],
        index=0,
    )
with col3:
    is_power_steering = st.selectbox(
        label="Is Power Steering?",
        options=["Yes", "No"],
        index=0,
    )
# is_tpms, is_speed_alert
col1, col2 = st.columns(2)
with col1:
    is_tpms = st.selectbox(
        label="Is Tire Pressure Monitoring System (TPMS)?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_speed_alert = st.selectbox(
        label="Is Speed Alert?",
        options=["Yes", "No"],
        index=0,
    )
# is_parking_sensors, is_parking_camera
col1, col2 = st.columns(2)
with col1:
    is_parking_sensors = st.selectbox(
        label="Is Parking Sensors?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_parking_camera = st.selectbox(
        label="Is Parking Camera?",
        options=["Yes", "No"],
        index=0,
    )
# is_central_locking, is_power_door_locks, airbags
col1, col2, col3 = st.columns(3)
with col1:
    is_central_locking = st.selectbox(
        label="Is Central Locking?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_power_door_locks = st.selectbox(
        label="Is Power Door Locks?",
        options=["Yes", "No"],
        index=0,
    )
with col3:
    airbags = int(st.number_input(label="Airbags", value=6))
# rear_brakes_type, is_brake_assist
col1, col2 = st.columns(2)
with col1:
    rear_brakes_type = st.selectbox(
        label="Rear Brakes Type",
        options=["Disc", "Drum"],
        index=0,
    )
with col2:
    is_brake_assist = st.selectbox(
        label="Is Brake Assist?",
        options=["Yes", "No"],
        index=0,
    )
# is_front_fog_lights, is_day_night_rear_view_mirror
col1, col2 = st.columns(2)
with col1:
    is_front_fog_lights = st.selectbox(
        label="Is Front Fog Lights?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_day_night_rear_view_mirror = st.selectbox(
        label="Is Day Night Rear View Mirror?",
        options=["Yes", "No"],
        index=1,
    )
# is_rear_window_wiper, is_rear_window_washer, is_rear_window_defogger
col1, col2, col3 = st.columns(3)
with col1:
    is_rear_window_wiper = st.selectbox(
        label="Is Rear Window Wiper?",
        options=["Yes", "No"],
        index=0,
    )
with col2:
    is_rear_window_washer = st.selectbox(
        label="Is Rear Window Washer?",
        options=["Yes", "No"],
        index=0,
    )
with col3:
    is_rear_window_defogger = st.selectbox(
        label="Is Rear Window Defogger?",
        options=["Yes", "No"],
        index=0,
    )


# Penginputan DataFrame
df = pd.DataFrame(
    {
        "subscription_length": [subscription_length],
        "vehicle_age": [vehicle_age],
        "customer_age": [customer_age],
        "region_code": [region_code],
        "region_density": [region_density],
        "segment": [segment],
        "model": [model],
        "fuel_type": [fuel_type],
        "max_torque": [max_torque],
        "max_power": [max_power],
        "engine_type": [engine_type],
        "airbags": [airbags],
        "is_esc": [is_esc],
        "is_adjustable_steering": [is_adjustable_steering],
        "is_tpms": [is_tpms],
        "is_parking_sensors": [is_parking_sensors],
        "is_parking_camera": [is_parking_camera],
        "rear_brakes_type": [rear_brakes_type],
        "displacement": [displacement],
        "cylinder": [cylinder],
        "transmission_type": [transmission_type],
        "steering_type": [steering_type],
        "turning_radius": [turning_radius],
        "length": [length],
        "width": [width],
        "gross_weight": [gross_weight],
        "is_front_fog_lights": [is_front_fog_lights],
        "is_rear_window_wiper": [is_rear_window_wiper],
        "is_rear_window_washer": [is_rear_window_washer],
        "is_rear_window_defogger": [is_rear_window_defogger],
        "is_brake_assist": [is_brake_assist],
        "is_power_door_locks": [is_power_door_locks],
        "is_central_locking": [is_central_locking],
        "is_power_steering": [is_power_steering],
        "is_driver_seat_height_adjustable": [is_driver_seat_height_adjustable],
        "is_day_night_rear_view_mirror": [is_day_night_rear_view_mirror],
        "is_ecw": [is_ecw],
        "is_speed_alert": [is_speed_alert],
        "ncap_rating": [ncap_rating],
    }
)

# Tampil hasil hasil penginputan
with st.expander("Lihat hasil penginputan data"):
    st.dataframe(data=df, width=800, height=10)

# Load preprocessor dan model
preprocessor = joblib.load("preprocessor.joblib")
model = joblib.load("model.joblib")

# Melakukan prediksi
if st.button("Predict"):
    new_df = preprocessor.transform(df)  # melakukan preprocessing
    predict = model.predict(new_df)  # melakukan prediction
    # Hasil prediction
    if predict[0] == 0:
        st.subheader("Hasil Prediksi Asuransi Kendaraan: Tidak Klaim")
    else:
        st.subheader("Hasil Prediksi Asuransi Kendaraan: Klaim")
