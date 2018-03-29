def minIndex(list, fromIndex):
    """
        Retourne l'index de l'element le plus petit dans la liste
        à partir de l'index fromIndex
    """
    minIndex = fromIndex
    lastIndex = len(list) - 1
    if fromIndex < lastIndex:
        for index in range(fromIndex + 1, lastIndex):
            if(list[index] < list[minIndex]):
                minIndex = index
    return minIndex


def swap(list, index1, index2):
    """
        Echange les elements d'index i1 et i2 dans la liste
    """
    tmp = list[index1]
    list[index1] = list[index2]
    list[index2] = tmp

def sortRight(list, fromIndex):
    """
        Tri des elements a droite de l'index
    """
    if fromIndex == len(list) - 1:
        return
    minIdx = minIndex(list, fromIndex)
    if minIdx != fromIndex:
        swap(list, minIdx, fromIndex)
    sortRight(list, fromIndex + 1)

def sort(list):
    """
    Trier les elements
    """
    sortRight(list, 0)

list = [3, 6, 2, 1, 9]
sort(list)
print(list)
