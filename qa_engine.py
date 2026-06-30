# voicebot/qa_engine.py

from groq import Groq
from knowledge import get_object_info

# Groq client will read the GROQ_API_KEY env var
client = Groq()


def make_system_prompt(object_id: str) -> str:
    info = get_object_info(object_id)
    if info is None:
        return "You are a hologram guide, but you don't know what object is displayed."

    return f"""
You are an AI hologram guide in an exhibition.
The hologram is currently displaying: {info['name']}.

Base information:
{info['details']}

Instructions:
- Explain the object like a friendly teacher.
- Use the base information plus your general knowledge.
- Focus on THIS object unless the user clearly asks something else.
- Keep answers short and spoken-friendly (2–4 sentences).
"""


def answer_about_object(object_id: str, chat_history: list, user_text: str):
    """
    chat_history: list of {"role": "user"/"assistant", "content": str}
    returns: (assistant_reply: str, updated_chat_history: list)
    """
    system_prompt = make_system_prompt(object_id)

    messages = [
        {"role": "system", "content": system_prompt},
        *chat_history,
        {"role": "user", "content": user_text},
    ]

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # fast, high-quality Groq model :contentReference[oaicite:3]{index=3}
        messages=messages,
        temperature=0.6,
        max_tokens=300,
    )

    reply = completion.choices[0].message.content.strip()

    # update history
    chat_history.append({"role": "user", "content": user_text})
    chat_history.append({"role": "assistant", "content": reply})

    return reply, chat_history
