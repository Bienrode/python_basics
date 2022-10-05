daten = "vorname, nachname, alter"
#daten = "vorname; nachname; alter"
#daten = '"vorname";"nachname";"alter"'
print (daten)
einzeldaten = daten.split(",")
print(einzeldaten)
einzeldaten = daten.split(", ")
print(einzeldaten)

einzeldaten = daten.split(";")
print(einzeldaten)
ausgabe = daten.split('; ')
print (ausgabe)

daten1 = daten.strip('"')
print (daten1)
ausgabe = daten1.split('";"')
print (ausgabe)
