🍳 Smart Recipe Generator

An AI-powered recipe generator that creates personalized recipes based on ingredients, cuisine preference, diet type, and cooking time using Google Gemini LLM.

Built with Python, Gradio, and Gemini API, this application demonstrates how Large Language Models can be used to generate structured and useful content from user inputs.

🚀 Features
Generate recipes using AI (Google Gemini)
Input your available ingredients
Choose Cuisine Type
Select Diet Preference
Choose Meal Type
Limit Cooking Time
AI generates:
Recipe Name
Ingredients List
Cooking Steps
Preparation & Cooking Time
Nutrition Information
Ingredient Substitutions
Chef Tips
Difficulty Level
🧠 Technologies Used
Python
Gradio – Web UI for the application
Google Gemini API – Large Language Model
google-genai SDK
Prompt Engineering
🏗️ Project Architecture
User Input
   ↓
Gradio Web Interface
   ↓
Python Backend (generate_recipe function)
   ↓
Prompt Construction
   ↓
Gemini LLM API
   ↓
Generated Recipe Output
   ↓
Displayed in UI
📂 Project Structure
smart-recipe-generator
│
├── app.py                # Main Gradio application
├── requirements.txt      # Python dependencies
├── project_llm.ipynb     # Development notebook
└── README.md             # Project documentation
⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/smart-recipe-generator.git
cd smart-recipe-generator

Install dependencies:

pip install -r requirements.txt
🔑 Setup Environment Variable

Create an environment variable for your Gemini API Key.

Example (Linux/Mac):

export GOOGLE_API_KEY="your_api_key_here"

Example (Windows):

set GOOGLE_API_KEY=your_api_key_here

You can get your API key from:

https://aistudio.google.com/app/apikey

▶️ Run the Application

Start the app:

python app.py

The Gradio interface will launch in your browser.

🖥️ Example Usage

Input:

Ingredients: paneer, tomato, onion
Cuisine: Indian
Diet: Vegetarian
Meal Type: Dinner
Cooking Time: 30 minutes

Output:

Recipe Name: Paneer Masala

Ingredients:
- Paneer
- Tomatoes
- Onion
- Spices

Cooking Steps:
1. Heat oil in a pan
2. Add onions and sauté
3. Add tomatoes and spices
4. Add paneer cubes
5. Cook until done
🎯 Learning Objectives

This project demonstrates:

LLM Application Development
Prompt Engineering
AI-Powered Content Generation
Building Interactive AI Interfaces
Integrating APIs with Web Apps
