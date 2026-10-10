import chromadb
import ollama

# 1. Inizializziamo ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# 2. Creiamo la collezione specificando la distanza per Similarità del Coseno ('cosine')
collection = chroma_client.get_or_create_collection(
    name="miei_documenti",
    metadata={"hnsw:space": "cosine"}
)

# 3. Documenti di prova
documenti = [
    "Il gatto è un animale domestico indipendente che ama dormire molte ore al giorno.",
    "Il cane è un animale fedele, spesso definito il migliore amico dell'uomo.",
    "Python è un linguaggio di programmazione molto popolare per l'intelligenza artificiale e lo sviluppo web."
]
ids = ["doc1", "doc2", "doc3"]

print("-> Indicizzazione dei documenti nel database vettoriale...")

# 4. Calcoliamo gli embedding per i documenti (usando il prefisso per i documenti)
for i, doc in enumerate(documenti):
    response = ollama.embeddings(
        model="nomic-embed-text", 
        prompt=f"search_document: {doc}"
    )
    
    collection.upsert(
        documents=[doc],
        embeddings=[response["embedding"]],
        ids=[ids[i]]
    )

print("-> Documenti indicizzati con successo!\n")

# 5. Domanda dell'utente
domanda = "Parlami dei cani"
print(f"Domanda dell'utente: {domanda}")

# Generiamo l'embedding per la domanda (usando il prefisso per le query)
domanda_emb = ollama.embeddings(
    model="nomic-embed-text", 
    prompt=f"search_query: {domanda}"
)["embedding"]

# Cerchiamo nel database
risultati = collection.query(
    query_embeddings=[domanda_emb],
    n_results=1
)

# Estraiamo il documento più simile
contesto_trovato = risultati["documents"][0][0]
print(f"Contesto recuperato dal database: {contesto_trovato}\n")

# 6. Generazione con Ollama
prompt_finale = f"""Usa esclusivamente le informazioni nel contesto sottostante per rispondere alla domanda.

Contesto:
{contesto_trovato}

Domanda: {domanda}
Risposta:"""

print("-> Interrogazione di Ollama in corso...")
risposta_ollama = ollama.chat(
    model="qwen3.6",
    messages=[{"role": "user", "content": prompt_finale}]
)

print("\n--- Risposta Finale ---")
print(risposta_ollama["message"]["content"])