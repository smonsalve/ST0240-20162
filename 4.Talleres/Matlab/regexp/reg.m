str = {'Madrid, Spain','Romeo and Juliet','MATLAB is great'};
capExpr = '[A-Z]';
spaceExpr = '\s';

capStartIndex = regexp(str,capExpr);
spaceStartIndex = regexp(str,spaceExpr);

disp(capStartIndex)