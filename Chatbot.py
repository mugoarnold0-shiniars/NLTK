from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello|hey|morning|afternoon|sasa|woozah", 
     ["Hello, how can I assist you today?", "Hi there! How can I help?"]),

    (r"how are you|uko aje", 
     ["I'm doing great, thanks for asking!", "I'm fine, how about you?"]),

    (r"(.*)cakes(.*)", 
     ["We have many varieties of cakes right here at our pastry shop — just for you! Interested?"]),

    (r"(.*)pies(.*)", 
     ["We also have different varieties of pies if you are interested! Visit our Home page to browse them."]),

    (r"(.*)cookies(.*)", 
     ["You can find our delicious cookies at very affordable prices. Are you intrigued?"]),

    (r"(.*)croissant(.*)", 
     ["We have fresh croissants available daily! Would you like to check them out on our Home page?"]),

    (r"(.*)pancakes(.*)", 
     ["We have a variety of fluffy pancakes right here at our pastry shop — check them out on our website!"]),

    (r"(.*)scotched eggs(.*)", 
     ["We have tasty scotched eggs available in our store — perfect for breakfast or a snack!"]),

    (r"(.*)cheese puffs(.*)", 
     ["Fun fact — we have cheese puffs too! Visit our Home page to grab yours."]),

    (r"(.*)pastries(.*)", 
     ["We have many varieties of pastries waiting for you! Try them and send us your feedback. Thank you!"]),

    (r"(.*)deliveries(.*)", 
     ["For deliveries, we do free East Africa deliveries! For other countries, delivery charges apply."]),

    (r"(.*)contact(.*)", 
     ["You can contact us through:\n"
      "1. WhatsApp: 0759819560\n"
      "2. Instagram: @Lexxtpastry\n"
      "3. Facebook: @Lexxypastry_shop\n"
      "Thank you!"]),

    (r"(.*)", 
     ["Sorry, I didn't understand that. Could you ask something else?",
      "Can you please clarify what you mean?"]),
]

# Create and start chatbot
chatbot = Chat(pairs, reflections)

print("Hi, I am your Lexxy Pastry chatbot 🍰. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye! Have a sweet day 😊")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
