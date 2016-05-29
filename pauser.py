from pydub import AudioSegment
from pydub.silence import split_on_silence
import random
import sys

file_name = sys.argv[1]

sound = AudioSegment.from_mp3(file_name)

chunks = split_on_silence(sound,min_silence_len=300,silence_thresh=-70)#silence time:700ms and silence_dBFS<-70dBFS

print "processing ..."

num_chunks = len(chunks)
print str(num_chunks) + " pauses injected"
print "granularity: " + str(len(sound)/num_chunks/1000) + " seconds"

new = AudioSegment.empty()
for i in range(0,num_chunks):
  new += chunks[i]
  silence = AudioSegment.silent(duration=len(chunks[i]) + 300)
  new += silence

save_name = "paused-"+file_name
new.export(save_name, format="mp3")
