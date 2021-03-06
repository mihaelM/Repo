# -*- coding: utf-8 -*-
from .. import db
from ..models import Korisnik, Uloga

def dodaj_korisnika(user, pas, ime, prezime, uloga):
    korisnik = Korisnik(korisnikKorisIme = user,
                        korisnikPas = pas,
                        ime = ime,
                        prezime = prezime,
                        uloga = uloga)
    db.session.add(korisnik)

# unos pocetnih korisnika u bazu
def insert_korisnici():


    uloga_administrator = Uloga.query.filter_by(imeUloge = "Administrator").first()
    uloga_djelatnik = Uloga.query.filter_by(imeUloge = "Djelatnik").first()
    uloga_korisnik = Uloga.query.filter_by(imeUloge = "Korisnik").first()

   
    dodaj_korisnika("Lana", "Lana", "Lana", "Lana", uloga_djelatnik)
    dodaj_korisnika("Petra", "Petra", "Petra", "Petra", uloga_djelatnik)
    dodaj_korisnika("Ana", "Ana", "Ana", "Ana", uloga_djelatnik)
    dodaj_korisnika("Ema", "Ema", "Ema", "Ema", uloga_djelatnik)
    dodaj_korisnika("Lucija", "Lucija", "Lucija", "Lucija", uloga_djelatnik)
    dodaj_korisnika("Sara", "Sara", "Sara", "Sara", uloga_djelatnik)
    dodaj_korisnika("Mia", "Mia", "Mia", "Mia", uloga_djelatnik)
    dodaj_korisnika("Nika", "Nika", "Nika", "Nika", uloga_djelatnik)
    dodaj_korisnika("Marija", "Marija", "Marija", "Marija", uloga_djelatnik)
    dodaj_korisnika("Iva", "Iva", "Iva", "Iva", uloga_djelatnik)

    dodaj_korisnika("Luka", "Luka", "Luka", "Luka", uloga_korisnik)
    dodaj_korisnika("Ivan", "Ivan", "Ivan", "Ivan", uloga_korisnik)
    dodaj_korisnika("Marko", "Marko", "Marko", "Marko", uloga_korisnik)
    dodaj_korisnika("David", "David", "David", "David", uloga_korisnik)
    dodaj_korisnika("Filip", "Filip", "Filip", "Filip", uloga_korisnik)
    dodaj_korisnika("Josip", "Josip", "Josip", "Josip", uloga_korisnik)
    dodaj_korisnika("Petar", "Petar", "Petar", "Petar", uloga_korisnik)
    dodaj_korisnika("Karlo", "Karlo", "Karlo", "Karlo", uloga_korisnik)
    dodaj_korisnika("Matej", "Matej", "Matej", "Matej", uloga_korisnik)
    dodaj_korisnika("Ivano", "Ivano", "Ivano", "Ivano", uloga_korisnik)

    dodaj_korisnika("Mate", "Mate", "Mate", "Mate", uloga_korisnik)
    dodaj_korisnika("Mislav", "Mislav", "Mislav", "Mislav", uloga_korisnik)
    dodaj_korisnika("Antun", "Antun", "Antun", "Antun", uloga_korisnik)
    dodaj_korisnika("Danijel", "Danijel", "Danijel", "Danijel", uloga_korisnik)
    dodaj_korisnika("Dorijan", "Dorijan", "Dorijan", "Dorijan", uloga_korisnik)
    dodaj_korisnika("Jure", "Jure", "Jure", "Jure", uloga_korisnik)
    dodaj_korisnika("Robert", "Robert", "Robert", "Robert", uloga_korisnik)
    dodaj_korisnika("Sime", "Sime", "Sime", "Sime", uloga_korisnik)
    dodaj_korisnika("Bartol", "Bartol", "Bartol", "Bartol", uloga_korisnik)
    dodaj_korisnika("Damjan", "Damjan", "Damjan", "Damjan", uloga_korisnik)
    dodaj_korisnika("Frane", "Frane", "Frane", "Frane", uloga_korisnik)
    dodaj_korisnika("Nino", "Nino", "Nino", "Nino", uloga_korisnik)
    dodaj_korisnika("Vedran", "Vedran", "Vedran", "Vedran", uloga_korisnik)
    dodaj_korisnika("Vid", "Vid", "Vid", "Vid", uloga_korisnik)
    dodaj_korisnika("Alen", "Alen", "Alen", "Alen", uloga_korisnik)
    dodaj_korisnika("Hrvoje", "Hrvoje", "Hrvoje", "Hrvoje", uloga_korisnik)
    dodaj_korisnika("Franko", "Franko", "Franko", "Franko", uloga_korisnik)
    dodaj_korisnika("Adam", "Adam", "Adam", "Adam", uloga_korisnik)
    dodaj_korisnika("Benjamin", "Benjamin", "Benjamin", "Benjamin", uloga_korisnik)
    dodaj_korisnika("Mauro", "Mauro", "Mauro", "Mauro", uloga_korisnik)
    dodaj_korisnika("Jurica", "Jurica", "Jurica", "Jurica", uloga_korisnik)
    dodaj_korisnika("Kristian", "Kristian", "Kristian", "Kristian", uloga_korisnik)
    dodaj_korisnika("Marijan", "Marijan", "Marijan", "Marijan", uloga_korisnik)
    dodaj_korisnika("Matko", "Matko", "Matko", "Matko", uloga_korisnik)
    dodaj_korisnika("Denis", "Denis", "Denis", "Denis", uloga_korisnik)
    dodaj_korisnika("Zvonimir", "Zvonimir", "Zvonimir", "Zvonimir", uloga_korisnik)
    dodaj_korisnika("Noel", "Noel", "Noel", "Noel", uloga_korisnik)
    dodaj_korisnika("Vanja", "Vanja", "Vanja", "Vanja", uloga_korisnik)
    dodaj_korisnika("Valentino", "Valentino", "Valentino", "Valentino", uloga_korisnik)
    dodaj_korisnika("Adriano", "Adriano", "Adriano", "Adriano", uloga_korisnik)
    dodaj_korisnika("Arian", "Arian", "Arian", "Arian", uloga_korisnik)
    dodaj_korisnika("Franjo", "Franjo", "Franjo", "Franjo", uloga_korisnik)
    dodaj_korisnika("Ivor", "Ivor", "Ivor", "Ivor", uloga_korisnik)
    dodaj_korisnika("Sebastian", "Sebastian", "Sebastian", "Sebastian", uloga_korisnik)
    dodaj_korisnika("Andro", "Andro", "Andro", "Andro", uloga_korisnik)
    dodaj_korisnika("Emil", "Emil", "Emil", "Emil", uloga_korisnik)
    dodaj_korisnika("Ilija", "Ilija", "Ilija", "Ilija", uloga_korisnik)

        #dodaj_korisnika("Roko", "Roko", "Roko", "Roko", uloga_korisnik)
    #dodaj_korisnika("Leon", "Leon", "Leon", "Leon", uloga_korisnik)
    #dodaj_korisnika("Mihael", "Mihael", "Mihael", "Mihael", uloga_korisnik)
    #dodaj_korisnika("Jakov", "Jakov", "Jakov", "Jakov", uloga_korisnik)
    #dodaj_korisnika("Antonio", "Antonio", "Antonio", "Antonio", uloga_korisnik)
    #dodaj_korisnika("Fran", "Fran", "Fran", "Fran", uloga_korisnik)
    #dodaj_korisnika("Dominik", "Dominik", "Dominik", "Dominik", uloga_korisnik)
    #dodaj_korisnika("Mateo", "Mateo", "Mateo", "Mateo", uloga_korisnik)
    #dodaj_korisnika("Gabriel", "Gabriel", "Gabriel", "Gabriel", uloga_korisnik)
    #dodaj_korisnika("Ante", "Ante", "Ante", "Ante", uloga_korisnik)
    #dodaj_korisnika("Lovro", "Lovro", "Lovro", "Lovro", uloga_korisnik)
    #dodaj_korisnika("Patrik", "Patrik", "Patrik", "Patrik", uloga_korisnik)
    #dodaj_korisnika("Niko", "Niko", "Niko", "Niko", uloga_korisnik)
    #dodaj_korisnika("Noa", "Noa", "Noa", "Noa", uloga_korisnik)
    #dodaj_korisnika("Matija", "Matija", "Matija", "Matija", uloga_korisnik)
    #dodaj_korisnika("Borna", "Borna", "Borna", "Borna", uloga_korisnik)
    #dodaj_korisnika("Nikola", "Nikola", "Nikola", "Nikola", uloga_korisnik)
    #dodaj_korisnika("Jan", "Jan", "Jan", "Jan", uloga_korisnik)
    #dodaj_korisnika("Marin", "Marin", "Marin", "Marin", uloga_korisnik)
    #dodaj_korisnika("Toni", "Toni", "Toni", "Toni", uloga_korisnik)
    #dodaj_korisnika("Gabrijel", "Gabrijel", "Gabrijel", "Gabrijel", uloga_korisnik)
    #dodaj_korisnika("Tin", "Tin", "Tin", "Tin", uloga_korisnik)
    #dodaj_korisnika("Vito", "Vito", "Vito", "Vito", uloga_korisnik)
    #dodaj_korisnika("Dino", "Dino", "Dino", "Dino", uloga_korisnik)
    #dodaj_korisnika("Bruno", "Bruno", "Bruno", "Bruno", uloga_korisnik)
    #dodaj_korisnika("Emanuel", "Emanuel", "Emanuel", "Emanuel", uloga_korisnik)
    #dodaj_korisnika("Leo", "Leo", "Leo", "Leo", uloga_korisnik)
    #dodaj_korisnika("Stjepan", "Stjepan", "Stjepan", "Stjepan", uloga_korisnik)
    #dodaj_korisnika("Andrej", "Andrej", "Andrej", "Andrej", uloga_korisnik)
    #dodaj_korisnika("Duje", "Duje", "Duje", "Duje", uloga_korisnik)
    #dodaj_korisnika("Tomislav", "Tomislav", "Tomislav", "Tomislav", uloga_korisnik)
    #dodaj_korisnika("Domagoj", "Domagoj", "Domagoj", "Domagoj", uloga_korisnik)
    #dodaj_korisnika("Kristijan", "Kristijan", "Kristijan", "Kristijan", uloga_korisnik)
    #dodaj_korisnika("Teo", "Teo", "Teo", "Teo", uloga_korisnik)
    #dodaj_korisnika("Lukas", "Lukas", "Lukas", "Lukas", uloga_korisnik)
    #dodaj_korisnika("Martin", "Martin", "Martin", "Martin", uloga_korisnik)
    #dodaj_korisnika("Mario", "Mario", "Mario", "Mario", uloga_korisnik)
    #dodaj_korisnika("Dorian", "Dorian", "Dorian", "Dorian", uloga_korisnik)
    #dodaj_korisnika("Adrian", "Adrian", "Adrian", "Adrian", uloga_korisnik)
    #dodaj_korisnika("Dario", "Dario", "Dario", "Dario", uloga_korisnik)
    #dodaj_korisnika("Leonardo", "Leonardo", "Leonardo", "Leonardo", uloga_korisnik)
    #dodaj_korisnika("Toma", "Toma", "Toma", "Toma", uloga_korisnik)
    #dodaj_korisnika("Juraj", "Juraj", "Juraj", "Juraj", uloga_korisnik)
    #dodaj_korisnika("Sven", "Sven", "Sven", "Sven", uloga_korisnik)
    #dodaj_korisnika("Marino", "Marino", "Marino", "Marino", uloga_korisnik)
    #dodaj_korisnika("Rafael", "Rafael", "Rafael", "Rafael", uloga_korisnik)
    #dodaj_korisnika("Andrija", "Andrija", "Andrija", "Andrija", uloga_korisnik)
    #dodaj_korisnika("Lovre", "Lovre", "Lovre", "Lovre", uloga_korisnik)
    #dodaj_korisnika("Stipe", "Stipe", "Stipe", "Stipe", uloga_korisnik)
    #dodaj_korisnika("Simun", "Simun", "Simun", "Simun", uloga_korisnik)
    #dodaj_korisnika("Viktor", "Viktor", "Viktor", "Viktor", uloga_korisnik)
    #dodaj_korisnika("Erik", "Erik", "Erik", "Erik", uloga_korisnik)
    #dodaj_korisnika("Daniel", "Daniel", "Daniel", "Daniel", uloga_korisnik)