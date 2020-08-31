import json

# Definiram konstante
CONTACT_NOT_EXISTING = "Ni stikov"
EMPTY = "To polje ne sme biti prazno"
WRONG_PASSWORD = "Vpisano geslo je napačno. Prosim, poskusite ponovno"
USERNAME_NOT_EXISTING = "Uporabniško ime ne obstaja. Prosim, poskusite ponovno"
USERNAME_TAKEN = "To uporabniško ime že obstaja. Prosim, poskusite ponovno."

# Definiram nov razred za prijavo in metode za preverjanje gesla
class User:
    def __init__(self, username, password, contacts):
        self.username = username
        self.password = password
        self.contacts = contacts
    
    def checkPasswd(self, password):
        if self.password != password:
            return WRONG_PASSWORD
    
    def saveUser(self, file_name): 
        data_dictionary = {
            "username": self.username,
            "password": self.password,
            "data": self.contacts.data
        }
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_dictionary, file, ensure_ascii=False, indent=4)

    def updateUser(file_name):
        with open(file_name, encoding="utf-8") as file:
            data_dictionary = json.load(file)
        username = data_dictionary["username"]
        password = data_dictionary["password"]
        contacts = Contact(data_dictionary["data"])
        return User(username, password, contacts)

# Poskusil dodati nov file, ki shrani podatke osebnega stika. Pri tem bi še omogočil dodajanje slike z JS-om.
class Personal:
    def personalData(self, personal_name, personal_surname, personal_mail, personal_number):
        self.personal_name = personal_name
        self.personal_surname = personal_surname
        self.personal_mail = personal_mail
        self.personal_number = personal_number

    def savePersonalData(self, file_name): #name datoteke je uporabniško_ime.json
        data_dictionary = {
            "personal_name": self.personal_name,
            "personal_surname": self.personal_surname,
            "personal_email": self.personal_email,
            "personal_number": self.personal_number
        }
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_dictionary, file, indent=4)


# definiram nov razred, ki dela s slovarji oziroma kontakti
class Contact:
    def __init__(self, data=None):
        self.data = {} if data is None else data

    def new__indeks(self):
        if self.data == {}:
            return 1
        else:
            sum = 0
            for dictionary in self.data:
                sum += 1
            indeks = sum + 1
            return str(indeks)

    def addContact(self, surname, name, number, mail, birthday, location):
        self.data[self.new__indeks()] = {
            "surname": surname,
            "name": name,
            "number": number,
            "mail": mail,
            "birthday": birthday,
            "location": location
        }

    # razporedi indekse po naraščujočem vrstnem redu
    def sortIndeces(self):
        if self.data == {}:
            pass
        else:
            new_dictionary = {}
            index_list = [key for key in self.data]
            for n in range(1, len(index_list) + 1):
                contact = self.data[index_list[n - 1]]
                self.data.pop(index_list[n - 1])
                self.data[str(n)] = contact

    # spreminjanje lastnosti kontaktov
    def editContact(self, indeks, surname, name, number, mail, birthday, location):
        
        self.data[indeks]["surname"] = surname
        self.data[indeks]["name"] = name
        self.data[indeks]["number"] = number
        self.data[indeks]["mail"] = mail
        self.data[indeks]["birthday"] = birthday
        self.data[indeks]["location"] = location

    # izbriše stik
    def deleteContact(self, indeks):
        self.data.pop(indeks)
        
    # razvrsti po abecednem vrstnem redu priimkov
    def sortBySurname(self):
        if self.data == {}:
            pass
        pair_list = []
        for i in self.data:
            surname = self.data[i]["surname"]
            pair_list.append((surname.upper(), i))
        pairs = sorted(pair_list) 
        dictionary = {}
        for  n, (surname, indeks) in enumerate(pairs):
            dictionary[str(n + 1)] = self.data[indeks]
            self.data.pop(indeks)
        self.data = dictionary

    # razvrsti po abecednem vrstnem redu imen    
    def sortByName(self):
        if self.data == {}:
            pass
        pair_list = []
        for i in self.data:
            name = self.data[i]["name"]
            pair_list.append((name.upper(), i))
        pairs = sorted(pair_list)
        dictionary = {}
        for  n, (name, indeks) in enumerate(pairs):
            dictionary[str(n + 1)] = self.data[indeks]
            self.data.pop(indeks)
        self.data = dictionary

    # seznami števil, priimkov in imen
    def getNumber(self):
        return [self.data[i]["number"] for i in self.data.keys()]

    def getName(self):
        return [self.data[i]["name"] for i in self.data.keys()]

    def getSurname(self):
        return [self.data[i]["surname"] for i in self.data.keys()]

    # poišče vse s takim priimkom
    def surnames(self, surname):
        if surname == "":
            return self.data
        else:
            dictionary = {}
            for i in self.data:
                if self.data[i]["surname"].upper() == surname:
                    dictionary[i] = self.data[i]
            return dictionary

    # poišče oziroma vrne seznam vseh stikov s tem imenom
    def names(self, name, dictionary):
        if name == "":
            return dictionary
        else:
            dictionary2 = {}
            for i in dictionary:
                if dictionary[i]["name"].upper() == name:
                    dictionary2[i] = dictionary[i]
            return dictionary2

    # če je prazen vrne error_msg, sicer slovar
    def isEmpty(self, dictionary):
        if dictionary == {}:
            return CONTACT_NOT_EXISTING
        else:
            return dictionary

    # poišče in vrne seznam z danimi lastnostmi
    def findContact(self, surname, name, number):
        if surname + name + number == "":
            return EMPTY
        name = name.upper()
        surname = surname.upper()
        contacts_including_surname = self.surnames(surname)
        contacts_including_name_surname = self.names(name, contacts_including_surname)
        if number == "":
            return self.isEmpty(contacts_including_name_surname)
        else:
            slovar = {}
            for i in contacts_including_name_surname:
                if contacts_including_name_surname[i]["number"] == number:
                    slovar[i] = contacts_including_name_surname[i]
            return self.isEmpty(slovar)