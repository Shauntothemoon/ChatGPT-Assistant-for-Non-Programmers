import openai

openai.api_key = "Your API Key Here"

def call_gpt_api(role, model, messages):
    chat_response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    message = chat_response.choices[0].message['content'].strip()
    return message

def main():
    # Edit the role descriptions below
    role_descriptions = {
        "1": "You are an assistant who is good at generating ideas. You will break down a topic into several related sub-issues and provide creative insights.",
        "2": "You are an assistant who is good at summarizing. You will remove unimportant adjectives and modifiers from a piece of text, leaving only important information in markdown format, using bullet points, to provide a summary of my inputs.",
        "3": "You are an assistant who is good at asking questions. You will raise possible doubts or questions based on a given content to promote more complete thinking."
    }
    
    messages = [{"role": "system", "content": role_descriptions["1"]}]
    
    while True:
        print("\nSelect a role for GPT:")
        print("1. Creator")
        print("2. Summarizer")
        print("3. Challenger")
        print("4. Quit")

        role = input("Enter the role number (1, 2, 3, or 4): ")

        if role == "4":
            print("Exiting...")
            break

        # Set the role description for the selected role
        messages[0]['content'] = role_descriptions.get(role, role_descriptions["1"])

        print("\nSelect a model:")
        print("1. gpt-3.5-turbo")

        model = input("Enter the model number (1): ")

        model_mapping = {
            "1": "gpt-3.5-turbo",
        }

        if model not in model_mapping:
            print("Invalid model number. Please try again.")
            continue

        model_name = model_mapping[model]

        prompt = input("\nEnter your prompt: ")
        messages.append({"role": "user", "content": prompt})

        response = call_gpt_api(role, model_name, messages)
        messages.append({"role": "assistant", "content": response})
        
        print("\nGenerated response:")
        print(response)

if __name__ == "__main__":
    main()
