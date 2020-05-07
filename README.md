# Desktop Based Voice Assistant Pi Using Speech Recognition

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
   <img width="580" height="550" src="https://user-images.githubusercontent.com/64901486/81280337-f1c4c780-9075-11ea-97ca-3ca229cd11ae.PNG">
   </p>
   
## Python Libraries: 

1. SpeechRecognition - Library for performing speech recognition, with support for several engines and APIs, online and offline.
    *
	                    Speech recognition engine/API support:
							       * CMU Sphinx (works offline)
									 * Google Speech Recognition
									 * Google Cloud Speech API
									 * Wit.ai
									 * Microsoft Bing Voice Recognition
									 * Houndify API
									 * IBM Speech to Text
									 * Snowboy Hotword Detection (works offline)
                        The SpeechRecognition module requires [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) Module for Microphone input

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

## Troubleshooting:

Some of the pre-defined commands that the pi can understand are:

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

