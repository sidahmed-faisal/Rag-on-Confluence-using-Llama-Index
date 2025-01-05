import requests
import streamlit as st


def list_spaces():
    try:
        response = requests.get("http://localhost:8000/get-spaces")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch document list. Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching the document list: {str(e)}")
        return []

def list_pages(spaceKey):
    try:
        response = requests.post(f"http://localhost:8000/get-pages?space={spaceKey}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch document list. Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching the document list: {str(e)}")
        return []

def get_chat_answer(space, page, question):
            
    url = "http://localhost:8000/chat"
    
    headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    
    if page == None:

        data = {
            "question": question,
            "space": space
        }

        response = requests.post(url, headers=headers, json=data)

        return response.json()
    
    else:
        
        data = {
            "question": question,
            "space": space,
            "page_id": [
                "294939"
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        return response.json()

