# ist-alles-in-ordnung

![hackathon banner](pictures/hackathon-banner.png?raw=true "hackathon banner")
This project is one of the projects in [voice and traveling hackathon](https://www.workstreams.ai/voice-travel-google-hackathon-berlin-september-27-28.html).

Have you traveled to a place without knowing how to speak the local language, and suddenly you saw something unusual. You don't know if you should stay or run away?

Our goal is helping travelers when they travel to a country they have never visited and don't know how to speak the local language. When there is an emergency situation, talk to your google assistant. We will provide you the **realtime local news in your mother language** so that you will know if you are safe right now.

## team members
```
Mia Chang, Data Scientist
Muhammad Samir, Experience Design Lead 
Samuel Tseng, Data Scientist
```

## app name
I am safe

## logo
![Team Logo](pictures/team-logo.png?raw=true "Team Logo")

## tech stack
- google dialogflow 
- python flask 
- twitter developer API
- azure web app

## google voice assistant workflow
![google voice assistant workflow](pictures/voice-assistant-workflow.png?raw=true "voice assistant workflow")

We modified the workflow from [Google Dialogflow Fulfillment Documentation](https://cloud.google.com/dialogflow/docs/fulfillment-overview) as above image.

1. the user triggers our application
2. google dialogflow does intent matching, receive a `real-time news check of my current location` request from the user
3. with the location information from the user, use fulfillment calls the flask app
4. flask app talks to twitter developer API, fetching the latest trending hashtag and news from the given city.
5. send the twitters back to the callback
6. dialogflow send our message to the user
7. user will receive `Based on your location, everything is safe and here are some tweets and news...`

## demo site
https://ist-alles-in-ordnung.azurewebsites.net

```
https://ist-alles-in-ordnung.azurewebsites.net/test
shows what's the latest trend hashtag in Berlin city
```

## demo youtube videos

source: from Workstreams.ai

[![I am safe demo from Workstreams.ai](https://img.youtube.com/vi/pcPcLv_Jd9w/0.jpg)](https://www.youtube.com/watch?v=pcPcLv_Jd9w)

source: from Samuel Tseng

[![I am safe demo from Samuel Tseng](https://img.youtube.com/vi/QFmGyPBsgXc/0.jpg)](https://www.youtube.com/watch?v=QFmGyPBsgXc)