# Named Entity Recognition with dslim/bert-base-NER

### Introduction
This project introduces a web application for Named Entity Recognition (NER) using the `dslim/bert-base-NER` model, built with Gradio. The application enables users to input text and identifies various entities such as names, locations, and organizations. It is particularly useful for developers, data scientists, and linguists who need to extract structured information from unstructured text data.

### Implementation Details
The implementation involves the following components:
1. **Environment and API Key Management**: Uses the `dotenv` library to securely load environment variables, including an API key for interacting with the NER service.
2. **API Communication**: Utilizes the `get_completion` function to send text to the NER API endpoint and receive identified entities.
3. **Entity Merging**: Implements `merge_tokens`, a function that processes the tokenized output from the API to merge consecutive tokens that belong to the same entity, improving the readability and utility of the output.
4. **Gradio Interface Configuration**: 
   - The interface features a text input box where users can enter the text they want analyzed.
   - The output is a highlighted text display that visually differentiates recognized entities.
5. **Interaction and Event Handling**: Configures the interface to handle user inputs dynamically, using the `ner` function to update the display based on the processed API responses.
