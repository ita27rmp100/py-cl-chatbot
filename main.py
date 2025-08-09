# import neded data
import os , ast
from groq import Groq
from termcolor import colored
from dotenv import load_dotenv
load_dotenv()
# vars 
intro = "# py-cl-chabot -> "
# Generate a request
def request_response(prompt, max_tokens=4096, temperature=0.7):
    client = Groq(
        api_key=os.getenv('groq_api'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    return chat_completion.choices[0].message.content
# interact interface with user
print(colored(f"{intro} bot : ","red") +" Hello, how can I assist you today? ")
while True :
    you = input(colored(f"{intro} you : ","green"))
    if you == "$exit$" :
        print(colored(f"{intro} bot : ","red") +" GoodBye hannouni? ")
        break
    else :
        print(colored(f"{intro} bot : ","red") + request_response(you))