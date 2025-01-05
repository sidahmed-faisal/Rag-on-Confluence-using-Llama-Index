import requests
import streamlit as st
from api_utils import *


# Main App
st.title("Chat with Confluence")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Display the sidebar
selected_space, selected_page = display_sidebar()

# Display the chat interface
display_chat_interface(selected_space, selected_page)
