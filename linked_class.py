from myiterator import MyIterator

class Set:
    def __init__(self, elements=None):
        self.elements = {}
        if elements != None:
            if len(elements) != len(set(elements)):
                elements = set(elements)
            for element in elements:
                self.elements[element] = element

    def __iter__(self):
        return MyIterator(self.elements)

    def add(self, element):
        if element in self.elements.keys():
            return 'The element {0} has already been in the set'.format(element)
        self.elements[element] = element

    def remove(self, element):
        if element not in self.elements.keys():
            return 'The element {0} not in the set'.format(element)
        self.elements.pop(element)

    def size(self):
        return len(self.elements.keys())

    def contains(self, element):
        if element in self.elements.keys():
            return True
        return False

    def equals(self, otherSet):
        if self.elements.keys() == otherSet.elements.keys():
            return True
        else:
            return False

    def union(self, otherSet):
        newSet = list(set(self.elements.keys()) | set(otherSet.elements.keys()))
        unionSet = Set(newSet)
        return unionSet

    def intersection(self, otherSet):
        newSet = list(set(self.elements.keys()) & set(otherSet.elements.keys()))
        intersectionSet = Set(newSet)
        return intersectionSet

    def difference(self, otherSet):
        newSet = list(set(self.elements.keys()) ^ set(otherSet.elements.keys()))
        differenceSet = Set(newSet)
        return differenceSet

    def is_subset_of(self, otherSet):
        if set(self.elements.keys()) < set(otherSet.elements.keys()):
            return True
        return False

    def __str__(self):
        return '[' + ', '.join(str(x) for x in self.elements.keys()) + ']'
