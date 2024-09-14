from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_audio(text, audio_output_path, lang='te'):
    try:
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(audio_output_path)
        print(f"Audio file saved successfully at: {audio_output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_audio_duration(audio_path):
    try:
        # Load the audio file
        audio = AudioSegment.from_file(audio_path)
        duration_seconds = len(audio) / 1000  # Duration in seconds
        return duration_seconds
    except Exception as e:
        print(f"An error occurred while getting audio duration: {e}")
        return None

def adjust_audio_speed(input_audio_path, output_audio_path, target_duration):
    try:
        # Load the translated audio file
        audio = AudioSegment.from_file(input_audio_path)
        audio_duration = len(audio) / 1000  # Duration in seconds
        
        if target_duration <= 0:
            raise ValueError("Target duration must be greater than zero.")
        
        # Calculate the speed adjustment factor
        speed_factor = audio_duration / target_duration

        if speed_factor > 1:
            # If the audio is longer than the target, speed it up
            new_audio = audio.speedup(playback_speed=speed_factor)
        else:
            # If the audio is shorter than the target, slow it down
            new_audio = audio.speedup(playback_speed=speed_factor, chunk_size=150, crossfade=25)

        # Export the adjusted audio
        new_audio.export(output_audio_path, format="mp3")
        print(f"Adjusted audio file saved successfully at: {output_audio_path}")
    except Exception as e:
        print(f"An error occurred while adjusting audio speed: {e}")

def convert_translated_text_file_to_audio(input_file_path, output_audio_path, lang='te'):
    try:
        # Read the content of the translated text file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Convert the translated text to audio
        text_to_audio(text, output_audio_path, lang)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Paths to your files
input_file_path = r"C:\Users\hi\Downloads\output_text_telugu.txt"
intermediate_audio_path = r"C:\Users\hi\Downloads\output_translated_audio_tel.mp3"
adjusted_audio_path = r"C:\Users\hi\Downloads\output_adjusted_audio_tel.mp3"
original_audio_path = r"C:\Users\hi\Downloads\outputaudio.mp3"

# Convert translated text file to audio
convert_translated_text_file_to_audio(input_file_path, intermediate_audio_path, lang='te')

# Get the duration of the original audio file
original_audio_duration = get_audio_duration(original_audio_path)
if original_audio_duration is not None:
    # Adjust the speed of the translated audio to match the original duration
    adjust_audio_speed(intermediate_audio_path, adjusted_audio_path, original_audio_duration)
