Real-Time Translate
这个项目可以实现录音、将录音内容自动转录为英文文本，然后将英文文本翻译成中文。

环境准备
确保安装 Python 3（建议使用 Python 3.7 或更高版本）。
安装项目所需的依赖库：

pip install -r requirements.txt
项目结构
main.py - 程序入口，实现整个流程的集成。
record_audio.py - 使用麦克风录音并保存为 WAV 文件。
transcribe_audio.py - 将音频文件转录为英文文本。
translate_text.py - 将英文文本翻译成中文文本。
使用方法
打开命令行终端，进入项目根目录。
运行 main.py：

python main.py
程序将在 3 秒后自动开始录音，录音时长为 1 分钟。
录音结束后，程序会将音频文件转录为英文文本并翻译成中文文本。
最后，英文转录文本将保存在 output/transcription_english.txt，中文翻译文本将保存在 output/transcription_chinese.txt。
注意事项
请确保在安静的环境中进行录音，以获得更好的转录结果。
这个程序使用了 OpenAI 的 Whisper ASR API 和 GPT-3.5-turbo API，请确保您有正确的 API 密钥并在相应的文件中进行配置。
当前程序版本使用的是默认音频设备，如果需要使用其他音频设备，请修改 record_audio.py 文件中的设备索引。
后续改进
支持实时转录和翻译功能。
提供多种输入音频格式支持。
允许用户指定录音时长和其他参数。
在转录和翻译过程中实现更高的准确性。
