from chatbot.nlp import get_response
#from tts.voice_engine import speak_text
#from animation.character import animate_avatar

def main():
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Waifu:", response)
        #speak_text(response)
        #animate_avatar(response)

if __name__ == "__main__":
    main()
