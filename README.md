# MPG Tracker-Telegram Bot


This bot was created to be a simple replacement for the notepad you keep in your car.

For a brief introduction to me and this bot, visit <https://youtu.be/1nGnibCOtdc>

Before using or hosting this bot, you should download a telegram client on your computer or phone and log in.



## How to host this bot on windows
***

### To host this bot, there are **four** things you need to do.

- Download the Mpg Tracker folder
- Install python 3.9
- Install python-telegram-bot
- BotFather registration


### Installing python 3.9

1. go to the windows app store
2. search for python 3.9
3. Click `install`
4. Run cmd and verify installation by running python in cmd with `python --version`

### Installing python-telegram-bot

This is likely the easiest part of installation.
Simply open cmd and type `pip install python-telegram-bot --upgrade`.
When finished, close the command prompt.

For more information, you can visit <https://pypi.org/project/python-telegram-bot/>

### Registering a new bot with BotFather

1. Open telegram and navigate to the search bar
2. Type in @BotFather and click to start a new chat. Be sure to choose the official account, noted with a checkmark.
3. In the chats message bar, type `/newbot`.
4. Continue following the directions until finished.
5. After successfull registration, you will need to find the bots API token.
    1. in the chat, type `/mybots`.
    2. choose the bot you just created.
    3. Click API token.
    4. Save the API key somewhere safe. Treat it like a password.
6. Lastly, open the Mpg Tracker folder and navigate to \__pycache__.
6. Open privateVariables with a text editor (such as notepad), and paste the API key inside quotes.

    > API_KEY = "123456789"
   

### After the completion of these steps, you should be able to run the bot.

1. open cmd and navigate to the mpg tracker main folder.
2. type `python main.py`
    - The bot will reamain active as long as the cmd window is open.
    - To stop the bot, simply close the window.


## How to use this bot
***
1. Search for the registered bot name and start a new chat.

    This will be the name you gave to BotFather. It should start with @.
2. Click start and type **/help**
    
    Aditional instructions will be displayed at that point.




## File explination
***

There are **five** files that the average host should be familliar with.

- The README.md, of course
- main.py
    - main is the brain of this bot. It ties the whole project together.
    - If you are familiar with PTB, feel free to add new features to your copy.
- privateVariables.py
    - This is simply a log of important variables for main. 
    - API key goes here.
- SQliteStudio.exe
    This is a third party Sqlite3 manager.
    Ive included this to make database managment easier.  
    It is located under mpg tracker/sqlite3/gui/sqlitestudio
- tracker.db
    This is where all user data is stored.
    It can be loaded into and modified by SQliteStudio or by SQL in the command prompt.


## How it works
***

This bot uses Several programs and packages.
    
- Telegram <https://telegram.org/> 
- Python 3.9.7 <https://www.python.org/>
- Python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot>
- Sqlite3 <https://www.sqlite.org/index.html>
- SQliteStudio <https://sqlitestudio.pl/>


Well, to be quite honest, i couldnt tell you how most of these programs work. Im gratefull to be able to include them, and their information can be found at the links above.

My handiwork is in the files 'main' and 'privateVariables'. 

Main is a relatively simple filter that can recieve and send messages. It Functions as a middleman between the database and telegram/python-telegram-bot. It logs user information  
 and can return it through specific commands.
Each users information is logged along with their user id, and only returned to that same user. Users have the ability to make entires, view entries, make quick calculations  
 based on that data (such as calculating all time gas mileage), and delete entries.

privateVariables is a short list of any variables main needs in order to operate. The API key is stored here, as well as the help commands text. It allows the main file to be less cluttered.

## Considerations
***

Alright. Well then. Here we are. The end. The conclution. XD

Have you ever been in the car and wondered "What is my gas milage?". Maybe you considered grabbing a calculator, but no, that would take too much time.  
Youre late for work after all. Too bad you dont have one of those new cars that log your MPG for you. That would be nice.  
Well, after "been there, done that"ing for several years, I decided to write my own program that does this for me. Piece of cake. Learned to code and solved a personal problem at the same time.  

Initially, I had hoped to make this an android app, but time constraints put me down another path. Rather than Creating something from scratch, i took my own mediocre bot skills and developed a program i can be proud of.  
Now i dont have to worry about pencils, papers, and calculators in my car. With a quick text message at the pump, I can forget about it.  




***
written by **Kaden Hansen**; 11/08/2021