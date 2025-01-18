KnowledgeGPT

Overview

KnowledgeGPT is a Flask-based web application that provides users with access to domain-specific GPT models, enabling tailored AI-powered experiences. Users can explore different themes such as GeoGPT, MediGPT, and HassGPT, each designed to address unique knowledge areas.

Features

User-Friendly Interface: Modern, responsive UI with interactive elements for smooth navigation.

Custom GPT Models: Domain-specific configurations for GeoGPT, MediGPT, and HassGPT.

Real-Time Interaction: Input queries and receive AI-generated responses instantly.

Modular Design: Easy to extend and maintain.

Prerequisites

Python 3.8 or higher

Pip package manager

Virtual environment (optional but recommended)

Installation

Clone the repository:

git clone <https://github.com/ShadowGod300/KnowledgeGpt>
cd KnowledgeGpt

Create and activate a virtual environment (optional):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required dependencies:

pip install - flask, torch, transformers

Usage

Start the Flask server:

python app.py

Open your browser and navigate to:

http://127.0.0.1:5000

Select a theme from the homepage to start interacting with the AI models:

GeoGPT: For geography-related queries

MediGPT: For medical and health-related queries

HassGPT: For humanities and social sciences-related queries

Input your query in the text box and press Submit to receive an AI-generated response.

File Structure

app.py: Backend logic using Flask, defining routes and integrating the GPT-2 model.

templates/: HTML templates for different pages:

home.html: Homepage for navigation

index.html: Main landing page for theme selection

medi_gpt.html: Interface for MediGPT

Additional templates can be added for other themes.

static/: (Optional) Directory for storing CSS, JS, and images if needed in future enhancements.

Key Routes

/: Landing page

/geogpt: GeoGPT page

/medigpt: MediGPT page

/hassgpt: HassGPT page

/generate: API endpoint for generating responses using the GPT model

Customization

Changing the Model

To use a different GPT model, update the model_name in app.py:

model_name = "<new-model-name>"

Ensure the new model is compatible with the Hugging Face Transformers library.

Adding New Themes

Create a new HTML template in the templates/ folder.

Add a new route in app.py for the theme.

Customize the GPT behavior by adjusting parameters in the /generate endpoint.

Troubleshooting

Model not loading:
Ensure the transformers library is installed and the model name is correct.

CSS not applying:
Verify all HTML files link to the correct stylesheet or inline styles.

Server not starting:
Check for errors in app.py and ensure all dependencies are installed.

Future Enhancements

Add more specialized GPT themes (e.g., TechGPT, EduGPT).

Integrate authentication for personalized experiences.

Implement caching for frequently asked queries.

Deploy the application to a cloud service like AWS or Heroku.

License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

Happy Exploring with KnowledgeGPT!

