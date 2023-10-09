from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("pturule_V0.1.pdf")
pages = loader.load_and_split()