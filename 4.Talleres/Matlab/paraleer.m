
archivo = fopen('ejemplo.txt','r');


for i=1:6
	linea = fgetl(archivo);
	if mod(i,2)==0;  
		disp(linea)
	end
end

disp(fgetl(archivo))

% linea = fgetl(archivo);
% disp(linea)
% nlines = fskipl(archivo, 4);
% linea = fgetl(archivo);
% disp(linea)

%cont = 0;

% while(!feof(archivo))
% 	cont = cont + 1;
% 	linea = fgetl(archivo);
% 	if(!isempty(strfind(linea,'matlab')))
% 		disp(linea)
% 		disp(cont)
% 	end
	
% end