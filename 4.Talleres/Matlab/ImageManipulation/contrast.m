%% Function contrast
% Receives an image and modifies its colors but editing the matrix.
function contrasted = contrast(I)
    %% Transformation.
    % Convert the array to doubles to be able to make floating point
    % arithmetic operations
    contrasted = double(I);
    % Substract 127 from each pixel and multiply by 1.5. These are
    % arbitrary values for a specific contrast.
    contrasted=contrasted+(contrasted - 67)*1.5;
    %% Validation
    % Be sure nothing is out of the range 0-255
    contrasted=max(contrasted,0);
    contrasted=min(contrasted,255);
    % Convert it back to an image format with int values
    contrasted=image(uint8(floor(contrasted)));

end