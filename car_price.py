import streamlit as st
import pandas as pd 
import joblib
import statsmodels
st.title("Car Price Prediction")
st.subheader("Predict the price of a car based on its features!")

# load the csv
df=pd.read_csv("cars24-car-price.csv")
# display the dataset
st.dataframe(df.head())
#import joblib 
model=joblib.load("cars24_linear_regression_model.joblib")

# model.predict(test_input)



st.write("Enter the details of the car to predict its price.")

col1, col2 = st.columns(2)
with col1:

    year = st.number_input("Enter car year", min_value=1990, max_value=2026, value=2015)

    fuel_type = st.selectbox("Select the fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
    engine = st.slider("Set the Engine Power",
                       500, 5000, step=100)

    seller_type = st.selectbox("Select seller type", ["Dealer", "Individual", "Trustmark Dealer"])
with col2:
    transmission_type = st.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])
    seats = st.selectbox("Enter the number of seats",
                       [4,5,7,9,11])

    km_driven = st.number_input("Enter km driven", min_value=0, value=30000)
    

## Encoding Categorical features
## Use the same encoding as used during the training. 
expected_cols = model.model.exog_names

if st.button("Predict Price"):

    input_df = pd.DataFrame([[0.0] * len(expected_cols)], columns=expected_cols)

    if "const" in input_df.columns:
        input_df.loc[0, "const"] = 1

    if "max_power" in input_df.columns:
        input_df.loc[0, "max_power"] = engine

    if "mileage" in input_df.columns:
        input_df.loc[0, "mileage"] = 19.7   # later make this an input field

    if "age" in input_df.columns:
        input_df.loc[0, "age"] = 2024 - year

    if "km_driven" in input_df.columns:
        input_df.loc[0, "km_driven"] = km_driven

    if "make" in input_df.columns:
        input_df.loc[0, "make"] = 1   # temporary placeholder

    if fuel_type in input_df.columns:
        input_df.loc[0, fuel_type] = 1

    if transmission_type in input_df.columns:
        input_df.loc[0, transmission_type] = 1

    if seller_type in input_df.columns:
        input_df.loc[0, seller_type] = 1

    if str(seats) in input_df.columns:
        input_df.loc[0, str(seats)] = 1

    st.write(input_df)

    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]}")