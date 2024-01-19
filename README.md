# FAISS Excel DataLoader for LangChain

This repository contains a Python script (`excel_data_loader.py`) that demonstrates how to use LangChain for processing Excel files, splitting text documents, and creating a FAISS (Facebook AI Similarity Search) vector store. The script leverages the LangChain library for embeddings and vector stores and utilizes multithreading for parallel processing.

## Requirements

- **[LangChain](https://github.com/langchain-ai):** LangChain is a library for natural language processing tasks, including document loading, text splitting, and vector stores.
  
  ```bash
  pip install langchain
  ```

- **[FAISS](https://github.com/facebookresearch/faiss):** FAISS is a library for efficient similarity search and clustering of dense vectors.
  
  ```bash
  pip install faiss
  ```

- **Other requirements:** Install additional dependencies by running:
  
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/umangpurwar03/FAISS-Excel-dataloader-LLM
    ```

2. Navigate to the repository directory:

    ```bash
    cd FAISS-Excel-dataloader-LLM
    ```

## Usage

1. Modify the `data_dir` variable in `excel_dataloader.py` to point to the directory containing your Excel files.

2. Run the script:

    ```bash
    python excel_dataloader.py
    ```

    This script will process each Excel file in parallel using multithreading, loading the data, splitting the text into chunks, creating embeddings using Hugging Face models, and finally, storing the vectors in a FAISS vector store.

## Customization

- You can customize the model used for embeddings by modifying the `model_name` parameter in the `HuggingFaceEmbeddings` initialization.

- Adjust the chunk size and overlap in the `RecursiveCharacterTextSplitter` initialization according to your requirements.

- Feel free to customize other parameters and configurations based on your specific use case.

## Multithreading

The script uses multithreading to process multiple Excel files concurrently. The `process_excel_files_in_parallel` function initializes a separate thread for each Excel file, allowing for efficient parallel processing. Adjust the number of threads based on your system's capabilities and requirements.

## [CSV dataloader](https://github.com/umangpurwar03/FAISS-CSV-dataloader-LLM)

If you want CSV data loader you can clink on this[Link](https://github.com/umangpurwar03/FAISS-CSV-dataloader-LLM)

## License

This code is released under the MIT License. Feel free to use and modify it according to your needs.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai)
- [FAISS](https://github.com/facebookresearch/faiss)

If you find this code helpful or have suggestions for improvement, please feel free to contribute or open an issue.
