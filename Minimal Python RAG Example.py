# 1. Knowledge Base (Your external documents)
documents = [
    "Alice likes cats.",
    "Bob enjoys pizza.",
    "Charlie codes in Python.",
    "The office coffee machine is on the 2nd floor."
]

# 2. Simple Retrieval Function (Keyword/Overlap or basic matching)
def retrieve_context(query):
    # Find the document that shares the most words with the query
    query_words = set(query.lower().split())
    best_doc = max(documents, key=lambda doc: len(query_words.intersection(set(doc.lower().split()))))
    return best_doc

# 3. Augment and Generate (Simulating LLM prompt assembly)
def generate_answer(query):
    context = retrieve_context(query)
    
    # Construct the augmented prompt
    prompt = f"""Use the context below to answer the question.

Context: {context}
Question: {query}
Answer:"""
    
    # In a real app, you would send this 'prompt' to OpenAI, Ollama, or another LLM.
    # Here we mock the LLM output using the retrieved context:
    return f"Based on the context ('{context}'): {context}"

# --- Test the RAG Program ---
user_query = "What does Charlie do?"
response = generate_answer(user_query)
print(response)
