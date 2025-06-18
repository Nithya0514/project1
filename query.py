from vector_db import VectorDB

db = VectorDB()

print("Ask a question (type 'exit' to quit):")
while True:
    query = input("\n> ")
    if query.lower() == "exit":
        break
    results = db.search(query)
    print("\nAnswer:", results[0].replace('\n', ' '))
