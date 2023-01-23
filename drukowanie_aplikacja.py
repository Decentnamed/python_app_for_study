# Prosta aplikacja do symulacji obsługi druku i skanu
# Aplikacja nie wpływa w żaden sposób na działanie drukarek i skanerów. Jest to aplikacja bez obsługi fizycznych urządzeń (Tzw. symulator)
# Autor: Dawid Grabowicz nr. albumu: 58990
# Data: 16.05.2022
# Wersja: 1.0.0


import os
import time
import math


clear = lambda: os.system('cls')

# KLASA DRUKARKA
class Drukarka():
    # konstruktor klasy
    def __init__(self, nazwa, skan):
        self.nazwa = nazwa
        self.toner = 100.00
        self.usb = False
        self.wifi = False
        self.kartki = 250 # kartki w drukarce - 250 to maksymalna ilosc
        self.aktywna = False
        self.historia = []
        self.skan = skan
    
    # metoda do pobierania nazwy drukarki
    def nazwa_drukarki(self):
        return self.nazwa

    # metoda do ustalenia połączenia drukarki z USB
    def polaczenie_usb(self, polaczenie):
        self.usb = polaczenie
    
    # metoda do ustalenia połączenia drukarki z WIFI
    def polaczenie_wifi(self, polaczenie):
        self.wifi = polaczenie

    # metoda sprawdzająca czy drukarka jest połączona z USB lub WIFI
    def czy_aktywna(self):
        if self.usb == True or self.wifi == True:
            self.aktywna = True
            return self.aktywna
        else:
            self.aktywna = False
            return self.aktywna
    
    # metoda zwracająca ilość toneru w drukarce
    def ile_toneru(self):
        return self.toner
    
    # metoda zwracająca ilość kartek w kontenerze drukarki
    def ile_kartek(self):
        return self.kartki
    
    # metoda do ustalania ubutku toneru w drukarce
    def ubytek_toneru(self, ubytek):
        self.toner -= ubytek

    # metoda do uzupełniania toneru w drukarce
    def wymien_toner(self):
        self.toner = 100.00
    
    # metoda do ustalania ubytku kartek w drukarce
    def usun_kartki(self, kartki):
        self.kartki -= kartki

    # metoda do uzupełniania kartek w drukarce
    def uzupelnij_kartki(self, kartki):
        if kartki >= 1 and kartki <= 250:
            self.kartki += kartki
        else:
            print("Zbyt mała lub duża ilość kartek")

    # metoda do dodawania historii w drukarce
    def dodaj_historie(self, historia):
        self.historia.append(historia)

    # metoda pobierająca całą historię drukarki
    def historia_drukarki(self):
        if len(self.historia) == 0:
            print("Brak historii druku")
        else:
            print("#### początek historii ####")
            print("")
            for i in range(len(self.historia)):
                print(str(i + 1) + ")" + self.historia[i])
        print("")
        print("#### koniec historii ####")

    # metoda zwracająca informację czy drukarka ma opcję skan
    def czy_jest_opcja_skan(self):
        return self.skan

# KLASA DRUKOWANIE
class Drukowanie():
    # konstruktor klasy 
    def __init__(self):
        self.__drukowanie = False
        self.druk = False # jednostronny = False, dwustronny = True
        self.kolor = False # czarno-biały = False, kolorowy = True
        self.strony = 1
        self.orientacja = False # pionowa = False, pozioma = True
    
    # metoda do ustalania domyślnych ustawień drukowania
    def domyslne_ustawienia(self):
        self.druk = False
        self.kolor = False
        self.orientacja = False
    
    # metoda do ustalania konfiguracji druku
    def konfiguracja_druku(self, druk, kolor, orientacja):
        self.druk = druk
        self.kolor = kolor
        self.orientacja  = orientacja
    
    # metoda startująca drukowanie
    def druk_start(self, strony):
        self.drukowanie = True
        print("Drukowanie w toku...")
        time.sleep(strony * 0.1)
        self.drukowanie = False
        print("Drukowanie zakończone")
    
    # metoda zatrzymująca drukowanie
    def druk_stop(self):
        self.drukowanie = False
        print("Drukowanie zatrzymane")

    # metoda sprawdzająca czy drukarka aktualnie drukuje
    def czy_drukuje(self):
        return self.drukowanie


# KLASA SKANOWANIE
class Skanowanie():
    # konstruktor klasy
    def __init__(self):
        self.skanowanie = False
        self.strony = 1
        self.adres = '' # adres email, na który wysłany będzie skan dokumentu

    # metoda do skanowania i wysyłania kopii na adres email
    def skan_email_start(self, strony, adres):
        self.skanowanie = True
        print("Skanowanie w toku...")
        time.sleep(strony * 0.1)
        self.skanowanie = False
        print("Skanowanie zakończone...")
        print("Wysłano kopię na adres email: {}".format(adres))
    
    # metoda do skanowania i drukowania kopii
    def skan_druk_start(self, strony):
        self.skanowanie = True
        print("Skanowanie w toku...")
        time.sleep(strony * 0.1)
        self.skanowanie = False
        print("Skanowanie zakończone")
    
    # metoda do zatrzymywania skanu
    def skan_stop(self):
        self.skanowanie = False
    
    # metoda sprawdzająca czy drukarka skanuje
    def czy_skanuje(self):
        return self.skanowanie
    
# Interfejsy użytkownika

# funkcja do czyszczenia konsoli
def gui_czysc():
    clear()

# glowny interfejs
def gui_glowne():    
    print("1) Drukowanie")
    print("2) Skanowanie")
    print("3) Połączenie drukarki")
    print("4) Historia druku, kartki, toner")
    print("5) Wyjscie z aplikacji")

# interfejs drukowania
def gui_drukowanie():
    print("1) Konfiguracja druku")
    print("2) Druk domyślny")
    print("3) Powrót")

# interfejs skanowania
def gui_skanowanie():
    print("1) Skan na maila")
    print("2) Skan i druk")
    print("3) Powrót")

# interfejs historii, uzupełnienie toneru i kartek
def gui_historia_toner_kartki():
    print("1) Historia drukarki")
    print("2) Uzupełnij toner")
    print("3) Uzupełnij kartki")
    print("4) Powrót")

# PROGRAM GLOWNY
def program_glowny():
    # Instancje klas, drukarki, drukowanie, skanowanie
    minolta = Drukarka('Minolta', True)
    brother = Drukarka('Brother', True)
    hp = Drukarka('HP', False)
    drukowanie = Drukowanie()
    skanowanie = Skanowanie()
    wybor_glowny = '' # zmienna wyboru głównego

    while wybor_glowny != '5':
        gui_glowne() # wywołanie interfejsu głównego
        wybor_glowny = input() # wybor opcji w interfejsie i przypisanie wartośći
        gui_czysc() # czyszczenie konsoli

        # opcja drukowanie
        if wybor_glowny == '1':
            wybor_drukowanie = '' 
            while wybor_drukowanie != '3':
                gui_drukowanie()
                wybor_drukowanie = input()
                gui_czysc()

                # opcja druku z własną konfiguracją użytkownika
                if wybor_drukowanie == '1':
                    print("Podaj dane do konfiguracji: ")
                    druk = str(input("Druk jednostronny = 0, Druk dwustronny = 1: "))
                    kolor = str(input("Druk czarno-biały = 0, Druk kolorowy = 1: "))
                    orientacja = str(input("Orientacja pionowa = 0, Orientacja pozioma = 1: "))
                    kartki = 0
                    strony = int(input("Strony: "))

                    if druk == '0':
                        druk = bool(False)
                        kartki = strony # kartki = strony dla druku jednostronnego
                    else:
                        druk = bool(True)
                        kartki = math.ceil(strony / 2) # obliczanie potrzebnych kartek do wydrukowania dla druku dwustronnego

                    if kolor == '0':
                        kolor = bool(False)
                    else:
                        kolor = bool(True)

                    if orientacja == '0':
                        orientacja = bool(False)
                    else:
                        orientacja = bool(True)   

                    gui_czysc()
                    toner = strony * 0.1
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())

                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1': # wybor drukarki 1 i logika do drukowania
                        if minolta.czy_aktywna() == True:
                            if minolta.ile_kartek() >= kartki:
                                minolta.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if minolta.ile_toneru() >= toner:
                                minolta.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.konfiguracja_druku(druk, kolor, orientacja)
                            drukowanie.druk_start(strony)
                            minolta.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")

                    if wybor_drukarki == '2': # wybor drukarki 2 i logika do drukowania
                        if brother.czy_aktywna() == True:
                            if brother.ile_kartek() >= kartki:
                                brother.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if brother.ile_toneru() >= toner:
                                brother.ubytek_toneru(toner) 
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.konfiguracja_druku(druk, kolor, orientacja)
                            drukowanie.druk_start(strony)
                            brother.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")
                    
                    if wybor_drukarki == '3': # wybor drukarki 3 i logika do drukowania
                        if hp.czy_aktywna() == True:
                            if hp.ile_kartek() >= kartki:
                                hp.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if hp.ile_toneru() >= toner:
                                hp.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.konfiguracja_druku(druk, kolor, orientacja)
                            drukowanie.druk_start(strony)
                            hp.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")                  

                # opcja druku z konfiguracją domyślną
                if wybor_drukowanie == '2':
                    strony = int(input("Strony: "))
                    gui_czysc()
                    kartki = strony 
                    toner = strony * 0.1
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1': # wybor drukarki 1 i logika do drukowania
                        if minolta.czy_aktywna() == True:
                            if minolta.ile_kartek() >= kartki:
                                minolta.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if minolta.ile_toneru() >= toner:
                                minolta.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.domyslne_ustawienia()
                            drukowanie.druk_start(strony)
                            minolta.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")

                    if wybor_drukarki == '2': # wybor drukarki 2 i logika do drukowania
                        if brother.czy_aktywna() == True:
                            if brother.ile_kartek() >= kartki:
                                brother.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if brother.ile_toneru() >= toner:
                                brother.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.domyslne_ustawienia()
                            drukowanie.druk_start(strony)
                            brother.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")
                    
                    if wybor_drukarki == '3': # wybor drukarki 3 i logika do drukowania
                        if hp.czy_aktywna() == True:
                            if hp.ile_kartek() >= kartki:
                                hp.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if hp.ile_toneru() >= toner:
                                hp.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.domyslne_ustawienia()
                            drukowanie.druk_start(strony)
                            hp.dodaj_historie("Drukowanie " + str(strony) + " stron")
                        else:
                            print("Drukarka jest nieaktywna...")

        # opcja skanowanie
        if wybor_glowny == '2':
            wybor_skanowanie = ''
            while wybor_skanowanie != '3':
                gui_skanowanie()
                wybor_skanowanie = input()
                gui_czysc()

                if wybor_skanowanie == '1': # wybor skanowania i wyslanie kopii na maila
                    email = input("Podaj e-mail: ")
                    strony = int(input("Strony: "))
                    gui_czysc()
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1': # wybor drukarki 1 i logika do skanowania i wyslania kopii na maila
                        if minolta.czy_aktywna() == True:     
                            if minolta.czy_jest_opcja_skan() == True:
                                skanowanie.skan_email_start(strony, email)
                                minolta.dodaj_historie("Skanowanie " + str(strony) + " stron na email " + str(email))
                            else:
                                print("Ta drukarka nie ma opcji skanu...")
                        else:
                            print("Drukarka jest nieaktywna...")
                    if wybor_drukarki == '2': # wybor drukarki 2 i logika do skanowania i wyslania kopii na maila
                        if brother.czy_aktywna() == True:
                            if brother.czy_jest_opcja_skan() == True:
                                skanowanie.skan_email_start(strony, email)
                                brother.dodaj_historie("Skanowanie " + str(strony) + " stron na email " + str(email))
                            else:
                                print("Ta drukarka nie ma opcji skanu")
                        else:
                            print("Drukarka jest nieaktywna")
                    if wybor_drukarki == '3': # wybor drukarki 1 i logika do skanowania i wyslania kopii na maila
                        if hp.czy_aktywna() == True:
                            if hp.czy_jest_opcja_skan() == True:
                                skanowanie.skan_email_start(strony, email)
                                hp.dodaj_historie("Skanowanie " + str(strony) + " stron na email " + str(email))
                            else:
                                print("Ta drukarka nie ma opcji skanu")
                        else:
                            print("Ta drukarka jest nieaktywna")
                
                if wybor_skanowanie == '2': # wybor skanowania i druk kopii
                    strony = int(input("Strony: "))
                    gui_czysc()
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1': # wybor drukarki 1 i logika do skanowania i drukowania
                        if minolta.czy_aktywna() == True:     
                            skanowanie.skan_druk_start(strony)
                            if minolta.ile_kartek() >= kartki:
                                minolta.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if minolta.ile_toneru() >= toner:
                                minolta.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.druk_start(strony)
                            minolta.dodaj_historie("Skanowanie i druk " + str(strony) + " stron ")
                        else:
                            print("Drukarka jest nieaktywna...")
                    if wybor_drukarki == '2': # wybor drukarki 2 i logika do skanowania i drukowania
                        if brother.czy_aktywna() == True:
                            skanowanie.skan_druk_start(strony)
                            if brother.ile_kartek() >= kartki:
                                brother.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if brother.ile_toneru() >= toner:
                                brother.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.druk_start(strony)
                            brother.dodaj_historie("Skanowanie i druk " + str(strony) + " stron ")
                        else:
                            print("Drukarka jest nieaktywna")
                    if wybor_drukarki == '3': # wybor drukarki 3 i logika do skanowania i drukowania
                        if hp.czy_aktywna() == True:
                            skanowanie.skan_druk_start(strony)
                            if hp.ile_kartek() >= kartki:
                                hp.usun_kartki(kartki)
                            else:
                                print("Niewystarczająca ilość kartek, uzupełnij kontener.")
                            if hp.ile_toneru() >= toner:
                                hp.ubytek_toneru(toner)
                            else:
                                print("Niewystarczająca ilość toneru, uzupełnij toner.")
                            drukowanie.druk_start(strony)
                            hp.dodaj_historie("Skanowanie i druk " + str(strony) + " stron ")
                        else:
                            print("Ta drukarka jest nieaktywna")

        # opcje drukarki, połączenie itd
        if wybor_glowny == '3':
            polaczenie_minolta = ''
            polaczenie_brother = ''
            polaczenie_hp = ''
            
            if minolta.czy_aktywna() == True:
                polaczenie_minolta = 'Połączona'
            else:
                polaczenie_minolta = 'Rozłączona'
            if brother.czy_aktywna() == True:
                polaczenie_brother = 'Połączona'
            else:
                polaczenie_brother = 'Rozłączona'
            if hp.czy_aktywna() == True:
                polaczenie_hp = 'Połączona'
            else:
                polaczenie_hp = 'Rozłączona'
            
            print("1) Drukarka {} {}".format(minolta.nazwa_drukarki(), polaczenie_minolta))
            print("2) Drukarka {} {}".format(brother.nazwa_drukarki(), polaczenie_brother))
            print("3) Drukarka {} {}".format(hp.nazwa_drukarki(), polaczenie_hp))

            wybor_decyzji = input("Czy chcesz podłączyć komunikację do drukarki? 0 - NIE, 1 - TAK: ")
            if wybor_decyzji == '1':
                wybor_drukarki = input("Wybierz numer drukarki: ")
                if wybor_drukarki == '1': # wybor drukarki 1 i logika do połaczenia drukarki
                    wifi = str(input("WIFI (0 - NIE, 1 - TAK): "))
                    usb = str(input("USB (0 - NIE, 1 - TAK): "))
                    gui_czysc()
                    if wifi == '1':
                        wifi = bool(True)                 
                        minolta.polaczenie_wifi(wifi)
                        print("Minolta połączona z WIFI")
                    if wifi == '0':
                        wifi = bool(False)
                        minolta.polaczenie_wifi(wifi)
                        print("Minolta rozłączona z WIFI")
                    if usb == '1':
                        usb = bool(True)
                        minolta.polaczenie_usb(usb)
                        print("Minolta połączona z USB")
                    if usb == '0':
                        usb = bool(False)
                        minolta.polaczenie_usb(usb)
                        print("Minolta rozłączona z USB")
                
                if wybor_drukarki == '2': # wybor drukarki 1 i logika do połaczenia drukarki
                    wifi = str(input("WIFI (0 - NIE, 1 - TAK): "))
                    usb = str(input("USB (0 - NIE, 1 - TAK): "))
                    gui_czysc()
                    if wifi == '1':
                        wifi = bool(True)
                        print("Brother połączona z WIFI")
                    if wifi == '0':
                        wifi = bool(False)
                        print("Brother rozłączona z WIFI")
                    if usb == '1':
                        usb = bool(True)
                        print("Brother połączona z USB")
                    if usb == '0':
                        usb = bool(False)
                        print("Brother rozłączona z USB")
                    brother.polaczenie_wifi(wifi)
                    brother.polaczenie_usb(usb)
                
                if wybor_drukarki == '3': # wybor drukarki 1 i logika do połaczenia drukarki
                    wifi = str(input("WIFI (0 - NIE, 1 - TAK): "))
                    usb = str(input("USB (0 - NIE, 1 - TAK): "))
                    gui_czysc()
                    if wifi == '1':
                        wifi = bool(True)
                        print("hp połączona z WIFI")
                    if wifi == '0':
                        wifi = bool(False)
                        print("hp rozłączona z WIFI")
                    if usb == '1':
                        usb = bool(True)
                        print("hp połączona z USB")
                    if usb == '0':
                        usb = bool(False)
                        print("hp rozłączona z USB")
                    hp.polaczenie_wifi(wifi)
                    hp.polaczenie_usb(usb)

        # opcja historii drukarki, wymiana toneru i kartek
        if wybor_glowny == '4':
            wybor_historia = ''
            while wybor_historia != '4':
                gui_historia_toner_kartki()
                wybor_historia = input()
                gui_czysc() 
                if wybor_historia == '1':
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1':
                        minolta.historia_drukarki()
                    elif wybor_drukarki == '2':
                        brother.historia_drukarki()
                    elif wybor_drukarki == '3':
                        hp.historia_drukarki()
                    else:
                        print("Nie ma takiej drukarki na liscie")
                
                # opcja wymiany toneru w drukarce
                if wybor_historia == '2':
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1':
                        minolta.wymien_toner()
                        print("Wymieniono toner w drukarce {}".format(minolta.nazwa_drukarki()))
                    elif wybor_drukarki == '2':
                        brother.wymien_toner()
                        print("Wymieniono toner w drukarce {}".format(brother.nazwa_drukarki()))
                    elif wybor_drukarki == '3':
                        hp.wymien_toner()
                        print("Wymieniono toner w drukarce {}".format(hp.nazwa_drukarki()))
                    else:
                        print("Nie ma takiej drukarki na liscie")
                
                # opcja uzupełnienia kartek w drukarce
                if wybor_historia == '3':
                    kartki_uzupelnij = int(input("Ilość kartek do kontenera: "))
                    gui_czysc()
                    print("1) Drukarka ", minolta.nazwa_drukarki())
                    print("2) Drukarka ", brother.nazwa_drukarki())
                    print("3) Drukarka ", hp.nazwa_drukarki())
                    wybor_drukarki = input()
                    gui_czysc()
                    if wybor_drukarki == '1':
                        minolta.uzupelnij_kartki(kartki_uzupelnij)
                        print("Uzupełniono kartki w drukarce {}".format(minolta.nazwa_drukarki()))
                    elif wybor_drukarki == '2':
                        brother.uzupelnij_kartki(kartki_uzupelnij)
                        print("Uzupełniono kartki w drukarce {}".format(brother.nazwa_drukarki()))
                    elif wybor_drukarki == '3':
                        hp.uzupelnij_kartki(kartki_uzupelnij)
                        print("Uzupełniono kartki w drukarce {}".format(hp.nazwa_drukarki()))
                    else:
                        print("Nie ma takiej drukarki na liscie")
                              

# WYWOLANIE PROGRAMU GLOWNEGO
if __name__ == '__main__':
    program_glowny()
