import streamlit as st
import replicateBackend as rb



# Initial messages
if "messages" not in st.session_state.keys():
    st.session_state["messages"] = [{
        "role": "assistant",
        "content": "Hello there, how can I help?"
    }]

# Display messages
if "messages" in st.session_state and st.session_state.messages:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User input
user_prompt = st.chat_input()

if user_prompt is not None:
    imagelink = rb.generateImageFromApi(user_prompt)
    st.image(imagelink,caption=f"Image link {imagelink}")
