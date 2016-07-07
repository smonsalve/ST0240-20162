import csv

def cleaning(nombre_archivo):
	with open(nombre_archivo, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		print nombre_archivo.split(".")[0]
		# for row in reader:
		# 	if (row[0])!="  ":
		# 		#print row
		# 		print row[0] + "," + row[1] + "," +row[2] + "," +row[3] + ":" + row[4] + "," + row[5] + "/" +row[6] + "/" +row[7]
		# # 	entrada[row[1]] = str(row[3])+":"+str(row[4])
		# elif(row[0]=="2" or row[0]=="3"):
		# 	salida[row[1]] = str(row[3])+":"+str(row[4])

archivos = open("indice.txt")
for line in archivos:
	  cleaning(" "+line.rstrip('\n'))

entrada = {}
salida = {}