

from translate import Translator
import re

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def chunk_text(text, chunk_size=500):
    # Split the text into chunks of a specified size
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def extract_punctuation(text):
    # Extract punctuation from the text and their positions
    punctuation_positions = []
    for match in re.finditer(r'[,.!?;]', text):
        punctuation_positions.append((match.start(), match.group()))
    return punctuation_positions

def reapply_punctuation(original_text, translated_text, punctuation_positions):
    # Reapply punctuation to the translated text
    translated_text_list = list(translated_text)
    for position, punctuation in punctuation_positions:
        if position < len(translated_text_list):
            translated_text_list.insert(position, punctuation)
    return ''.join(translated_text_list)

def translate_file(input_file_path, output_file_path, target_language):
    try:
        # Read the content of the file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Extract punctuation from the original text
        punctuation_positions = extract_punctuation(text)
        
        # Split the text into manageable chunks
        text_chunks = chunk_text(text)
        
        # Translate each chunk and concatenate the results
        translated_text = ""
        for chunk in text_chunks:
            translated_text += translate_text(chunk, target_language)
        
        # Reapply punctuation to the translated text
        translated_text_with_punctuation = reapply_punctuation(text, translated_text, punctuation_positions)
        
        # Write the translated text to a new file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_text_with_punctuation)
        
        print(f"Translation to {target_language} completed successfully and saved to {output_file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = r"C:\Users\hi\Downloads\transcription_output_whisper.txt" 
output_file_path_hindi = r"C:\Users\hi\Downloads\output_text_hindi.txt"
output_file_path_telugu = r"C:\Users\hi\Downloads\output_text_telugu.txt"
output_file_path_urdu = r"C:\Users\hi\Downloads\output_text_urdu.txt"

# Translate to Hindi
translate_file(input_file_path, output_file_path_hindi, "hi")

# Translate to Tamil
translate_file(input_file_path, output_file_path_telugu, "te")

# Translate to Urdu
translate_file(input_file_path, output_file_path_urdu, "ur")
