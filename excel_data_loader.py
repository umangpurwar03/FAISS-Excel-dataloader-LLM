from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import UnstructuredExcelLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from multiprocessing import Pool

# Define paths
data_dir = 'data'
faiss_db = 'vectorstore/db_faiss'

def process_excel_file(excel_path):
    # Load the Excel file using UnstructuredExcelLoader
    loader = UnstructuredExcelLoader(excel_path, mode="elements")
    document = loader.load()
    print(f"Loaded Excel file: {excel_path}")

    # Initialize a text splitter to divide documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(document)
    print(f"Texts splitted for Excel file: {excel_path}")

    # Initialize HuggingFaceEmbeddings using a specific model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    print(f"Embeddings created for Excel file: {excel_path}")

    # Create a vector store using FAISS from the text chunks and embeddings
    db = FAISS.from_documents(texts, embeddings)
    print(f"Vector store created for Excel file: {excel_path}")

    # Save the vector store locally
    db.save_local(os.path.join(faiss_db, f"{os.path.basename(excel_path)}_db"))

def process_excel_files_in_parallel():
    # Ensure the directory exists
    if not os.path.exists(faiss_db):
        os.makedirs(faiss_db)

    # List all Excel files in the directory
    excel_files = [file for file in os.listdir(data_dir) if file.endswith('.xlsx')]

    # Use a multiprocessing Pool for parallel processing
    with Pool() as pool:
        pool.map(process_excel_file, [os.path.join(data_dir, excel_file) for excel_file in excel_files])

if __name__ == "__main__":
    process_excel_files_in_parallel()
