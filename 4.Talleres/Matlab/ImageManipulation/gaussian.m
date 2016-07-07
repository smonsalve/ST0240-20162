%% Function that applies a mathematical equation as a transformation to the center of the image.
function gaussian(I)
    %% Part B: Emphasizing the middle by using a gaussian function
    [xdim,ydim,zdim]=size(I);
    % Create the meshgrid
    [X,Y]=meshgrid(1:xdim,1:ydim);
    % Insert the function into the three positions we are going to use to
    % multiply the image by. Note that the three positions (RGB) have the
    % same equation.
    % e^(-10*((((x-100)^2)+(y-100)^2))/(100*100)))
    Mask(:,:,1)= exp(-10/(xdim*ydim)*((X-xdim/2).^2+(Y-ydim/2).^2))';
    Mask(:,:,2)=Mask(:,:,1);
    Mask(:,:,3)=Mask(:,:,1);
    
    % Apply the transformation and convert the image back to an int format.
    image(uint8(floor(double(I).*Mask)));
end