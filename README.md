# Desktop Based Voice Assistant Pi Using Speech Recognition

**Pi** is a Desktop based Personal Voice-Assistant and devloped using python 3.5+ version.

It works on the principle of **speech reccognition** i.e., it takes human speech as input and converts the speech-to-text using the **Google API** and can further communicate with the user, based on the command (speech) recieved. Upon recieving the command the **pi** executes the python block associated with the keyword in command. To *speak* or *communicate* back with the user it has to convert text-to-speech which is done with the help of **Microsoft Speech API** (SAPI).

Some of the Tasks that the Pi can perform are:

1. Greeting the user upon start-up
2. Bithday notifier
3. Reminder notifier
4. Water reminder notification
5. Tells current day's date and day
6. Gives weather updates
7. Tells any random joke
8. Open's any desired website/URL
9. Gives latest news feed
10. tells about anything from wikipedia
11. carry outs a search request using googlesearch
12. Tells the possible meanings of the word or phrase
13. Gives the latest updates on coronavirus in India/World (or any other specific country )
14. Suggests some of the most read books in the current week (source: Goodreads)
15. Launches any application
16. Calculates any simple mathematical expression
17. Answers basic general questions
18. Suggests some of the top movies to watch (source: IMDB)

***
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

***
## Requirements:

1. Desktop (Windows OS)
2. Python version supported: 3.5+
3. Microsoft Speech API [[SAPI](https://www.microsoft.com/en-in/download/details.aspx?id=27226)]

## Scheduling Python Script on Start-Up

To Automate the Voice-Assistant Pi on start-up, we need to schedule the python script to run when the system starts using the following steps:
1. Create a Batch File

...Open a New Text Document
...and add the python.exe path and the python script path to it as shown below:
... 
