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
    
    def sort_priimki(self):
        '''Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so priimki urejeni po abecedi'''
        if self.data == {}:
            pass
        seznam_parov = [] # seznam parov [('novak', 1), ('lokar', 2), ('', 3), ('48', 4)]
        for i in self.data:
            priimek = self.data[i]['priimek']
            seznam_parov.append((priimek.upper(), i))
        pari = sorted(seznam_parov) # seznam uredimo po abecedi [('', 3), ('48', 4), ('lokar', 2), ('novak', 1)]
        slovar = {}
        for  n, (priimek, index) in enumerate(pari):
            slovar[str(n + 1)] = self.data[index]
            self.data.pop(index)
        self.data = slovar

    def sort_ime(self):
        '''Slovar kontaktov uredi tako, da si vrednosti ključev sledijo od 1 do n, pri čemer so imena urejena po abecedi'''
        if self.data == {}:
            pass
        seznam_parov = []
        for i in self.data:
            ime = self.data[i]['ime']
            seznam_parov.append((ime.upper(), i))
        pari = sorted(seznam_parov)
        slovar = {}
        for  n, (ime, index) in enumerate(pari):
            slovar[str(n + 1)] = self.data[index]
            self.data.pop(index)
        self.data = slovar

    def stevilke_imenik(self):
        return [self.data[i]['stevilka'] for i in self.data.keys()]

    def priimki_imenik(self):
        return [self.data[i]['priimek'] for i in self.data.keys()]

    def imena_imenik(self):
        return [self.data[i]['ime'] for i in self.data.keys()]
    
    def kontakti_priimek(self, priimek):
        '''Vrne slovar vseh kontaktov, ki imajo tak priimek'''
        if priimek == '':
            return self.data
        else:
            slovar = {}
            for i in self.data:
                if self.data[i]['priimek'].upper() == priimek:
                    slovar[i] = self.data[i]
            return slovar

    def kontakti_ime(self, ime, slovar):
        '''Vrne slovar vseh kontaktov, ki imajo tako ime (in priimek od prej)'''
        if ime == '':
            return slovar
        else:
            slovar2 = {}
            for i in slovar:
                if slovar[i]['ime'].upper() == ime:
                    slovar2[i] = slovar[i]
            return slovar2
    
    def ali_je_prazen(self, slovar):
        if slovar == {}:
            return NO_CONTACT
        else:
            return slovar

    def poisci_kontakt(self, priimek, ime, stevilka):
        '''Poisce slovar z vsemi kontakti, ki ustrezajo danim argumentom'''
        if priimek + ime + stevilka == '':
            return EMPTY
        ime = ime.upper()
        priimek = priimek.upper()
        kontakti_s_tem_priimkom = self.kontakti_priimek(priimek)
        kontakti_s_tem_priimkom_in_imenom = self.kontakti_ime(ime, kontakti_s_tem_priimkom)
        if stevilka == '':
            return self.ali_je_prazen(kontakti_s_tem_priimkom_in_imenom)
        else:
            slovar = {}
            for i in kontakti_s_tem_priimkom_in_imenom:
                if kontakti_s_tem_priimkom_in_imenom[i]['stevilka'] == stevilka:
                    slovar[i] = kontakti_s_tem_priimkom_in_imenom[i]
            return self.ali_je_prazen(slovar)
    