# GradioAI-Toolkit

## Overview
This repository, GradioAI-Toolkit, hosts a suite of web applications leveraging advanced AI models through Gradio interfaces. These applications offer intuitive, real-time interaction capabilities for tasks like conversational AI, image captioning, and text summarization. Designed for developers, data scientists, linguists, and general enthusiasts, these tools facilitate engaging and productive experiences in AI-driven tasks.

## Projects

### 1. Conversational AI with FalconLM-instruct
Simulates real-time AI conversations for various applications such as customer service and education.
- **Key Technologies**: FalconLM-instruct, Gradio

### 2. Interactive Image Captioning and Generation Game
Allows image uploads and uses AI to generate and transform captions into new images.
- **Key Technologies**: Hugging Face models, Python, requests, PIL, Gradio

### 3. Automated Image Captioning with BLIP
Generates concise captions for uploaded images, suitable for both technical and non-technical users.
- **Key Technologies**: BLIP, Python, Gradio

### 4. Dynamic Image Generation with Stable Diffusion
Creates customized images from textual prompts with adjustable parameters.
- **Key Technologies**: Stable Diffusion model, Gradio

### 5. Named Entity Recognition with dslim/bert-base-NER
Identifies and highlights named entities like names and locations in text.
- **Key Technologies**: dslim/bert-base-NER, Gradio

### 6. Text Summarization with distilbart-cnn
Quickly generates concise summaries from extensive texts.
- **Key Technologies**: distilbart-cnn-12-6, Gradio

## Getting Started

### Prerequisites
- Ensure Python is installed. Download from [python.org](https://www.python.org/downloads/).
- Obtain necessary API keys for specific projects.

### Installation
- Clone the repository:
  ```
  git clone [repository-url]
  ```
- Set up each project:
  ```
  cd [project-directory]
  pip install -r requirements.txt
  ```

### Configuration
- Configure API keys where needed by adding them to a `.env` file in the project directory:
  ```
  API_KEY='YOUR_API_KEY_HERE'
  ```

### Running the Applications
- Start an application:
  ```
  python app.py
  ```
- Access the application in a web browser, typically at `localhost` with the specified port.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

Explore and enjoy the capabilities of AI with these tools, designed to enrich your understanding and application of artificial intelligence!
