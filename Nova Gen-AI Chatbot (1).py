#Disclaimer: To run the Nova Gen-AI, you will need to install a gen-AI extension in your IDE’s terminal by typing “pip install google-generativeai” or “pip install google.generativeai”.


import google.generativeai as genai
genai.configure(api_key="AIzaSyDhDu-Vn9nTQndGaRDtVjrh0Vll8CPedto")
print("HI, I'M NOVA!\n")
def chat_with_gemini (user_input):
    model = genai.GenerativeModel ("gemini-pro" )
    response = model.generate_content(user_input)
    return response.text
while True:
    user_input = input("You: ")
    if user_input. lower() in ["quit", "exit", "bye"]:
        print("Chatbot Nova: Goodbye!")
        break
    print("Chatbot Nova:", chat_with_gemini(user_input))