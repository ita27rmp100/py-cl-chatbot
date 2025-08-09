# import neded data
import os , sqlite3
from groq import Groq
from termcolor import colored
from dotenv import load_dotenv
load_dotenv()
# connection & set-up with DB
connection = sqlite3.connect("histrory.db")
db = connection.cursor()
try :
    db.execute("create table chats (chatname varchar(200))")
except :
    pass

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
# options' functions
def NewChat() :
    try :
        db.execute("create table history (command varchar(200))")
    except :
        pass
    # chatting
    print(colored(f"{intro} bot : ","red") +" Hello, how can I assist you today? ")
    while True :
        you = input(colored(f"{intro} you : ","green"))
        if you == "$exit$" :
            print(colored(f"{intro} bot : ","red") +" GoodBye hannouni? ")
            break
        else :
            print(colored(f"{intro} bot : ","red") + request_response(you))
            
# interact interface with user
print(colored(f"{intro} Welcome to py-cl-chatbot. Please choose one of the following options:", "blue"))
print("""
-> Start a new chat: press 1
-> Open an old chat: press 2
-> Display the list of chats: press 3
-> Delete a previous chat: press 4
""")
select = input(colored(f"{intro} Please select the number that represents the service you want: ", "blue"))

