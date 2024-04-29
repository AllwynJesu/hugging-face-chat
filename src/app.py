# Import the necessary modules from the Transformers library
from transformers import pipeline, Conversation
from transformers.utils import logging

# Set the logging level to error to suppress informational messages
logging.set_verbosity_error()

# Create a conversational pipeline using the "facebook/blenderbot-400M-distill" model
# This model is a distilled version of Facebook's Blender chatbot, this can be changed to any other model
chatbot = pipeline(task="conversational", model="facebook/blenderbot-400M-distill")

# Initialize the conversation variable as None
# This variable will later hold the conversation history
conversation = None

# Start a loop that continuously asks for user input, processes it, and prints the chatbot's response
# The loop continues until the user types "bye"
while True:
    # Take the user's input and add newline characters at the beginning and end
    user_message = f"\n{input('User: ')}\n"

    # If the user types "bye", break the loop
    if user_message.strip().lower() == "bye":
        break

    # If it's the first message (i.e., conversation is None), create a new Conversation object
    # Otherwise, add the user's message to the existing conversation
    if conversation is None:
        conversation = Conversation(user_message)
    else:
        conversation.add_message({"role": "user", "content": user_message})

    # Pass the updated conversation object to the chatbot pipeline
    # The pipeline updates the conversation with the model's response
    chatbot(conversation)

    # Print the chatbot's response
    print("Assistant: ", conversation.messages[-1]["content"])
