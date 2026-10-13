# document_processor.py
import os
import uuid
from config import Config


class DocumentProcessor:
    @staticmethod
    def process_documents():
        documents = []
        metadatas = []
        ids = []

        MIN_CHARS = 100  # sotto questa soglia il chunk viene unito al successivo

        for filename in os.listdir(Config.DOCUMENTS_DIR):
            if filename.endswith(".txt"):
                with open(os.path.join(Config.DOCUMENTS_DIR, filename), 'r', encoding='utf-8') as file:
                    chunks = file.read().replace('\n', '.').split('### ')

                    # Unisco i chunk troppo corti (es. titoli di sezione isolati)
                    merged = []
                    buffer = ""
                    for chunk in chunks:
                        if chunk.isspace() or chunk == "":
                            continue
                        buffer = buffer + chunk + " "
                        if len(buffer) >= MIN_CHARS:
                            merged.append(buffer.strip())
                            buffer = ""

                    # Se a fine file resta un pezzo corto, non lo perdo
                    if buffer:
                        if merged:
                            merged[-1] = merged[-1] + " " + buffer.strip()
                        else:
                            merged.append(buffer.strip())

                    for chunk in merged:
                        documents.append(chunk)
                        metadatas.append({"source": filename})
                        ids.append(str(uuid.uuid4()))

        return documents, metadatas, ids

    @staticmethod
    def read_first_lines(file_path, n_lines=100):
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line, _ in zip(file, range(n_lines))]