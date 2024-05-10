# Automated Image Captioning with BLIP

This project introduces a Python-based web application for automated image captioning utilizing the BLIP model. Leveraging Gradio for the web interface, the application allows users to upload images and receive captions that describe the contents of the images succinctly. The application is designed to be user-friendly, accessible, and efficient, catering to both developers and non-technical users who require quick image captioning services.

### Implementation Details
The implementation is structured around several key components:
1. **Environment Setup**: The application uses a `.env` file for environment management, loading necessary variables like the API key for the BLIP service using the `dotenv` library.
2. **API Communication**: A dedicated function `get_completion` handles communication with the BLIP API endpoint. This function constructs the appropriate headers, manages the request, and processes the response.
3. **Image Handling**: The function `image_to_base64_str` converts images from PIL format to a base64 string, preparing them for API submission.
4. **Gradio Interface**: The user interface is created with Gradio. It includes:
   - An image upload field.
   - A textbox for displaying the generated captions.
   - Sample images to demonstrate the model's capabilities.
5. **Server and Interface Launch**: The Gradio interface is configured to run on a specified port with settings appropriate for deployment, including non-flaggable outputs to maintain privacy.
