# importing packages
import speech_recognition as sr
import win32com.client as wincl
import os
import sys
import re
import subprocess
import requests
import json
from bs4 import BeautifulSoup
import time
import datetime
from time import strftime
import calendar
import webbrowser
from googlesearch import search
import pyjokes
from pyowm import OWM
import wikipedia
from newsapi import NewsApiClient
from win10toast import ToastNotifier
import wolframalpha
import oxforddictionaries

# Invoking SAPI [Microsoft Speech API]
speak = wincl.Dispatch("SAPI.SpVoice")

# Converts Text-To-Speech; Converts only string value
def PiSays(str):
    try:
        speak.Speak(str)
    except:
        print('Error')

# Greets the User upon start-up with respect to the time of the time
def GreetUser():
    try:
        day_time = int(strftime('%H'))
        if day_time < 12:
            PiSays("Hello Ps, Good morning, Its Good To Have You Back")
            print('Pi :' + ' Hello Ps, Good morning, Its Good To Have You Back')
        elif 12 <= day_time < 18:
            PiSays("Hello Ps, Good afternoon, Its Good To Have You Back")
            print('Pi :' + ' Hello Ps, Good afternoon, Its Good To Have You Back')
        else:
            PiSays("Hello Ps, Good evening, Its Good To Have You Back")
            print('Pi :' + ' Hello Ps, Good evening, Its Good To Have You Back')
    except:
        print("error")
    PiSays(".. I am Pi, Your Personal Voice Assistant ..")
    print('Pi :' + ' I am Pi, Your Personal Voice Assistant')
    PiSays(".. How can I Assist You .. ")
    print('Pi :' + ' How can I Assist You')

# Checks for any birthday event for the current day
def BirthdayNotifier():
    file_read = open(BirthdayFile, 'r') # opens the file read mode
    today = time.strftime('%d%m')
    i = 0
    for line in file_read:
        if today in line:
            line = line.split(' ')
            print("Its " + line[1] + '\'s' + " Birthday Today")
            PiSays("Its " + line[1] + '\'s' + " Birthday Today")
            bday_notification.show_toast("Birthday Notification", "Its " + line[1] + '\'s' + " Birthday Today",duration=4) # Invokes Desktop Notification
            i += 1

    if i == 0:
        time.sleep(2)
        print("No Birthdays Today!")
        PiSays("No Birthday's Today")
        bday_notification.show_toast("Birthday Notification", "No Birthday's Today",duration=4)  # Invokes Desktop Notification

# Checks for any reminder for the cureent day
def ReminderNotifier():
    file_read = open(ReminderFile, 'r') # opens the file read mode
    today = time.strftime('%d%m')
    i = 0
    for line in file_read:
        if today in line:
            line = line.split(' ')
            print("Pi : " + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + ' ' + line [5] + ' ' + line [6])
            PiSays(line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + ' ' + line [5] + ' ' + line [6])
            reminder_notification.show_toast("Reminder", line[1] + ' ' + line[2] + ' ' + line[3] + ' ' +line[4] + ' ' + line [5] + ' ' + line [6], duration=4) # Invokes Desktop Notification
            i += 1
    if i == 0:
        time.sleep(2)
        print("Pi : No Reminders Today!")
        PiSays("No Reminders Today!")
        reminder_notification.show_toast("Reminder", "No Reminders For Today", duration=4)  # Invokes Desktop Notification

# Invoking/Calling GreetUser() Function
GreetUser()

# Calling BirthdayNotifier() Function
BirthdayFile = 'F:\BirthdayFile.txt'  # File Location
bday_notification = ToastNotifier()
PiSays("Let me Check for Any Birthdays Today !")
print("Pi : Let me Check for Any Birthdays Today !")
BirthdayNotifier()

# Calling ReminderNotifier() Function
ReminderFile = 'F:\ReminderFile.txt'  # File Location
reminder_notification = ToastNotifier()
PiSays("Let me Check for Any Reminders Today !")
print("Pi : Let me Check for Any Reminders Today !")
ReminderNotifier()

# Define a Function to Recognize Input Speech
def RecognizeSpeech():
    r = sr.Recognizer() # an instance of speech_recognition; to recognize speech
    with sr.Microphone() as source:
        print('...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 2000
        audio = r.listen(source, phrase_time_limit=5) # listens to the User
    try:
        UserCommand = r.recognize_google(audio).lower()  # Recognizes Listened Speech Using Google Speech API
        print('You said: ' + UserCommand + '\n')
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        UserCommand = RecognizeSpeech(); # If speech unrecognized, the RecognizeSpeech() is Invoked again and again until recognized
    return UserCommand


# Defining a Function of a Set of Predefined tasks Using if..elif Statements
def SelectTask(UserCommand):

    # Water-reminder notification every hour at '00' Minutes
    time_now = time.strftime('%M') # returns only minute value
    if time_now == 0:
        water_notftn = ToastNotifier()
        water_notftn.show_toast("Water Reminder 🥛",duration=4)

    try:
        # 1. Tells the Cureent Day and Date
        if "date" in UserCommand:
            def todays_date(date):
                day, month, year = (int(i) for i in date.split(' '))
                dayNumber = calendar.weekday(year, month, day)
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                return (days[dayNumber])

            day_object = datetime.date.today().strftime("%d %m %y")
            print('Today is ' + todays_date(day_object) + ' And the Date is ' + day_object)
            PiSays(" Today is " + todays_date(day_object) + "And the Date is " + day_object)

        # 2. Opens the Desired Website
        elif "open" in UserCommand:
            website_request = re.search('open (.+)', UserCommand)
            if website_request:
                domain = website_request.group(1)
                print('The Requested Website is  https://www.' + domain + '.com')
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)

            print('The website you have requested has been opened for you.')
            PiSays("The website you have requested has been opened for you.")

        # 3. carry outs a search request using googlesearch
        elif 'search' in UserCommand:
            search_request = re.search('search (.+)', Usercommand)
            if search_request:
                query = search_request.group(1)
                print('Your Search Results are :')
                PiResponse("Your Search Results are :")
                for url in search(query, stop=3):
                    print(url)
                    webbrowser.open(url)

            print("Your Search Request is Completed")
            PiSays("Your Search Request is Completed")

        # 4. Tells any random joke from the pyjokes module
        elif "tell me a joke" in UserCommand:
            joke = pyjokes.get_joke()
            print(joke)
            PiSays(joke)

        # 5. Gives Weather Updates
        elif 'weather' in UserCommand:
            owm = OWM(API_key='39150c1224ea99f8dcc8ccbd7403afd5') # PyOWM API_key
            obs = owm.weather_at_place('Hyderabad,India') # location of required weather updates
            w = obs.get_weather()
            w.get_reference_time(timeformat='iso')
            x = w.get_detailed_status() # returns Atmosphere status
            y = w.get_humidity() # returns humidity
            z = w.get_temperature(unit='celsius') # returns temperatutre

            print('The Atmosphere Has ' + x)
            PiSays('The Atmosphere Has ' + x)
            print('The Maximum Temperature For Today is %d degree celsius and the Minimum Temperature is %d degree celsius' % (z['temp_max'], z['temp_min']))
            PiSays('The Maximum Temperature is %d degree celsius and the Minimum Temperature is %d degree celsius' % (z['temp_max'], z['temp_min']))
            print('And The Humidity Outside is %d percentage.' % (y))
            PiSays('And The Humidity Outside is %d percentage.' % (y))

            if z['temp'] >= 30:
                print('The Weather Outside is Very Hot, I Suggest You Stay Home and Stay Hydrated ')
                PiSays('The Weather Outside is Very Hot, I Suggest You Stay Home')
            elif z['temp'] > 24 and z['temp'] < 30:
                print('The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths and a Hat to avoid Heat')
                PiSays('The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths and a Hat to avoid Heat')
            elif z['temp'] > 16 and z['temp'] <= 24:
                print('The Weather Outside is Warm, I Suggest You Wear Sunglasses and a Hat')
                PiSays('The Weather Outside is Warm, I Suggest You Wear Sunglasses and a Hat')
            elif z['temp'] < 16:
                print('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')
                PiSays('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')

        # 6. Comes up with latest top 5 news headlines from India
        elif 'news' in UserCommand:
            newsapi = NewsApiClient(api_key='d444d79c864946ea9661ac0bd781aa47') # Enter Your API Key from NewsAPI
            top_headlines = newsapi.get_top_headlines(q='India', language='en', )
            for article in top_headlines['articles'][:5]:
                print('Title : ' + article['title'])
                PiSays('Title : ' + article['title'])
                print('Description : ' + article['description'], '\n')
                PiSays('Description : ' + article['description'])

        # 7. Tells the possible meanings of the word or phrase
        elif 'meaning' in UserCommand:
            reg_ex = re.search('Tell me the meaning of (.+)', UserCommand)
            if reg_ex:
                word_id = reg_ex.group(1)

                app_id = '4ea13c64' # app_id from oxforddictionaries
                app_key = 'ee330a18c6d1b84caa707af849421635' #app_key from oxforddictionaries
                language = 'en'
                url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower()
                urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/' + language + '/?corpus=nmc&lemma=' + word_id.lower()
                r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
                name_json = r.json()
                name_list = []
                for name in name_json['results']:
                    name_list.append(name['word'])
                print("You searched for the word : " + word_id)
                PiSays("You searched for the word : " + word_id)
                url_mean = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
                mean_json = r.json()
                mean_list = []
                PiSays("I can Read it out for you")
                for result in mean_json['results']:
                    for lexicalEntry in result['lexicalEntries']:
                        for entry in lexicalEntry['entries']:
                            for sense in entry['senses']:
                                mean_list.append(sense['definitions'][0])
                            for i in mean_list:
                                print(word_id + " : " + i)
                                PiSays(word_id + " : " + i)

        # 8. Gives the latest updates on coronavirus in India using Web-Scraping
        elif 'corona' or 'virus' in UserCommand:
            url = "https://www.worldometers.info/coronavirus/country/india/" # Website URL address used for web-scraping
            req = requests.get(url)
            bsObj = BeautifulSoup(req.text, "html.parser")
            data = bsObj.find_all("div", class_="maincounter-number")
            print('Give me Moment Ps, I am Scraping data for you')
            PiSays("Give me Moment Ps, I am Scraping data for you")
            print("Total Cases: ", data[0].text.strip())
            PiSays("Total Cases: " + data[0].text.strip())
            print("Total Deaths: ", data[1].text.strip())
            PiSays("Total Deaths: " + data[1].text.strip())
            print("Total Recovered: ", data[2].text.strip())
            PiSays("Total Recovered: " + data[2].text.strip())

        # 9. Suggests some of the most read books in the current week (Updates weekly)
        elif "book" or "suggest" in UserCommand:
            url = "https://www.goodreads.com/book/most_read" # Website URL address used for web-scraping
            req = requests.get(url)
            bsObj = BeautifulSoup(req.text, "html.parser")
            book_title = bsObj.find_all(class_="bookTitle")
            author_name = bsObj.find_all(class_="authorName")

            print('Here are the 5 Most Read Books This Week In India : \n')

            print(book_title[0].text.strip() + " by " + author_name[0].text.strip())
            PiSays(book_title[0].text.strip() + " by " + author_name[0].text.strip())
            print(book_title[1].text.strip() + " by " + author_name[1].text.strip())
            PiSays(book_title[1].text.strip() + " by " + author_name[1].text.strip())
            print(book_title[2].text.strip() + " by " + author_name[2].text.strip())
            PiSays(book_title[2].text.strip() + " by " + author_name[2].text.strip())
            print(book_title[3].text.strip() + " by " + author_name[3].text.strip())
            PiSays(book_title[3].text.strip() + " by " + author_name[3].text.strip())
            print(book_title[4].text.strip() + " by " + author_name[4].text.strip())
            PiSays(book_title[4].text.strip() + " by " + author_name[4].text.strip())

        # 10. Launch's any application preceeded with 'launch' in UserCommand
        elif 'launch' in UserCommand:
            launch_application = re.search('launch (.+)', UserCommand)
            application = launch_application.group(1)
            if "chrome" in application: # Launches Google Chrome
                print("Openning Google Chrome")
                PiSays("Openning Google Chrome")
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') # File location
                return
            elif "word" in application: # Launches Microsoft Word
                print("Opening Microsoft Word")
                PiSays("Opening Microsoft Word")
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Word.lnk') # File location
                return
            elif "excel" in application: # Launches Microsoft Word
                print("Opening Microsoft Excel")
                PiSays("Opening Microsoft Excel")
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Excel.lnk') # File location
                return

            elif "vlc" in application: # Launches VLC
                print("Opening VLC Media Player")
                PiSays("Opening VLC Media Player")
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\\VLC media player.lnk') # File location
                return
            else:
                PiSays("Application not available")
                return

        # 11. Calucates simple mathematical expressions (basic calculations like a calculator); preceeded with 'pi' in UserCommand
        # 12. Answers any basic general question; preceeded with 'pi' in UserCommand
        elif "pi" in UserCommand:
            app_id = "5A773V-U2P37TE6VH" # wolframalpha app_id
            client = wolframalpha.Client(app_id)
            indx = UserCommand.lower().split().index('pi')
            query = UserCommand.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            PiSays("The answer is " + answer)
            return

        # 13. Returns some of the top movies to watch from IMDB, using web-scraping
        elif "watch" or "movie" in UserCommand:
            url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm" # Website URL address used for web-scraping
            req = requests.get(url)
            bsObj = BeautifulSoup(req.text, "html.parser")
            data = bsObj.find_all("<a>")
            print('Give me Moment Ps, I am Scraping data for you')
            PiSays("Give me Moment Ps, I am Scraping data for you")
            print("Total Cases: ", data[0].text.strip())
            PiSays("Total Cases: " + data[0].text.strip())
            print("Total Deaths: ", data[1].text.strip())
            PiSays("Total Deaths: " + data[1].text.strip())
            print("Total Recovered: ", data[2].text.strip())
            PiSays("Total Recovered: " + data[2].text.strip())

        # 14. Shut's down Voice Assistant
        elif "shut" or "down" in UserCommand:
            print('Bye Bye Ps, Have a good day')
            PiSays('Bye Bye Ps, Have a good day')
            sys.exit()

    except:
        print('I am Sorry I Could not Find any Match Can You Repeat your UserCommand')
        PiSays("I am Sorry I Could not Understand You, Could You Please Repeat Your UserCommand")


# Calling The SelectTask() Function with RecognizeSpeech() as its argument, Resulting in Infinite loop
while True:
    SelectTask(RecognizeSpeech())
