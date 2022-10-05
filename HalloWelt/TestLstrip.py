# lstrip()


inhalt = " Python rocks "
ausgabe = inhalt.lstrip()
print(ausgabe)

print(ausgabe + ", daher Python lernen")

inhalt = "321 Python 3 rocks"
ausgabe = inhalt.lstrip('123')
print(ausgabe)

inhalt = "321 Python 3 rocks"
ausgabe = inhalt.lstrip('1234')
print(ausgabe)

#  strip()

inhalt = " Python lernen "
ausgabe = inhalt.strip()
print(ausgabe)


inhalt = "1.) Python lernen "
ausgabe = inhalt.strip('1')
print(ausgabe)

inhalt = "1.) Python lernen "
ausgabe = inhalt.strip('123')
print(ausgabe)

inhalt = "1.) python lernen "
ausgabe = inhalt.strip('.) 1234567890')
print(ausgabe)

# rstrip()




