# VideoToSubtitle
Detect and extract hardcoded video subtitles into subtitle srt file

INSTALLATION

1. Install PaddlePaddle (PaddleOCR is a state-of-the art library for text detection and recognition) 

    1.1 Download Paddle whl file from : https://drive.google.com/file/d/1PAuRX-tm6hBbY0cB0w5jegFg42NVqWNa/view?usp=sharing
    1.2 From the download folder run: pip install paddlepaddle_gpu-2.6.0.post117-cp310-cp310-win_amd64.whl

    Note: This version is only for Windows system with CUDA 11.7

    For other versions visit: https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html

2. Install other dependencies

pip install -r requirements.txt

RUNNING
Open terminal and run this command: 
python main.py --video_path "VIDPATH" --save_dir "SAVEDIR" --language "LANG" --start_time "00:00:00" --end_time "00:10:00"


replace VIDPATH with path to video file

replace SAVEDIR with path where you want the srt file to be saved. Just give directory path. The saved file name will be  'subtitles.srt'

replace LANG with the language of the subtitles in the video. Use abbreviations. E.g. For english use "en" .  For other languages see the supported_languages.png file

start_time and end_time are the time for which the subtitle are made. Format is HH:MM:SS
