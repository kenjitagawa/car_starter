import requests
import re
import io
import json
import os

class CarStarterService:

    def __init__(self, url: str, status_url: str, auth_token: str, vehicle_id: str, user_agent: str, check_mode: bool = False):
        self.url = url
        self.status_url = status_url + vehicle_id
        self.auth_token = auth_token
        self.vehicle_id = vehicle_id
        self.check_mode = check_mode
        self.user_agent = user_agent

        self.headers = {
            'Accept': '*/*',
            'User-Agent': f'{self.user_agent}',
            'Accept-Language': 'en-CA,en-US;q=0.9,en;q=0.8',
            'Authorization': f'Basic {self.auth_token}',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        self.headers_api = self.headers.copy()
        self.headers_api['Content-Type'] = 'application/json'

    def __str__(self):
        return f'CarStarterService(url={self.url}, \
        status_url={self.status_url}, \
        auth_token={self.auth_token}, \
        vehicle_id={self.vehicle_id}, \
        check_mode={self.check_mode}), \
        user_agent={self.user_agent}), \
        headers={self.headers}), \
        headers_api={self.headers_api})'
    
    def lock_door(self) -> json:
        payload = json.dumps({
            "CarCommand": "0",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None
        
        response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        return response
    
    def unlock_door(self) -> json:
        payload = json.dumps({
            "CarCommand": "1",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None
        
        response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        return response
        

    def turn_on(self) -> json:
        # Command 3 is responsible for turning on the car
        payload = json.dumps({
            "CarCommand": "3",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None
        
        print('Sending command to car...')
        try:
            response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        except Exception as e:
            print('Error sending command to car.')
            print(e)
            return None
        print('Command sent to car.')
        return response

    def turn_off(self) -> json:
        payload = json.dumps({
            "CarCommand": "4",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None
        
        response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        return response 
    
    def heating_seats(self) -> json:
        payload = json.dumps({
            "CarCommand": "11",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None
        
        response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        return response 
    
    def defrost(self) -> json:
        payload = json.dumps({
            "CarCommand": "12",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None

        response = requests.request("POST", self.url, headers=self.headers_api, data=payload)
        return response 


    def get_status(self) -> json:
        payload = json.dumps({
            "CarCommand": "1",
            "VehicleId": self.vehicle_id
        })

        if self.check_mode:
            print('Check mode is on, not sending command to car.')
            return None

        response = requests.request("GET", self.status_url, headers=self.headers, data=payload)
        return response


if __name__ == '__main__':

    debug = True
    check_mode = False

    if debug:
        from dotenv import load_dotenv
        load_dotenv()

        AUTH_TOKEN = os.getenv('AUTH_TOKEN')
        STATUS_URL = os.getenv('STATUS_URL')
        URL = os.getenv('API_URL')
        VEHICLE_ID = os.getenv('VEHICLE_ID')
        USER_AGENT = os.getenv('USER_AGENT')

    else:
        AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

    car_starter_service = CarStarterService(
        url=URL,
        status_url=STATUS_URL,
        auth_token=AUTH_TOKEN,
        vehicle_id=VEHICLE_ID,
        user_agent=USER_AGENT,
        check_mode=check_mode
    )

    print("Launching the car starter service... Please wait.\n\n")

    while True:
        ## YES, I KNOW THIS IS BAD PRACTICE. This was just supposed to be a POC. 
        ## The pretty code is above, this one we know how to do, I just didn't put
        ## the time into it yet.

        ######### PLEASE IGNORE THE UGLYNESS BELOW #########
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################

        ## NOOOO Don't look here!

        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        ####################################################

        ## Why are you here? Go back up! Stop doing this to me! 

        print("What would you like to do?")
        print("1. Turn on the car")
        print("2. Turn off the car")
        print("3. Get the status of the car")
        print("4. Open the door")
        print("5. Lock the door")
        print("6. Turn on the heating seats")
        print("7. Turn on the defrost")
        print("8. Debug")
        print("0. Exit the program")


        prompt = int(input("Please enter a number: "))
        if prompt == 1:
            print("Turning on the car... Please wait.")
            response = car_starter_service.turn_on()
            print(response)
        elif prompt == 2:
            print("Turning off the car... Please wait.")
            response = car_starter_service.turn_off()
            print(response)
        elif prompt == 3:
            print("Getting the status of the car... Please wait.")
            response = car_starter_service.get_status()
            print(json.loads(response.dumps()))
        elif prompt == 4:
            print("Opening the door... Please wait.")
            response = car_starter_service.open_door()
            print(response)
        elif prompt == 5:
            print("Locking the door... Please wait.")
            response = car_starter_service.lock_door()
            print(response)
        elif prompt == 6:
            print("Turning on the heating seats... Please wait.")
            response = car_starter_service.heating_seats()
            print(response)
        elif prompt == 7:
            print("Turning on the defrost... Please wait.")
            response = car_starter_service.defrost()
            print(response)
        elif prompt == 8:
            print("Debugging the car starter service...")
            print(car_starter_service)


        elif prompt == 0:
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid input. Please try again.")
            continue
