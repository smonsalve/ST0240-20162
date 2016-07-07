archivo = fopen("ejemplo.txt");

texto = ""

while(!feof(archivo))
	linea = fgetl(archivo);
	texto = [texto, ' ',linea];
end

disp(texto)