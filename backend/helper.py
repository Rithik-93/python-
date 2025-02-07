from audio_extract import extract_audio as original_extract_audio

def extract_audio(videoPath: str, output_path: str):
    original_extract_audio(input_path=videoPath, output_path=output_path)

# extract_audio('../uploads/videos/upload_a.mp4', './a.mp3')
