from huggingface_hub import InferenceClient
import streamlit as st
client = InferenceClient(
    "HuggingFaceH4/zephyr-7b-beta",
    token="YOUR_HUGGINFACE_API_KEY_HERE", #Create a new API key from huggingface.co, and add it here 
)

def get_response(user_input):
    
    output = client.chat_completion(
        messages=[{"role": "user", "content": user_input}],
        max_tokens=500,
        stream=False,
    )
        
    return output.choices[0]["message"]["content"] if output else "I am sorry, I don't understand that."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Hello! How can I help you today?"}]
st.title("My chatbot")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:= st.chat_input("You:"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


if st.session_state["messages"][-1]["role"] =="user":
    response = get_response(prompt)
    st.session_state.messages.append({"role": "system", "content": response})
    with st.chat_message("system"):
        st.write(response)