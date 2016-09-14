def loop_size(node):
    l=[node]
    while True:
        print(node)
        if node.next:
            if node.next in l:
                return len(l) - l.index(node.next)
            else:
                l.append(node.next)
                node = node.next
        else:
            return None
node = Node()
n
