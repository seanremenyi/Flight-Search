import json
import os


class IataCode():

    def __init__(self, prompt: str) -> None:
        self.prompt = prompt
        self.all_iata_codes = self.load_iata_codes()
        self.iata_code = self.get_code()

    def city_choice(self, prompt: str) -> str:
        user_input = input(f"\n{prompt}\n").capitalize()
        return user_input

    def load_iata_codes(self) -> dict:
        with open("IATA-codes.json", "r") as data_file:
            raw_json = data_file.readline()
            code_repo = json.loads(raw_json)
            return code_repo

    def correct_spelling(self, city: str) -> str:
        return self.all_iata_codes[city][1]

    def multiple_options(self, city: str) -> dict:
        options = {}
        count = 1
        for cities in self.all_iata_codes:
            if (len(city) < 4) and (city == cities[:len(city)]):
                options[count] = [cities, self.all_iata_codes[cities]]
                count += 1
            else:
                if cities[:4] == city[:4]:
                    options[count] = [cities, self.all_iata_codes[cities]]
                    count += 1
        return options

    def display_options(self, options: dict) -> None:
        try:
            if options == {}:
                os.system('clear')
                print("Couldn't find any results")
                return self.get_code()
            else:
                print("Did you mean one of the following options?\n")
                for choices in options:
                    city = options[choices][0]
                    country = options[choices][1][0]
                    print(f"{choices} :  {city}, {country}")
        except:
            return self.get_code()

    def choice(self, options: dict) -> str:
        user_input = input("""\nChoose one of the following options
Input reference number on the left
Or hit enter to search again\n""")
        try:
            return options[int(user_input)][1][1]
        except:
            return self.get_code()

    def get_code(self) -> str:
        city = self.city_choice(self.prompt)
        try:
            return self.correct_spelling(city)
        except:
            options = self.multiple_options(city)
            self.display_options(options)
            return self.choice(options)
