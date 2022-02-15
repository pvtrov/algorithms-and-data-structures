"""
Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim
"""

""" robimy jak LIS, tylko zamiast mnijeszy/wieszy robimy przedzialowo, i potem te klocki które nie są w podciągu usuwamy"""
