import json

# Definiram konstante za prijavo
WRONG_USERNAME = "Vpisano uporabniško ime ne obstaja. Prosim, poskusite ponovno."
USER_TAKEN = "To uporabniško ime je že v uporabi. Prosim, poskusite ponovno."
WRONG_PASS = "Vpisano geslo ni pravilno. Prosim, poskusite ponovno."

# Ostale konstante
MULTIPLE = "M"
NO_CONTACT = "N"
EMPTY = "Polje ne sme biti prazno."

######################################################################################
# Slovar katerega ključi (keys) so nadpomenke našim podatkom, vrednosti pa so podatki.
# Prilagam primer:
#
# {
# "69":
#     {
#         "priimek": "KLINC",
#         "ime": "TILEN",
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

    def add_new(self, priimek, ime, stevilka, email, rojstni, kraj):
        self.data[self.index()] = {
            "priimek": priimek,
            "ime": ime,
            "stevilka": stevilka,
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


    def sort_povezava(self, index, priimek, ime, stevilka, email, rojstni, kraj):
        self.data[index]["priimek"] = priimek
        self.data[index]['ime'] = ime
        self.data[index]['stevilka'] = stevilka
        self.data[index]['email'] = email
        self.data[index]['rojstni'] = rojstni
        self.data[index]['kraj'] = kraj

    # Brisanje kontakta
    
    def del_contact(self, index):
        self.data.pop(index)
    