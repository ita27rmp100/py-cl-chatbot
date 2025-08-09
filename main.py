# import neded data
import os , sqlite3
from groq import Groq
from termcolor import colored
from dotenv import load_dotenv
load_dotenv()
# connection & set-up with DB
connection = sqlite3.connect("chatbot.db")
db = connection.cursor()
try :
    db.execute("create table chats (chatname varchar(50))")
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
    name = input(colored(f"{intro} Please, Enter the name of new chat : ",'blue'))
    try :
        db.execute(f"insert into chats() values(?)",(name))
        db.execute(f"create table {name} (you varchar(2048), bot varchar(2048))")
    except :
        print(colored("ERROR, This chat is already exist.","yellow"))
    # chatting
    print(colored(f"{intro} bot : ","red") +" Hello, how can I assist you today? ")
    while True :
        you = input(colored(f"{intro} you : ","green"))
        if you == "$exit$" :
            print(colored(f"{intro} bot : ","red") +" GoodBye hannouni.")
            break
        else :
            bot = request_response(you)
            print(colored(f"{intro} bot : ","red") + bot)
            db.execute(f"insert into {name}(you,bot) values(?,?);",(you,bot))
def OldChat() :
    pass
def ListChats() :
    db.execute("select * from chats")
    data = db.fetchall()
    if not data:
        print(colored("No chats found.", "yellow"))
        return
    chats = ''
    for chat in data :
        chats +=str(chat[0]+'\n')
    print(chats)
def DeleteChat() :
    name = input(colored(f"{intro} Please, Enter the name of chat you want to delete : ",'blue'))
    try :
        db.execute(f"drop table '{name}'")
        db.execute("delete from chats where chatname =?",(name,)) 
        print(colored("Chat was deleted successfully.", "green"))
    except :
        print(colored("ERROR, This chat doesn't exist.","yellow"))
# interact interface with user
print(colored(f"{intro} Welcome to py-cl-chatbot.","blue"))
while True :
    print(
        colored(" Please choose one of the following options:", "blue"),
        """
            -> Close the script : press 0
            -> Start a new chat: press 1
            -> Open an old chat: press 2
            -> Display the list of chats: press 3
            -> Delete a previous chat: press 4
        """)
    select = int(input(colored(f"{intro} Please select the number that represents the service you want: ", "blue")))
    if select == 0 :
        print(colored(f"{intro} Thank you for using py-cl-chatbot, See you next time.", "blue"))
        break
    elif select == 1 :
        NewChat()
    elif select == 2 : 
        OldChat()
    elif select == 3 :
        ListChats()
    elif select == 4 :
        DeleteChat()
    else :
        print(colored(f"{intro} Wrong input, please read the instructions carefully and try again","yellow"))