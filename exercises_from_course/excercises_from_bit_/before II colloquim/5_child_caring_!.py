"""
Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary, reprezentujące czas rozpoczęcia
i zakończenia danej aktywności. Zaimplementuj algorytm, który przyporządkuje każdej aktywności literę C lub J, oznaczającą,
że daną aktywność z synem wykona odpowiednio Cersei lub Jaime, w taki sposób, że żaden rodzic nie wykonuje pokrywających
się czasowo aktywności. Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”, a jeśli istnieje,
to zwraca odpowiedniego stringa.
Przykładowo: (99, 150), (1, 100), (100, 301), (2,5), (150, 250) - odpowiedź to JCCJJ (lub CJJCC).
"""