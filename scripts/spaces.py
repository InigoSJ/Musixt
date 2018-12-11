import midi
from secondary_funcs import *

def silence(pitch_length,base_duration,delay,note_velocity):
  on,off=note_sound(0,pitch_length,base_duration,delay,0)
  return on,off

def skip_space(pitch_lengh,base_duration,delay,note_velocity):
  on,off=note_sound(0,0,0,0,0)
  return on,off
