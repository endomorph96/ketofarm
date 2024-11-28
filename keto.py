# # main.py
# # Aufgabe 1
# # Ganze Zahlen (int)
# integer_literal = 42
#
# # Gleitkommazahlen (float)
# float_literal = 3.14
#
# # Zeichenfolgen (str)
# string_literal = "Hallo, Python!"
#
# # Booleans (bool)
# boolean_literal_true = True
# boolean_literal_false = False
#
# # Listen (list)
# list_literal = [1, 2, 3, "Python", 4.5, True]
#
# # Ausgabe der Literale
# print("Integer Literal:", integer_literal)
# print("Float Literal:", float_literal)
# print("String Literal:", string_literal)
# print("Boolean Literal (True):", boolean_literal_true)
# print("Boolean Literal (False):", boolean_literal_false)
# print("List Literal:", list_literal)
#
# #Aufgabe 2
# # Speichert die Anzahl der Schüler in einer Klasse
# number_of_students = 30
#
# # Speichert den Durchschnitt der Noten einer Prüfung
# average_grade = 85.7
#
# # Enthält den Namen des besten Schülers
# top_student_name = "Aslam Dozent"
#
# # Gibt an, ob die Prüfung bestanden wurde (True = bestanden, False = nicht bestanden)
# exam_passed = True
#
# # Speichert eine Liste mit den Noten aller Schüler
# grades_list = [95, 87, 78, 88, 92]
#
# # Ausgabe der Variablen
# print("Anzahl der Schüler:", number_of_students)
# print("Durchschnittsnote:", average_grade)
# print("Bester Schüler:", top_student_name)
# print("Prüfung bestanden:", exam_passed)
# print("Notenliste:", grades_list)


#Aufgabe 3

# # Globale Variable
# wert1 = 42
#
# def beispiel_funktion():
#     global wert1  # Zugriff auf die globale Variable
#     print(f"Globale Variable innerhalb der Funktion: {wert1}")
#
#     # Lokale Variable mit demselben Namen
#     global wert2  # "global" wandelt eine Lokale Variable in eine globale Variable um.
#     wert2 = 100
#     print(f"Lokale Variable innerhalb der Funktion: {wert2}")
#
#     # Lokale Variable mit demselben Namen
#     wert3 = 200
#     print(f"Lokale Variable innerhalb der Funktion: {wert3}")
#
#
#
# # Aufruf der Funktion
# beispiel_funktion()
#
# # Ausgabe der globalen Variable außerhalb der Funktion
# print(f"Globale Variable außerhalb der Funktion: {wert1}") # "f" ermöglicht es in einem Text eine variable einzubauen mit {variable}.
# print(f"Globale Variable außerhalb der Funktion: {wert2}")
# # Dieser Werte würde so nicht ausgegeben werden, weil er Lokal und nicht Global ist ->>> print(f"Globale Variable außerhalb der Funktion: {wert3}")
#

# # Aufgabe 4
# def äußere_funktion():
#     wert = 10  # Variable im Namensraum der äußeren Funktion
#
#     def innere_funktion():
#         nonlocal wert  # Zugriff auf die Variable der äußeren Funktion
#         wert += 5
#         print(f"Wert innerhalb der inneren Funktion: {wert}")
#
#     print(f"Wert vor dem Aufruf der inneren Funktion: {wert}")
#     innere_funktion()
#     print(f"Wert nach dem Aufruf der inneren Funktion: {wert}")
#
# # Aufruf der äußeren Funktion
# äußere_funktion()

# # Aufgabe 5
#
# # Aufgabe 1: Verwendung von len() und type()
# text = "Hallo, Welt!"
# zahlen = [1, 2, 3, 4, 5, "Das ist eine Liste"]
#
# print(f"Länge von 'text': {len(text)}")  # Gibt die Länge des Strings aus (Leerzeichen zählen mit)
# print(f"Typ von 'text': {type(text)}")  # Gibt den Typ der Variable aus
#
# print(f"Länge von 'zahlen': {len(zahlen)}")  # Gibt die Länge der Liste aus
# print(f"Typ von 'zahlen': {type(zahlen)}")  # Gibt den Typ der Variable aus
#
# # Aufgabe 2: Verwendung von sum(), max() und min()
# werte = [10, 20, 5, 40, 15]
#
# print(f"Summe der Werte: {sum(werte)}")  # Gibt die Summe der Listenelemente aus
# print(f"Summe der Werte: {sum(werte)}")  # Gibt die Summe der Listenelemente aus
# print(f"Maximalwert: {max(werte)}")     # Gibt den größten Wert der Liste aus
# print(f"Minimalwert: {min(werte)}")     # Gibt den kleinsten Wert der Liste aus
#
# # Aufgabe 3: Verwendung von sorted()
# unsortiert = [8, 3, 7, 1, 9, 4]
# sortiert_aufsteigend = sorted(unsortiert)  # Sortiert die Liste in aufsteigender Reihenfolge
# sortiert_absteigend = sorted(unsortiert, reverse=True)  # Sortiert in absteigender Reihenfolge
#
# print(f"Unsortierte Liste: {unsortiert}")
# print(f"Sortierte Liste (aufsteigend): {sortiert_aufsteigend}")
# print(f"Sortierte Liste (absteigend): {sortiert_absteigend}")
