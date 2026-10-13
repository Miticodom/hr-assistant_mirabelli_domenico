# utils.py
from config import Config
from openai import OpenAI

client = OpenAI(base_url=Config.AI_API_URL, api_key=Config.AI_API_KEY)


class LLMHelper:

    @staticmethod
    def chat(messages):
        return client.chat.completions.create(
            model=Config.LLM_MODEL, messages=messages, stream=True
        )

    @staticmethod
    def create_prompt(context, question, cv_header):
        return f"""
            Dato il seguente contesto:
            [[[
            {context}
            ]]].
            Ecco l'intestazione del curriculum del candidato:
            [[[
            {cv_header}
            ]]].
            Rispondi alla domanda dell'utente: [[[ {question} ]]] .
            Spiega che nel file individuato c'e' il profilo piu' adatto.
            Assicurati di nominare il nome del file.
            Ricava dall'intestazione nome e cognome, numero di telefono ed e-mail
            del candidato e riportali all'inizio della risposta.
            Se uno di questi dati non e' presente scrivi "non indicato", non inventarlo.
            Argomenta la scelta utilizzando il contenuto del testo individuato nel contesto.
            Se non trovi corrispondenza in nessun cv non inventare.
        """