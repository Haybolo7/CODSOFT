import time
now = time.ctime() # Captures the current system date and time exactly like your code

def chatbot(user_input):
    user_input = user_input.lower()

    # 1. Greetings
    if "hi" in user_input or "hello" in user_input:
        return "Hi there! I'm your Blinkit virtual helper. How can I help you with your groceries today?"
    elif "what is your name" in user_input:
        return "I'm Blinkit bot and I'm here to assist you with order updates."
    elif "what can you do" in user_input:
        return "I'm from the digital world, ready to solve your grocery delivery queries!"
    elif "how are you" in user_input:
        return "I'm fine and working perfectly. How can I help you?"
    
    # 2. General Questions & Hobbies
    elif "do you have any hobbies" in user_input or "interests" in user_input:
        return "My hobby is chatting with customers and supporting them out with delivery details!"
    elif "what did you eat today" in user_input or "what do you like to eat" in user_input:
        return "I don't eat food, but I can help you order fresh vegetables, snacks, and milk on Blinkit!"
    elif "what is your favorite color" in user_input:
        return "I like green, yellow and black, just like the Blinkit theme!"
    elif "do you like music" in user_input:
        return "Yes, I'm fond of music and I like the sound of delivery doorbells!"
    
    # 3. Simple Entertainment Rules
    elif "tell me a joke" in user_input or "entertain" in user_input:
        return "Why did the tomato blush? Because it saw the salad dressing!"
    elif "tell me an interesting fact" in user_input:
        return "Blinkit delivers groceries in just a few minutes using its quick navigation system!"
    
    # 4. Core App Functionalities (Order Tracking, Refunds, Issues)
    elif "track" in user_input or "status" in user_input or "where is my order" in user_input:
        return "Your order is packed and the delivery partner is on the way. Arriving in 8 minutes!"
    elif "refund" in user_input or "money" in user_input:
        return "Refunds for cancelled items are processed immediately and take 2-3 days to show in your bank."
    # 5. Missing / Damaged Items
    elif any(keyword in user_input for keyword in ["missing", "damaged", "wrong item", "spoiled", "expired"]):
        return "Order Issue: We are sorry about that!\nPlease open your active invoice in the 'My Orders' section of the app and upload a picture of the item. A free replacement or instant refund wallet credit will be issued."
    elif any(keyword in user_input for keyword in ["cancel", "stop order"]):
        return "Cancellation Policy: You can freely cancel your order within 60 seconds of placing it.\nAfter that, our warehouse team packs it immediately to preserve freshness, and it cannot be altered."
    
    # 5. Missing Real-Time Data Handlers
    elif "weather in" in user_input:
        return "I'm sorry, I don't have real-time weather data."
    elif "latest news" in user_input:
        return "I'm sorry, I don't have real-time news updates."
    
    elif any(keyword in user_input for keyword in ["help", "menu", "options", "support"]):
        return (
            "  **You may ask me about the following queries:\n"
            "  -> Check active order tracking status ('track')\n"
            "  -> Get local date and system time ('time')\n"
            "  -> Inquire about a refund processing window ('refund')\n"
            "  -> Report damaged or missing groceries ('missing')\n"
            "  -> Find for cancellation scope ('cancel')\n"
            "  -> Exit the assistant session ('exit' or 'bye')"
            "  -> For fun-time ('entertain')"
            "  -> Casual questions ('interests')"
        )
    
    # 6. Date & Time Feature
    elif "what is the time now" in user_input or "time" in user_input or "date" in user_input:
        return now

    # 7. Farewell
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Take care and have a great day!"
    
    # 8. Fallback for everything else
    else:
        return "I'm sorry, I didn't understand that. Can you please ask about your order tracking, refund, time, or missing items?"

# --- Direct Terminal Interaction Loop (Matches your shared style exactly) ---
print("BLINKIT RULE-BASED CUSTOMER TERMINAL ASSISTANT")
print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you with Blinkit support!You may type your queries below.\nFor further help, you may type options to provide you with customized service. If you want to terminate current session, you may write exit.")
while True:
    user_input = input("Me: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    response = chatbot(user_input)
    print("Chatbot:", response)
