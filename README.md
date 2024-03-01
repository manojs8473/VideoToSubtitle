# VideoToSubtitle
Detect and extract hardcoded video subtitles into subtitle srt file

**INSTALLATION**
Make sure you have CUDA and cuDNN installed on your system
Ideally CUDA 11.7 and cuDNN v8.4.1
If you have CUDA 11.7 already, download cuDNN v8.4.1 from : https://drive.google.com/file/d/1L3PwFszUul6l4xyeMAEsttQtcLFOlTgh/view?usp=sharing
-Extract the cuDNN folder
-Copy the bin,include,lib folder to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7"

1. Install PaddleOCR (PaddleOCR is a state-of-the art library for text detection and recognition) 

    1.1 Download PaddlePaddle whl file from : 
    Windows 11,CUDA 11.7 https://drive.google.com/file/d/1PAuRX-tm6hBbY0cB0w5jegFg42NVqWNa/view?usp=sharing
    Windows 10,CUDA 11.7 https://drive.google.com/file/d/1DiNpU-AIE8rwa5VldAEds-ySiRQ1bc8K/view?usp=sharing

    For other versions visit: https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html

  
    1.3 From the download folder run: `pip install 'downloaded .whl file'`


    1.4 Install PyMuPDF manually (need v1.20.2. pip install casues problem sometimes)

    Download PyMuPDF:
    Windows 10: https://drive.google.com/file/d/1BsTqOrQJGZbDb_arNy0IwJjrrS6pjN34/view?usp=sharing
    Windows 11: https://drive.google.com/file/d/1AQuhBaS23tW8y0iJwL1YltIhcRfzI4fy/view?usp=sharing

    Install: `pip install 'downloaded .whl file'`


    Install paddleocr: `pip install paddleocr>=2.7`  


2. Install other dependencies

    Run from the main code directory `pip install -r requirements.txt`


**RUNNING**

Open terminal and run this command: 
`python main.py --video_path "VIDPATH" --save_dir "SAVEDIR" --language LANG --start_time "00:00:00" --end_time "00:10:00"`


replace VIDPATH with path to video file

replace SAVEDIR with path where you want the srt file to be saved. Just give directory path. The saved file name will be  'subtitles.srt'

replace LANG with the language of the subtitles in the video. Use abbreviations. E.g. For english use "en" .  For other languages see the supported_languages.png file

start_time and end_time are the time for which the subtitle are made. Format is HH:MM:SS

Additionally, use `--use_gpu=True` flag to do processing using GPU

Note: During first run with a new language, the model files for that language will be downloaded automatically.
