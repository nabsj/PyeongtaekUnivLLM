from langchain.text_splitter import RecursiveCharacterTextSplitter
from loader import pages
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 3000,
    chunk_overlap = 300,
    length_function = len,
    is_separator_regex= False,
)
text = text_splitter.split_documents(pages)