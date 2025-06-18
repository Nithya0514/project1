import faiss
import pickle
from sentence_transformers import SentenceTransformer

class VectorDB:
    def __init__(self):
        with open("faiss_chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)
        self.index = faiss.read_index("faiss_index.bin")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query, top_k=1):
        q_vector = self.model.encode([query])
        distances, indices = self.index.search(q_vector, top_k)
        return [self.chunks[i] for i in indices[0]]
