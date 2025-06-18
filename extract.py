import fitz  # PyMuPDF
import pickle

pdf_path = "Breathe ESG Overview.pdf"
doc = fitz.open(pdf_path)
chunks = []

for page in doc:
    text = page.get_text()
    split_text = text.split(". ")
    chunks.extend(split_text)

with open("faiss_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)
