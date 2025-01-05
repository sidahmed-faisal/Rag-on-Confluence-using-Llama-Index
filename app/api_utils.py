import requests
import streamlit as st



def list_spaces():
    try:
        response = requests.get("http://localhost:8000/get-spaces")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch spaces list. Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        st.error(f"An error occurred while fetching spaces list: {str(e)}")
        return {}


def list_pages(spaceKey):
    try:
        response = requests.post(f"http://localhost:8000/get-pages?space={spaceKey}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch pages from space. Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        st.error(f"An error occurred while fetching pages from space: {str(e)}")
        return {}


def get_chat_answer(space, page, question):
    url = "http://localhost:8000/chat"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    data = {"question": question, "space": space}
    if page is not None:
        data["page_id"] = [page]

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to get chat answer. Error: {response.status_code} - {response.text}")
            return {"error": "Unable to fetch answer."}
    except Exception as e:
        st.error(f"An error occurred while fetching chat answer: {str(e)}")
        return {"error": "An exception occurred."}


def display_sidebar():
    st.sidebar.header("Select Space and Page")
    spaces = list_spaces()
    
    if not spaces:
        st.sidebar.warning("No spaces available.")
        return None, None

    space_name = st.sidebar.selectbox("Select a Space", list(spaces.keys()))
    space_id = spaces[space_name]
    
    pages = list_pages(space_id)
    page_name = st.sidebar.selectbox(
        "Select a Page if you want to search specific page",
        ["None"] + list(pages.keys())
    )
    page_id = pages.get(page_name) if page_name != "None" else None

    return space_id, page_id


def display_chat_interface(space, page):
    st.header("Chat Interface")

    if space is None:
        st.warning("Please select a space from the sidebar to start.")
        return

    question = st.text_input("Enter your question:", "")
    if st.button("Ask"):
        if question.strip():
            response = get_chat_answer(space, page, question)
            
            answer = response.get("answer", "No answer received.")
            st.write("**Answer:**", answer)

            # Display additional details in an expander
            with st.expander("Show Additional Details"):
                relevance_score = response.get("relevance_score", "N/A")
                relevancy = response.get("relevancy", "N/A")

                st.write("**Relevance Score:**", relevance_score)
                st.write("**Relevancy:**", relevancy)
        else:
            st.error("Please enter a valid question.")