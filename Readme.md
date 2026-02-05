############## RAM BOT ##############

> RAMBOT is an AI Assistant made in Python


## For students.. :

>> This project is very helpful for the students who are learning Python and want to make a project in Python.

>> I prefer Visual Studio Code for the development of the project.

* The steps to run the project are as follows:

1. Open Visual Studio Code
2. Click on the settings icon on the bottom left corner and click on the `Command Palette`
3. Type `Create Virtual Environment` and press Enter
4. Select the folder where you want to create the virtual environment
5. Choose the Python version which you want to use
6. Now `.venv` folder will be created in the folder which you have selected
7. Now open the terminal in Visual Studio Code
8. Type `\.venv\Scripts\activate` and press Enter
9. Now the virtual environment is activated
10. Now you can install the required packages in the virtual environment

>> The project uses my name at some places so you can replace my name with your name

such as `creator = "Manish kumar chaubey"` you can replace `Manish kumar chaubey` with your name




## Features

- [x] Greet
- [x] Time
- [x] Date
- [x] Weather
- [x] News
- [x] Wikipedia
- [x] Youtube
- [x] Google

## Installation

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
pip install wikipedia
pip install requests
pip install beautifulsoup4
pip install pywhatkit
pip install pyautogui
pip install wolframalpha
pip install subprocess
pip install datetime
pip install re
pip install random
```

## Explanation of the project

>> There are 2 files in the project
1. RAMBOT.py
2. Greetings.py

>> RAMBOT.py is the main file which contains the code for the AI Assistant
>> Greetings.py is the file which contains the code for the Greetings

>> There is a class called as `RAMBOT` in the RAMBOT.py file which contains all the functions for the AI Assistant

>> In Greetings.py file, there are 2 dictionaries which contains the Greetings and the Responses and according to the queries the responses are given by the AI Assistant randomly.

>> The engine used for the AI Assistant is `sapi5` which is a built-in voice engine in Windows OS. You can change the engine according to your OS. 

>> Here are some of the engines which you can use according to different OS

1. sapi5 - Windows OS
2. nsss - MacOS
3. espeak - Linux

>> The AI Assistant can perform various tasks like telling the time, date, weather, news, searching on Wikipedia, opening Youtube, Google, etc.

>> Some tasks like playing music, sending emails, etc. are not included in the project but in another version of the project, these tasks will be included.

>> The AI Assistant can also answer the questions which are asked by the user.

>> The AI Assistant can also perform the tasks which are asked by the user like opening any application, etc.


## Usage

```python

import RAMBOT

ram = RAMBOT.RAMBOT()
ram.wishMe()
ram.takeCommand()

```





## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## COPYRIGHT © 2024 Manish kumar chaubey
    
    ```
    All rights reserved by Manish kumar chaubey
    ```
        
        `




