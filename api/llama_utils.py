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


embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.embed_model = embed_model

# Settings.embed_model= OpenAIEmbedding()

splitter = SentenceSplitter(chunk_size=1024,chunk_overlap=100)


load_dotenv()


def evaluate_response(question ,response):

    evaluation_model = OpenAI(temperature=0, model= "gpt-3.5-turbo")

    evaluator = RelevancyEvaluator(llm=evaluation_model)

    eval_result = evaluator.evaluate_response(query= question , response=response)

    return eval_result

def answer_question(question, documents):


    nodes = splitter.get_nodes_from_documents(documents)

    chroma_client = chromadb.PersistentClient()
    chroma_collection = chroma_client.create_collection("documents")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex(nodes, storage_context=storage_context)

    queryengine = index.as_query_engine(similarity_top_k=3)

    try:

        response = queryengine.query(question)

        evaluation = evaluate_response(question=question , response=response)

        result = "No Hallucination" if evaluation.passing == True else "Hallucinated"
        
        # Cleanup: delete the Chroma collection after execution
        chroma_client.delete_collection("documents")


        return {
            "answer" : response,
            "relevancy": result
        }


    except Exception as e:
        return e











