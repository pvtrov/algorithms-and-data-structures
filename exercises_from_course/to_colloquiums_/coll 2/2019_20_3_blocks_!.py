"""
Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany jest jako jednostronnie domknięty przedział (ai, bi],
gdzie ai, bi ∈ N, i ma wysokość 1 (należy założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie,
czyli wartości ai są parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek
dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i przestaje spadać. Kolejność spadania
klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, albo w całości ląduje na innych klockach.
Rozważmy przykładowy zbiór klocków K = {K1, K2, K3, K4}, gdzie:

K1 = (2, 4], K2 = (5, 7], K3 = (3, 6], K4 = (4, 5].

Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy kolejność K1, K2, K3, K4
poprawna nie jest (K3 nie leży w całości na innych klockach)

Proszę podać algorytm (bez implementacji), który sprawdza czy dla danego zbioru klocków
istnieje poprawna kolejność spadania. Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność.
"""