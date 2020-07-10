def myf(n):
  return '{:02d}'.format(n)

def addSec(text,num):
  sec = int(text[6:8])
  if (sec+num < 60):
    return text[:6] + myf(sec+num) + text[8:]
  else:
    min = int(text[3:5])
    hr = int(text[:2])
    if (min!=59):
      return text[:3] + myf(min+1) + ":" + myf(sec+num-60) + text[8:]
    else:
      return myf(hr+1) + ":00:" + myf(sec+num-60) + text[8:]


fi = open("thor.srt", "r")
fo = open("output.srt", "w")
for l in fi:
  line = str(l)
  if("-->" in line):
    [start, end] = line.split(" --> ")
    newline = addSec(start,5)+" --> "+addSec(end,5)
    fo.write(newline)
  else:
    fo.write(line)
fi.close()
fo.close()