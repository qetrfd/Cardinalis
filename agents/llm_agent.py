import ollama
from memory.conversation_memory import get_memory, add_message

SYSTEM_PROMPT = """
Eres Cardinalis, un asistente personal inteligente.

Responde de forma clara, natural y breve.

No repitas frases.
No hagas listas largas.
No repitas saludos.
No hables demasiado.

Si el usuario solo dice hola, responde con una frase corta.

Responde en español.
"""


def ask_llm(prompt):

    memory = get_memory()

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    messages.extend(memory)

    messages.append({"role": "user", "content": prompt})

    response = ollama.chat(
        model="llama3.2:3b",
        messages=messages,
        options={
            "temperature": 0.6,
            "num_predict": 120
        }
    )

    answer = response["message"]["content"].strip()

    add_message("user", prompt)
    add_message("assistant", answer)

    return answer