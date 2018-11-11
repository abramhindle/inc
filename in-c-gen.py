#!/usr/bin/env python
# the score was transcribed by Shawn from https://moderndevice.com/author/shawn-3/
# my stance is that the score is Terry Riley's and Shawn's ownership of the transcription is not clear. His intent was freely redistribute but the score is obviously Terry Riley's
#
# Anyways here's the header block of the file from https://moderndevice.com/documentation/terry-rileys-in-c-for-arduino-with-the-fluxamasynth/
#
# My generator code is under the same license as Music21
#
# This script Copyright (c) 2006-2018 Abram Hindle, Michael Scott Cuthbert and
# cuthbertLab. Music21 code (excluding content encoded in the corpus) is free
# and open-source software, licensed under the Lesser GNU Public License (LGPL)
# or the BSD License
# 
# The music21 Toolkit
# 
# Music21 is Copyright (c) 2006-2017, Michael Scott Cuthbert and cuthbertLab.
# Music21 code (excluding content encoded in the corpus) is free and
# open-source software, licensed under the Lesser GNU Public License (LGPL) or
# the BSD License.  The music21 Corpus
# 
# The LGPL/BSD music21 software is distributed with a corpus of encoded
# compositions which are distributed with the permission of the encoders (and,
# where needed, the composers or arrangers) and where permitted under United
# States copyright law. Some encodings included in the corpus may not be used
# for commercial uses or have other restrictions: please see the licenses
# embedded in individual compositions or directories for more details.
# 
# To the best of our knowledge, the music (if not the encodings) in the corpus
# are either out of copyright in the United States and/or are licensed for
# non-commercial use. These works, along with any works linked to in the
# virtual corpus, may or may not be free in your jurisdiction. If you believe
# this message to be in error regarding one or more works please contact
# Michael Cuthbert at the address provided on the contact page.
# 
#
'''
// 
// Terry Riley's In C
// 
// This sketch implements Terry Riley's "In C" composition for 
// the Fluxamasynth Shield.. 
// For the score and more background visit:
// http://en.wikipedia.org/wiki/In_C
// http://imslp.org/wiki/In_C_(Riley,_Terry)
//
// http://moderndevice.com/product/fluxamasynth-shield/
// https://github.com/moderndevice/Fluxamasynth-Shield
//
// This code expects an analog input on A1 to control tempo
'''

# here's the transcription I ripped from  Shawn in https://moderndevice.com/documentation/terry-rileys-in-c-for-arduino-with-the-fluxamasynth/
# // An array containing the score. The first element is a MIDI note 0-127
# // followed by a duration in sixteenth notes. Each part ends with a 255 
# //
score = [
  [0, 1],                                             #// part 0
  [60, 1, 64, 3, 60, 1, 64, 3, 60, 1, 64, 3],         #// part 1
  [60, 1, 64, 1, 65, 2, 64, 2, 0, 3],                 #// part 2
  [0, 2, 64, 2, 65, 2, 64, 2],                        #// part 3
  [0, 2, 64, 2, 65, 2, 67, 2],                        #// part 4
  [64, 2, 65, 2, 67, 2, 0, 2],                        #// part 5
  [72, 16, 72, 16],                                   #// part 6
  [0, 14, 60, 1, 60, 1, 60, 2, 0, 18],                #// part 7
  [67, 24, 65, 16, 65, 16],                           #// part 8
  [71, 1, 67, 1, 0, 14],                              #// part 9
  [71, 1, 67, 1],                                     #// part 10
  [65, 1, 67, 1, 71, 1, 67, 1, 71, 1, 67, 1],         #// part 11
  [65, 2, 67, 2, 71, 16, 71, 4],                      #// part 12
  [71, 1, 67, 3, 67, 1, 65, 1, 67, 2, 0, 3, 67, 7],   #// part 13
  [72, 16, 71, 16, 67, 16, 66, 16],                   #// part 14
  [67, 1, 0, 15],                                     #// part 15
  [67, 1, 71, 1, 72, 1, 71, 1],                       #// part 16
  [71, 1, 72, 1, 71, 1, 72, 1, 71, 1, 0, 1],          #// part 17
  [64, 1, 68, 1, 64, 1, 68, 1, 64, 3, 64, 2],         #// part 18
  [0, 6, 79, 6],                                      #// part 19
  [64, 1, 66, 1, 64, 1, 66, 1, 57, 3, 64, 1, 65, 1, 
   64, 1, 65, 1, 64, 1],                              #// part 20
  [66, 12],                                           #// part 21
  [64, 6, 64, 6, 64, 6, 64, 6, 64, 6, 66, 6, 67, 6, 
   69, 6, 71, 2],                                     #// part 22
  [64, 2, 66, 6, 66, 6, 66, 6, 66, 6, 67, 6, 
   69, 6, 71, 6],                                     #// part 23
  [64, 2, 66, 2, 67, 6, 67, 6, 67, 6, 67, 6, 
   67, 6, 69, 6, 71, 2],                              #// part 24
  [64, 2, 66, 2, 67, 2, 69, 6, 69, 6, 69, 6, 
   69, 6, 69, 6, 71, 6],                              #// part 25
  [64, 2, 66, 2, 67, 2, 69, 2, 71, 6, 71, 6, 71, 6, 
   71, 6, 71, 6],                                     #// part 26
  [64, 1, 66, 1, 64, 1, 66, 1, 67, 2, 64, 1, 
   67, 1, 66, 1, 64, 1, 66, 1, 64, 1],                #// part 27
  [64, 1, 66, 1, 64, 1, 66, 1, 64, 3, 64, 1],         #// part 28
  [64, 12, 67, 12, 72, 12],                           #// part 29
  [72, 24],                                           #// part 30
  [67, 1, 65, 1, 67, 1, 71, 1, 67, 1, 71, 1],         #// part 31
  [65, 1, 67, 1, 65, 1, 67, 1, 71, 1, 65, 13, 67, 6], #// part 32
  [67, 1, 65, 1, 0, 2],                               #// part 33
  [67, 1, 65, 1],                                     #// part 34
  [65, 1, 67, 1, 71, 1, 67, 1, 71, 1, 67, 1, 71, 1, 
   67, 1, 71, 1, 67, 1, 0, 14, 70, 4, 79, 12,
   81, 2, 79, 4, 83, 2, 79, 6, 79, 2, 76, 12, 
   79, 2, 78, 14, 0, 10, 76, 10, 77, 24],             #// part 35
  [65, 1, 67, 1, 71, 1, 67, 1, 71, 1, 67, 1],         #// part 36
  [65, 1, 67, 1],                                     #// part 37
  [65, 1, 67, 1, 71, 1],                              #// part 38
  [71, 1, 67, 1, 65, 1, 67, 1, 71, 1, 72, 1],         #// part 39
  [71, 1, 65, 1],                                     #// part 40
  [71, 1, 67, 1],                                          #// part 41
  [72, 16, 71, 16, 69, 16, 72, 16],                   #// part 42
  [77, 1, 76, 1, 77, 1, 76, 1, 76, 2, 76, 2, 76, 2, 77, 
   1, 76, 1],                                         #// part 43
  [77, 2, 76, 4, 76, 2, 72, 4],                       #// part 44
  [74, 4, 74, 4, 67, 4],                              #// part 45
  [67, 1, 74, 1, 76, 1, 74, 1, 0, 2, 67, 2, 67, 2, 0, 
   2, 67, 2, 67, 1, 74, 1, 76, 1, 74, 1],             #// part 46
  [74, 1, 76, 1, 74, 2],                              #// part 47
  [67, 24, 67, 16, 64, 16, 64, 4],                    #// part 48
  [65, 1, 67, 1, 70, 1, 67, 1, 70, 1, 67, 1],         #// part 49
  [65, 1, 67, 1],                                     #// part 50
  [65, 1, 67, 1, 70, 1],                              #// part 51
  [67, 1, 70, 1],                                     #// part 52
  [70, 1, 67, 1]                                      #// part 53
]
assert len(score) == 54, "Len: %s" % len(score)
import music21
 
# now we want to make midi files 00.mid to 53.mid

for i in range(0,len(score)):
    filename = "inc/{:02d}.mid".format(i)
    s = music21.stream.Stream()
    phrase = score[i]
    for j in range(0,len(phrase)/2):
        mnote = phrase[2*j]
        duration = phrase[2*j+1]
        note = music21.note.Note(mnote, quarterLength=4*duration/16.0) # 16th to 1/4
        s.append(note)
    fp = s.write('midi', fp=filename)
