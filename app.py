from flask import Flask, request, jsonify
import os
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Specify the absolute path to your PDF folder
PDF_FOLDER = "/Users/navneet.dagdiya/geo_bot_data"
if not os.path.exists(PDF_FOLDER):
    os.makedirs(PDF_FOLDER)  # Ensure the folder exists

# Load models
embedder = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding model
qa_pipeline = pipeline("text-generation", model="GPT2")  # Your GPT model

# Function to extract text from all PDFs in the folder
def load_pdfs():
    documents = []
    for file_name in os.listdir(PDF_FOLDER):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, file_name)
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append(text)
    return documents

# Load and embed the documents
documents = load_pdfs()
document_embeddings = [embedder.encode(doc, convert_to_tensor=True) for doc in documents]

# RAG pipeline
def retrieve_and_answer(query):
    # Embed the query
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    # Find the closest document
    scores = [util.pytorch_cos_sim(query_embedding, doc_emb)[0][0].item() for doc_emb in document_embeddings]
    best_doc_idx = scores.index(max(scores)) if scores else None

    if best_doc_idx is not None and scores[best_doc_idx] > 0.5:  # Threshold for relevance
        context = documents[best_doc_idx]
        response = qa_pipeline(f"Context: {context}\nQuestion: {query}", max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    else:
        return "Sorry, I don't know the answer to that."

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt.strip():
            return jsonify({"error": "Empty prompt"}), 400

        answer = retrieve_and_answer(prompt)
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
