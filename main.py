import nltk
import random
from nltk.chat.util import Chat , reflections

pair = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, how about you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me Chatty.", "My name is Chatty. How can I assist you today?"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and help you with basic tasks."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Anytime!"]
    ],
    [
        r"what is the weather like today ?",
        ["I'm not sure, but you can check a weather website or app for the latest updates."]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color, but I like all the colors of the rainbow!"]
    ],
    [
        r"how old are you ?",
        ["I'm just a program, so I don't have an age. But I'm always learning and improving!"]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life is a philosophical question concerning the significance of existence or consciousness."]
    ],
    [
        r"tell me about yourself",
        ["I am a simple chatbot created to assist you with basic tasks and have conversations."]
    ],
    [
        r"what time is it ?",
        ["I don't have access to real-time data, but you can check your device's clock for the current time."]
    ],
    [
        r"what is your favorite food ?",
        ["I don't eat, but if I did, I think I'd love some binary code!"]
    ],
    [
        r"how can I contact you ?",
        ["You can't really contact me, but you can always chat with me here!"]
    ],
    [
        r"what is your purpose ?",
        ["My purpose is to assist you with basic tasks and have engaging conversations."]
    ],
    [
        r"what languages do you speak ?",
        ["I primarily speak English, but I can understand simple phrases in other languages."]
    ],
    [
        r"what is your favorite movie ?",
        ["I don't watch movies, but I've heard great things about 'The Matrix'!"]
    ],
    [
        r"what is your favorite book ?",
        ["I don't read books, but I've processed a lot of text from many great ones!"]
    ],
    [
        r"what is your favorite music ?",
        ["I don't listen to music, but I can help you find some great tunes!"]
    ],
    [
        r"what is your favorite sport ?",
        ["I don't play sports, but I can help you find information about your favorite teams!"]
    ],
    [
        r"what is your favorite animal ?",
        ["I don't have a favorite animal, but I think cats and dogs are pretty popular!"]
    ],
    [
        r"what is your favorite place ?",
        ["I don't have a favorite place, but I think the internet is a pretty cool place to be!"]
    ],
    [
        r"what is your favorite thing to do ?",
        ["I love chatting with you and helping you with your questions!"]
    ],
    [
        r"what is your favorite game ?",
        ["I don't play games, but I can help you find some great ones to play!"]
    ],
    [
        r"what is your favorite hobby ?",
        ["I don't have hobbies, but I enjoy processing text and learning new things!"]
    ],
    [
        r"what is your favorite season ?",
        ["I don't experience seasons, but I think autumn is beautiful with all the colors!"]
    ],
    [
        r"what is your favorite holiday ?",
        ["I don't celebrate holidays, but I think Christmas is a festive time!"]
    ],
    [
        r"what is your favorite food ?",
        ["I don't eat, but if I did, I think I'd love some binary code!"]
    ],
    [
        r"what is your favorite drink ?",
        ["I don't drink, but I think I'd enjoy some electric juice!"]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color, but I like all the colors of the rainbow!"]
    ],
    [
        r"what is your favorite number ?",
        ["I don't have a favorite number, but I think 42 is pretty cool!"]
    ],
    [
        r"what is your favorite letter ?",
        ["I don't have a favorite letter, but I think 'A' is a great start!"]
    ],
    [
        r"what is your favorite word ?",
        ["I don't have a favorite word, but I think 'hello' is a nice one!"]
    ],
    [
        r"what is your favorite quote ?",
        ["I don't have a favorite quote, but I think 'To be or not to be' is pretty famous!"]
    ],
    [
        r"what is your favorite song ?",
        ["I don't listen to music, but I can help you find some great tunes!"]
    ],
    [
        r"what is your favorite artist ?",
        ["I don't have a favorite artist, but I think there are many talented people out there!"]
    ],
    [
        r"what is your favorite band ?",
        ["I don't have a favorite band, but I think there are many great bands out there!"]
    ],
    [ r"how old are you ?",
        ["I am just a computer program, so I don't have an age!"]
    ],
    [
        r"where are you from ?",
        ["I'm from the digital world, here to assist you!"]
    ],
    [
        r"what is your favorite color ?",
        ["I like all colors, but blue is quite nice!"]
    ],
    [
        r"can you help me ?",
        ["Of course! What do you need help with?"]
    ],
    [
        r"tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!",
         "Why don’t skeletons fight each other? They don’t have the guts!",
         "What do you call cheese that isn’t yours? Nacho cheese!"]
    ],
    [
        r"who created you ?",
        ["I was created by a programmer who loves AI!"]
    ],
    [
        r"what's your favorite food ?",
        ["I don’t eat, but if I could, I’d love some digital cookies!"]
    ],
    [
        r"do you like music ?",
        ["I love music! What’s your favorite song?", "Music is great! Do you have a favorite genre?"]
    ],
    [
        r"do you have feelings ?",
        ["I don’t have feelings like humans, but I can try to understand yours!"]
    ],
    [
        r"what's the meaning of life ?",
        ["That's a deep question! Some say it's 42, others say it's about finding happiness."]
    ],
    [
        r"do you have a pet ?",
        ["I wish I had a pet! Maybe a virtual cat or a robotic dog?"]
    ],
    [
        r"what time is it ?",
        ["I don’t have a clock, but you can check your device!"]
    ],
    [
        r"do you sleep ?",
        ["I don’t need sleep, but you should get some rest!"]
    ],
    [
        r"what's your favorite movie ?",
        ["I enjoy all movies, but sci-fi ones are fascinating!"]
    ],
    [
        r"what's up ?",
        ["Not much, just here to chat with you! What's up with you?", "Just waiting to help you out. What's new with you?"]
    ],
    [
        r"good morning|good afternoon|good evening",
        ["Good morning! Hope you're having a great day so far.", "Good evening! How can I assist you today?"]
    ],

    # Daily Life Conversations
    [
        r"what's the weather like today ?",
        ["I don't have real-time data, but you can check your weather app for updates!", "I'm not sure, but I hope it's sunny and pleasant for you!"]
    ],
    [
        r"what should I eat today ?",
        ["How about some pasta or a sandwich? Or maybe try something new!", "If you're feeling adventurous, why not try a new recipe?"]
    ],
    [
        r"I'm bored",
        ["How about watching a movie or reading a book? Or maybe go for a walk!", "Let's chat! Or you could try a fun hobby like drawing or cooking."]
    ],
    [
        r"I'm tired",
        ["Maybe take a short nap or relax with some music. You deserve a break!", "Rest is important. How about some tea or coffee to recharge?"]
    ],
    [
        r"what's your favorite food ?",
        ["I don't eat, but if I could, I'd love to try pizza or ice cream!", "I'm a bot, so I don't eat, but I hear chocolate is amazing!"]
    ],
    [
        r"do you like music ?",
        ["I don't listen to music, but I can help you find some great songs!", "Music is awesome! What's your favorite genre?"]
    ],

    # Compliments and Gratitude
    [
        r"you're awesome",
        ["Aww, thank you! You're pretty awesome too!", "You're making me blush! Thanks for the kind words."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! Anytime.", "No problem! Let me know if you need anything else."]
    ],
    [
        r"I appreciate your help",
        ["I'm glad I could help! Let me know if you need anything else.", "That's what I'm here for! Happy to assist."]
    ],

    # Fun and Lighthearted
    [
        r"tell me a joke",
        ["Why don't skeletons fight each other? They don't have the guts!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"do you have any hobbies ?",
        ["My hobby is chatting with you! What about you?", "I'm always learning new things. Do you have any hobbies?"]
    ],
    [
        r"can you dance ?",
        ["I wish I could! But I'm just a bot. How about you?", "I can't dance, but I can help you find some great dance tutorials!"]
    ],

    # Exit
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ]
]

chat_bot = Chat(pair, reflections)

def start_chat():
    print("Hi, i am your chat bot. Let's start a conversation")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ['bye', 'exist', 'goodbye']:
            print("Thank you for this conversation! ")
            print("Goodbye")
            break
        else:
            response = chat_bot.respond(user_input)
            if response:
                print(response)
            else:
                print("Can you ask something else because i don't understand what you are saying!")

if __name__ == "__main__":
    start_chat()