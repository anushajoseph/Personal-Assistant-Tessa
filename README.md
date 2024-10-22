# ***Personal Assistant Tessa***
<p align="center">
 <img width="600px" src="https://user-images.githubusercontent.com/84260242/134184077-fa68311c-65da-4391-b9e1-c642e8439771.png"/>
</p>
<span style="font-family: 'Lucida Console';">Introducing our all new personal assistant Tessa.....</span>
<p>An intelligent virtual assistant (IVA) or intelligent personal assistant (IPA) is a software agent that can perform tasks or services for an individual based on commands or questions. The term "chatbot" is sometimes used to refer to virtual assistants generally or specifically accessed by online chat. In some cases, online chat programs are exclusively for entertainment purposes. Some virtual assistants are able to interpret human speech and respond via synthesized voices. Users can ask their assistant questions, control home automation devices, and media playback via voice, and manage other basic tasks such as email, to-do lists, and calendars with verbal (spoken?) commands. A similar concept, however with differences, lays under the dialogue systems.</p>

 ***We are very thankful for giving us this opportunity so we could really use our brains on the project. This project helped us to understand some core concepts and workflows on creating a personal assistant using Python. We learned how to take commands and reply to them according to the user's needs. We got to know about several modules in Python which were used for certain needs in the project. Overall it was a great learning experience.***
 
- Input taken: From user
- Output: Voice and action generated based on given data.
<br/>

## Team members:

**1.** [ANUSHA JOSEPH](https://github.com/anushajoseph)<br/>
**2.** [SANDRA ROSA ANTONY](https://github.com/Sandra-Rosa)<br/>
**3.** [SNEHA C SHAJI](https://github.com/sneha2180)

## Link to product walkthrough:
 
https://www.loom.com/share/584e40a0f592426998ef6908241fc1d7
 
## Libraries used:
 
- speech_recognition

- pyttsx3

- pywhatkit

- datetime

- wikipedia

- pyjokes

- requests

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

**4.** Open Terminal and Run 

```shell
$ Tessa.py
```

## How it works:
 
**1.** Imported speech_recognition for recognising the voice of the user.
 
**2.** Imported pyttsx3 for converting text to speech.
 
**3.** Changed male voice to female voice by setting index number to 1 (voices[1]).
 
**4.** Added basic commands in the code.
 
**5.** Got access to Youtube and Google using pywhatkit.
 
**6.** Imported datetime to know the current date or time if asked by the user.
 
**7.** Got access to wikipedia by importing python wikipedia.
 
**8.** Added jokes by importing the library pyjokes.
 
**9.** Imported requests to get json data from URL to give current weather condition of the place asked.
 
**10.** It is all set to run.
 
## Actions performed:
 
 <table>
<tr>
 <td><h5>COMMAND</h5></td>   
 <td><h5>REPLY</h5></td>
</tr>
<tr>
 <td>hi / hello</td>		   
 <td>What can I do for you?</td>		
</tr>
<tr>
 <td>who are you / what can you do</td>		   
 <td>I am Tessa your personal assistant. I am programmed to perform minor tasks like, play songs in youtube, search in google chrome, tell date and time, search in wikipedia, tell current weather in different places and you can ask me to tell a joke too</td>
</tr>
 <tr>
 <td>who made you /<br/> who created you / who discovered you</td>		   
 <td>I was built by Anusha, Sandra and Sneha.</td>
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

<p align="center">
<img src="personalassistant.gif"/>
<br/><br/>
🌟 Star this repository if you find it useful.
</p>
