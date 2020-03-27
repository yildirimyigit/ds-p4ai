# Single link, Queue and Stack


class Element:

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __repr__(self):
        return self.data.__repr__()


class Queue:

    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        if not self.top:
            self.top = Element(data)
            self.last = self.top
        else:
            self.last.next = Element(data)
            self.last = self.last.next

        self.size += 1

    def dequeue(self):
        if self.empty():
            return None

        top = self.top
        self.size -= 1

        self.top = self.top.next

        if self.size == 0:
            self.top = None
            self.last = None

        return top

    def peek(self):
        return self.top

    def empty(self):
        return self.size == 0

    def __repr__(self):
        m_repr = '[' + self.top.__repr__()
        cur = self.top.next
        for _ in range(self.size-1):
            m_repr += ', ' + cur.__repr__()
            cur = cur.next
        return m_repr + ']'


class Stack:

    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def push(self, data):
        if not self.last:
            self.last = Element(data)
            self.top = self.last
        else:
            self.last = Element(data, self.last)

        self.size += 1

    def pop(self):
        if self.empty():
            return None

        last = self.last
        self.size -= 1

        self.last = self.last.next

        if self.size == 0:
            self.top = None
            self.last = None

        return last

    def top(self):
        return self.last

    def empty(self):
        return self.size == 0

    def __repr__(self):
        m_repr = '[' + self.last.__repr__()
        cur = self.last.next
        for _ in range(self.size-1):
            m_repr += ', ' + cur.__repr__()
            cur = cur.next
        return m_repr + ']'


def queue_test():
    input_queue = Queue()

    input_queue.enqueue('DOWN')
    input_queue.enqueue('RIGHT')
    input_queue.enqueue('B')

    print(input_queue)
    print(input_queue.dequeue()) # 'DOWN'

    print(input_queue)
    print(input_queue.dequeue()) # 'RIGHT'

    print(input_queue)
    print(input_queue.dequeue()) # 'B'

    try:
        print(input_queue.dequeue().data)
    except Exception as e:
        print("Queue Empty")

# queue_test()


def stack_test():
    input_stack = Stack()

    input_stack.push('DOWN')
    input_stack.push('RIGHT')
    input_stack.push('B')

    print(input_stack)
    print(input_stack.pop()) # 'B'

    print(input_stack)
    print(input_stack.pop()) # 'RIGHT'

    print(input_stack)
    print(input_stack.pop()) # 'DOWN'

    try:
        print(input_stack.pop().data)
    except Exception as e:
        print("Stack Empty")

# stack_test()


def list_stack():
    m_list = []

    m_list.append('DOWN')
    m_list.append('RIGHT')
    m_list.append('B')

    print(m_list.pop()) # 'B'

    print(m_list[-1])
    m_list[-1] = None

    print(m_list.pop()) # 'RIGHT'

    print(m_list.pop()) # 'DOWN'

# Questions


def balanced_parenthesis(math_op):
    mem = Stack()

    for c in math_op:
        if c == '(':
            mem.push(c)
        elif c == ')':
            if mem.empty():
                return False
            mem.pop()

    return mem.empty()


print(balanced_parenthesis("(a+(b-c))"))
print(balanced_parenthesis("(a+b-c))"))
print(balanced_parenthesis("((a+b-c)"))

print(balanced_parenthesis(")a+b-c("))
# Double link, Queue and Stack


class DoubleElement(Element):

    def __init__(self, data, _next=None, _prev= None):
        super().__init__(data, _next)
        self.prev = _prev

    def __repr__(self):
        return self.data.__repr__()


class DoubleLinkList:

    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def append(self, data):
        if not self.top:
            self.top = DoubleElement(data)
            self.last = self.top
        else:
            self.last.next = DoubleElement(data, _prev=self.last)
            self.last = self.last.next

        self.size += 1

    def pop(self):
        if self.empty():
            return None

        last = self.last
        self.size -= 1

        self.last = self.last.prev

        if self.size == 0:
            self.top = None
            self.last = None
        else:
            self.last.next = None

        return last

    def peek(self):
        return self.last

    def empty(self):
        return self.size == 0

    def get(self, n):
        # if n > self.size:
        #     return None
        el = self.top
        for _ in range(n):
            # Control without using size
            if not el.next:
                return None
            el = el.next
        return el

    def get_middle(self):
        # Using size
        # return self.get(self.size // 2)

        slow = self.top
        fast = self.top

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def insert(self, data, n):
        print("Implement Insert")

    def delete(self, n):
        print("Implement Delete")

    def __repr__(self):
        m_repr = '[' + self.top.__repr__()
        cur = self.top.next
        for _ in range(self.size-1):
            m_repr += ' <-> ' + cur.__repr__()
            cur = cur.next
        return m_repr + ']'


def double_link_test():
    print('===== double_link_test ====')
    double_link_list = DoubleLinkList()

    double_link_list.append('DOWN')
    double_link_list.append('RIGHT')
    double_link_list.append('B')

    print(double_link_list)
    print(double_link_list.pop()) # 'DOWN'

    print(double_link_list)
    print(double_link_list.pop()) # 'RIGHT'

    print(double_link_list)
    print(double_link_list.pop()) # 'B'

    try:
        print(double_link_list.pop().data)
    except Exception as e:
        print("List Empty")


double_link_test()


class CircularLinkList:

    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def append(self, data):
        if not self.top:
            self.top = DoubleElement(data)
            self.last = self.top
            self.top.prev = self.last
            self.last.next = self.top
        else:
            self.last.next = DoubleElement(data, _next=self.top, _prev=self.last)
            self.last = self.last.next
            self.top.prev = self.last

        self.size += 1

    def pop(self):
        if self.empty():
            return None

        last = self.last
        self.size -= 1

        self.last = self.last.prev

        if self.size == 0:
            self.top = None
            self.last = None
        else:
            self.top.prev = self.last
            self.last.next = self.top

        return last

    def peek(self):
        return self.top

    def empty(self):
        return self.size == 0

    def __repr__(self):
        m_repr = '[ <- ' + self.top.__repr__()
        cur = self.top.next
        for _ in range(self.size-1):
            m_repr += ' <-> ' + cur.__repr__()
            cur = cur.next
        return m_repr + ' -> ]'


def circular_link_test():
    print('===== circular_link_test ====')
    circular_link_list = CircularLinkList()

    circular_link_list.append('DOWN')
    circular_link_list.append('RIGHT')
    circular_link_list.append('B')

    print(circular_link_list)
    print(circular_link_list.pop()) # 'DOWN'

    print(circular_link_list)
    print(circular_link_list.pop()) # 'RIGHT'

    print(circular_link_list)
    print(circular_link_list.pop()) # 'B'

    try:
        print(circular_link_list.pop().data)
    except Exception as e:
        print("List Empty")


circular_link_test()

# Questions


def get_element_test():
    print('===== get_element_test ====')
    m_list = DoubleLinkList()

    # 10 elements
    for c in '8964213897':
        m_list.append(int(c))

    print(m_list.get(5))
    print(m_list.get(7))
    print(m_list.get(9))
    print(m_list.get(11))


get_element_test()


def get_middle_element_test():
    print('===== get_middle_element_test ====')
    m_list = DoubleLinkList()

    # 10 element
    for c in '8964213897':
        m_list.append(int(c))

    print(m_list.get_middle())

    # 13 element
    for c in '132':
        m_list.append(int(c))

    print(m_list.get_middle())

    m_list.pop()
    m_list.pop()
    m_list.pop()
    m_list.pop()

    # 9 element
    print(m_list.get_middle())


get_middle_element_test()


def insert_test():
    print('===== insert_test ====')
    m_list = DoubleLinkList()

    m_list.insert('B', 0)
    m_list.insert('RIGHT', 0)
    m_list.insert('DOWN', 0)

    print(m_list)

    m_list.insert('v', 1)
    print(m_list)
    m_list.insert('z', 2)
    print(m_list)
    m_list.insert('u', 5)
    print(m_list)


insert_test()


def delete_test():
    print('===== delete_test ====')
    m_list = DoubleLinkList()

    for c in '8964213897':
        m_list.append(int(c))

    print(m_list)

    m_list.delete(9)
    print(m_list)

    m_list.delete(0)
    print(m_list)

    m_list.delete(4)
    print(m_list)


delete_test()
