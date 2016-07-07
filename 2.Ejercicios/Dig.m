a = [1,1,0;0,1,0;0,0,1];
%disp(a)

function es_diagonal(orden, mat)
	diag = 1;
	for i=1:orden
		for j=1:orden
			if (i!=j)
				%printf('i:%d j:%d',i,j)
				if (mat(i,j)!=0)
					diag = 0;
				end
			end
		end
	end
	if (diag == 1)
		printf('Verdadero\n')
	else
		printf('Falso\n')
	end
end

es_diagonal(3,a)

