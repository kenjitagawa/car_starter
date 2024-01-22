# Car Starter

## Description

Over the past weekend, I spent some time analyzing the remote starter of my car. I wanted to see if I could reverse engineer the endpoints of the API and build a script to start my car from my computer. I was successful in doing so, and I wanted to share my findings with the community. I have not disclosed the brand nor the information for the API endpoints for security reasons. The script can be found within the repository, however, it will not work without the API endpoints, which you will have to find for your vehicle. Here is a brief overview of the process I took to reverse engineer the application.

## Why?

Why not? :)
I wanted to learn new things, and this was one that had crossed my mind before.

## Disclaimer

These are the steps for my car. The steps may be different for your car. Additionally, I am not responsible for any damage that may occur to your vehicle. Please be careful when reverse engineering your vehicle. I am not responsible for any damage that may occur to your vehicle.

## Reverse Engineering

### Step 1: Intercepting the API Requests

The first step in reverse engineering the application was to intercept the API requests. I used a tool called [Proxyman](https://proxyman.io/) to intercept the requests. I then opened the application and logged in. I then went to the Proxyman application and found the request that was sent to the API. I then right-clicked on the request and selected "Copy as cURL". I then pasted the cURL command into a text editor and saved it for later use.

### Step 2: Analyzing the cURL Command

The next step was to analyze the cURL command. I noticed that the command was using the POST method and was sending a JSON payload. I also noticed that the command was using a simple auth for authenticating. I then copied the JSON payload and saved it for later use.

## Step 3: Building the Script

The final step was to build the script. I used Python to build the script. I began by testing out the cURL command in the terminal. I then used the `requests` library to send the request. This step was a lot of playing around with the code to get it to work, authenticate and send requests to multiple of the available endpoints. The app allows for the following actions to be performed:

- Start the car
- Stop the car
- Lock the car
- Unlock the car
- Get the status of the car
- Open the trunk

All of these actions can be performed using the script and are all part of the endpoints. Once you have all of the endpoints, and you make sure that the requests are authenticated, you can build the script and align the code with the standards of the language you are using. From there, you can buildout whatever you might want to do with the script.  

## Step 4: Finding the other Endpoints

In order to find the other endpoints, you can repeat the steps above but with each command within the app. For example, if you want to find the endpoint for locking the car, you would lock the car using the app and then repeat the steps above. You would then find the endpoint for locking the car. You can then add this endpoint to the script and use it to lock the car. The same can be done for all of the other actions.

## Conclusion

The process of reverse engineering the application was a lot of fun. I learned a lot about how the application works and how to build a script to interact with the API. This shows how easy we can discover how applications work behind the UI. A fun challenge, is to checkout what other apps within your phone are doing when you open them and they first connect to the internet (I was shocked by LinkedIn). From this point, you can build a script to interact with the API and perform actions that the app can do. You can schedule the car to turn on at a certain time. You can build a better UI for the app (mine has a pretty ugly UI). Additionally, you can make use of the same principles to get the API endpoints for other apps and build scripts/wrappers to interact with them.
