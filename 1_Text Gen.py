import streamlit as st
import replicateBackend as rp

st.sidebar.success("Select Your Choice", icon="✅")


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
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        # Add style
        with st.spinner("Loading..."):
            ai_response = rp.generateTextFromApi(user_prompt)
            st.write(ai_response)

    new_ai_message = {
        "role": "assistant",
        "content": ai_response
    }
    st.session_state.messages.append(new_ai_message)


