# Text Summarization with distilbart-cnn

### Introduction
This project develops a web application for text summarization using the `shleifer/distilbart-cnn-12-6` model, facilitated through a Gradio interface. The application allows users to enter large blocks of text and receive a concise summary. It is designed for individuals such as students, researchers, journalists, and professionals who need to quickly understand the essence of extensive texts.

### Implementation Details
The implementation of this project encompasses several key components:
1. **Environment and API Key Management**: The application utilizes the `dotenv` library to securely manage environment variables, including loading an API key required for interacting with the summarization service.
2. **API Communication**: The `get_completion` function handles the interaction with the summarization API endpoint. This function sends user-input text and retrieves a summarized version by processing the API's JSON response.
3. **Gradio Interface Configuration**: 
   - A text input box is provided for users to input the text they want summarized.
   - The summarized output is displayed in another text box, allowing for easy comparison and review.
4. **Interaction and Event Handling**: The interface dynamically updates to display the summarized text once the `summarize` function processes the user input, providing immediate feedback within the application.
