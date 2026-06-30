# main.py
from voicebot.stt import listen_text
from voicebot.tts import speak
from voicebot.qa_engine import answer_about_object
from knowledge import get_object_info
from hologram import project_object
from intent import detect_display_command, list_known_objects


def main():
    current_object_id = None
    chat_history = []

    speak("Hello, I am your hologram assistant.")
    speak("How can i help you today.")

    #print("Objects you can display:")
    #print(list_known_objects())

    while True:
        user_text = listen_text()
        if not user_text:
            continue

        if user_text.lower() in ("quit", "exit", "bye"):
            speak("Goodbye.")
            break

        # 1) Is this a display command?
        requested_object = detect_display_command(user_text)
        if requested_object is not None:
            info = get_object_info(requested_object)
            if info is None:
                speak("I don't have that object yet.")
                continue

            current_object_id = requested_object
            chat_history = []  # reset per-object chat

            project_object(current_object_id)
            speak(f"Displaying {info['name']}. {info['short_intro']}")
            speak("You can now ask me questions about this object.")
            continue

        # 2) If no object selected yet
        if current_object_id is None:
            speak("First tell me which object to display.")
            continue

        # 3) Treat as a question about the current object
        answer, chat_history = answer_about_object(current_object_id, chat_history, user_text)
        print("Bot:", answer)
        speak(answer)


if __name__ == "__main__":
    main()
