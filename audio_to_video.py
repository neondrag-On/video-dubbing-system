from moviepy.editor import VideoFileClip, AudioFileClip

def merge_audio_with_video(video_path, audio_path, output_path):
    try:
        # Load the original video file
        video = VideoFileClip(video_path)
        
        # Load the translated audio file
        audio = AudioFileClip(audio_path)
        
        # Set the audio of the video clip to the translated audio
        video_with_audio = video.set_audio(audio)
        
        # Write the result to a new file
        video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        print(f"Video with translated audio saved successfully to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_path = r"C:\Users\hi\Downloads\How to instantly become a better public speaker.mp4"
audio_path = r"C:\Users\hi\Downloads\output_adjusted_audio_hin.mp3"
output_path = r"C:\Users\hi\Downloads\final_video.mp4"

# Merge the translated audio with the original video
merge_audio_with_video(video_path, audio_path, output_path)
