"""
W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie niż na realnej odległości między
dwoma punktami. Mamy mapę Krakowa, między skrzyżowaniami na ulicach są zaznaczone odległości i czasy przejazdu.
W Krakowie (jak wszyscy wiemy ;) ) są ulice jedno- i dwukierunkowe. Kierowcy potrzebują aplikacji, która pomoże im
znajdować drogi, które pozwalają dotrzeć ze skrzyżowania A do B w jak najkrótszym czasie, a spośród tych o najmniejszym
czasie wybiera i zwraca najkrótszą pod względem odległości.
Mamy przetworzyć Q zapytań w postaci (skrzyżowanieA, skrzyżowanieB) i na każde z nich odpowiedzieć parą (czas, dystans)
najlepszej drogi. Wszystkie zapytania odnoszą się do tego samego grafu.
Jakie rozwiązanie daje najlepszą klasę złożoności w każdym z poniższych przypadków?
Q = O(1), E = O(V)
Q = O(1), E = O(V^2)
Q = O(V), E = O(V)
Q = O(V), E = O(V^2)
"""