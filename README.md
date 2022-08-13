# Recapify
An application that will help you summarize your usage of Spotify.

## Summary
This application allows the users to autheniticate their Spotify account using OAuth 2.0 and access its information through authorisation. Through Recapify, the user can access a summary of their Spotify usage. The features working in this first version are:

* User's Top Artists
* User's Most played Songs
* User's Recently Played Songs
* User's Playlists List

## Installation Guide
https://developer.spotify.com/dashboard/login login to Spotify for developers using your Spotify Account, if you don't have a Spotify account you can make one for free at https://www.spotify.com/uk/signup.

<img width="858" alt="image" src="https://user-images.githubusercontent.com/102866922/184502478-03ac732c-231f-478c-ba6f-a624cc028888.png">

![image](https://user-images.githubusercontent.com/102866922/184502508-1461ead8-5aac-4f49-bc53-9efcd57afe44.png)

On the dashboard click create an app, with your app information and set the redirect uri to http://127.0.0.1:5000/api_callback.

![image](https://user-images.githubusercontent.com/102866922/184502543-e9809bb9-b4c9-40f4-894f-96f071c1b43a.png)


If you are using a different port than 5000 then make sure to update this in the creds and the developer account.

![image](https://user-images.githubusercontent.com/102866922/184502565-6c0a4a1d-3b27-4369-ac9d-99e21d385c3e.png)

![image](https://user-images.githubusercontent.com/102866922/184502589-7713ee24-3e74-4cf0-9b30-7230acce931e.png)

Create a new file called creds.py using creds_template and insert your Client_ID and Client_Secret (this data is specific to your account and shouldn't be shared with anyone or via Github) then finally install Flask and Spotipy by Python Package manager or pip.
Run the app.py file
<maybe insert a video tutorial>

## Helpful Documentation
* Spotipy documentation can be found here https://spotipy.readthedocs.io/en/master/
* Recapify uses OAuth2.0 to access your Spotify data and restores your session with access tokens. More information can be found in this documentation https://developer.spotify.com/documentation/general/guides/authorization/
* All Spotify API endpoints are listed here https://developer.spotify.com/documentation/web-api/reference/#/

## How to Navigate the App
Once the application runs it will ask you to log in with your Spotify account information then will grant you access to Recapify and will redirect you to the homepage. There is a sidebar with all the navigation features which you can browse through. The homepage also includes a snippet of the data the sidebar will show you. This is what the sidebar looks like:

<img width="158" alt="image" src="https://user-images.githubusercontent.com/102866922/184502278-ca76176d-ce44-4d88-9b71-a642cf62a71e.png">

## Collaborators 
ledunc
lucywhitchurch
KatieC97
amartinarias
14/08/2022

CFG Degree Final Project
