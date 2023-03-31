# animal-bones
Hausarbeit für Modul "Informatik in den Geistes- und Kulturwissenschaften"

> [!note] Animal Bone Metrical Archive Project (ABMAP) - Überblick
> Datenbank mit Knochenmaßen domestizierter Tieren
> Zusammengetragen aus mehr als 100 archäologischen Fundenstellen
> **Fundort:** Südengland 
> **Zeitspanne:** Bronzezeit (2200 v.Chr.) - heute

# Überblick
Alle Daten stammen aus dem [Animal Bone Metrical Archive Project (ABMAP)](https://archaeologydataservice.ac.uk/archives/view/abmap/).
Der Datensatz enthält insgesamt knapp 61 000 Maße von über 24 700 Knochen aus mehr als 100 archäologischen Sammlungen. Alle Knochen wurden in Südengland gefunde und umfassen eine Zeitspanne von 1000 v.Chr. bis heute. Hauptsächlich sind Knochen von Schafen, Ziegen und Rindern enthalten, aber es sind auch Daten von Schweinen, Pferden, Hunden, Hühnern, Gänsen und Katzen verfügbar. 

## Erfasste Merkmale
Der Datensatz ist multivariat, d.h. für jeden Knochen wurden mehrere Merkmale erfasst:
Jeder Datenpunkt ist ein Maß ('MEASURE') in $mm$ einer bestimmten Messart ('MEASTYPE') und wurde einem Knochen zugeordnet, wobei ein Knochen mehrere Maße haben kann. 
Jeder Knochen hat eine eindeutige ID ('BONEID') und wurde einer Spezies zugeordnet ('SPECIES'). Außerdem wird angegeben, um welchen Knochentyp es sich jeweils handelt ('ELEMENT') und von welcher Körperseite er stammt ('SIDE').
Jeder Eintrag wurde absoult datiert ('RANGE') und einer Periode der Urgeschichte zugeordnet ('PERIOD') . 
Zusätzlich wurde jeweils der Fundort verzeichnet ('SITECODE', 'SITE', 'COUNTY') und woher die ursprünglichen Daten stammen ('REFERENCE')
Zum Datenmanagement sind noch einige Metadaten verfügbar.

## Probleme und Lösungsansätze
1. Die Daten sind nur über eine Online-Datenbank verfügbar - Pro Query lassen sich maximal 10.000 Ergebnisse herunterladen
   &rarr; Fokus auf eine Tierart
   &rarr; Für Pferde gibt es < 10.000 Einträge (3.099)

2. Die Funde konnten teilweise nur sehr grob datiert werden
   &rarr; Mit gewissen Ungenauigkeiten leben

3. Es wurden viele unterschiedliche Maß-Dimensionen benutzt (z.B. Längen, Breiten und Umfänge zwischen verschiednen Fixpunkten am Knochen)
   - Das macht einen Vergleich extrem schwierig
   - Idee: Für jeden Knochentyp nur die am häufigsten vorhandene Dimension vergleichen oder, wenn möglich, jeweils Längen und Breiten zusammenfassen

4. Größenunterschiede können verschiedene Ursachen haben, z.B. Alter oder Rasse
	- Jungtiere sind kleiner als ausgewachsene, aber Altersangaben fehlen - Das Ausschließen von Jungtierknochen ist häufig unmöglich und oft statistisch vernachlässigbar (s. Driesch1976)
	- Verschiedene Rassen = verschiedene Größen (z.B. Shetland Pony vs. Shire Horse)
	&rarr; Fragestellung entsprechend anpassen
	&rarr; Mit Ungenauigkeiten leben

## Mögliche Fragestellungen
- Lässt sich anhand der Knochenmaße seit der Bronzezeit ein Trend in der Größenentwicklung von domestizierten Pferden erkennen?
- Wurden zu bestimmten Zeitpunkten eher größere/kräftigere Rassen bevorzugt? Lässt sich vom Zeitpunkt auf mögliche Gründe schließen? (Fleisch, Arbeitskraft, Krieg, ...)
