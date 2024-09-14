from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from moviepy.editor import VideoFileClip
import os

def detect_gender(audio_path):
    try:
        # Load the audio file
        [Fs, x] = audioBasicIO.read_audio_file(audio_path)
        
        # Extract audio features
        mt_features, _, _ = MidTermFeatures.mid_feature_extraction(x, Fs, 1.0 * Fs, 1.0 * Fs, 0.5 * Fs)
        
        # Load pre-trained gender classifier
        model = SVC.load('gender_classifier_model.pkl')
        
        # Prepare feature vector
        features = np.mean(mt_features, axis=1)
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features.reshape(-1, 1)).flatten()
        
        # Predict gender
        prediction = model.predict([features_scaled])
        
        if prediction[0] == 0:
            return "male"
        else:
            return "female"
    except Exception as e:
        print(f"An error occurred while detecting gender: {e}")
        return None

def extract_audio_from_video(video_path, audio_output_path):
    try:
        # Load the video file
        video = VideoFileClip(video_path)
        
        # Extract and save the audio from the video
        video.audio.write_audiofile(audio_output_path)
        
        print("Audio extracted successfully and saved to:", audio_output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_path = r"C:\Users\hi\Downloads\How to instantly become a better public speaker.mp4"
audio_path = r"C:\Users\hi\Downloads\audio_from_video.mp3"

extract_audio_from_video(video_path, audio_path)
gender = detect_gender(audio_path)
print(f"Detected gender: {gender}")



