# kubełki na listach

class Node():

    def __init__(self):
        self.value = None
        self.next = None


def tab_to_list(array):
    h = Node()
    c = h
    for i in range(len(array)):
        x = Node()
        x.value = array[i]
        c.next = x
        c = x

    return h.next


def print_list(list):
    while list is not None:
        print(list.value, "->", end=" ")
        list = list.next
    print("|")


def insertion_sort(bucket):
    if bucket.next is None:
        return None
    sorted_list = bucket
    bucket = bucket.next
    sorted_list.next = None
    while bucket is not None:
        current = bucket
        bucket = bucket.next
        if current.value < sorted_list.value:
            current.next = sorted_list
            sorted_list = current
        else:
            search = sorted_list
            while search.next is not None and current.value > search.next.value:
                search = search.next
            current.next = search.next
            search.next = current
    return sorted_list


def bucket_sort(head):
    length = 0
    counter_head = head
    while counter_head is not None:
        length += 1
        counter_head = counter_head.next

    section = 10 / length
    buckets = [Node for _ in range(length)]
    counter_head = head
    while counter_head is not None:  # wkładam elementy do dobrych kubeczków
        index = int(counter_head.value / section)
        temporary = buckets[index]
        while temporary.next is not None:
            temporary = temporary.next
        temporary.next = counter_head
        counter_head = counter_head.next
        temporary = temporary.next
        temporary.next = None

    for i in range(len(buckets)):  # sortuje każdy kubeczek
        if buckets[i].next is not None:
            if buckets[i].next.next is None:
                buckets[i] = buckets[i].next
            else:
                buckets[i] = insertion_sort(buckets[i].next)

    final_list = buckets[0]
    helper = final_list
    for i in range(1, len(buckets)):
        if buckets[i].value is not None:
            while helper.next is not None:
                helper = helper.next
            helper.next = buckets[i]
            helper = helper.next
    return final_list