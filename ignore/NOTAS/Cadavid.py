path = "input/"
file_name = open(path+'Nombres.txt', 'r')
cont = 0
finalNote = 0.0
def totalNotes(day,qua):
    if(day == 0):
        if(qua == 3):
            return 6.0
        else:
            return float(qua) * 2.5
    if(day == 1):
        if(qua == 3):
            return 5.0
        else:
            return float(qua) * 2.0
    if(day == 2):
        if(qua == 3):
            return 4.0
        else:
            return float(qua) * 1.5
#menu1 = input("Ingrese:\n 1. para imprimir las notas de todos los estudiantes\n 2. para el resultado de un estudiante\n")
menu1 = 1

if(menu1 == 1):
    for line in file_name:
    	code_id = line.rstrip()
    	student_file = open(path+code_id, 'r')
    	lines = student_file.readlines()
    	studentName = lines[0].rstrip()
    	notes = lines[1].rstrip()
        notas = [int(notes[0]),int(notes[2]),int(notes[4])]
        total = int(notes[0]) + int(notes[2]) + int(notes[4])
    	if total > 3:
    		print("Error! no hay mas de 3 problemas por resolver")
    		break
    	elif (total == 2 or total == 1):
    		finalNote = totalNotes(0,notas[0]) + totalNotes(1,notas[1]) + totalNotes(2,notas[2])
    	elif total == 3:
    		cont = notas[0]
    		finalNote = totalNotes(0,notas[0])
    		for n in range(1,3):
    			if(cont == 3):
    		 		break
    			else:
    				if( cont == 1 and notas[n] == 2):
    					cont = 3
    					finalNote = finalNote + totalNotes(n,1) + 1.0
    				elif(cont == 2 and notas[n] == 1):
    					cont = 3
    					finalNote = finalNote + 1.0
    				elif(cont == 0 and notas[n] >= 1):
    					cont = cont + notas[n]
    					finalNote = finalNote + totalNotes(n,notas[n])
    				elif(cont == 1 and notas[n] == 1):
    					cont = 2
    					finalNote = finalNote + totalNotes(n,1)
    					continue
    	if(notes[6] > 0):
    		finalNote = finalNote + 1.0
    	print(studentName + ": " + str(finalNote))
elif (menu1 == 2):
    studentCode = raw_input("Ingrese codigo del estudiante: ")
    studentCode = studentCode + (".txt")
    student_file = open(path+studentCode, 'r')
    lines = student_file.readlines()
    studentName = lines[0].rstrip()
    notes = lines[2].rstrip()
    notas = [int(notes[0]),int(notes[2]),int(notes[4])]
    total = int(notes[0]) + int(notes[2]) + int(notes[4])
    if total > 3:
    	print("Error! no hay mas de 3 problemas por resolver")
    elif (total == 2 or total == 1):
    	finalNote = totalNotes(0,notas[0]) + totalNotes(1,notas[1]) + totalNotes(2,notas[2])
    elif total == 3:
    	cont = notas[0]
    	finalNote = totalNotes(0,notas[0])
    	for n in range(1,3):
    		if(cont == 3):
    	 		break
    		else:
    			if( cont == 1 and notas[n] == 2):
    				cont = 3
    				finalNote = finalNote + totalNotes(n,1) + 1.0
    			elif(cont == 2 and notas[n] == 1):
    				cont = 3
    				finalNote = finalNote + 1.0
    			elif(cont == 0 and notas[n] >= 1):
    				cont = cont + notas[n]
    				finalNote = finalNote + totalNotes(n,notas[n])
    			elif(cont == 1 and notas[n] == 1):
    				cont = 2
    				finalNote = finalNote + totalNotes(n,1)
    				continue
    if(notes[6] > 0):
    	finalNote = finalNote + 1.0
    print(studentName + ": " + str(finalNote))