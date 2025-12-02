from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from pydub.playback import play

def basic_loop(input_file, iterations=3):
    try:
        audio = AudioSegment.from_file(input_file)
        #combined = AudioSegment.empty()
        #for _ in range(iterations):
        #    combined = combined.append(audio, crossfade=5)
        # combined.export("loop.mp3", format="mp3")
        play(audio * iterations)
    except Exception as e:
        print(f"Error creating crossfaded loop: {str(e)}")
        
def basic_play(input_file):
    try:
        audio = AudioSegment.from_file(input_file)
        play(audio)
    except Exception as e:
        print(f"Error creating crossfaded loop: {str(e)}")
        
def fade(input_file: str):
    audio = AudioSegment.from_file(input_file)
    fade = audio.fade_in(10000).fade_out(30000)
    play(fade)
    
# audio = AudioSegment.from_file('SirDuke.mp3')
# play(audio)
# trim the silence at beginning
# play(audio[3780:])
# example of slicing and looping
# intro = audio[3780:13270]
# play(intro*4)
# bass = audio[20300:23000]
# play(bass)
# both
# play(intro.append(bass))