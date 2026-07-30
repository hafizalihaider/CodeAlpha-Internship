<<<<<<< HEAD
"""
==============================================================================
CodeAlpha Internship

Project-4 : Basic Chatbot

Author            : Muhammad Ali Haider
Date              : July 31, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
A simple rule-based chatbot that interacts with users using predefined
responses. The chatbot accepts user input, responds to common greetings
and questions, and exits when the user types "bye" or "goodbye".

Concepts Used:
- Functions
- Loops
- Conditional Statements
- User Input / Output
- String Methods
- any() Function

Modules Used:
- None
==============================================================================
"""


# Display welcome banner
print("=" * 70)
print(f"{'Welcome to Basic Chatbot':^70}")
print("=" * 70)

print("\nType 'bye' anytime to exit.\n")


# Chatbot function
def chatbot(user):

    # Greetings
    if any(word in user for word in ["hi", "hello", "hey"]):
        print("Bot: Hello! How can I assist you today?")

    # Ask about chatbot's condition
    elif "how are you" in user:
        print("Bot: I'm fine. How are you? How can I assist you today?")

    # Chatbot introduction
    elif "what is your name" in user:
        print("Bot: I'm a simple Python chatbot.")

    # Creator information
    elif "who made you" in user:
        print("Bot: I was created by Muhammad Ali Haider.")

    # Chatbot capabilities
    elif "what can you do" in user:
        print("Bot: I can answer simple predefined questions.")

    # Thank you response
    elif "thank you" in user:
        print("Bot: You're welcome!")

    # Exit chatbot
    elif any(word in user for word in ["bye", "goodbye"]):
        print("Bot: Goodbye! Thank you for using Basic Chatbot.")
        exit()

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")


# Main chatbot loop
while True:

    print()

    # Read user input
    user = input("You: ").lower()

    # Process user message
=======
"""
==============================================================================
CodeAlpha Internship

Project-4 : Basic Chatbot

Author            : Muhammad Ali Haider
Date              : July 31, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
A simple rule-based chatbot that interacts with users using predefined
responses. The chatbot accepts user input, responds to common greetings
and questions, and exits when the user types "bye" or "goodbye".

Concepts Used:
- Functions
- Loops
- Conditional Statements
- User Input / Output
- String Methods
- any() Function

Modules Used:
- None
==============================================================================
"""


# Display welcome banner
print("=" * 70)
print(f"{'Welcome to Basic Chatbot':^70}")
print("=" * 70)

print("\nType 'bye' anytime to exit.\n")


# Chatbot function
def chatbot(user):

    # Greetings
    if any(word in user for word in ["hi", "hello", "hey"]):
        print("Bot: Hello! How can I assist you today?")

    # Ask about chatbot's condition
    elif "how are you" in user:
        print("Bot: I'm fine. How are you? How can I assist you today?")

    # Chatbot introduction
    elif "what is your name" in user:
        print("Bot: I'm a simple Python chatbot.")

    # Creator information
    elif "who made you" in user:
        print("Bot: I was created by Muhammad Ali Haider.")

    # Chatbot capabilities
    elif "what can you do" in user:
        print("Bot: I can answer simple predefined questions.")

    # Thank you response
    elif "thank you" in user:
        print("Bot: You're welcome!")

    # Exit chatbot
    elif any(word in user for word in ["bye", "goodbye"]):
        print("Bot: Goodbye! Thank you for using Basic Chatbot.")
        exit()

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")


# Main chatbot loop
while True:

    print()

    # Read user input
    user = input("You: ").lower()

    # Process user message
>>>>>>> aefc2f7c5a0c4a6c555f06b1b9115337647c29a6
    chatbot(user)