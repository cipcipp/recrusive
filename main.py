#please create looping recrusively

i = 0
def recrusive(i):
  i++
  a = "oke {}".format(i)
  if(i<100):
    return recrusive(i)
  else:
    return a
