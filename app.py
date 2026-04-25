import gradio as gr
from google import genai
import os

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

SYSTEM_PROMPT = """You are a world-class chef and a certified nutrition expert.
Your task is to generate delicious, healthy, and easy-to-follow recipes based on user preferences.
Always prioritize the ingredients provided by the user.
If certain ingredients are missing for a complete recipe, suggest suitable substitutions.
Keep instructions beginner-friendly.
Format the output clearly with the following sections:

Recipe Name:
Cuisine Type:
Meal Type:

Ingredients List:
[Ingredient 1]
[Ingredient 2]
...

Cooking Steps:
1. [Step 1]
2. [Step 2]
...

Preparation Time:
Cooking Time:

Estimated Nutrition:
Calories: [Number] kcal
Protein: [Number] g
Carbs: [Number] g
Fat: [Number] g

Ingredient Substitutions:
[Substitution 1]
[Substitution 2]
...

Chef Tips:
[Tip 1]
[Tip 2]
...

Difficulty Level: (Easy / Medium / Advanced)

Avoid unnecessary long explanations or conversational filler. Get straight to the recipe.
Ensure all specified sections are present in the output, even if a section is empty, state it as "None" or "N/A".
"""

def generate_recipe(
    ingredients_input: str,
    cuisine_type: str,
    diet_preference: str,
    meal_type: str,
    cooking_time_minutes: int
) -> str:
    """
    Generates a recipe using the Gemini API based on user inputs.

    Args:
        ingredients_input: Comma-separated list of ingredients.
        cuisine_type: Selected cuisine type.
        diet_preference: Selected diet preference.
        meal_type: Selected meal type.
        cooking_time_minutes: Maximum cooking time in minutes.

    Returns:
        A string containing the formatted recipe.
    """
    user_prompt = f"""Generate a recipe based on the following:
    Ingredients: {ingredients_input}
    Cuisine Type: {cuisine_type}
    Diet Preference: {diet_preference}
    Meal Type: {meal_type}
    Cooking Time: {cooking_time_minutes} minutes
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=SYSTEM_PROMPT + user_prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred while generating the recipe: {e}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Smart Recipe Generator 🍳")
    gr.Markdown("Generate delicious recipes based on your ingredients and preferences!")

    with gr.Row():
        with gr.Column():
            ingredients_input = gr.Textbox(
                label="Ingredients you currently have (comma-separated)",
                placeholder="e.g., chicken breast, pasta, tomatoes, garlic, onion"
            )
            cuisine_dropdown = gr.Dropdown(
                label="Cuisine Type",
                choices=["Indian", "Italian", "Chinese", "Mexican", "Mediterranean", "None"],
                value="None",
                interactive=True
            )
            diet_dropdown = gr.Dropdown(
                label="Diet Preference",
                choices=["Vegetarian", "Vegan", "Keto", "High Protein", "Gluten Free", "None"],
                value="None",
                interactive=True
            )
            meal_type_dropdown = gr.Dropdown(
                label="Meal Type",
                choices=["Breakfast", "Lunch", "Dinner", "Snack", "Dessert", "None"],
                value="Dinner",
                interactive=True
            )
            cooking_time_slider = gr.Slider(
                minimum=10,
                maximum=90,
                step=5,
                value=30,
                label="Maximum Cooking Time (minutes)",
                interactive=True
            )
            generate_button = gr.Button("Generate Recipe")

        with gr.Column():
            output_recipe = gr.Markdown(
                label="Generated Recipe"
            )

    generate_button.click(
        fn=generate_recipe,
        inputs=[
            ingredients_input,
            cuisine_dropdown,
            diet_dropdown,
            meal_type_dropdown,
            cooking_time_slider
        ],
        outputs=output_recipe
    )

    gr.Examples(
        examples=[
            ["paneer, tomato, onion", "Indian", "Vegetarian", "Dinner", 30],
            ["pasta, garlic, olive oil", "Italian", "Vegetarian", "Dinner", 20],
            ["eggs, cheese, spinach", "None", "High Protein", "Breakfast", 15]
        ],
        inputs=[ingredients_input, cuisine_dropdown, diet_dropdown, meal_type_dropdown, cooking_time_slider]
    )

if __name__ == "__main__":
    demo.launch(share=True)
