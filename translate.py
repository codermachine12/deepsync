from moviepy.editor import VideoFileClip
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

# Step 1: Extract Audio from Video
def extract_audio(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)
# Step 2: Convert Audio to Text
def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    return text

# Step 3: Translate Text to Malayalam
def translate_text_google(text, target_language='ml'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

 #Step 4: Convert Translated Text to Audio
def text_to_speech(text, output_audio_path, language='ml'):
    tts = gTTS(text=text, lang=language)
    tts.save(output_audio_path)

# Main function to combine all steps
def process_video(video_path, output_audio_path,output_translated_audio_path):
    # Extract audio from video
    extract_audio(video_path, output_audio_path)
    
    # Convert extracted audio to text
    text = audio_to_text(output_audio_path)
    print(f"Original Text: {text}")
    
    # Translate text to Malayalam
    translated_text = translate_text_google(text)
    print(f"Translated Text: {translated_text}")
    
    # Convert translated text to speech
    text_to_speech(translated_text, output_translated_audio_path)
    print(f"Translated speech saved as {output_translated_audio_path}")
# Example usage
inp=input("Enter male or female")
video_path = r"C:\Users\rohan\Downloads\WhatsApp Video 2024-08-29 at 11.05.51 AM.mp4"
output_audio_path = r'C:\Users\rohan\Wav2Lip\translation\demo.wav'
output_translated_audio_path = r'C:\Users\rohan\Wav2Lip\translation\demotrans.mp3'
if inp=="female":
    process_video(video_path, output_audio_path,output_translated_audio_path)
elif inp=="male":
    process_videom()