import json

# Definirane konstante za prijavo
UPORABNIK_NE_OBSTAJA = 'Vpisano uporabniško ime ne obstaja. Prosim, poskusite ponovno.'
UPORABNIK_ZASEDEN = 'To uporabniško ime je že v uporabi. Prosim, poskusite ponovno.'
NAPACNO_GESLO = 'Vpisano geslo ni pravilno. Prosim, poskusite ponovno.'

# Ostale konstante
VECKRATNA_POJAVITEV = 'V'
KONTAKTA_NI = 'N'
PRAZNO = 'Polje ne sme biti prazno.'

# Definiram razred "Prijava", ki shranjuje uporabniška imena in gesla
# Povezave dopolnim z razredom "Povezave()"
class Prijava:
    def __init__(self, username, password, povezave):
        self.username = username
        self.password = password
        self.povezave = povezave