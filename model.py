import json

# Definirane konstante za prijavo
WRONG_USERNAME = "Vpisano uporabniško ime ne obstaja. Prosim, poskusite ponovno."
USER_TAKEN = "To uporabniško ime je že v uporabi. Prosim, poskusite ponovno."
WRONG_PASS = "Vpisano geslo ni pravilno. Prosim, poskusite ponovno."

# Ostale konstante
MULTIPLE = "V"
NO_CONTACT = "N"
EMPTY = "Polje ne sme biti prazno."

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

    def update_file(self, in_file):
        slovar = {
            "username": self.username,
            "password": self.password,
            "update": self.povezave.povezave
        }
        with open(in_file, "w", encoding="utf-8") as vhodna: #json
            json.dump(slovar_stanja, in_file, ensure_ascii=False, indent=4)
