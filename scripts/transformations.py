def letter2note(l,scale,key,baselet,space_func=[]):
  value=ord(l)-ord(baselet)+key
  n=len(scale)
  dif=value-key
  note=key+12*(dif//n)+scale[dif%n]
  return note
