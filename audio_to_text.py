import whisper
from pydub import AudioSegment

# Specify the paths to the audio file
audio_path = r"C:\Users\hi\Downloads\outputaudio.mp3"
audio_wav_path = r"C:\Users\hi\Downloads\outputaudio.wav"
transcription_output_path = r"C:\Users\hi\Downloads\transcription_output_whisper.txt"  # File to save transcription

# Convert the audio file to wav format
audio = AudioSegment.from_mp3(audio_path)
audio.export(audio_wav_path, format="wav")

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe audio with Whisper
result = model.transcribe(audio_wav_path)

# Print and save the transcription with punctuation
with open(transcription_output_path, 'w', encoding='utf-8') as file:
    file.write(result['text'])

print(f"Punctuated transcription saved to: {transcription_output_path}")
