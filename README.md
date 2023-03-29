# animal-bones
Hausarbeit für Modul "Informatik in den Geistes- und Kulturwissenschaften"

# Überblick

Der Datensatz des [Animal Bones Metrical Archive](https://archaeologydataservice.ac.uk/archives/view/abmap/index.cfm) enthält knapp 61 000 Maße von über 24 700 Knochen. Hauptsächlich sind Knochen von Schafen, Ziegen und Rindern enthalten, aber es sind auch Daten von Schweinen, Pferden, Hunden, Hühnern, Gänsen und Katzen verfügbar.
Die in den Daten erfassten Merkmale beschreiben bei archäologischen Ausgrabungen gefundene Knochen. Der Datensatz ist multivariat, d.h. für jeden Knochen wurden mehrere (genau 17) Merkmale erfasst.

### Erfasste Merkmale
Jeder Datenpunkt ist ein Maß ('MEASURE') in $mm$ einer bestimmten Messart ('MEASTYPE') und wurde einem Knochen zugeordnet, wobei ein Knochen mehrere Maße haben kann. 
Jeder Knochen hat eine eindeutige ID ('BONEID') und wurde einer Spezies zugeordnet ('SPECIES'). Außerdem wird angegeben, um welchen Knochentyp es sich jeweils handelt ('ELEMENT') und von welcher Körperseite er stammt ('SIDE').
Jeder Eintrag wurde absoult datiert ('RANGE') und einer Periode der Urgeschichte zugeordnet ('PERIOD') . 
Zusätzlich wurde jeweils der Fundort verzeichnet ('SITECODE', 'SITE', 'COUNTY') und woher die ursprünglichen Daten stammen ('REFERENCE')
Zum Datenmanagement sind noch einige Metadaten verfügbar.

## Probleme und Lösungsansätze
1. Die Daten sind nur über Online-Datenbank verfügbar - Pro Query lassen sich maximal 10.000 Ergebnisse herunterladen
   &rarr; Fokus auf eine Tierart
   &rarr; für Pferde gibt es < 10.000 Einträge (3.099)

2. Die Funde konnten teilweise nur sehr grob datiert werden
   &rarr; Mit gewissen Ungenauigkeiten leben

3. Es wurden viele unterschiedliche Messarten benutzt (Länge, Breite, Umfang, Breite an einer bestimmten Stelle eines Knochens, etc.)
   - das macht einen Vergleich extrem schwierig
   - evt. ein Messart nehmen, was bei vielen benutzt wurde und nur diese Maße miteinander vergleichen? Oder jeweils Längen und Breiten zusammenfassen wenn möglich?

4. Größenunterschiede können verschiedene Ursachen haben, z.B. Alter oder Rasse
	- Jungtiere sind kleiner als ausgewachsene, aber Altersangaben fehlen
	- Verschiedene Rassen = verschiedene Größen (z.B. Shetland Pony vs. Shire Horse)
	&rarr; Fragestellung entsprechend anpassen

## Mögliche Fragestellungen
- Lässt sich anhand der Knochenmaße seit der Bronzezeit ein Trend in der Größenentwicklung von domestizierten Pferden erkennen?
- Wurden zu bestimmten Zeitpunkten eher größere/kräftigere Rassen bevorzugt? Lässt sich vom Zeitpunkt auf mögliche Gründe schließen? (Fleisch, Arbeit, Krieg, ...)
