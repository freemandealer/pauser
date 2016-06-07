#!/usr/bin/python

from pydub import AudioSegment
from pydub.silence import split_on_silence
import random
import sys
import getopt

silence_len = 400     # default silence len: 400ms
silence_thresh = 70  # default silence thresh < -70dBFS
blank = 1             # default blank len = 1 x chunk len + extra_blank len
extra_blank = 300

def usage():
  print '''\nUsage:

  python pauser.py -f filename [-s silence_len] [-d silence_thresh] [-b blank]

'''

def evaluate(granularity):
  if granularity < 3:
    print "granularity too small!"
    print "[Suggestion] increase silence length(current is %d ms) via '-s'\n\
option and/or silence threshold(current is %d) via '-d' option.\n"\
    %(silence_len, silence_thresh)
  if granularity > 10:
    print "granularity too large!"
    print "[Suggestion] decrease silence length(current is %d ms) via '-s'\n\
option and/or silence threshold(current is %d) via '-d' option.\n"\
    %(silence_len, silence_thresh)

def main(argv):
  try:
    opts, args = getopt.getopt(argv[1:], 'hf:s:d:b:', ['help'])
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)
  for opt, val in opts:
    if opt in ('-h', '--help'):
      usage()
      sys.exit(1)
    elif opt in ('-f'):
      file_name=val
    elif opt in ('-s'):
      silence_len=int(val)
    elif opt in ('-d'):
      silence_thresh=int(val);
    elif opt in ('-b'):
      blank=int(val);
    else:
      print "Invalid option."
      usage()
      sys.exit(2)

  try:
    sound = AudioSegment.from_mp3(file_name)
  except:
    print "\nCannot open file: %s\n"%file_name

  chunks = split_on_silence(sound,min_silence_len=silence_len,silence_thresh=0-silence_thresh)
  print "processing ..."

  num_chunks = len(chunks)
  print str(num_chunks) + " pauses injected"
  granularity = len(sound)/num_chunks/1000;
  print "granularity: " + str(granularity) + " seconds"
  evaluate(granularity)

  new = AudioSegment.empty()
  for i in range(0,num_chunks):
    new += chunks[i]
    silence = AudioSegment.silent(duration=blank*len(chunks[i]) + extra_blank)
    new += silence

  save_name = "paused-"+file_name
  new.export(save_name, format="mp3")

if __name__ == '__main__':
    main(sys.argv)
