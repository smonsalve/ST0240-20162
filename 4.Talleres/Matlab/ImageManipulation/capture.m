function data = capture()
    a = imaqhwinfo;
    [camera_name, camera_id, format] = getCameraInfo(a);


    % Capture the video frames using the videoinput function
    % You have to replace the resolution & your installed adaptor name.
    vid = videoinput(camera_name, camera_id, format);

    % Set the properties of the video object
    set(vid, 'FramesPerTrigger', Inf);
    set(vid, 'ReturnedColorspace', 'rgb')
    vid.FrameGrabInterval = 5;

    %start the video aquisition here
    start(vid)

    % Get the snapshot of the current frame
    data = getsnapshot(vid);
    % Stop the video aquisition.
    stop(vid);
    % Flush all the image data stored in the memory buffer.
    flushdata(vid);
end
