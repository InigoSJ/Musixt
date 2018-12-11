import midi

def note_sound(note_pitch,pitch_length,base_duration,delay,note_velocity):
  note_len=int(pitch_length*base_duration)
  on = midi.NoteOnEvent(tick=note_len-delay, velocity=note_velocity, pitch=note_pitch)
  off= midi.NoteOffEvent(tick=delay, pitch=note_pitch)
  return on,off
