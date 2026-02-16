import streamlit as st
from src.componets.predict_pipeline import UserData, PredictPipeline


st.title("Insurance Cost Prediction")

st.write("Enter your details below to estimate your medical insurance charges.")

name = st.text_input("Name")

age = st.number_input("Age", min_value=20, max_value=120)

sex = st.selectbox("Sex", ["male", "female"])

bmi = st.number_input("BMI", format="%.2f")

children = st.number_input("Children", min_value=0)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox(
    "Region",
    ["southwest", "northwest", "southeast", "northeast"]
)


if st.button("Predict Charges"):

    user_data = UserData(
        age=age,
        sex=sex,
        bmi=bmi,
        children=children,
        smoker=smoker,
        region=region
    )

    dataframe = user_data.create_data_frame()
    pred_obj = PredictPipeline()
    prediction = pred_obj.predict_data(dataframe)

    result = round(prediction[0], 2)

    st.success(f"Hello {name} !")
    st.success(f"Estimated Insurance Charges: {result:,.2f}")
