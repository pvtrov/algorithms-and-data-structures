"""
Student chce wypuścić n różnych pok´emonów (numerowanych od 0 do n − 1) z klatek
(pok´eball’i). Wypuszczony Pok´emon natychmiast atakuje swojego wybawiciela, chyba że (a) jest
spokojny, lub (b) w okolicy znajdują się co najmniej dwa uwolnione pok´emony, na które ten
pok´emon poluje. Proszę zaimplementować funkcję:

int* releaseThemAll( HuntingList* list, int n ),

gdzie list to lista z informacją, które pok´emony polują na które (lista nie zawiera powtórzeń):
struct HuntingList {
    HuntingList* next; // następny element listy
    int predator; // numer pokemona, który poluje
    int prey; } // numer pokemona, na którego poluje

Funkcja powinna zwrócić n elementową tablicę z numerami pok´emonów w kolejności
wypuszczania (tak, żeby wypuszczający nie został zaatakowany) lub NULL jeśli taka kolejność nie
istnieje. Każdy wypuszczony pok´emon zostaje ”w okolicy”. Jeśli pok´emon nie występuje na liście
jako predator to znaczy, że jest spokojny. Zaimplementowana funkcja powinna być możliwie jak
najszybsza. Proszę krótko oszacować jej złożoność
"""
"""
O(n^2logn) -> wyjebana no
"""

def tab_to_list(array):
    for i in range(len(array)-1):
        array[i].next = array[i+1]
    array[-1].next = None
    return array[0]


class Pokemon:
    def __init__(self, int, prays):
        self.next = None
        self.predator = int
        self.pray = prays


def at_least_two(released, temp):
    counter = 0

    index = 0
    while index < len(temp.pray):
        key = temp.pray[index]
        if released[key] is True:
            counter += 1
            if counter >= 2:
                return True
        index += 1
    return False


def release_them_all(pokemon, n):
    queue_of_releasing = []
    releases = {}

    temp_head = pokemon
    while temp_head is not None:        # realising only calm pokemons and adding released to dictionary  O(n)
        if temp_head.pray is None:
            queue_of_releasing.append(temp_head.predator)
            releases[temp_head.predator] = True
        elif len(temp_head.pray) == 1:
            return None
        else:
            releases[temp_head.predator] = False
        temp_head = temp_head.next

    temp = pokemon
    while temp is not None:
        if not releases[temp.predator]:
            if at_least_two(releases, temp):
                queue_of_releasing.append(temp.predator)
                releases[temp.predator] = True
                temp = pokemon
            else:
                temp = temp.next
        else:
            temp = temp.next

    if len(queue_of_releasing) < n:
        return None
    else:
        return queue_of_releasing


hunting_lists = [Pokemon(1, [2, 6]), Pokemon(2, [4]), Pokemon(3, None), Pokemon(4, None), Pokemon(5, None), Pokemon(6, [3, 4])]
print(release_them_all(tab_to_list(hunting_lists), 6))

