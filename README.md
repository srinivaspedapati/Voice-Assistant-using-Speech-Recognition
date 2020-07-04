# Desktop Based Voice Assistant Pi Using Speech Recognition

<p align="center">
<img width="1110" height="300" src="https://user-images.githubusercontent.com/64901486/81291860-35c0c800-9088-11ea-99b6-44d4f7ca4435.png">
</p>


**Pi** is a Desktop based Personal **Voice-Assistant** and devloped using python 3.5+ version.

   It works on the principle of **Speech-Reccognition** i.e., it takes human speech as input and converts the **speech-to-text** using the **Google API** and can further communicate with the user, based on the command (speech) recieved. Upon recieving the command the **Pi** executes the python block associated with the keyword in command. 
   
   To *speak* or *communicate* back with the user it has to convert **text-to-speech** which is done with the help of **Microsoft Speech API** (SAPI).

**Some of the Tasks that the Pi can perform are:**

* Greeting the user upon start-up
* Bithday notifier
* Reminder notifier
* Water reminder notification
* Tells current day's date and day
* Gives weather updates
* Tells any random joke
* Open's any desired website/URL
* Gives latest news feed
* tells about anything from wikipedia
* carry outs a search request using googlesearch
* Tells the possible meanings of the word or phrase
* Gives the latest updates on coronavirus in India/World (or any other specific country )
* Suggests some of the most read books in the current week (source: Goodreads)
* Launches any application
* Calculates any simple mathematical expression
* Answers basic general questions
* Suggests some of the top movies to watch (source: IMDB)


## Requirements:

1. Desktop (Windows OS)
2. Python version supported: 3.5+
3. Microsoft Speech API [[SAPI](https://www.microsoft.com/en-in/download/details.aspx?id=27226)]

## Working:

   <p align="center">
   <img width="580" height="600" src="https://user-images.githubusercontent.com/64901486/81293169-7d485380-908a-11ea-974c-0a7330d74c9d.PNG">
   </p>
   
## Python Libraries: 

1. [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/#files) - Library for performing speech recognition, with support for several engines and APIs, online and offline. The SpeechRecognition module requires [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) Module for Microphone input.

2. **[win32com](https://pypi.org/project/pywin32/)** - This module allows us to easily access Window’s Component Object Model (COM) and control Microsoft applications via python. In this script, we use this module to invoke SAPI.

3. **[win10toast](https://pypi.org/project/win10toast/#files)** - An easy-to-use Python library for displaying Windows 10 Toast Notifications which is useful for Windows GUI development.

4. **[pyowm]()** - PyOWM is a client Python wrapper library for [OpenWeatherMap](https://openweathermap.org/) web APIs. It allows quickly retrieve weather updates and also other data. However, This requires API key to Retrieve data availible at the website 

5. **[newsapi](https://pypi.org/project/newsapi/#files)** - For News Updates from [News API](https://newsapi.org/), The API_key can be obtained from the website.

6. **[wikipedia](https://pypi.org/project/wikipedia/#files)** - Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. Search Wikipedia, get article summaries, get data like links and images from a page, and more. 

7. **[wolframalpha](https://pypi.org/project/wolframalpha/#files)** - This module is a computational knowledge engine or answer engine that answers  our basic mathematical computational querys or general questions. The app_idan obtained from [WolframAlpha](https://www.wolframalpha.com/.

8. **[oxforddictionaries]()** - This is a python wrapper for the [Oxford Dictionary](https://developer.oxforddictionaries.com/) API. The Oxford API offers a free plan with up to 3,000 requests per month with ull access to Oxford Dictionaries data, although we will need to register for an API key availible at the website.

[Installing Wheel Package Guide](https://www.youtube.com/watch?v=MzV4N4XUvYc)

Some of the modules comes pre-installed with python.

## Scheduling Python Script on Start-Up:

To Automate the Voice-Assistant Pi on start-up, we need to schedule the python script to run when the system starts, using following steps:

1. **Create a Batch File**

     Open a Text Document and Add python.exe and python script path to it in the below syntax:
   
   ```
   "python.exe path" "python_script path"
   ```
  
   ![SS1](https://user-images.githubusercontent.com/64901486/81271504-d0f67500-9069-11ea-8586-b040e96daf93.PNG)

     Save the Text Document as batch file using the _.bat_ extension & Double-click the batch file to run it.
  
     <p align="center">
     <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270367-42352880-9068-11ea-83ea-6c90e3cdc407.PNG">
     </p>
  
 2. **Open Task Scheduler**

      Create a Basic Task & Enter the Name and Description of the Task, Click **Next**.
      <p align="center">
      <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270381-46614600-9068-11ea-8b8a-d739792daa87.PNG">
      </p>

      Click **Next**. Select the Task Trigger Time, as **When computer turns on**, Click **Next**.
     <p align="center">
     <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270386-495c3680-9068-11ea-906d-40b6154e3160.png">
     </p>

      Now Select the Action to Perform, as **start a program**, Click **Next**.
     <p align="center">
     <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270389-4a8d6380-9068-11ea-8c3e-b02b1b670a25.png">
     </p>

      Browse the Batch File path and add it and Click **Finish**.
     <p align="center">
     <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270392-4bbe9080-9068-11ea-8e6c-f9a45c0d8c2b.png">
     </p>

     <p align="center">
     <img width="550" height="375" src="https://user-images.githubusercontent.com/64901486/81270385-495c3680-9068-11ea-8f62-41308e640d57.png">
     </p>


## **Some of the pre-defined commands that the Pi can understand are:**

* What _date_ is today?
* How is the _weather_ today?
* Tell me a _joke_
* _Open_ Chrome // command must be preceeded with keyword 'Open'
* _Open_ Word  // command must be preceeded with keyword 'Open'
* Give me some _news_ Updates
* _search_ encyclopedia // command must be preceeded with keyword 'search'
* Tell me the meaning of '___'
* Give me updates on _corona virus_
* suggest me a _book_ to read
* _pi_ what is 2 plus 3? // command must be preceeded with pi
* _pi_ what is cos 0? // command must be preceeded with pi
* _pi_ what is the capital of india? // command must be preceeded with pi
* suggest me _movie_ to _watch_
* pi _shutdown_

## Screenshots:

<p align="center">
<img width="1110" height="550" src="https://user-images.githubusercontent.com/64901486/81290169-3572fd80-9085-11ea-86ea-8d191739e1aa.PNG">
</p>
<p align="center">
<img width="1110" height="550" src="https://user-images.githubusercontent.com/64901486/81290192-428fec80-9085-11ea-90de-1b2d160bf304.PNG">
</p>
<p align="center">
<img width="1110" height="550" src="https://user-images.githubusercontent.com/64901486/81290176-386dee00-9085-11ea-80f2-b30219f0da70.PNG">
</p>
<p align="center">
<img width="1110" height="550" src="https://user-images.githubusercontent.com/64901486/81290181-3ad04800-9085-11ea-9377-65dd6400bce1.PNG">
</p>
<p align="center">
<img width="1110" height="550" src="https://user-images.githubusercontent.com/64901486/81290184-3c017500-9085-11ea-8541-538e554a30ba.PNG">
</p>

## Troubleshoot:

**[[1]. SpeechRecognition](https://pypi.org/project/SpeechRecognition/#troubleshooting)**
