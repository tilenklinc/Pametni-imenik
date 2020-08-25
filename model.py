import json

# Definirane konstante za prijavo
WRONG_USERNAME = "Vpisano uporabniško ime ne obstaja. Prosim, poskusite ponovno."
USER_TAKEN = "To uporabniško ime je že v uporabi. Prosim, poskusite ponovno."
WRONG_PASS = "Vpisano geslo ni pravilno. Prosim, poskusite ponovno."

# Ostale konstante
MULTIPLE = "V"
NO_CONTACT = "N"
EMPTY = "Polje ne sme biti prazno."

######################################################################################
# Slovar katerega ključi (keys) so nadpomenke našim podatkom, vrednosti pa so podatki.
# Prilagam primer:
#
# {
# "69":
#     {
#         'priimek': 'KLINC',
#         'ime': 'TILEN',
#         'številka': '987654321',
#         'elektronski naslov': 'tilen.cinc@gmail.com',
#         'rojstni dan': '14. 1. 2004',
#         'kraj': 'Ljubljana'
#     }
# }
######################################################################################

# Definiram razred "Prijava", ki shranjuje uporabniška imena in gesla
# Povezave dopolnim z razredom "Povezave()"
# Preverim ustreznost gesla, si zapomnim stanje
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
            json.dump(slovar, in_file, ensure_ascii=False, indent=4)

    def get_state(file_name):
        with open(file_name, encoding="utf-8") as vhodna:
            slovar = json.load(vhodna)
        username = slovar["username"]
        password = slovar["password"]
        povezave = Povezave(slovar["data"])
        return Prijava(username, password, povezave)

