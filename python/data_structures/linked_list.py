
class SList:
    def __init__(self):
        self.head = None

    def insert_at(self, val, n):
        if self.head.next == None:
            self.add_to_front(val)
            return self
        index = 1
        runner = self.head
        new_node = SLNode(val)
        # index and n are the nth element of list
        # 1: 1st Element, 2: 2nd Element
        while (index < n):
            if (n - index) == 1:
                temp = runner.next
                runner.next = new_node
                new_node.next = temp
                break
            runner = runner.next
            index += 1
        return self

    # Adding

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next, self.head = self.head, new_node
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    # Removing
    def remove_from_front(self):
        if self.head == None:
            return False

        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return False
        if self.head.next == None:
            self.head = None
            return False
        runner = self.head
        while (runner.next != None):
            runner = runner.next
            if runner.next.next == None:
                runner.next = None
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


# Let's test our class!

my_list = SList()  # create a new instance of a list
my_list.add_to_front("are")
my_list.add_to_front("Linked lists")
my_list.add_to_back("fun!")
# my_list.print_values()

# chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

# my_list.remove_from_back()
# my_list.print_values()

my_list.insert_at("haha", 2)
my_list.print_values()
