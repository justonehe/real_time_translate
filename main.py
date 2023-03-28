import record_audio
import transcribe_audio
import translate_text
import os
import time


output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
audio_filename = os.path.join(output_dir, "recorded_audio.wav")

def main():
    print("程序将在3秒后自动开始录音。")
    time.sleep(3)
    
    record_audio.record_audio(audio_filename, duration=60)

    # 2. 调用whisper的库，把WAV文件转成英文文字，并保存成txt
    print("转录音频...")
    english_transcript = transcribe_audio.transcribe_audio(audio_filename)
    with open("transcription_english.txt", "w") as f:
        f.write(english_transcript)

    # 3. 调用GPT-3.5 API把英文txt翻译成中文，并保存成txt
    print("翻译成中文...")

    chinese_translation = translate_text.translate_to_chinese(english_transcript)
    with open("translation_chinese.txt", "w") as f:
        f.write(chinese_translation)

if __name__ == "__main__":
    main()
