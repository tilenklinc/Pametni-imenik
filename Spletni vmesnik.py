import bottle
from model import User, Contact, WRONG_PASSWORD, USERNAME_NOT_EXISTING, USERNAME_TAKEN
import os
import hashlib

uporabniki = {}
skrivnost = 'Secret'

#iz direktorija uporabniki izbere ustrezno datoteko
for file_name in os.listdir('uporabniki'):
    user = User.updateUser(os.path.join('uporabniki', file_name))
    uporabniki[user.username] = user

# dobimo razred User, ki vsebuje name in passwd
def current_user():
    username = bottle.request.get_cookie('username', secret=skrivnost)
    return uporabniki[username] 

def imenik_uporabnika():
    return current_user().contacts

def save_current_user():
    user = current_user()
    user.saveUser(os.path.join('uporabniki', f'{user.username}.json'))

# oblika login in register page-a
@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')

@bottle.get('/prijava/')
def prijava_get():
    return bottle.template('prijava.html', obvestilo=None)

@bottle.post('/prijava/')
def prijava_post():
    username = bottle.request.forms.getunicode('username')
    if username not in uporabniki:
        napaka = USERNAME_NOT_EXISTING
        return bottle.template('prijava.html', obvestilo=napaka)
    passwd = bottle.request.forms.getunicode('passwd')
    h = hashlib.blake2b()
    h.update(passwd.encode(encoding='utf-8'))
    password = h.hexdigest()
    user = uporabniki[username]
    if user.checkPasswd(password) == WRONG_PASSWORD:
        napaka = WRONG_PASSWORD
        return bottle.template('prijava.html', obvestilo=napaka)
    bottle.response.set_cookie('username', user.username, path='/', secret=skrivnost)
    bottle.redirect('/imenik/')

@bottle.get('/registracija/')
def registracija_get():
    return bottle.template('registracija.html', obvestilo=None)

@bottle.post('/registracija/')
def registracija_post():
    username = bottle.request.forms.getunicode('username')
    if username in uporabniki:
        napaka = USERNAME_TAKEN
        return bottle.template('registracija.html', obvestilo=napaka)
    passwd = bottle.request.forms.getunicode('passwd')
    h = hashlib.blake2b()
    h.update(passwd.encode(encoding='utf-8'))
    password = h.hexdigest()
    user = User(
        username,
        password,
        Contact()
        )
    uporabniki[username] = user
    bottle.response.set_cookie('username', user.username, path='/', secret=skrivnost)
    bottle.redirect('/imenik/')

# oblika vseh podstrani
@bottle.get('/imenik/')
def nacrtovanje_imenika():
    slovar_podatkov = imenik_uporabnika().data
    save_current_user()
    return bottle.template('imenik.html',imenik=slovar_podatkov)

@bottle.get('/profile_card/')
def profileCard():
    return bottle.template("profile_card.html")

@bottle.get("/poglej-imenik/")
def imenik():
    slovar_podatkov = imenik_uporabnika().data
    return bottle.template('imenik.html', imenik=slovar_podatkov)

@bottle.post('/odjava/')
def odjava():
    save_current_user()
    bottle.response.delete_cookie('username', path='/')
    bottle.redirect('/')

@bottle.get('/profile_card_uredi/')
def profileCardUredi():
    return bottle.template("profile_card_uredi.html")

@bottle.get('/profile_card/')
def profileCard():
    return bottle.template("profile_card.html")

@bottle.get("/dodaj-kontakt/")
def addContact():
    return bottle.template("dodaj-kontakt.html")

@bottle.post('/dodaj-kontakt/')
def addContact():
    surname = bottle.request.forms.getunicode('surname')
    name = bottle.request.forms.getunicode('name')
    number = str(bottle.request.forms.getunicode('number'))
    mail = bottle.request.forms.getunicode('mail')
    birthday = bottle.request.forms.getunicode('birthday')
    location = bottle.request.forms.getunicode('location')
    imenik_uporabnika().addContact(surname, name, number, mail, birthday, location)
    imenik_uporabnika().sortIndeces()
    save_current_user()
    bottle.redirect('/imenik/')

@bottle.post('/izbrisi-kontakt<indeks>/')
def deleteContact(indeks):
    imenik_uporabnika().deleteContact(indeks)
    imenik_uporabnika().sortIndeces()
    bottle.redirect('/imenik/')

@bottle.get('/uredi-kontakt<indeks>/')
def editContact(indeks):
    slovar_podatkov = imenik_uporabnika().data
    save_current_user()
    return bottle.template('uredi_kontakt.html', imenik=slovar_podatkov, indeks=indeks)

@bottle.post('/uredi-kontakt<indeks>/')
def editcontact(indeks):
    surname = bottle.request.forms.getunicode('surname')
    name = bottle.request.forms.getunicode('name')
    number = str(bottle.request.forms.getunicode('number'))
    mail = bottle.request.forms.getunicode('mail')
    birthday = bottle.request.forms.getunicode('birthday')
    location = bottle.request.forms.getunicode('location')
    stevilo = str(indeks)
    imenik_uporabnika().editContact(stevilo, surname, name, number, mail, birthday, location)
    save_current_user()
    bottle.redirect('/imenik/')

#@bottle.get("/profil/")

@bottle.get("/poisci-kontakt/")
def findContact():
    return bottle.template('iskanje.html', rezultat=None)

@bottle.post('/poisci-kontakt/')
def findContact():
    surname = bottle.request.forms.getunicode('iskanje-surname')
    name = bottle.request.forms.getunicode('iskanje-name')
    number = str(bottle.request.forms.getunicode('iskanje-number'))
    rezultat = imenik_uporabnika().findContact(surname, name, number)
    return bottle.template('iskanje.html', rezultat=rezultat)

@bottle.post("/uredi-kontakte-po-priimkih/")
def sortBySurname():
    imenik_uporabnika().sortBySurname()
    bottle.redirect('/imenik/')

@bottle.post("/uredi-kontakte-po-imenih/")
def sortByName():
    imenik_uporabnika().sortByName()
    bottle.redirect('/imenik/')
    

bottle.run(debug=True, reloader=True)