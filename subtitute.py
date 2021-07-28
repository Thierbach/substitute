'''
Dieser Code entfernt aus einer Textdatei die 10.000 kontextfreien Begriffe (UNI Leipzig
http://pcai056.informatik.uni-leipzig.de/downloads/etc/legacy/Papers/top10000de.txt)
sowie die alle Ziffern und Interpunktions- und Sonderzeichenzeichen
23.07.2021 @ tt51
'''

import time

startTime = (time.time())
# lade die Textdatei
with open ('Wohnungs-Mietvertrag.txt', 'r') as fileOCR:
    textOCR = fileOCR.read()
    # entferne die folgenden Zeichen
    specialChars = """!#$%^'&*()-—.,‚;:|/_[]?"“„0123456789"""
    for specialChar in specialChars:
        textOCR = textOCR.replace(specialChar, '')
    # print(textOCR)

# lade die 10.000 kontextfreien Begriffe
with open('top10000de.txt', 'rb') as file:
# with open('german.dic', 'rb') as file:
    contextWords = file.read().split()
    # print(contextWords)

# iteriere durch die OCR-Textdatei und prüfe geben die kontextfreien Begriffe
textWords = textOCR.split()
resultWords = [word for word in textWords if word.encode('utf-8') not in contextWords]
result = sorted(set(resultWords))

# prüfe Ergebnis gegen Verben mit Großnuchstaben am Anfang gegen die kontextfreien Begriffe
resultWords = [word for word in result if word.lower().encode('utf-8') not in contextWords]
result = sorted(set(resultWords))

substantive = []
for i in result:
    if i[0] == i[0].upper():
        substantive.append(i)

print(substantive)

print('Die Originaldatei hat', len(textWords), 'Wörter!')
print('Wir haben', len(substantive), 'kontextspezifische Einträge gefunden!')
# print('Wir haben', len(result), 'kontextspezifische Einträge gefunden!')

# räume auf

file.close()
fileOCR.close()

endTime = (time.time())

print('Latenz:', endTime - startTime)




