import requests
import json
import datetime

class Query():
    
    def __init__(self):
        # print("Country Codes must be the IATA code for the Airport\nIATA codes are the corresponding 3 Capitalized letters\n")
        # self.origin= self.get_IATA_code("Enter your Origin city:")
        # self.destination = self.get_IATA_code("Enter your Destinatin city:")
        # print("\n\nSearch Flights among a range of dates\nDates are of the format dd/mm/yyyy\n")
        # self.starting_range = self.get_date("Look for Flights from the:")
        # self.ending_range = self.get_date("Look for Flights up until:")
        # self.query_results = self.api_call()
        self.origin = self.code_lookup()
    
    
    # def get_IATA_code(self,question):
    #     try:
    #         user_input= input(f"{question}\n")
    #         response = requests.get(f"https://api.skypicker.com/flights?flyFrom={user_input}&to=SYD&curr=AUD&dateFrom=01/01/2021&dateTo=03/01/2021&partner=picky&v=3")
    #         data = json.loads(response.text)
    #         return user_input
    #     except:
    #         self.get_IATA_code(question)


    # def get_date(self, question):
    #     user_input = input(f"{question}\n")
    #     try :
    #         day,month,year = user_input.split('/')
    #         datetime.datetime(int(year),int(month),int(day))
    #         return user_input
    #     except ValueError:
    #         self.get_date(question)

    
    # def api_call(self):
    #     response = requests.get(f"https://api.skypicker.com/flights?flyFrom={self.origin}&to={self.destination}&curr=AUD&dateFrom={self.starting_range}&dateTo={self.ending_range}&partner=picky&v=3")
    #     data =  json.loads(response.text)
    #     return data["data"]    
        
    def code_lookup(self):
        user_input=input("which city?").capitalize()
        try:
            with open("IATA-codes.json", "r") as data_file:
                raw_json = data_file.readline()
                code_repo = json.loads(raw_json)
                print(code_repo[user_input])
        except KeyError:
            print("Did you mean one of the following?")
            options = {}
            count = 1
            with open("IATA-codes.json", "r") as data_file:
                raw_json = data_file.readline()
                code_repo = json.loads(raw_json)
                for x in code_repo:
                    if x[:4] == user_input[:4]:
                        options[count]= [x, code_repo[x]]
                        count +=1
            for items in options:
                print(f"{items} :  {options[items][0]}, {options[items][1][0]}")
            city_choice = input("If city in list, please input the number, otherwise type back to search again")
            if city_choice == "back":
                return self.code_lookup()
            else:
                print(options[int(city_choice)][1][1])
            
            
            
            
            
query1=Query()
        