import json

CONTACT_NOT_EXISTING = "N"
EMPTY = "To polje ne sme biti prazno"
WRONG_PASSWORD = "Vpisano geslo je napačno. Prosim, poskusite ponovno"
USERNAME_NOT_EXISTING = "Uporabniško name ne obstaja. Prosim, poskusite ponovno"
USERNAME_TAKEN = "To uporabniško ime že obstaja. Prosim, poskusite ponovno."

class user:
    def __init__(self, username, password, contacts):
        self.username = username
        self.password = password
        self.contacts = contacts # to je razred Contact()
    
    def checkPasswd(self, password):
        if self.password != password:
            return WRONG_PASSWORD
    
    def saveUser(self, file_name): #name datoteke je uporabniško_ime.json
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
        contacts = Contact(data_dictionary["data"]) # tu mora biti Contact(), če ne dobimo seznam in ne razreda
        return user(username, password, contacts)


class Contact:
    def __init__(self, data=None):
        self.data = {} if data is None else data

    def new__indeks(self):
        if self.data == {}:
            return 1
        else:
            sum = 0
            for slovar in self.data:
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

    def sortIndeces(self):
        """Uredi indekse po vrsti od 1 do dolžine slovarja"""
        if self.data == {}:
            pass
        else:
            new_dictionary = {}
            index_list = [key for key in self.data]
            for n in range(1, len(index_list) + 1):
                contact = self.data[index_list[n - 1]]
                self.data.pop(index_list[n - 1])
                self.data[str(n)] = contact

    def editContact(self, indeks, surname, name, number, mail, birthday, location):
        """Posodobitev podatkov"""
        self.data[indeks]["surname"] = surname
        self.data[indeks]["name"] = name
        self.data[indeks]["number"] = number
        self.data[indeks]["mail"] = mail
        self.data[indeks]["birthday"] = birthday
        self.data[indeks]["location"] = location

    def deleteContact(self, indeks):
        self.data.pop(indeks)

    def sortBySurname(self):
        """Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so priimki urejeni po abecedi"""
        if self.data == {}:
            pass
        pair_list = [] # seznam parov [("novak", 1), ("lokar", 2), ("", 3), ("48", 4)]
        for i in self.data:
            surname = self.data[i]["surname"]
            pair_list.append((surname.upper(), i))
        pairs = sorted(pair_list) # seznam uredimo po abecedi [("", 3), ("48", 4), ("lokar", 2), ("novak", 1)]
        slovar = {}
        for  n, (surname, indeks) in enumerate(pairs):
            slovar[str(n + 1)] = self.data[indeks]
            self.data.pop(indeks)
        self.data = slovar
        
    def sortByName(self):
        """Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so imena urejena po abecedi"""
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

    def getNumber(self):
        return [self.data[i]["number"] for i in self.data.keys()]

    def getSurname(self):
        return [self.data[i]["surname"] for i in self.data.keys()]

    def getName(self):
        return [self.data[i]["name"] for i in self.data.keys()]

    def surnames(self, surname):
        """Vrne slovar vseh kontaktov, ki imajo tak surname"""
        if surname == "":
            return self.data
        else:
            dictionary = {}
            for i in self.data:
                if self.data[i]["surname"].upper() == surname:
                    dictionary[i] = self.data[i]
            return dictionary

    def names(self, name, dictionary):
        """Vrne slovar vseh kontaktov, ki imajo tako name (in surname od prej)"""
        if name == "":
            return dictionary
        else:
            dictionary2 = {}
            for i in dictionary:
                if dictionary[i]["name"].upper() == name:
                    dictionary2[i] = dictionary[i]
            return dictionary2

    def isEmpty(self, slovar):
        if dictionary == {}:
            return CONTACT_NOT_EXISTING
        else:
            return dictionary

    def findContact(self, surname, name, number):
        """Poisce slovar z vsemi contacts, ki ustrezajo danim argumentom"""
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