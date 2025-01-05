import streamlit as st
from api_utils import list_spaces

def display_sidebar():

    # Sidebar: List spaces
    st.sidebar.header("Spaces")
    if st.sidebar.button("Get spaces"):
        with st.spinner("Getting spaces..."):
            # Fetch documents using the list_spaces function
            spaces = list_spaces()
            # If spaces are returned, display them
            # If spaces are returned, display them
            if spaces:
                for title, space_id in spaces.items():
                    # Display each space's title and page_id in the sidebar
                    st.sidebar.write(f"Title: {title}")
                    st.sidebar.write(f"Space ID: {space_id}")
                    st.sidebar.write("-" * 30)  # Just to separate spaces visually
            else:
                st.sidebar.write("No spaces found.")
