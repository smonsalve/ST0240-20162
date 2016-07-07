%Sistema de notas de una materia universitaria
%Lectura de datos a partir de un archivo indice

ind = fopen('indice.txt','r');
n=1;
while ~feof(ind)
   leer_linea = fgetl(ind);
   C(n)= cellstr(leer_linea);
   n=n+1;
end
fclose(ind);

indice.cantidadArchivos= str2num(C{1,1}(23));
indice.estudiantesTotales= str2num(C{1,2}(22:length(C{1,2})));

indice.parcial1.nombre= C{1,4};
indice.parcial1.porcEvaluacion1= str2num(C{1,5}(24:length(C{1,5})));
indice.parcial1.estPresentaron= str2num(C{1,6}(14:length(C{1,6})));
indice.parcial1.totPuntos= str2num(C{1,7}(15));
indice.parcial1.estNoPresentaron= [str2num(C{1,8}(29:length(C{1,8})))];
indice.parcial1.porcenPuntos= [str2num(C{1,9}(20:length(C{1,9})))];

indice.parcial2.nombre= C{1,11};
indice.parcial2.porcEvaluacion1= str2num(C{1,12}(24:length(C{1,12})));
indice.parcial2.estPresentaron= str2num(C{1,13}(14:length(C{1,13})));
indice.parcial2.totPuntos= str2num(C{1,14}(15));
indice.parcial2.estNoPresentaron= [str2num(C{1,15}(29:length(C{1,15})))];
indice.parcial2.porcenPuntos= [str2num(C{1,16}(20:length(C{1,16})))];

indice.parcial3.nombre= C{1,18};
indice.parcial3.porcEvaluacion1= str2num(C{1,19}(24:length(C{1,19})));
indice.parcial3.estPresentaron= str2num(C{1,20}(14:length(C{1,20})));
indice.parcial3.totPuntos= str2num(C{1,21}(15));
indice.parcial3.estNoPresentaron= [str2num(C{1,22}(29:length(C{1,22})))];
indice.parcial3.porcenPuntos= [str2num(C{1,23}(20:length(C{1,23})))];

P1= fopen(indice.parcial1.nombre, 'r');
notas1= csvread(P1);
P2= fopen(indice.parcial2.nombre, 'r');
notas2= dlmread(P2);
P3= fopen(indice.parcial3.nombre, 'r');
notas3= csvread(P3);


%Notas de cada uno de los examenes

r= 1:indice.estudiantesTotales;
N1= zeros(15,1);
for i= r
  nota= (sum(notas1(i,2:5)))/20;
  N1(i)= nota;
end

N2= zeros(15,1);
for i= r
  nota= (sum(notas2(i,2:5)))/20;
  N2(i)= nota;
end

N3= zeros(15,1);
for i= r
  nota= (sum(notas3(i,2:5)))/20;
  N3(i)= nota;
end

%Arreglo de las notas de cada uno de los estudiantes

A= cat(2,N1,N2,N3);

alm= zeros(1,3);
cont= 1;
while cont <= (1:r)
  alm= A(cont,:);
  cont= cont+1;
end

%Nota promedio por cada evaluacion

promedio_parcial1 = mean(N1)
promedio_parcial2 = mean(N2)
promedio_parcial3 = mean(N3)


%Desviacion tipica por cada evaluacion

desvTip_parcial1 = std(N1)
desvTip_parcial2 = std(N2)
desvTip_parcial3 = std(N3)

% graficar notas

grafico= plot(alm);

title ('Graficos por estudiante');
xlabel ('evaluaciones');
ylabel ('nota');