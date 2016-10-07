% exp (i*pi)
% A = [10,8,14,2,3]
%plot(A)


% if

% TIPO 1

a = 10
b = 15
c = 0

if (a<b)
  c = 5
endif

disp(c)

% TIPO 2 

a = 10
b = 15
c = 0

if (a>b)
  c = 10  
else
  c = 15
endif
  
disp(c)
  
% TIPO 3  
  
a = 10
b = 15
c = 0

  
if (b>c)
  c = 1
elseif(c<a)
  c = 2
else
  c = 3 
endif
 
disp(c)