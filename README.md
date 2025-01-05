<p align="center">
    <img src="[https://www.google.com/url?sa=i&url=https%3A%2F%2Finfosecwriteups.com%2Fhundreds-of-companies-internal-data-exposed-the-confluence-cloud-misconfiguration-63cbc143caea&psig=AOvVaw1dXVbXv4_iIlEjM01aSs7_&ust=1736175014475000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLjL_Izq3ooDFQAAAAAdAAAAABAE](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYfY6DlNSLekxManGscXSkHnGNFdw-N4ajCA&s)" align="center" width="30%">
</p>
<p align="center"><h1 align="center">RAG-ON-CONFLUENCE-USING-LLAMA-INDEX</h1></p>
<p align="center">
	<em>Unleash AI-powered knowledge with llama magic!</em>
</p>

<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)

---

##  Overview

The Rag-on-Confluence-using-Llama-Index project streamlines document retrieval and question answering by integrating language models and chroma vector store. Its key features include efficient document processing, accurate response evaluation with **RelevancyEvaluator** from llama-index, and seamless Confluence interaction. Targeting users seeking streamlined AI-powered information retrieval, it enhances data reliability and user experience.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **FastAPI** for setting up a server to interact with Confluence.</li><li>Integrates **Confluence API** for retrieving documents, pages, and spaces.</li><li>Orchestrates document retrieval, question answering, and evaluation using a combination of vector indexing and AI models in `api/llama_utils.py`.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows **PEP 8** guidelines for Python code consistency.</li><li>Uses **Pydantic models** in `api/pydantic_models.py` for structuring and validating input data.</li><li>Implements error handling in `api/app.py` for robustness.</li></ul> |
| 📄 | **Documentation** | <ul><li>Contains a `requierments.txt` file specifying project dependencies.</li><li>Provides inline code comments for better code understanding.</li><li>Includes detailed explanations in code files like `api/confluence_utils.py` for clarity.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **external services** for embeddings and evaluation in `api/llama_utils.py`.</li><li>Enables interaction with **Confluence API** for seamless data retrieval.</li><li>Facilitates integration of various language models and indexing services within the project architecture.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Divides functionalities into separate modules like `api/llama_utils.py`, `api/pydantic_models.py`, and `api/confluence_utils.py` for better organization.</li><li>Encapsulates related functionalities within individual files for maintainability.</li><li>Follows a modular design pattern for scalability and ease of maintenance.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes document processing and response evaluation for **efficiency**.</li><li>Utilizes **vector indexing** and AI models for accurate responses to user queries.</li><li>Ensures **fast response times** for user interactions with Confluence.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Handles **authentication** securely in `api/confluence_utils.py` for Confluence API interactions.</li><li>Implements **data encryption** for sensitive information handling.</li><li>Follows **security best practices** to prevent vulnerabilities.</li></ul> |

---

##  Project Structure

```sh
└── Rag-on-Confluence-using-Llama-Index/
    ├── api
    │   ├── app.py
    │   ├── confluence_utils.py
    │   ├── llama_utils.py
    │   └── pydantic_models.py
    ├── app
    │   ├── api_utils.py
    │   ├── chat_interface.py
    │   ├── sidebar.py
    │   └── streamlit_app.py
    └── requierments.txt
```


###  Project Index
<details open>
	<summary><b><code>RAG-ON-CONFLUENCE-USING-LLAMA-INDEX/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index/blob/master/requierments.txt'>requierments.txt</a></b></td>
				<td>Facilitates integration of various language models and indexing services within the project architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- api Submodule -->
		<summary><b>api</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index/blob/master/api/llama_utils.py'>llama_utils.py</a></b></td>
				<td>- The code in `api/llama_utils.py` orchestrates document retrieval, question answering, and evaluation using a combination of vector indexing and AI models<br>- It integrates with external services for embeddings and evaluation, providing a streamlined process for generating relevant responses to user queries<br>- The code ensures efficient document processing and accurate response evaluation within the project's architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index/blob/master/api/pydantic_models.py'>pydantic_models.py</a></b></td>
				<td>- Defines Pydantic models for querying questions, spaces, and page IDs<br>- This code file plays a crucial role in structuring and validating input data for the API endpoints<br>- It ensures that the incoming data adheres to the specified schema, enhancing the reliability and consistency of the system.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index/blob/master/api/app.py'>app.py</a></b></td>
				<td>- The code in api/app.py sets up a FastAPI server to interact with Confluence, allowing users to retrieve spaces, pages, and chat with a chatbot<br>- It handles requests to fetch spaces, pages, and chat messages, providing error responses when necessary<br>- The server runs on port 8000, facilitating seamless communication with Confluence.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index/blob/master/api/confluence_utils.py'>confluence_utils.py</a></b></td>
				<td>- Enables interaction with Confluence API to retrieve documents, pages, and spaces<br>- Handles authentication and data retrieval, abstracting away complexities<br>- Facilitates seamless integration with ConfluenceReader for efficient data loading and space management.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with Rag-on-Confluence-using-Llama-Index, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python version **3.9+**


###  Installation

Install Rag-on-Confluence-using-Llama-Index using one of the following methods:

**Build from source:**
**Backend**

1. Clone the Rag-on-Confluence-using-Llama-Index repository:
```sh
❯ git clone https://github.com/sidahmed-faisal/Rag-on-Confluence-using-Llama-Index
```

2. Navigate to the project directory:
```sh
❯ cd Rag-on-Confluence-using-Llama-Index
```

3. Install the project dependencies:

```sh
❯ pip install requirements.txt
```
4. Add to **.env** file the following: **CONFLUENCE_USERNAME** (your email), **CONFLUENCE_PASSWORD** (API token you can obtain from : **<https://id.atlassian.com/manage-profile/security/api-tokens>**), **URL** for your confluence domain and **OPENAI_API_KEY** from OpenAI
```sh
CONFLUENCE_USERNAME=""
CONFLUENCE_PASSWORD=""
URL=""
OPENAI_API_KEY=""
```

4. Navigate to the **/api** directory and run:

```sh
❯ fastapi run app.py
```

5- Access the backend swagger from:

```sh
http://127.0.0.1:8000/docs#/
```


###  Frontend
1. Navigate to the project directory:
```sh
❯ cd Rag-on-Confluence-using-Llama-Index
```

2. Navigate to the ./app directory:
```sh
❯ cd ./app

3. Navigate to the ./app directory:
```sh
❯ streamlit run streamlit_app.py

---
