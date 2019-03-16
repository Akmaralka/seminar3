from linked_class import FDS, ListNode


stack = FDS()
queue = FDS()

item = ListNode(10)
stack.push(item)
queue.enqueue(item)
item = ListNode(7)
stack.push(item)
queue.enqueue(item)
item = ListNode(22)
stack.push(item)
queue.enqueue(item)
item = ListNode(7)
stack.push(item)
queue.enqueue(item)
# queue.dequeue()
# stack.pop()
for number, data in enumerate(queue):
    print('Queue #%d - %s' % (number + 1, data))
print('-----------------')
for number, data in enumerate(stack):
    print('Stack #%d - %s' % (number + 1, data))
print('-----------------')

set1 = set('abracadabra')
set2 = set('alacazam')
print('Unique - %s' % set1)
print('Intersection - %s' % (set1 & set2))
print('Union - %s' % (set1 | set2))
print('In Abracadabra but not in Alacazam - %s' % (set1 - set2))
print('In Alacazam but not in Abracadabra - %s' % (set2 - set1))
print('Difference - %s' % (set1 ^ set2))
print('Abracadabra is subsetof Alacazam - %s' % (set1 <= set2))
print('Alacazam is subsetof Abracadabra - %s' % (set2 <= set1))
