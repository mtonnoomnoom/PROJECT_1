import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.containts.containts import DATA_FILE, DB_SRC
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from src.utils.get_data import load_vocabulary
class DatabaseManager:
    def __init__(self):
        """Initialize database parameters and setup embedding function."""
        load_dotenv()
        
        self.database_name = os.environ['DATABASE_NAME']
        self.database_dir = DB_SRC
        self.embedding_model = os.environ['EMBEDDINGMODEL']
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=self.embedding_model)
        self.client = self._initialize_client()
        self.collection = self._get_or_create_collection()

    def _initialize_client(self):
        """Create the database directory if it doesn't exist and initialize Chroma client."""
        if not os.path.exists(self.database_dir):
            os.mkdir(self.database_dir)
            print("Database directory created successfully.")
        print("create database")

        return chromadb.PersistentClient(path=self.database_dir)

    def _get_or_create_collection(self):
        """Retrieve or create the collection with the specified name and embedding function."""
        print("get or create collection")
        collection = self.client.get_or_create_collection(
            name=self.database_name,
            metadata={"hnsw:space": "cosine"},
            embedding_function=self.embedding_func
        )

        return collection

    def add_data(self, data, ids_list):
        """Add data and corresponding metadata to the collection."""
        if not isinstance(data, list) :
            raise ValueError("Data and metadata should be lists.")
        print("begin add data")

       
        batch_size = 1000
        for i in range(0, len(data), batch_size):
            batch_data = data[i:i + batch_size]
            
            batch_ids = ids_list[i:i + batch_size]
            self.collection.add(documents=batch_data, ids=batch_ids)
            print(f"Added batch {i // batch_size + 1}")

        print("Data added to the database successfully.")

    def remove_database(self):
        """Remove the collection from the database."""
        self.client.delete_collection(name=self.database_name)
        print("Database collection removed successfully.")

    def query_collection(self, questions: [str], number_answer=1) :
        """Get data from vector database"""
        print('Get data from vector database')
        collection_answer = self.collection.query(
            query_texts=questions,
            n_results=number_answer,
        )

        collection_documents = collection_answer['documents']
        collection_distances = collection_answer['distances']
        
        return collection_documents[0],collection_distances[0]


if __name__ == "__main__":
    vocabulary = load_vocabulary()
    ids=[]
    for i in range(len(vocabulary)):
        ids.append(str(i))
    db_manage = DatabaseManager()

    db_manage.add_data(data=vocabulary,  ids_list=ids)