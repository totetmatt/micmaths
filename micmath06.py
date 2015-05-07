import copy
violet = [4,[1,2,3,0,0,0,0,0]]
jaune = [1,[9,8,7,6,5,4,0,0,0,0,0,0,0]]
vert = [7,[1,2,3,4,0,0,0,0,0,0,0,4,3,2,1,0,0,0,0,0,0]]
bleu = [2,[6,5,6,5,0,0,0,0,0]]
rose = [8,[7,8,9,7,8,9,0,0,0,0]]

system = [violet,jaune,vert,bleu,rose]

t = 0
def total(s):
    return sum([x[1][x[0]] for x in s ])
def inc(s):
    for k,v in enumerate(s):
        if k %2 == 0:
            v[0]= (v[0]+1)%len(v[1])
        else:
            v[0]-=1
            if(v[0]<0):
                v[0]+=len(v[1])
def dec(s):
    for k,v in enumerate(s):
        if k %2 != 0:
            v[0]= (v[0]+1)%len(v[1])
        else:
            v[0]-=1
            if(v[0]<0):
                v[0]+=len(v[1])

i = 0
maxi = 0
print "****  Increment  ****"
inc_system = copy.deepcopy(system)
while maxi != 31: 
    inc(inc_system)
    i+=1
    
    if maxi < total(inc_system):
        maxi = total(inc_system)
        print 'Iteration +',i
        print total(inc_system)
i = 0
maxi = 0
print "****  Decrement  ****"
dec_system = copy.deepcopy(system)
while maxi != 31: 
    dec(dec_system)
    i+=1
    
    if maxi < total(dec_system):
        maxi = total(dec_system)
        print 'Iteration -',i
        print total(dec_system)
