import json

# Definiram konstante za prijavo
WRONG_USERNAME = "Vpisano uporabniško name ne obstaja. Prosim, poskusite ponovno."
USER_TAKEN = "To uporabniško name je že v uporabi. Prosim, poskusite ponovno."
WRONG_PASS = "Vpisano passwd ni pravilno. Prosim, poskusite ponovno."

# Ostale konstante
MULTIPLE = "M"
NO_CONTACT = "N"
EMPTY = "Polje ne sme biti EMPTY."

######################################################################################
# Slovar katerega ključi (keys) so nadpomenke našim podatkom, vrednosti pa so data.
# Prilagam primer:
#
# {
# "69":
#     {
#         "surname": "KLINC",
#         "name": "TILEN",
#         "številka": "987654321",
#         "elektronski naslov": "tilen.cinc@gmail.com",
#         "rojstni dan": "14. 1. 2004",
#         "kraj": "Ljubljana"
#     }
# }
######################################################################################

# Definiram razred "Prijava", ki shranjuje uporabniška imena in gesla
# Preverim ustreznost gesla, si zapomnim stanje
# Povezave kasneje dopolnim z razredom "Povezava()"

class Prijava:

    def __init__(self, username, password, povezave):
        self.username = username
        self.password = password
        self.povezave = povezave

    def preveri_password(self, password):
        if self.password != password:
            return WRONG_PASS

    def save_state(self, file_name):
        slovar = {
            "username": self.username,
            "password": self.password,
            "data": self.povezave.data
        }
        with open(file_name, "w", encoding="utf-8") as vhodna: #json
            json.dump(slovar, vhodna, ensure_ascii=False, indent=4)

    def get_state(file_name):
        with open(file_name, "r", encoding="utf-8") as vhodna:
            slovar = json.load(vhodna)
        username = slovar["username"]
        password = slovar["password"]
        povezave = Povezava(slovar["data"])
        return Prijava(username, password, povezave)

# Definiram nov razred v katerega dodam metode za delo s stiki

class Povezava:

    def __init__(self, data=None):
        self.data = {} if data is None else data

    def index(self):
        if self.data == {}:
            return 1
        else:
            sum = 0
            for slovar in self.data:
                sum += 1
            index = sum + 1
            return str(index)

    def add_new(self, surname, name, number, email, rojstni, kraj):
        self.data[self.index()] = {
            "surname": surname,
            "name": name,
            "number": number,
            "email": email,
            "rojstni": rojstni,
            "kraj": kraj
        }

    def sort_index(self):
        if self.data == {}:
            pass
        else:
            new_dict = {}
            index_dict = [key for key in self.data]
            for n in range (1, len(index_dict) + 1):
                povezava = self.data[index_dict[n - 1]]
                self.data.pop(index_dict[n - 1])
                self.data[str(n)] = povezava


    def sort_povezava(self, index, surname, name, number, email, rojstni, kraj):
        self.data[index]["surname"] = surname
        self.data[index]['name'] = name
        self.data[index]['number'] = number
        self.data[index]['email'] = email
        self.data[index]['rojstni'] = rojstni
        self.data[index]['kraj'] = kraj

    # Brisanje kontakta
    
    def del_contact(self, index):
        self.data.pop(index)
    
    def sort_priimki(self):
        '''Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so priimki urejeni po abecedi'''
        if self.data == {}:
            pass
        pair_list = [] # seznam parov [('novak', 1), ('lokar', 2), ('', 3), ('48', 4)]
        for i in self.data:
            surname = self.data[i]['surname']
            pair_list.append((surname.upper(), i))
        pairs = sorted(pair_list) # seznam uredimo po abecedi [('', 3), ('48', 4), ('lokar', 2), ('novak', 1)]
        slovar = {}
        for  n, (surname, index) in enumerate(pairs):
            slovar[str(n + 1)] = self.data[index]
            self.data.pop(index)
        self.data = slovar

    def sort_ime(self):
        '''Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so imena urejena po abecedi'''
        if self.data == {}:
            pass
        pair_list = []
        for i in self.data:
            name = self.data[i]['name']
            pair_list.append((name.upper(), i))
        pairs = sorted(pair_list)
        slovar = {}
        for  n, (name, index) in enumerate(pairs):
            slovar[str(n + 1)] = self.data[index]
            self.data.pop(index)
        self.data = slovar

    def stevilke_imenik(self):
        return [self.data[i]['number'] for i in self.data.keys()]

    def priimki_imenik(self):
        return [self.data[i]['surname'] for i in self.data.keys()]

    def imena_imenik(self):
        return [self.data[i]['name'] for i in self.data.keys()]
    
    def surnames(self, surname):
        '''Vrne slovar vseh kontaktov, ki imajo tak surname'''
        if surname == '':
            return self.data
        else:
            slovar = {}
            for i in self.data:
                if self.data[i]['surname'].upper() == surname:
                    slovar[i] = self.data[i]
            return slovar

    def names(self, name, slovar):
        '''Vrne slovar vseh kontaktov, ki imajo tako name (in surname od prej)'''
        if name == '':
            return slovar
        else:
            slovar2 = {}
            for i in slovar:
                if slovar[i]['name'].upper() == name:
                    slovar2[i] = slovar[i]
            return slovar2
    
    def isEmpty(self, slovar):
        if slovar == {}:
            return NO_CONTACT
        else:
            return slovar

    def findContact(self, surname, name, number):
        '''Poisce slovar z vsemi contacts, ki ustrezajo danim argumentom'''
        if surname + name + number == '':
            return EMPTY
        name = name.upper()
        surname = surname.upper()
        contacts_including_surname = self.surnames(surname)
        contacts_including_name_surname = self.names(name, contacts_including_surname)
        if number == '':
            return self.isEmpty(contacts_including_name_surname)
        else:
            slovar = {}
            for i in contacts_including_name_surname:
                if contacts_including_name_surname[i]['number'] == number:
                    slovar[i] = contacts_including_name_surname[i]
            return self.isEmpty(slovar)
    