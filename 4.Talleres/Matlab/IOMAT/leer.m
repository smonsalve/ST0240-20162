f=fopen('in/3Indice.txt','r');

cantArch = 0;
cantEst = 0;
evalu = {};
puntos = 0;
porcen = [];
presentaron = 0;
nopresentaron = 0;

if(!feof(f))
	linea = fgetl(f);
	if(!isempty(strfind(linea,'Cantidad de Archivos'))) 
		cantArch = str2num(linea(23:end)); 
	end

	if(!isempty(strfind(linea,'Estudiantes totales'))) 
		cantEst = str2num(linea(22:end)); 
	end
	disp(length(linea))
end

for i=1:cantArch
	while(length(linea) < 2)
		linea = fgetl;
	end
	if(!isempty((strfind(linea,'csv')) || (strfind(linea,'txt')) || (strfind(linea,'ttt'))))
		nomArch = linea ;
	elseif(!isempty(strfind(linea,'Total Puntos:'))) 
		puntos = str2num(linea(15:end)); 
	elseif(!isempty(strfind(linea,'Presentaron:'))) 
		presentaron = str2num(linea(14:end)); 
	elseif(!isempty(strfind(linea,'Estudiantes que no presentaron: ')))
		nopresentaron = linea(33:end); 
	elseif(!isempty(strfind(linea,'porcentajes ='))) 
		porcen = str2num(linea(14:end)); 
	end

	s = struct("archivo",nomArch, "puntos", puntos, "presentaron", presentaron, "nopresentaron", nopresentaron, "porcentajes", porcen);
	evalu(end+1) = s;
end

disp(evalu)
