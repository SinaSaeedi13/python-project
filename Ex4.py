#Sina Saeedi,,, 4012061020

Letter_up=['A','B','C','D','E','F','G','H']
Letter_down=['a','b','c','d','e','f','g','h']
number=['1','2','3','4','5','6','7','8']
HB=input(' enter horizontal position of the bishop (A,B,C,D,E,F,G,H): ')
if HB not in Letter_up and HB not in Letter_down :
    print ('horizontal input for bishop is not from the list')
else:
    VB=input(' enter vertical position of the bishop (1,2,3,4,5,6,7,8): ')
if VB not in number :
    print ('vertical input for bishop is not from the list')
else:
    HK=input(' enter horizontal position of the knight (A,B,C,D,E,F,G,H): ')
if HK not in Letter_up and HK not in Letter_down :
    print ('horizontal input for knight is not from the list')
else:
    VK=input('Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ')
if VK not in number:
    print ('vertical input for knight is not from the list')
HB=HB.upper()
VB=VB.upper()
HK=HK.upper()
VK=VK.upper()
HB=Letter_up.index(HB)
VB=number.index(VB)
HK=Letter_up.index(HK)
VK=number.index(VK)
HB+=1
VB+=1
HK+=1
VK+=1
if HB==HK and VB==VK:
    print('horizontal and vertical positions of bishop and knight can not be the same!')

    
#checking bishop hitting knight
    
    
a=HB
b=VB
while True:
    if a==HK and b==VK:
        print('bishop can hit knight!')
        break
    else:
        a+=1
        b+=1
    if a==9:
        break
c=HB
d=VB
while True:
    if c==HK and d==VK:
        print('bishop can hit knight!')
        break
    else:
        c+=1
        d-=1
    if c==9:
        break
e=HB
f=VB
while True:
    if e==HK and f==VK:
        print('bishop can hit knight!')
        break
    else:
        e-=1
        f+=1
    if f==9:
        break
g=HB
h=VB
while True:
    if g==HK and h==VK:
        print('bishop can hit knight!')
        break
    else:
        g-=1
        h-=1
    if h==0:
        break
if a!=HK and b!=VK or c!=HK and d!=VK or e!=HK and f!=VK or g!=HK and h!=VK :
    print('bishop can not hit knight')
    
#checking knight hitting bishop
aa=HK
bb=VK

aa+=1
bb+=2
print(aa)
print(bb)
if aa==HB and bb==VB:
    print('knight can hit bishop')
    aa+=1
    bb-=1
    print(aa)
    print(bb)
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    bb-=2
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    aa-=1
    bb-=1
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    aa-=2
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    aa-=1
    bb+=1
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    bb+=2
elif aa==HB and bb==VB:
    print('knight can hit bishop')
    aa+=1
    bb+=1
elif aa==HB and bb==VB:
    print('knight can hit bishop')
else:
    print('knight can not hit bishop')





        

    
    

    

    

    

        



    































