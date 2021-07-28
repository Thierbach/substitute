# substitute
Das Python Script eliminiert alle kontextfreien Begriffe auf Basis der top 10000 Wörter 
https://de.wikipedia.org/wiki/Liste_der_h%C3%A4ufigsten_W%C3%B6rter_der_deutschen_Sprache
der Deutschen Sprache (UNI Leipzig
http://pcai056.informatik.uni-leipzig.de/downloads/etc/legacy/Papers/top10000de.txt)
aus einem gegebenen Dokument. Übrig bleiben dann die kontextbehafteten Wörter, die für das 
Dokument (z.B. Mietvertrag.txt) relevant sind.

Um repräsentative Werte zur Klassifizierung zu erhalten, müssen in diesem Fall einige Mietverträge
analysiert werden. Alle Ergebnisse (= die kontextbezogenen Wörter) können in einer Textdatei 
gespeichert werden.

Die statistische Auswertung erfolgt dann durch den Linux Bash Befehl

sort test.txt | uniq -c | sort -nr

Als Ausgabe erhält man eine sortierte Liste mit Anzahl der Treffer pro Wört.
