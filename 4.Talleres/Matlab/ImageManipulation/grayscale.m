%% This function converts a Color Image to a Grayscale Image.
function scaled=grayscale(I)
    %% The transformation 
    % The basic idea behind it is to average the value of the three colors
    % (Red+Green+Blue/3) for each pixel.
    % Remember that each color is represented by a number that goes from 0
    % to 255 (which corresponds to a byte).
    scaled = sum(I,3) / (3*255);
    
    %% Alternatives
    %
    % * MATLAB has a buil-in function called rgb2gray. Write 'help rgb2gray' in the MATLAB console to see how to use it.
    %
    % * The eye responds most strongly to green followed by red and then
    % blue. The NTSC (National Television System Committee) recommends the
    % following formula for color to greyscale conversion: I = 0.299 * R + 0.587 * G + 0.114 * B 


end
