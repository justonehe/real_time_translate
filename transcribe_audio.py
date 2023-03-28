# 这里需要实现与Whisper ASR API的交互。由于我们没有具体的API细节，所以我们只提供一个示例函数。
# 请使用实际的API信息替换此示例。
import openai
import io
import tempfile
import os

openai.api_key ="your api key here"
def transcribe_audio(audio_filename):
    audio_file= open(audio_filename, 'rb') 
    
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript.get("text")


def transcribe_audio_files(cache_dir):
    transcriptions = []

    cache_files = sorted(os.listdir(cache_dir))

    for cache_file in cache_files:
        if cache_file.endswith('.wav'):
            with open(f"{cache_dir}/{cache_file}", 'rb') as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)

            transcriptions.append(transcript.get("text"))

    return " ".join(transcriptions)
