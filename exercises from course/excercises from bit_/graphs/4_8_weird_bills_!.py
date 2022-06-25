"""
Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana.
Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata.
Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku podróży
(jeśli jest ujemny, po prostu nic się nie płaci).

Np. na trasie 1-2-3-5 opłaty wyniosą kolejno: 60+20+0, a na trasie 1-4-5 będzie to 120+30

Mając dane:
1) graf połączeń w dowolnej reprezentacji (nieskierowany, ważony)
2) numery stacji początkowej i docelowej

Oblicz minimalny koszt przejechania tej trasy.
"""