"""
Dana jest lista zleceń. Każde zlecenie wymaga pewnego kapitału początkowego Ci, który należy mieć, żeby zacząć zlecenie
oraz zysk Pi, który doda się do naszego całkowitego kapitału, gdy wykonamy zlecenie. Mając kapitał początkowy W i liczbę
k wybierz co najwyżej k zleceń tak, że skończysz z maksymalnym możliwym kapitałem.
Przykład: k = 2, W = 0, P=[1,2,3], C=[0,1,1]. Rozwiązanie: na początku mamy kapitał 0, więc możemy wybrać tylko zlecenie
pierwsze. Po jego ukończeniu mamy kapitał równy 1, więc możemy wybrać albo zlecenie 2 albo 3. Zlecenie 3 ma większy
profit więc wybieramy zlecenie 3, ponieważ możemy wybrać już tylko 1 zlecenie (k = 2). Kończymy z kapitałem 4.
"""
