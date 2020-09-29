import json


class IataCode():
    
    def __init__(self, prompt):
        self.prompt = prompt
        self.all_iata_codes = self.load_iata_codes()
        self.iata_code = self.get_code()
        
    def city_choice(self, prompt):
        user_input = input(prompt).capitalize()
        return user_input
    
    def load_iata_codes(self):
        with open("IATA-codes.json", "r") as data_file:
            raw_json = data_file.readline()
            code_repo = json.loads(raw_json)
            return code_repo

    def correct_spelling(self, city):
        return self.all_iata_codes[city][1]
        
    def multiple_options(self, city):
        options = {}
        count = 1
        for cities in self.all_iata_codes:
            if (len(city) < 4) and (city==cities[:len(city)]):
                options[count]= [cities, self.all_iata_codes[cities]]
                count +=1
            else:
                if cities[:4] == city[:4]:
                    options[count]= [cities, self.all_iata_codes[cities]]
                    count +=1
        return options
            
    def display_options(self, options):
        try:
            if options == {}:
                print("Couldn't find any results")
                return self.get_code()
            else:
                print("Did you mean one of the following options?")
                for choices in options:
                    print(f"{choices} :  {options[choices][0]}, {options[choices][1][0]}")
        except:
            pass
        
    def choice(self, options):
        print("Choose one of the following options by inputing the reference number or input enter to go back to search""")
        user_input = input("number or back")
        try:
            return options[int(user_input)][1][1]
        except:
            return self.get_code()
    
    def get_code(self):
        city = self.city_choice(self.prompt)
        try:
            return self.correct_spelling(city)
        except:
            options = self.multiple_options(city)
            self.display_options(options)
            return self.choice(options)
                
