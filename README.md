# Interactive AI Tools with Gradio

## Overview
This repository contains a collection of innovative web applications focusing on AI-powered interactions, all facilitated by Gradio—an open-source framework for building machine learning and data science interfaces. Each project utilizes advanced machine learning models combined with Gradio interfaces to provide user-friendly, dynamic, and real-time functionalities ranging from conversational AI to text summarization. These projects are tailored for various users including developers, data scientists, linguists, and general enthusiasts interested in exploring the capabilities of AI in different domains such as image processing, text analysis, and interactive gaming.

## Projects

### 1. Conversational AI with FalconLM-instruct
- **Description**: A web application that simulates real-time AI conversations using the FalconLM-instruct model. It's ideal for customer service, education, and entertainment, featuring dynamic chat functionality, customizable interface settings, and effective session management.
- **Key Technologies**: FalconLM-instruct, Gradio

### 2. Interactive Image Captioning and Generation Game
- **Description**: This game allows users to upload images and interact with AI to generate and transform captions into new images, using Hugging Face's models. It supports real-time, interactive experiences online.
- **Key Technologies**: Hugging Face models, Python, requests, PIL, Gradio

### 3. Automated Image Captioning with BLIP
- **Description**: A Python-based application for automated image captioning using the BLIP model. It provides concise captions for uploaded images, suitable for both technical and non-technical users.
- **Key Technologies**: BLIP, Python, Gradio

### 4. Dynamic Image Generation with Stable Diffusion
- **Description**: Users can create customized images by entering textual prompts and adjusting optional parameters in a user-friendly Gradio interface.
- **Key Technologies**: Stable Diffusion model, Gradio

### 5. Named Entity Recognition with dslim/bert-base-NER
- **Description**: This application identifies named entities like names, locations, and organizations from user-inputted text, useful for developers, data scientists, and linguists.
- **Key Technologies**: dslim/bert-base-NER, Gradio

### 6. Text Summarization with distilbart-cnn
- **Description**: Enables quick generation of concise summaries from extensive texts, designed for students, researchers, journalists, and professionals.
- **Key Technologies**: distilbart-cnn-12-6, Gradio

## Getting Started

To begin using the interactive AI tools in this repository, follow these streamlined steps:

### Prerequisites
- **Python**: Ensure Python is installed on your system. Download from [python.org](https://www.python.org/downloads/).
- **API Keys**: Obtain necessary API keys for projects that require external service interactions.

### Cloning the Repository
Clone the repository to your local machine using:
```
git clone [repository-url]
```
Replace `[repository-url]` with the actual URL of the repository.

### Setting Up Projects
Navigate to each project's directory and install dependencies:
```
cd [project-directory]
pip install -r requirements.txt
```

### Configuring API Keys
For projects requiring API keys, create a `.env` file in the project directory and add your keys:
```
API_KEY='YOUR_API_KEY_HERE'
```

### Running the Applications
Launch the application using:
```
python app.py
```
Access the application via a web browser, typically at `localhost` with a specified port number.

Follow these steps to set up and start exploring the capabilities of each AI tool in this repo. 

## Contribution
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

We hope you find these applications useful and inspiring as you explore the capabilities of AI in various domains. Enjoy experimenting and learning with the tools here!
