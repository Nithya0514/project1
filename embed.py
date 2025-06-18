from sentence_transformers import SentenceTransformer
import faiss
import pickle

with open("faiss_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "faiss_index.bin")
