Documentation for the C-3PO Project
Description
The C-3PO project is a chatbot that can respond to queries using both text and voice. The bot can learn new information from the user and store it for future use.

Functions
play_sound(filename):

Description: Plays a sound file.
Parameters: filename - path to the sound file.
Returns: None.
search_online(query):

Description: Searches for answers online using Google.
Parameters: query - the query to search for.
Returns: Text content of the first found page or an error message.
load_info():

Description: Loads saved information from the info.json file.
Parameters: None.
Returns: Dictionary with information.
save_info(info):

Description: Saves information to the info.json file.
Parameters: info - dictionary with information to save.
Returns: None.
normalize_query(query):

Description: Normalizes the query to lowercase and removes spaces.
Parameters: query - the query to normalize.
Returns: Normalized query.
get_voice_input():

Description: Gets input from the user via the microphone.
Parameters: None.
Returns: Text input from the user or None on error.
respond(query, info):

Description: Responds to a query and optionally learns new information.
Parameters:
query - the query from the user.
info - dictionary with stored information.
Returns: None.
main():

Description: Main loop for interacting with the user.
Parameters: None.
Returns: None.
Commands
hello, hi, good morning:

Description: Greets the user.
Sound: hello.mp3
Response: "Hello! How can I assist you today?"
bye, goodbye:

Description: Says goodbye to the user.
Sound: bye.mp3
Response: "Goodbye!"
what is your name, whats your name, who are you:

Description: Provides information about itself.
Sound: name.mp3
Response: "I'm C-3PO, human-cyborg relations."
do you know [topic]:

Description: Checks if C-3PO knows about the topic, and if not, asks for new information.
Sounds: yes_know.mp3, no_dont_know.mp3, thank_you.mp3
Response: "Yes, I know about [topic]." or "No, I don't know about [topic]. Can you tell me about it?" and "Thank you! I've learned about [topic]."
who is [topic], what is [topic]:

Description: Provides information about the topic if known, or searches online for the answer.
Response: Information about the topic or the result of the online search.
