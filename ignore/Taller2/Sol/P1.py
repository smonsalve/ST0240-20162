t = int(raw_input())

for i in range(t):
    count = color = 0
    a = []
    for j in range(6):
        a.append(int(raw_input()))
    
#    print a
    if(a[0]+a[1]+a[2] > a[3]+a[4]+a[5]):
        count = 1

    if(a[0]>a[3]): color = 1
    elif(a[0]==a[3]):
         if(a[1] > a[4]): color = 1 
         elif(a[1] == a[2]):
             if(a[2]>a[5]): color=  1


    if count and color:
        print "Ambos"
    elif count :
        print "Cantidad"
    elif color:
        print "Color"
    else: 
        print "Ninguno"
