from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

import os
import logging
from dotenv import load_dotenv

from api.confluence_utils import Confluence_control
from api.llama_utils import answer_question
from api.pydantic_models import QueryInput

load_dotenv()


# Configure logging on log.txt
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("log.txt"),
                        logging.StreamHandler()
                    ])

# Load Confluence Username and Password on startup from env
@asynccontextmanager
async def lifespan(app: FastAPI):

    
    global  url , user_name , password , conful


    # Access the environment variables
    url = os.getenv('URL')
    user_name = os.getenv('CONFLUENCE_USERNAME')
    password = os.getenv('CONFLUENCE_PASSWORD')

    conful = Confluence_control(url=url , user=user_name, password=password)


    yield
    pass


app = FastAPI(lifespan=lifespan)


@app.get("/get-spaces")
async def get_spaces():

    try:

        spaces = conful.show_spaces()
        
        return spaces
    
    except Exception as e:

        return JSONResponse(f"Error while trying to get spaces  details: {e}", status_code=403)


@app.post("/get-pages")
async def get_pages(space):

    try:
        pages = conful.load_pages(space)

        return JSONResponse(pages)
    
    except Exception as e:
        return JSONResponse(f"Error while trying to get pages from space {space} details: {e}", status_code=404)

@app.post("/chat")
async def chat(request: QueryInput):

    if request.page_id == None:

        try:
            documents = conful.load_documents(request.space)

            response = answer_question(request.question, documents)
            
            return response
        
        except Exception as e:
            return JSONResponse(f"the Space you requested with id: {request.space} is not present",status_code=404)


    else :

        reader = conful.get_documents_reader()

        try:
            documents = reader.load_data(
                page_ids=request.page_id, include_attachments=True,)
            

            response = answer_question(request.question, documents)

            return JSONResponse(response)
            
        
        except Exception as e:
            return JSONResponse(f"one or more of the pages you requested aren't found  details: {e}",status_code=404)



# Run the APP on port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
