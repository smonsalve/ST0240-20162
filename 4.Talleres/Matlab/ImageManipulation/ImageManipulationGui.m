function varargout = ImageManipulationGui(varargin)
% IMAGEMANIPULATIONGUI MATLAB code for ImageManipulationGui.fig
%      IMAGEMANIPULATIONGUI, by itself, creates a new IMAGEMANIPULATIONGUI or raises the existing
%      singleton*.
%
%      H = IMAGEMANIPULATIONGUI returns the handle to a new IMAGEMANIPULATIONGUI or the handle to
%      the existing singleton*.
%
%      IMAGEMANIPULATIONGUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in IMAGEMANIPULATIONGUI.M with the given input arguments.
%
%      IMAGEMANIPULATIONGUI('Property','Value',...) creates a new IMAGEMANIPULATIONGUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before ImageManipulationGui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to ImageManipulationGui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help ImageManipulationGui

% Last Modified by GUIDE v2.5 07-Apr-2014 14:08:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @ImageManipulationGui_OpeningFcn, ...
                   'gui_OutputFcn',  @ImageManipulationGui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end

% End initialization code - DO NOT EDIT


% --- Executes just before ImageManipulationGui is made visible.
function ImageManipulationGui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to ImageManipulationGui (see VARARGIN)

% Choose default command line output for ImageManipulationGui
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
waitfor(msgbox({'This program will show you how to manipulate images in MATLAB' ' ' 'Please start by pushing the Capture button'}, 'Welcome'));


% --- Outputs from this function are returned to the command line.
function varargout = ImageManipulationGui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output; 


% --- Executes on button press in btnCapture.
function btnCapture_Callback(hObject, eventdata, handles)
% hObject    handle to btnCapture (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Opt.Interpreter = 'tex';
Opt.WindowStyle = 'normal';
waitfor(msgbox({'\bfWe are ready to capture an image from your webcam!\rm' ' ' 'We use our function \itCapture\rm to get the data from the webcam.' ' ' ...
    'A common way to represent color images is using a 3 dimensional array. if your image is m pixels high and n pixels wide, you would get a m x n x 3 array.' ' ' ...
    'The third dimension of the array corresponds to how much of the colors red green and blue are in an specific pixel. This sub array is also know as RGB.' ' ' ...
    'If you want to see how the 3 dimensional array looks like, just write \bf data=capture()\rm in your MATLAB console '},'Capturing', 'none', Opt));
data=capture();
axes(handles.axCaptured);
imshow(data)
waitfor(msgbox({'\bfOk, we just captured you. Now what?\rm' ' ' 'You can try some of the effects the program offer.' ' ' ...
    'Take a look at the code and try to understand it.' ' ' ...
    'Then go for the exercises.' ' ' },'Captured', 'none', Opt));



% --- Executes on button press in btnGrayscale.
function btnGrayscale_Callback(hObject, eventdata, handles)
% hObject    handle to btnGrayscale (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axCaptured);
data=getimage();
axes(handles.axGrayScale);
scaled=grayscale(data);
imshow(scaled)


% --- Executes on button press in btnConstrast.
function btnConstrast_Callback(hObject, eventdata, handles)
% hObject    handle to btnConstrast (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axCaptured);
data=getimage();
axes(handles.axContrast);
contrast(data);
%imshow(contrasted)


% --- Executes on button press in btnGaussian.
function btnGaussian_Callback(hObject, eventdata, handles)
% hObject    handle to btnGaussian (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axCaptured);
data=getimage();
axes(handles.axGaussian);
gaussian(data)



% --- Executes on button press in btnViewContrast.
function btnViewContrast_Callback(hObject, eventdata, handles)
% hObject    handle to btnViewContrast (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
open('contrast.m')



% --- Executes on button press in btnViewGaussian.
function btnViewGaussian_Callback(hObject, eventdata, handles)
% hObject    handle to btnViewGaussian (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
open('gaussian.m')


% --- Executes on button press in btnViewGray.
function btnViewGray_Callback(hObject, eventdata, handles)
% hObject    handle to btnViewGray (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
open('grayscale.m')


% --- Executes on button press in btnEditCodes.
function btnEditCodes_Callback(hObject, eventdata, handles)
% hObject    handle to btnEditCodes (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in btnExOne.
function btnExOne_Callback(hObject, eventdata, handles)
% hObject    handle to btnExOne (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Opt.Interpreter = 'tex';
Opt.WindowStyle = 'normal';
waitfor(msgbox({'\bfLets start with the contrast...\rm' ' ' 'What should you change in the code if you want different levels of contrast?' ' ' ...
    '\bf Go to the code and try with some values. \rm' ' '},'Capturing', 'none', Opt));



% --- Executes on button press in btnExTwo.
function btnExTwo_Callback(hObject, eventdata, handles)
% hObject    handle to btnExTwo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Opt.Interpreter = 'tex';
Opt.WindowStyle = 'normal';
waitfor(msgbox({'\bfNow, Lets modify the Grayscale function!\rm' ' ' 'The eye responds most strongly to \bfgreen\rm followed by \bfred\rm and then \bfblue.\rm' ' ' ...
    'The NTSC (National Television System Committee) recommends the following formula for color to greyscale conversion: ' ' ' ...
    '\bf I = 0.299 * R + 0.587 * G + 0.114 * B.\rm' ' ' ...
    'How would you change the \bfgrayscale.m\rm file ?'},'Capturing', 'none', Opt));

% --- Executes on button press in btnExThree.
function btnExThree_Callback(hObject, eventdata, handles)
% hObject    handle to btnExThree (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Opt.Interpreter = 'tex';
Opt.WindowStyle = 'normal';
waitfor(msgbox({'\bfFinally, Lets play with the Gaussian function!\rm' ' ' ...
    'First, try to change the mask value for Mask(:,:,2) to one. The result is that one of the colors is not applying the same transformation as the rest of them. \bfWhat do you observe?\rm ' ' '
    'Second, change some values on the Gaussian equation and describe how the transformation changes. Hint: change one at a time.' ' ' ...
    'Finally, can you make the selected region bigger or smaller?' ' '},'Capturing', 'none', Opt));
