const cameraFeed = document.getElementById('cameraFeed');
const startRecordingButton = document.getElementById('startRecording');
const stopRecordingButton = document.getElementById('stopRecording');
const audioRecording = document.getElementById('audioRecording');

let mediaRecorder;
let recordedChunks = [];
let stream;

// Check for user media support
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Start recording when the "Start Recording" button is clicked
    startRecordingButton.addEventListener('click', function () {
        // Access the camera and microphone
        navigator.mediaDevices.getUserMedia({ video: true, audio: true })
            .then(function (userStream) {
                stream = userStream;

                // Display camera feed in the video element
                cameraFeed.srcObject = stream;

                // Create a MediaRecorder to record audio
                mediaRecorder = new MediaRecorder(stream);

                // Add data to the recordedChunks array when available
                mediaRecorder.ondataavailable = function (event) {
                    if (event.data.size > 0) {
                        recordedChunks.push(event.data);
                    }
                };

                // Handle the stop event to save and play the recorded audio
                mediaRecorder.onstop = function () {
                    const blob = new Blob(recordedChunks, { type: 'audio/wav' });
                    recordedChunks = [];
                    audioRecording.src = URL.createObjectURL(blob);

                    // Create FormData to send the audio file
                    const formData = new FormData();
                    formData.append('audio_file', blob , 'recorded_audio.wav');

                    // Send the audio file using AJAX
                    fetch('/transcribe_audio', {
                        method: 'POST',
                        body: formData,
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Audio uploaded successfully:', data);
                    })
                    .catch(error => {
                        console.error('Error uploading audio:', error);
                    });
                };

                mediaRecorder.start();
                startRecordingButton.disabled = true;
                stopRecordingButton.disabled = false;
            })
            .catch(function (error) {
                console.error('Error accessing user media:', error);
            });
    });

    // Stop recording when the "Stop Recording" button is clicked
    stopRecordingButton.addEventListener('click', function () {
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            mediaRecorder.stop();
        }
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            cameraFeed.srcObject = null;
        }
        startRecordingButton.disabled = false;
        stopRecordingButton.disabled = true;
    });
} else {
    console.error('getUserMedia is not supported');
}
