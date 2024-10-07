import streamlit as st
import pickle
import numpy as np
import warnings

# Ignore warnings
warnings.filterwarnings(action='ignore')

# Load the trained model
loaded_model = pickle.load(open('trained_rfc_model.sav', 'rb'))

# Title of the app
st.title('Customer Churn Prediction App')

# Main function to take inputs and display prediction
def main():
    # Taking input from the user
    credit_score = st.text_input('Enter the customer credit score here')
    age = st.text_input('Enter the customer age here')
    tenure = st.text_input('Enter the tenure here')
    balance = st.text_input('Enter the customer balance here')
    products_number = st.text_input('Enter the number of products the customer uses here')
    credit_card = st.text_input('Does the customer have a credit card? (1 for Yes, 0 for No)')
    active_member = st.text_input('Is the customer an active member? (1 for Yes, 0 for No)')
    estimated_salary = st.text_input('Enter the estimated salary of the customer here')

    # Prediction function
    def churn_prediction(input_data):
        # Convert input data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # Reshape the array as we are predicting for a single instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Predict using the loaded model
        prediction = loaded_model.predict(input_data_reshaped)

        if prediction[0] == 0:
            return 'The customer will not churn.'
        else:
            return 'The customer is likely to churn.'

    # Code for prediction
    successfully = ''

    # Creating a button for prediction
    if st.button('Customer Churn Prediction'):
        # Convert inputs to appropriate types (numeric)
        try:
            input_data = [
                float(credit_score),
                int(age),
                int(tenure),
                float(balance),
                int(products_number),
                int(credit_card),
                int(active_member),
                float(estimated_salary)
            ]
            # Call the prediction function
            successfully = churn_prediction(input_data)
        except ValueError:
            successfully = 'Please enter valid input values.'

        st.success(successfully)

# Run the app
if __name__ == '__main__':
    main()
