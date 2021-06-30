'''
ffmpeg try
i = regular files
v = video

'''
import subprocess

output_video_mp4 = '/home/akash/git_workspace/Learn-Python/compression/media/sample55_output.mp3'
input_video = '/home/akash/git_workspace/Learn-Python/compression/media/sample55.flac'
# stream.run()
# streamx = subprocess.check_call(
#     ['ffmpeg', '-v', '-8', '-i', input_video, '-vf', 'scale=-2:480', '-preset', 'slow',
#         '-c:v', 'libx264', '-strict', 'experimental', '-c:a', 'aac', '-crf', '20', '-maxrate', '500k',
#         '-bufsize', '500k', '-r', '25', '-f', 'mp4', output_video_mp4, '-y']
# )

# streamx = subprocess.check_call(
#     ['ffmpeg', '-v', '-8', '-i', input_video, '-vf', 'scale=-2:144', '-preset', 'slow',
#         '-c:v', 'libx264', '-strict', 'experimental', '-c:a', 'aac', '-crf', '20', '-maxrate', '200k',
#         '-bufsize', '200k', '-r', '25', '-f', 'mp4', output_video_mp4, '-y']
# )


streamx = subprocess.check_call(
    ['ffmpeg', '-i', input_video, '-ar', '16000' , output_video_mp4]
)

