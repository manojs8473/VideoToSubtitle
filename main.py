from videocr import save_subtitles_to_file
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Extract hardcoded subtitles from video")
    
    parser.add_argument("--video_path", type=str, required=True,
                help="video path ")
    parser.add_argument("--language", type=str, required=True,
                help="language of the subtitles in the video")
    parser.add_argument("--start_time", type=str, default='00:00:00',
                help="start time in video to start processing from. Default is 00:00:00")
    parser.add_argument("--end_time", type=str, default='',
                help="end time in video to end processing from. Default is to the end of the video")
    parser.add_argument("--save_dir", type=str,
                default="./",
                help="dir to save subtile file")
    parser.add_argument('--use_gpu', type=bool, default=False,
                help='whether use gpu for processing')
    

    args = parser.parse_args()

    save_subtitles_to_file(args.video_path, args.save_dir+'/subtitles.srt', lang=args.language,time_start=args.start_time,time_end=args.end_time,
     sim_threshold=80, conf_threshold=75, 
     use_fullframe=True,use_gpu=args.use_gpu,
     brightness_threshold=150, 
     similar_image_threshold=500, frames_to_skip=1)
    
    print('Processing Completed!')


