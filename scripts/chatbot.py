import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize conversation history
conversation_history = []

bot_name = "R3060"

def get_updated_model():
    current_date = datetime.now().strftime("%Y-%m-%d")

    deprecated_models = {
        "gpt-3.5-turbo-0613": {
            "shutdown_date": "2024-06-13",
            "recommended_replacement": "gpt-3.5-turbo-1106"
        },
        # Add more deprecated models here
    }

    for model, deprecation_info in deprecated_models.items():
        shutdown_date = deprecation_info["shutdown_date"]
        recommended_replacement = deprecation_info["recommended_replacement"]
        if current_date >= shutdown_date:
           # print(f"Returning recommended replacement: {recommended_replacement}")
            return recommended_replacement

    return None

def chat_with_bot():
    print()
    print("\033[1;32;2m-----R3060-----\033[0m")
    print()
    
    # Get the initial model
    model = get_updated_model()

    # Dynamic introduction based on model
    bot_intro = f"Initializing With: {model}"
    print("\033[1m \u001B[32m R3060: ", bot_intro, " \033[0m")

    while True:
        user_input = input("\033[34mYou: \033[0m")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Get updated model
        model = get_updated_model()
        
        if model is None:
            model = "gpt-3.5-turbo-1106"

        # Load data from file
        with open("data/output/output_cleaned.txt", "r") as file:
            example_data = file.read()

        conversation_history.insert(0, {"role": "user", "content": example_data})

        conversation_history.append({"role": "user", "content": user_input})

        try:
            conversation_history.append({"role": "system", "content": f"{bot_name}: Waiting for response..."})
            
            # Generate bot response from OpenAI API
            response = client.chat.completions.create(
                model=model,
                messages=conversation_history  # Include conversation history
            )

            bot_response = response.choices[0].message.content

            # ChatGPT style letter by letter generation
            print()
            print('\033[1m \u001B[32m R3060: ', end=' \033[0m')
            for idx, letter in enumerate(bot_response):
                if letter == '\n':
                    print()
                    print("\033[1;32m R3060:", end=" \033[0;32m")
                else:
                    if idx == 0:
                        print('\033[0;32m', end='')
                    print(letter, end='\033[0;32m', flush=True)
                    time.sleep(0.01)
            print('\033[0m')
            print()

            # Save bot response to convo history
            conversation_history.append({"role": "system", "content": f"{bot_name}: {bot_response}"})

        except Exception as e:
            print("Error:", e)

chat_with_bot()

