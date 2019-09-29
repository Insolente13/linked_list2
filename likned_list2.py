class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    '''2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.'''
    def find(self, val):
        node = self.head
        f_node = None
        while node is not None:
            if node.value == val:
                f_node = node
                break
            node = node.next
        return f_node

    '''2.2. Добавьте в класс LinkedList2 метод поиска всех узлов 
    по конкретному значению (возвращается список найденных узлов).'''
    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list
    '''2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
    delete(val, all=False)
    где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.'''
    def delete(self, val, all=False):
        break_point = 0
        node = self.head

        while node is not None:
            #  удаляем первое и единственное
            if node.value == val and node.next is None and node.prev is None:
                self.head = None
                self.tail = None
                break_point += 1
            #  удаляем первое и НЕ единственное
            elif node.value == val and node.next is not None and node.prev is None:
                self.head = node.next
                self.head.prev = None
                break_point += 1
            #  удаляем последнее и НЕ единственное
            elif node.value != val and node.next is not None:
                if node.next.value == val and node.next.next is None:
                    node.next = None
                    self.tail = node
                    break_point += 1
                elif node.next.value == val and node.next.next is not None:
                    while node.next.value == val and node.next.next is not None:
                        if all is False and break_point != 0:
                            break
                        node.next.next.prev = node
                        node.next = node.next.next
                        break_point += 1

            if all == False and break_point != 0:
                break
            node = node.next

    '''2.7. Добавьте в класс LinkedList2 метод очистки 
    всего содержимого (создание пустого списка) -- clean()'''
    def clean(self):
        self.head = None
        self.tail = None

    '''2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()'''
    def len(self):
        node = self.head
        count_node = 0
        while node is not None:
            count_node += 1
            node = node.next
        return count_node  # здесь будет ваш код

    '''2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    insert(afterNode, newNode)
    Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
    Если afterNode = None и список непустой, добавьте новый элемент последним в списке.'''
    def insert(self, afterNode, newNode):
        #  Добавить вначало, если afterNode is None и список пустой
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        #  Добавить вконец, если afterNode is None и НЕ список пустой
        elif afterNode is None and self.head is not None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        elif afterNode is not None and self.head is not None:
            node = self.head
            while node is not None:
                #  Добавляем в конец, если список завершался на afterNode
                if node.value == afterNode.value and node.next is None:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                    self.tail = newNode
                    break
                #  Добавляем в середину, если afterNode в середине списка
                elif node.value == afterNode.value and node.next is not None:
                    node_next = node.next
                    node_prev = node
                    newNode.prev = node_prev
                    node.next = newNode
                    newNode.next = node_next
                    node_next.prev = newNode
                    break
                node = node.next

        else:
            return None

    '''2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.'''
    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            head_before = self.head
            newNode.next = head_before
            head_before.prev = newNode
            self.head = newNode

   
