
archivo = "codes.txt"

f = open(archivo,"r")

notas = {}
for line in f:
    a, b = line.split()
    bin_b = int("{0:b}".format(int(b)).zfill(5))
    notas[int(bin_b)]=0

print notas



def read_note(cod):
    note = 0
    if(len(line.split())!=7):
        print "Mal Formato codigo {}".format(cod)
    else:
        if line[0] == 3: note = 6
        elif line[1] == 3 : note = 5
        elif line[2] == 3 : note = 5
        
            
        
        
        



