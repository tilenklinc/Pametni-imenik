import json

# definirane konstante za prijavo
UPORABNISKO_IME_NE_OBSTAJA = 'Vpisano uporabniško ime ne obstaja. Prosim, poskusite ponovno'
UPORABNISKO_IME_ZE_OBSTAJA = 'To uporabniško ime je že v uporabi. Poskusite z drugim.'
NAPACNO_GESLO = 'Vpisano geslo ni pravilno. Prosim, poskusite ponovno'

# ostale konstante
VECKRATNA_POJAVITEV = 'V'
KONTAKTA_NI = 'N'
PRAZNO = 'Polje ne sme biti prazno'

# definiram razred "prijava", ki shranjuje uporabniška imena, gesla ter uporabniške povezave
class Stiki:
    def __init__(self, ime, priimek, stevilka, mail, naslov, krog):
        self.ime = ime
        self.priimek = priimek
        self.stevilka = stevilka
        self.mail = mail
        self.naslov = naslov
        self.krog = krog