#teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - ‚'
#teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#teststring = ' <html> ist eine tolle Sprache</html> '
teststring = "Hacker schleusen auch gerne Code ein! test()"
#teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#teststring = "Oder am Ende von Eingaben "
#teststring = "Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n"
#teststring = "<dieser String ist nun sanitized>"

#Leerzeichen am Anfang und Ende, sicher entfernen

sani1 = teststring.strip('')
print('Bereinigter String ohne Leerzeichen:\n' + sani1)
#Klammern entfernen !

sani2 = teststring.strip('()')
print('Bereinigter Text ohne Klammern () 2:\n' + sani2)
# Klammern und Leerzeichen (\<\>)  entfernen

sani3 = sani1.strip('\<\>')
print('Bereinigter Text ohne (\<\>) 3:\n' + sani3)

# Sonderzeichen für Programmierung am Ende entfernen!

sani4 = sani3.strip('; -“')
print('Bereinigter Text ohne Sonderzeichen (; -“) 4:\n' + sani4)
