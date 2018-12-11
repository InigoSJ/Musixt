import midi
from scripts.transformations import *
from scripts.spaces import *
from scripts.file_handler import *
from scripts.secondary_funcs import *

def text2midi(text,timing=[],scale=[0,2,4,5,7,9,11],name="example.mid",baselet="a",key=60,transformation=letter2note,space_func=skip_space,base_duration=100,delay=0,note_velocity=20,file_func=create_midi, **kwargs):
  
  text_length=len(text)
  timing_length=len(timing)
  
  if timing_length<text_length:
    dif=text_length-timing_length
    timing+=dif*[1]
  elif timing_length>text_length:
    timing=timing[:text_length]
    
  pattern = midi.Pattern(resolution=320)
  track = midi.Track()
  pattern.append(track)
  for i in range(text_length):
    letter=text[i]
    if letter==' ':
      on,off=space_func(timing[i],base_duration,delay,note_velocity)
    else:
      note=transformation(letter,scale,key,baselet,space_func) 
      on,off=note_sound(note,timing[i],base_duration,delay,note_velocity)
      
    track.append(on)
    track.append(off)
    
  eot = midi.EndOfTrackEvent(tick=1)
  track.append(eot)
  
  file_func(name,pattern,**kwargs)
