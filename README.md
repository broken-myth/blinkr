<h1><b>Blinkr.</b></h1>

A human eye on average blinks up to 20 times a minute. But, this rate drops to less than half while we look at our computer and smartphone screens. This reduced rate of blinking leads to consequences like vision changes and dry eyes.<b> Blinkr was built to combat this and help the users maintain a good eye health.</b>

Blinkr is an app built on top of python utilizing the Mediapipe and OpenCV libraries lets the user set a time interval (10 seconds by default) before starting the session. Once the session begins, the app starts checking for blinks in the time interval specified. If the user has not blinked in the given time interval, the app sends a beep alerting the user to blink. If the user had already blinked, once or more, within the set time duration, the app simply ignores and waits till the next iteration begins.

<br>

<b>Note :- The application gives the best results when the user is situated in a well-lighted surrounding and ensures that their face is clearly visible to the camera.The current version is supported for reading activities on desktop computers and laptops. The future versions will be supporting typing activities as well.</b>

Download the app [here](https://blinkr-app.netlify.app/)

<b> <h1> How it works ? </h1></b>

<b> <h2>Tech used :</h2></b>

<hr>

- <b>mediapipe</b> library for face detection and face landmark
  identification

- <b>winsound</b> library to produce beeps

- <b>tkinter</b> for GUI

- <b>OpenCV</b> to capture video

- <b>threading</b> to run a function to monitor blinks within the specified duration in the background

<br>

<b> <h2>Application Flow :</h2></b>

<hr>

Blinkr is made on top of **python** and utilizes **mediapipe** framework for face detection and landmarking, and OpenCV for capturing video.

- It all begins with OpenCV capturing video through the webcam which is then processed by face-mesh which detects the face in the video frame and provides 468 landmarks on the face.

- The frame given by OpenCV is in BGR by default but mediapipe processes RGB data.So, the BGR frame is converted to RGB before letting mediapipe process it.

- Out of the 468 landmarks given we take just the landmarks that surround the right and left eye.

- We then find the vertical and horizontal distance between the extremes of the eye(horizontal and vertical) and divide them(vertical distance/horizontal distance) to get the eye aspect ratio (EAR) and start counting blinks (It is said to be a blink when the EAR drops below a threshold (set as 0.3 in our app)).

- A thread is run parallelly which executes a function that checks if the blink count has been updated within the time duration set, and produces a beep if the blink count has not been updated.


<b> <h1> What's the future of Blinkr ? </h1></b>

<hr>

- The future versions of blinkr will support typing activities on laptops and desktop computers by introducing a calibration phase before beginning a session.
- Blinkr would also be available in the form of a webapp that is also supported on mobile phones and a browser extension.
- A system that rewards the user for having a healthy blink rate during the session shall also be introduced to make maintaining eye health more playful.
