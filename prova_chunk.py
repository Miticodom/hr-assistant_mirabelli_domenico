from document_processor import DocumentProcessor

documents, metadatas, ids = DocumentProcessor.process_documents()
print("chunk totali:", len(documents))
for doc, meta in zip(documents, metadatas):
    print(f"{meta['source']:<45} {len(doc):>5} caratteri | {doc[:60]!r}")
