import os
import io
import IPython.display
from PIL import Image
import base64 
import requests 
requests.adapters.DEFAULT_TIMEOUT = 60

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
hf_api_key = os.environ['HF_API_KEY']

# Helper function
import requests, json
from text_generation import Client

#FalcomLM-instruct endpoint on the text_generation library
client = Client(os.environ['HF_API_FALCOM_BASE'], headers={"Authorization": f"Basic {hf_api_key}"}, timeout=120)


def format_chat_prompt(message, chat_history, instruction):     # Format the chat prompt
    prompt = f"System:{instruction}"                            # Add the system message
    for turn in chat_history:                                   # Add the chat history
        user_message, bot_message = turn                        # Get the user and bot messages
        prompt = f"{prompt}\nUser: {user_message}\nAssistant: {bot_message}"        # Add the user and bot messages
    prompt = f"{prompt}\nUser: {message}\nAssistant:"                               # Add the user message
    return prompt

def respond(message, chat_history, instruction, temperature=0.7):   # Respond to the user message
    prompt = format_chat_prompt(message, chat_history, instruction) # Format the chat prompt
    chat_history = chat_history + [[message, ""]]                   # Add the user message to the chat history
    stream = client.generate_stream(prompt,                         # Generate the response
                                      max_new_tokens=1024,          # Set the maximum number of tokens
                                      stop_sequences=["\nUser:", "<|endoftext|>"],      # Set the stop sequences to not generate the user answer in response 
                                      temperature=temperature)                          # Set the temperature

    acc_text = ""                                                   # Initialize the accumulated text
    #Streaming the tokens
    for idx, response in enumerate(stream):                         # Iterate over the responses
            text_token = response.token.text                        # Get the text token

            if response.details:                                    
                return

            if idx == 0 and text_token.startswith(" "):             # Remove the leading space
                text_token = text_token[1:]                         

            acc_text += text_token                                  # Accumulate the text
            last_turn = list(chat_history.pop(-1))                  
            last_turn[-1] += acc_text                               
            chat_history = chat_history + [last_turn]               # Update the chat history
            yield "", chat_history                                  # Yield the response
            acc_text = ""                                           # Reset the accumulated text
            

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height=240) #just to fit the notebook
    msg = gr.Textbox(label="Prompt")
    with gr.Accordion(label="Advanced options",open=False):
        system = gr.Textbox(label="System message", lines=2, value="A conversation between a user and an LLM-based AI assistant. The assistant gives helpful and honest answers.")
        temperature = gr.Slider(label="temperature", minimum=0.1, maximum=1, value=0.7, step=0.1)
    btn = gr.Button("Submit")
    clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

    btn.click(respond, inputs=[msg, chatbot, system], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot, system], outputs=[msg, chatbot]) #Press enter to submit

gr.close_all()
demo.queue().launch(share=True, server_port=int(os.environ['PORT4']))    

# gr.close_all()
