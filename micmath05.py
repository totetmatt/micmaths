import random
def bothSum(lst,i):
    return [zero(lst)[i]+zero(lst)[i+1],zero(lst)[i+2]+zero(lst)[i+1]]
def zero(liste):
    return liste+[0,0]
maxi = 0

while True:
    liste = [5,4,3,2,1,2,3,4,5]
    maxiseq = []
    while len(liste)>2:
        i = random.randint(0, len(liste)-2)
        maxiseq+=[i+1]
        sumBoth = bothSum(liste,i)
  
        if i+2 < len(liste):
            liste[i+2]=sumBoth[1]
        liste[i] = sumBoth[0]
        liste.pop(i+1)
    if maxi < sum(liste):
        maxi = sum(liste)
        print "------"
        print maxi
        print maxiseq

    
