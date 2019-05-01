# // Beispielprogramm von Robin Czurylo
# Guten Tag. Mit diesem Programm möchte ich Ihnen meine
# aktuellen Fähigkeiten demonstrieren, damit für Sie eine
# Einschätzung meiner Eignung möglich ist. 

import sqlite3, time, random, re

class Rechner:

    def diff():
        # Funktion: f(x) = 6x^4 + x^3 + 12x + 5
        # => 24x^3 + 3x^2 + 12
        # Allgemeine Form: f(x)=a_n x^n + a_n-1 x^n-1 + ... + a0
        print("\nEs müssen Grad des Polynoms und die Koeffizienten " +
              "in absteigender Reihenfolge eingegeben werden.\n")
        
        max_exp = int(input("Grad des Polynoms: "))
        n = max_exp + 1
        
        coeff_init = [0] * n
        exp_init = [] 

        # Initialisiere Exponenten in absteigender Reihenfolge
        for i in range(max_exp,-1,-1):
            exp_init += [i]

        # Koeffizienten werden vom Benutzer eingelesen
        for i in range(0, len(coeff_init)):
            coeff_init[i] = int(input("Koeffizient " + str(i) + ": "))

        new_coeff = [0] * n
        new_exp = [0] * n

        # Berechne die neuen Koeffizienten und Exponenten
        for i in range(0, len(coeff_init)):
            new_coeff[i] = coeff_init[i] * exp_init[i]
            if exp_init[i] > 0:
                new_exp[i] = exp_init[i] - 1
            else:
                new_exp[i] = exp_init[i]

        # Darstellung des Polynoms
        print("\nDas Polynom f(x): ")

        for i in range(0,len(coeff_init)):
            if coeff_init[i] != 0:
                if exp_init[i] > 0:
                    print(str(coeff_init[i]) + "x^" + str(exp_init[i]), end=" + ")
                else:
                    print(str(coeff_init[i]))
            else:
                print("",end="")
                
        print("\nDie Ableitung f'(x) ist: ")

        for i in range(0,len(new_coeff)):
            if new_coeff[i] != 0:
                if new_exp[i] > 0:
                    print(str(new_coeff[i]) + "x^" + str(new_exp[i]), end=" + ")
                else:
                    print(str(new_coeff[i]))
            else:
                print("",end="")

    def integral():
        # Funktion f(x) = 24x^3 + 3x^2 + 12
        # => F(x) = 6x^4 + x^3 + 12x + C
        print("\nEs müssen Grad des Polynoms und die Koeffizienten " +
              "in absteigender Reihenfolge eingegeben werden.\n")
        
        max_exp = int(input("Grad des Polynoms: "))
        n = max_exp + 1
        
        coeff_init = [0] * n
        exp_init = []

        # Initialisiere Exponenten in absteigender Reihenfolge
        for i in range(max_exp, -1, -1):
            exp_init += [i]

        # Koeffizienten werden vom Benutzer eingelesen
        for i in range(0,len(coeff_init)):
            coeff_init[i] = int(input("Koeffizient " + str(i) + ": "))

        new_coeff = [0] * n
        new_exp = [0] * n

        # Berechne die neuen Koeffizienten und Exponenten
        for i in range(0, len(new_coeff)):
            new_coeff[i] = coeff_init[i] / (exp_init[i]+1)
            new_exp[i] = exp_init[i] + 1

        # Darstellung des Polynoms
        print("\nDas Polynom f(x): ")

        for i in range(0,len(coeff_init)):
            if coeff_init[i] != 0:
                if exp_init[i] > 0:
                    print(str(coeff_init[i]) + "x^" + str(exp_init[i]),end=" + ")
                else:
                    print(coeff_init[i])
            else:
                print("",end="")

        print("\nDie Stammfunktion F(x): ")

        for i in range(0, len(new_coeff)):
            if new_coeff[i] != 0:
                if new_exp[i] > 1:
                    print(str(new_coeff[i]) + "x^" + str(new_exp[i]),end=" + ")
                elif new_exp[i] == 1:
                    print(str(new_coeff[i]) + "x + C" )
            else:
                print("",end="")

    ## / Binär -> Dezimal Umwandler
    def binToDec():
        m = input("Binärzahl eingeben: ")
        # Initialisiere Dezimalzahl n_dec
        n_dec = 0
        
        # Berechne die Zweierpotenzen und addiere die Ergebnisse
        for i in range(len(m)-1, -1, -1):
            res = int(m[i]) * (2 ** (len(m)-1-i))
            n_dec += res
            
        return n_dec

    ## / Dezimal -> Binär Umwandler
    def decToBin():
        dz = int(input("Dezimalzahl eingeben: "))
        n_bin = ""
        # Teile die Zahl durch 2 und starte damit die Liste zerg
        # Halte den Rest in mods fest
        zerg = [dz // 2]
        mods = [dz % 2]

        i = 0
        while True:
            # Berechne alle Quotienten 
            erg = zerg[i] // 2
            zerg += [erg]
            # Berechne alle Reste
            emods = zerg[i] % 2
            mods += [emods]
        
            i += 1
            
            # Die Rechnung ist fertig, wenn der ganzzahlige Quotient 0 ist.
            if erg == 0:
                break

        # Nimm die Reste in umgekehrter Reihenfolge auf
        for i in range(len(mods)-1,-1,-1):
            n_bin += str(mods[i])
            
        return n_bin

    def menu():
        # Navigiert durch die Klasse 'Rechner'
        print("\n==== Im Menüpunkt 'Rechner' ====")
        print("Menüpunkte:" +
              "\n1. Ableitung von Polynomen" + 
              "\n2. Integration von Polynomen" + 
              "\n3. Dezimal/ Binär - Konvertierer" +
              "\n4. Zurück zum Hauptmenü")
        
        menu = input("Punkt auswählen: ")
        
        if menu == "1":
            Rechner.diff()
            Rechner.menu()

        elif menu == "2":
            Rechner.integral()
            Rechner.menu()

        elif menu == "3":
            print("\nUnterpunkte" +
                  "\n 1. Dezimal -> Binär" + 
                  "\n 2. Binär -> Dezimal")
            untermenu = input("Unterpunkt auswählen: ")

            if untermenu == "1":
                print("Binär: " + str(Rechner.decToBin()))
                Rechner.menu()

            elif untermenu == "2":
                print("Dezimal: " + str(Rechner.binToDec()))
                Rechner.menu()

            else:
                print("Ungültige Eingabe\n")
                Rechner.menu()
                
        elif menu == "4":
            Hauptmenu.menu()
            
        else:
            print("Ungültige Eingabe\n")
            Rechner.menu()

class Algorithmen:

    # // Wiederholte Quersummen
    # Für eine gegebene ganze Zahl n wird die wiederholte Quersumme berechnet.
    # // Beispiele
    # rep_qs(123) => 6
    # rep_qs(83) => 2 , da 8+3 = 11 und 1+1 = 2
    # rep_qs(4582) => 1, da 4+5+8+2=19, 1+9=10, 1+0=1

    def rep_qs(n):
        n_str = str(n)
        
        if len(n_str) > 1:
            qsum = 0
            
            for i in range(len(n_str)):
                qsum += int(n_str[i])

            # Wiederhole die Rechnung bis das Ergebnis aus einer
            # einzelnen Ziffer besteht
            if len(str(qsum)) > 1:
                return Algorithmen.rep_qs(qsum)
            
            else:
                return qsum

        else:
            return n
    
    # // Aufzählen und Überprüfen
    # Gibt die ersten n Zahlen an, dessen wiederholte Quersumme der
    # ersten Ziffern der letzten Ziffer gleicht.
    # Auch: Wie viele dieser Zahlen gibt es?
    # // Beispiele
    # 1236, da 1+2+3=6
    # 1282, da 1+2+8=11 und 1+1=2

    def new_rep_qs(n):
        # Initialisierung
        counter = 0
        numbers = []

        for i in range(0, n+1):
            i_str = str(i)

            # digits sind alle Ziffern der Zahl i bis auf die letzte
            digits = i_str[0:len(i_str)-1]

            # digit ist die letzte Ziffer der Zahl i
            digit = i_str[len(i_str)-1]

            # Benutze die Funktion rep_qs für die wiederholte Quersumme
            qsum = Algorithmen.rep_qs(digits)

            if str(qsum) == digit:
                counter += 1
                numbers += [i]

        return counter, numbers 

    # // Sortieralgorithmen und Laufzeiten
    # Es wird die Methode Bubblesort verwendet.

    def bubbleSortLaufzeit():
        l = []
        # Erstelle zufällige Liste mit 200 Elementen zwischen 0 und 15
        for i in range(200):
            num = random.randint(0,15)
            l += [num]
            
        print("Originale Liste: \n" + str(l), "\n")
        t0 = time.time()
        sortbubb = Algorithmen.bubbleSort(l)
        print("Sortierte Liste mit BubbleSort: \n" + str(sortbubb), "\n")
        t1 = time.time()
        # diff_ms ist die Lauzeit in Millisekunden
        diff_ms = (t1 - t0) * 1000
        diff_ms_str = str(diff_ms)
        print("Laufzeit: ", diff_ms_str[0:7], "Millisekunden")

    def bubbleSort(l):
        # Sortierung einer Liste mit BubbleSort. Zwei benachbarte
        # Elemente werden verglichen. Ist das nachfolgende Element
        # kleiner, so werden beide Elemente vertauscht.
        
        for i in range(len(l)-1,0,-1):
            for j in range(i):
                if l[j] > l[j+1]:
                    ind_j = l[j]
                    l[j] = l[j+1]
                    l[j+1] = ind_j
        return l

    def scan(l, i , j):
        # Zuerst wird das erste Element mit dem Rest der Liste verglichen.
        # Addieren sich keine Elemente zu Null, dann wird das zweite Element
        # mit dem Rest der Liste verglichen, dann das dritte etc.

        # // Beispiele
        # [8, 4, 8, 8, 8, 0, 7, 3, 4, 5] ergibt False.
        # [2, 2, 10, 3, 5, 1, 7, -3, 5] ergibt True,
        # da -3 + 3 = 0 sind.
        
        if i >= len(l):
            print("Listenende erreicht. Keine Elemente addieren sich zu Null.")
            return False
        
        elif j >= len(l):
            return Algorithmen.scan(l, i+1, i+2)
        
        elif l[i] + l[j] == 0:
            print(str(l[i]) + " + " + str(l[j]) + " = 0")
            return True
        
        else:
            return Algorithmen.scan(l, i, j+1)

    # // Initialisierung von scan(l, i, j)
    # init vergleicht das erste Element mit dem zweiten.
    def init():
        liste = []
        # Eine Liste mit zehn zufälligen Zahlen zwischen -10 und 10
        # wird erzeugt.
        for i in range(0, 10):
            num = random.randint(-10,10)
            liste += [num]
            
        print(liste)
        
        return Algorithmen.scan(liste, 0, 1)

    def histogram():
        # Erstellt eine liste l mit m Zahlen der Reichweite n
        n = 10
        m = 50
        l = []
        for i in range(m):
            num = random.randint(0, n-1)
            l += [num]
        print("\nListe: ", l)
        # Initialisierung
        counter = [0] * n
        # Geht die Liste l durch und prüft, wie oft jede Zahl vorkommt
        for i in range(len(l)):
            for j in range(n):
                if l[i] == j:
                    counter[j] += 1

        # Ausgabe
        print("\nHäufigkeiten: ", counter)
        print("\nZahl \t Häufigkeit")
        for i in range(n):
            print(i, "\t", counter[i] * "#")

    # // Anwendungen mit RegEx
    # 1. Text auf die Anzahl eines bestimmten Wortes durchsuchen
    # 2. Text auf Uhrzeiten durchsuchen
    # 3. Text auf Palindrome durchsuchen

    def searchText(n):
        search = input("Suche nach folgendem Wort: ")
        x = re.findall(search, n)
        print("Das Wort", search, "kommt", len(x), "mal vor im Text")

    def searchTimes(n):
        regexp = "(2[0-3]|[01]?[0-9]):([0-5][0-9])"
        z = re.search(regexp, n)

        if z == None:
            print("Keine Uhrzeiten im Text gefunden!")
            
        while z != None:
            print(z.group())
            n = n[z.end():]
            z = re.search(regexp, n)

    def searchPalindrome(n):
        # Gibt alle Palindrome und deren Anzahl an

        # Der Text wird in eine Liste verwandelt, wobei jedes
        # Wort im Text ein Element in der Liste darstellt
        words = re.split("\s", n)

        # Die Palindrome und deren Häufigkeit
        counter = 0
        res = []
        
        # Durchsuche jedes Element der Liste 
        for i in range(0, len(words)):
            rev_word = ""
            
            # Drehe jedes Wort einzeln um
            for j in range(len(words[i])-1, -1, -1):
                # Füge alle Buchstaben in umgekehrter Reihenfolge ein
                rev_word += words[i][j]
            
            # Palindrom gefunden, wenn das Wort an der Stelle i dem
            # umgekehrten Wort an Stelle i gleicht
            if rev_word == words[i]:
                counter += 1
                res += [rev_word]

        if counter == 0:
            print("Keine Palindrome im Text.")
        else:
            print("Anzahl: " + str(counter))
            print("Palindrome: " + str(res))

    def initRegEx():
        # Hilfsfunktion zum Navigieren der RegEx Funktionen
        print("\nDiese Funktion durchsucht einen Text mithilfe von " +
              "regulären Ausdrücken.")
        print("Möglichkeiten: " +
              "\n1. Text nach einem bestimmten Wort durchsuchen" +
              "\n2. Text nach Uhrzeiten durchsuchen" +
              "\n3. Text nach Palindromen durchsuchen" +
              "\n4. Zurück")
        
        txt = input("Text eingeben: ")

        untermenu = input("Option auswählen: ")
        
        if untermenu == "1":
            Algorithmen.searchText(txt)
            
        elif untermenu == "2":
            Algorithmen.searchTimes(txt)
            
        elif untermenu == "3":
            Algorithmen.searchPalindrome(txt)
            
        elif untermenu == "4":
            print("zurück")
            
        else:
            print("falsche eingabe")

    def menu():
        # Navigiert die Klasse "Algorithmen"
        print("\n==== Im Menüpunkt 'Algorithmen' ====")
        print("Menüpunkte:" +
              "\n1. Wiederholte Quersummen" + 
              "\n2. Aufzählen und Überprüfen" + 
              "\n3. Sortierung mit Bubblesort/ Laufzeit" + 
              "\n4. Durchsuchen einer Liste mit Rekursion" +
              "\n5. Histogramm einer Liste" +
              "\n6. Durchsuchen eines Strings mit regulären Ausdrücken" +
              "\n7. Zurück zum Hauptmenü")

        menu = input("Punkt auswählen: ")

        if menu == "1":
            print("\nEs wird die wiederholte Quersumme der eingegebenen " +
                  "Zahl berechnet.")
            zahl = int(input("Zahl eingeben: "))
            print("Die wiederholte Quersumme der Zahl " + str(zahl) +
                  " ist: " + str(Algorithmen.rep_qs(zahl)))
            Algorithmen.menu()
            
        elif menu == "2":
            print("\nEs werden die ersten n Zahlen und deren Häufigkeit " +
                  "ausgegeben, dessen wiederholte Quersumme der ersten " +
                  "Ziffern der letzten Ziffer entsprechen" +
                  "\nBeispiel: 1282, da 1+2+8=11 und 1+1=2")
            bound = int(input("n = "))
            
            res = Algorithmen.new_rep_qs(bound)
            print("Anzahl: " + str(res[0]) + "\nZahlen:" + str(res[1]))
            Algorithmen.menu()
            
        elif menu == "3":
            print("\nEine zufällig generierte Liste wird mit Bubblesort " +
                  "sortiert. Die Laufzeit wird auch angezeigt.\n")
            Algorithmen.bubbleSortLaufzeit()
            Algorithmen.menu()
            
        elif menu == "4":
            print("\nEs wird geprüft, ob eine zufällige Liste " +
                  "Elemente enthält, die sich zu Null addieren.\n")
            Algorithmen.init()
            Algorithmen.menu()
            
        elif menu == "5":
            print("\nDas Histogramm einer zufälligen Liste wird " +
                  "erzeugt.")
            Algorithmen.histogram()
            Algorithmen.menu()
            
        elif menu == "6":
            Algorithmen.initRegEx()
            Algorithmen.menu()
            
        elif menu == "7":
            Hauptmenu.menu()
            
        else:
            print("Ungültige Eingabe")
            Algorithmen.menu()

class Datenbank:
    
    def init():
        # Verbindung mit der Datenbank
        db = sqlite3.connect("chinook.db")
        cur = db.cursor()
        Datenbank.menu(db, cur)

    def show(db, cur):
        # Zeigt alle Tabellen der Datenbank an
        print("\nTabellen:")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()

        for i in range(len(tables)):
            print(i, tables[i][0])

    def inspect(db, cur):
        # Die Spaltennamen und sämtliche Inhalte einer Tabelle werden
        # angezeigt.
        try:
            option = str(input("Tabelle auswählen: "))
            cur.execute("PRAGMA table_info("+option+");")
            headers = cur.fetchall()

            for i in range(len(headers)):
                print(headers[i][1], end=" | ")

            cur.execute("SELECT * FROM " + option + ";")
            content = cur.fetchall()

            for i in range(len(content)):
                print("")
                for j in range(len(content[i])):
                    print(content[i][j], end=" | ")

        except:
            print("Tabelle nicht gefunden\n")

    def comm(db, cur):
        # Ein beliebiger sqlite3 Befehl wird ausgeführt
        print("Hinweis: Befehl muss in sqlite3 geschrieben werden.")
        try:
            sql = input("Anfrage: ")
            cur.execute(sql)
            content = cur.fetchall()
            print(content)
            db.commit()

        except:
            print("Falscher Befehl.")
                       
    def menu(db, cur):
        print("\n==== Im Menüpunkt 'Datenbanken' ====")
        print("Menüpunkte:")
        print("1: Tabellen anzeigen\n2: Tabelleninhalte einsehen\n3: SQL Anfrage\n"+
              "4: Schliessen")

        menu = input("Auswahl: ")
            
        if menu == "1":
            Datenbank.show(db, cur)
            Datenbank.menu(db, cur)
                        
        elif menu == "2":
            Datenbank.inspect(db, cur)
            Datenbank.menu(db, cur)

        elif menu == "3":
            Datenbank.comm(db, cur)
            Datenbank.menu(db, cur)
                
        elif menu == "4":
            db.close()
            print("Datenbank geschlossen.\n")
            Hauptmenu.menu()
            
        else:
            print("Keine gültige Eingabe!\n")
            Datenbank.menu(db, cur)

class Hauptmenu:

    def menu():
        print("\n==== Hauptmenü ====")
        print("1. Rechner" + 
              "\n2. Algorithmen" + 
              "\n3. Interaktion mit einer Datenbank" +
              "\n4. Programm beenden")
        menu = input("Punkt auswählen: ")

        if menu == "1":
            Rechner.menu()

        elif menu == "2":
            Algorithmen.menu()

        elif menu == "3":
            Datenbank.init()
            
        elif menu == "4":
            print("Beendet.")

        else:
            print("Ungültige Eingabe!\n")
            Hauptmenu.menu()
            
Hauptmenu.menu()
