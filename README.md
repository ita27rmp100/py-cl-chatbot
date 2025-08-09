# py-cl-chatbot

`py-cl-chatbot` is a Python command-line chatbot application that allows you to interact with the Groq API (LLaMA 3.3-70B model) while keeping a history of your chats stored locally in an SQLite3 database.

## Features

- **Create new chats** and store them locally.
- **Continue old chats** with preserved conversation history.
- **List all saved chats** for easy access.
- **Delete previous chats** from the database.
- **Interactive CLI interface** with colored text for better user experience.

## Requirements

Install dependencies using pip:

```bash
pip install groq termcolor python-dotenv
```

Python 3.7+ is recommended.

## Environment Variables

Create a `.env` file in the root directory with the following content:

```env
groq_api=YOUR_GROQ_API_KEY
```

## How to Use

Run the script:

```bash
python chatbot.py
```

You will be presented with an interactive menu:

```
--------------------------------------------------
Please choose one of the following options:
    -> Close the script : press 0
    -> Start a new chat: press 1
    -> Open an old chat: press 2
    -> Display the list of chats: press 3
    -> Delete a previous chat: press 4
```

### Commands Inside a Chat

- Type your message and press `Enter` to send it.
- Type `$exit$` to end the current chat session.

## Project Structure

```
chatbot.py       # Main script
chatbot.db       # SQLite database (auto-created on first run)
.env             # Stores the Groq API key
```

## Example

```text
# py-cl-chabot -> bot : Hello, how can I assist you today? 
# py-cl-chabot -> you : Hello bot!
# py-cl-chabot -> bot : Hi there! How's your day going?
```

## License

This project is licensed under the MIT License.