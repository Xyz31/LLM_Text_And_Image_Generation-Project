import streamlit as st
import replicateBackend as rp


# Create a dropdown for selecting integers from 0 to 9
default_temperature = 0.4
selected_tempearature = st.slider("Select a value for Temperature:", 0.1, 1.0, default_temperature,0.1)

st.write("You selected:", selected_tempearature)

# Create a slider for selecting values from 0 to 1 with a step size of 0.1
default_prob = 0.9
selected_prob = st.slider("Select a value for sampling probability:", 0.0, 1.0, default_prob, 0.1)

st.write("You selected:", selected_prob)

 # Read an integer from the user using st.number_input
default_length = 300
selected_length = st.number_input("Enter Number of Characters Needed:",value=default_length, step=1)

# Display the entered integer
st.write("You entered:", int(selected_length))

def setParameters():
    rp.temperature = selected_tempearature
    rp.prob = selected_prob
    rp.maxlength = selected_length

st.button('Set' , type='primary', on_click=setParameters())