# import openai
# import json

# # Set up OpenAI API credentials
# openai.api_key = ""

# # Load the dataset
# with open("dataset.json") as file:
#     dataset = json.load(file)

# # Function to generate a response from the chatbot
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

# # Function to train the chatbot
# def train_chatbot():
#     for item in dataset:
#         prompt = item["prompt"]
#         response = item["response"]
#         # Train the model by feeding it the prompt and response
#         generate_response(f"{prompt}\nResponse: {response}\n")

# # Function to interact with the chatbot
# def chat_with_bot():
#     while True:
#         user_input = input("User: ")
#         if user_input.lower() == "quit":
#             break
#         prompt = f"User: {user_input}\nAI:"
#         response = generate_response(prompt)
#         print(f"AI: {response}")

# # Train the chatbot
# train_chatbot()

# # Start the conversation with the chatbot
# print("Chatbot: Hello! How can I assist you today?")
# chat_with_bot()