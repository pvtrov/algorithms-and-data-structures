"""
Definiujemy relację znajomości między osobami jako symetryczną.

Znajomość:
1) pierwszego stopnia to bezpośrednia znajomość osoby
2) drugiego stopnia to bycie “znajomym znajomego” osoby, ale nie bezpośrednim znajomym osoby
3) trzeciego, czwartego, piątego stopnia, itd.
4) nieskończonego stopnia zachodzi wtedy gdy nie ma ciągu znajomości, który łączyłby dwie osoby

Mając na wejściu listę osób i znajomości pierwszego stopnia między nimi, chcemy znaleźć największy stopień znajomości
wśród każdej z możliwych par.
Znajdź optymalne rozwiązanie zarówno dla grafów rzadkich (|E| = O(|V|)), jak i gęstych (|E| = O(|V|^2)
"""