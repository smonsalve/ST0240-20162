index = "files.txt";
archivo = fopen(index, "r");
otros = {};
contenido = {};

while (not(feof(archivo)))
	linea = fgetl(archivo);
	otros(end + 1) = linea;
end

for a=1:length(otros)
	unarchivo = fopen(otros{a},"r");
	while (not(feof(unarchivo)))
		unalinea = fgetl(unarchivo);
		contenido(end+1) = unalinea;
	end 
end

disp(contenido)