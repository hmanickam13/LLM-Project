from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import OpenAI

# Look into env file and load variables
load_dotenv()

# # Initialize by creating an embedding instance
embeddings = OpenAIEmbeddings()

# # Sample text
# text = "This is just a sample text to check if the connection is working with OpenAI using the API Key."
# # Text needs to be encoded into numerical format to used with LLMs
# doc_embeddings = embeddings.embed_documents([text]) # Put in a linked-list if there are multiple things to embed
# print(doc_embeddings)

# Load the text file
loader = TextLoader('news/summary.txt')

# We use directory laoder when there are multiple text files
# We can specify whatever file type we want(.pdf,.doc,etc)
loader = DirectoryLoader('news', glob="**/*.txt")

# Print the loaded document
documents = loader.load()
# test
# print(len(documents))

# We split the individual words. We can specify parameters
    # chunckchunk_size (int): The maximum size (in characters) of each chunk. This parameter determines the length of each split document. Default is 1000.
    # chunk_overlap (int): The number of characters to overlap between consecutive chunks. This parameter controls the overlap between chunks to ensure continuity in the text. Default is 0, which means no overlap.
    # include_partial_chunks (bool): Whether to include partial chunks that do not reach the full chunk_size. If set to True, partial chunks will be included in the output. If set to False, partial chunks will be discarded. Default is False.
    # include_splitter_tokens (bool): Whether to include special splitter tokens in the output. If set to True, the splitter tokens indicating the start and end of each chunk will be included. If set to False, the splitter tokens will not be included. Default is False.
    # splitter_token (str): The special token used to mark the boundaries between chunks. This token is inserted between consecutive chunks when include_splitter_tokens is set to True. Default is "|||".
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
# Call the text_splitter and split the loaded documents
texts = text_splitter.split_documents(documents)

# test
# print(text)

# Create a vector store using the Chroma algorithm
vecstore = Chroma.from_documents(texts, embeddings)

# Create a RetrievalQA for question-answering using from_chain_type to initialize
qa = RetrievalQA.from_chain_type(
    
    # We can specify any LLM we want.
    llm=OpenAI(),
    
    # Chain type depends on your specific application.
    # The RetrievalQA.from_chain_type() method expects the chain type to be one of the following: 'stuff', 'map_reduce', 'refine', 'map_rerank'.
    chain_type="stuff",
    
    # Specifies the retriever component of the QA system
    # Converts the vectore into a retriever object
    retriever = vecstore.as_retriever()
    
    # Other parameters
    # top_k: Specifies the maximum number of retrievals to consider. Default is 10.
    # temperature: Controls the randomness of the retrieval scores. Higher values (e.g., 1.0) make the scores more uniform, while lower values (e.g., 0.2) emphasize the top retrievals. Default is 0.2.
    # max_length: Specifies the maximum length (in tokens) for the generated answer. Default is 20.
    # stop_chain_types: A list of chain types that should be excluded from the retrieval process. It allows you to filter out certain chain types from consideration.
)

def query(q):
    print(f"Query: {q}")
    print(f"Answer: {qa.run(q)}")

query("What are the effects of legislations surrounding emmisions on the Australian coal market?")
query("What are China's plan with renewable energy?")
query("Is there an export ban on Coal in Indonesia?")