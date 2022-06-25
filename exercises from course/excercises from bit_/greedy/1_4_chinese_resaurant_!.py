"""
W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem. Prowincję
można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę, a wartość 0,
że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i, to miasta o indeksach j
takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn potrzeba
aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.
"""