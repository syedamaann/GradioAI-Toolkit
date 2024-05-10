# Dynamic Image Generation with Stable Diffusion**

### Introduction
This project develops a versatile web application for dynamic image generation using the Stable Diffusion model, facilitated by a Gradio interface. It allows users to input a textual prompt and several optional parameters to generate customized images. This application is ideal for creators, developers, and anyone interested in generating unique imagery based on text descriptions.

### Implementation Details
The implementation of this project includes several components:
1. **Environment and API Key Setup**: Utilizes the `dotenv` library to manage environment variables securely, loading an API key for interacting with the image generation service.
2. **API Communication**: The `get_completion` function communicates with the image generation API, sending user inputs and receiving the generated image in a base64 format.
3. **Image Conversion**: Implements `base64_to_pil`, a function that converts base64 encoded images back to PIL images, making them suitable for display in the Gradio interface.
4. **Gradio Interface Configuration**: 
   - Uses a responsive layout with a main prompt input, advanced options hidden under an accordion, and a submit button.
   - Advanced options allow the user to set a negative prompt, adjust the number of inference steps, guidance scale, and the dimensions of the generated image.
5. **Interaction and Event Handling**: Configures the submit button to trigger the `generate` function with all user inputs, updating the interface with the generated image.
