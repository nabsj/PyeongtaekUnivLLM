from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from db_loader.load_db import load_db


def return_answer(question):
    llm = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature=1)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=load_db.as_retriever())
    result = qa_chain({"query":question})
    return result