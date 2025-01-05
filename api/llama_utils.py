from dotenv import load_dotenv

from llama_index.core.evaluation import (
    FaithfulnessEvaluator,
    RelevancyEvaluator
)

from llama_index.core import VectorStoreIndex,SummaryIndex
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core.node_parser import SentenceSplitter

from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

import chromadb
import logging


embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.embed_model = embed_model

# Settings.embed_model= OpenAIEmbedding()

splitter = SentenceSplitter(chunk_size=1024,chunk_overlap=100)


load_dotenv()

# Configure logging on log.txt
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("log.txt"),
                        logging.StreamHandler()
                    ])

def evaluate(question ,response):

    evaluation_model = OpenAI(temperature=0,)

    evaluator = RelevancyEvaluator(llm=evaluation_model)

    eval_result = evaluator.evaluate_response(query= question , response=response)

    return eval_result

def answer_question(question, documents):


    nodes = splitter.get_nodes_from_documents(documents)

    logging.info("Creating Chroma collection")

    chroma_client = chromadb.PersistentClient()
    chroma_collection = chroma_client.create_collection("documents")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    logging.info("Success!: Created Chroma collection")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex(nodes, storage_context=storage_context)


    queryengine = index.as_query_engine(similarity_top_k=3)

    try:

        logging.info(f"Generating Answer for question {question}")

        response = queryengine.query(question)

        logging.info(f"Success answer generated!")

        logging.info(f"Evaluating Answer: {response}")

        evaluation = evaluate(question=question , response=response)

        # result = "No Hallucination" if evaluation.passing == True else "Hallucinated"
        
        # Cleanup: delete the Chroma collection after execution
        chroma_client.delete_collection("documents")


        return {
            "answer" : response.response,
            "relevancy":  "Hallucinated"  if evaluation.passing == False else "No Hallucination"
        }


    except Exception as e:
        return e