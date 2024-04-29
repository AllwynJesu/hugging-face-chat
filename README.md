# Conversational Chatbot

This project is a simple implementation of a conversational chatbot using the Transformers library in Python. The chatbot continuously takes user input, processes it with a pre-trained conversational model, and prints the model's response.

## Requirements

- Python
- Pip

## Dependencies

This project uses the following Python libraries:

- Transformers

You can install these dependencies using pip:

```bash
pip install transformers
```

## Usage

To run the chatbot, execute the `src/app.py` script:

```bash
python src/app.py
```

The chatbot will start a loop that continuously asks for user input, processes it, and prints the chatbot's response. The loop continues until the user types "bye".

## Code Overview

The main script `src/app.py` starts by importing the necessary modules from the Transformers library and setting the logging level to error to suppress informational messages.

A conversational pipeline is created using the "facebook/blenderbot-400M-distill" model. This model is a distilled version of Facebook's Blender chatbot and it can be changed to any other model. This simple chatbot can be run locally

