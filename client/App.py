import streamlit as st
import requests

# Streamlit App
st.title("MyChat Bot with Gemini API")
st.write("A chatbot powered by Flask and Google's Gemini API.")
st.write("Enter your question below and click on the button to generate a response.")

# User input
user_input = st.text_area("Enter your question here:", height=150)

# Send prompt to Flask backend
if st.button("Generate Response"):
    if user_input.strip():
        try:
            with st.spinner("Fetching response..."):
                # Replace with your Flask backend URL
                backend_url = "http://127.0.0.1:5000/chat"
                response = requests.post(
                    backend_url,
                    json={"prompt": user_input}
                )
                
                # Display the response
                if response.status_code == 200:
                    st.success("Response:")
                    st.write(response.json().get("response"))
                else:
                    st.error(f"Error: {response.json().get('error')}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid prompt.")

st.caption("Built with Streamlit and Flask.")
st.caption("mvkcd////2025")
