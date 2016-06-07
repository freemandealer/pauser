#!/usr/bin/python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.silence import split_on_silence
import random
import sys
import getopt
import os

granularity = 400     # default granularity: 400ms
silence_thresh = 70  # default silence thresh < -70dBFS
blank = 1             # default blank len = 1 x (chunk len + extra_blank len)
extra_blank = 800
file_name=''

def usage():
  print '''\nUsage:

  python pauser.py -f filename [-g granularity] [-d silence_thresh] [-b blank] [-e extra_blank]

'''

def evaluate(avg_chunk_len):
  if avg_chunk_len < 3:
    print "chunks are too small!"
    print "[Suggestion] increase granularity(current is %d ms) via '-g'\n\
option and/or silence threshold(current is %d) via '-d' option.\n"\
    %(granularity, silence_thresh)
  if avg_chunk_len > 10:
    print "chunks are too large!"
    print "[Suggestion] decrease granularity(current is %d ms) via '-g'\n\
option and/or silence threshold(current is %d) via '-d' option.\n"\
    %(granularity, silence_thresh)

def main(argv):
  global granularity, silence_thresh, blank, extra_blank, file_name
  try:
    opts, args = getopt.getopt(argv[1:], 'hf:g:d:b:e:', ['help'])
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
    elif opt in ('-g'):
      granularity=int(val)
    elif opt in ('-d'):
      silence_thresh=int(val);
    elif opt in ('-b'):
      blank=int(val);
    elif opt in ('-e'):
      extra_blank=int(val);
    else:
      print "Invalid option."
      usage()
      sys.exit(2)

  if not os.path.isfile(file_name):
    print "\nCannot open file\n"
    sys.exit(2)
  sound = AudioSegment.from_mp3(file_name)

  chunks = split_on_silence(sound,min_silence_len=granularity,silence_thresh=0-silence_thresh)
  print "processing ..."

  num_chunks = len(chunks)
  print str(num_chunks) + " pauses injected"
  if 0 == num_chunks:
    print "\nSomething must be wrong :(\nTry -g/-d option maybe\n"
    sys.exit(2)
  avg_chunk_len = len(sound)/num_chunks/1000;
  print "average chunk len: " + str(avg_chunk_len) + " seconds"
  evaluate(avg_chunk_len)

  new = AudioSegment.empty()
  for i in range(0,num_chunks):
    new += chunks[i]
    silence = AudioSegment.silent(duration=blank*(len(chunks[i]) + extra_blank))
    new += silence

  save_name = "paused-"+file_name
  new.export(save_name, format="mp3")

if __name__ == '__main__':
    main(sys.argv)
