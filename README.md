# ***Personal Assistant Tessa***
<p align="center">
 <img width="600px" src="https://user-images.githubusercontent.com/84260242/134184077-fa68311c-65da-4391-b9e1-c642e8439771.png" />
</p>
<span style="font-family: 'Lucida Console';">Introducing our all new personal assistant tessa.....</span>
<p>An intelligent virtual assistant (IVA) or intelligent personal assistant (IPA) is a software agent that can perform tasks or services for an individual based on commands or questions. The term "chatbot" is sometimes used to refer to virtual assistants generally or specifically accessed by online chat. In some cases, online chat programs are exclusively for entertainment purposes. Some virtual assistants are able to interpret human speech and respond via synthesized voices. Users can ask their assistants questions, control home automation devices and media playback via voice, and manage other basic tasks such as email, to-do lists, and calendars with verbal (spoken?) commands. A similar concept, however with differences, lays under the dialogue systems.</p>

 ***We are very thankful for giving this oppurtunity so we could really use our brains on this project. This project helped us understand some core concepts and workflows on creating a personal assistant using several modules. We learned how to take commands and reply to those commands accordingly to the user needs. We learned about several modules in python to get certain needs.overall it was a great learning experience.***
 
<div align="center">
</div>
<br />

## Team members:
1. [ANUSHA JOSEPH](https://github.com/anushajoseph)
2. [SANDRA ROSA ANTONY](https://github.com/Sandra-Rosa)
3. [SNEHA C SHAJI](https://github.com/sneha2180)

-Input taken: From user

-Output: Voice and action generated based on given data.

 ## Libraries used:
 
-speech_recognition

-pyttsx3

-pywhatkit

-datetime

-wikipedia

-pyjokes

-requests
 
 ## Link to product walkthrough:
 
 https://www.loom.com/share/0b744d410cba478ebe39ddc107a679d8
 
 ## How to configure:
**1.** Installing pip [Python Package Manager]

```shell
$ sudo apt-get install python3-pip
```

**2.** Clone this repository to your local drive

```shell
$ git clone https://github.com/anushajoseph/SheHacks-Project1-Personalassistant-Tessa
```

**3.** Install dependencies

```shell
$ pip3 install -r requirements.txt
```

**4.** Open Terminal and Run the Flask Server

```shell
$ Tessa.py
```

 ## How it works?
 
 1.Imported speech_recognition for recognising the voice from the user.
 
 2.Imported pyttsx3 for converting text to speech.
 
 3.Changed male voice to female voice without any libraries (voice [1]).
 
 4.Added basic commands in code.
 
 5.Got access to youtube,browser and other platforms using pywhatkit.
 
 6.Imported datetime to know the current time if user asked.
 
 7.Got access to wikipedia by importing python wikipedia.
 
 8.Added jokes to tessa by importing the library pyjoke.
 
 9.Its all set.
 
  ## Actions performed:
 
 <table>
<tr>
 <td><h5>COMMAND</h5></td>   
 <td><h5>REPLY</h5></td>
</tr>
<tr>
 <td>hello</td>		   
 <td>What can I do for you?</td>		
</tr>
<tr>
 <td>who are you / what can you do</td>		   
 <td>I am Tessa your personal assistant. I am programmed to perform minor tasks like, play songs in youtube, search in google chrome, tell date and time, search in wikipedia, tell current weather in different places and you can ask me to tell a joke too</td>
</tr>
<tr>
 <td>play (song)</td>		   
 <td>playing (song)</td>
</tr>
<tr>
 <td>search (topic)</td>		   
 <td>searching (topic)</td>
</tr>
<tr>
 <td>time</td>		   
 <td>Current time is.....</td>
</tr>
<tr>
 <td>date</td>		   
 <td>Today is....</td>
 </tr><tr>
 <td>wikipedia (topic)</td>		   
 <td>(2 lines from the wikipedia page)</td>
 </tr><tr>
 <td>joke</td>		   
 <td>(joke from pyjokes)</td>
 </tr>
 <tr>
 <td>current weather in (place)</td>		   
 <td>(temprature in degree celsius with weather condition)</td>
 </tr>
  <tr>
 <td>bye</td>		   
 <td>Thank you. Assistance accomplished! Huzzah!</td>
 </tr>
</table>


 ![gif](ef0936558e58d6bebf73fee2ae895fe3.gif)
 
 
 <p align="center"> 🌟 Star this repository, if you find it useful.</p>
