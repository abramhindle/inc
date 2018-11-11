# Terry Riley's In C generator in Python using music21

I wanted each phrase of "In C" in a seperate and simple midi file so I made a python script using music21 to do so.

## Results

inc/00.mid to inc/53.mid contains all the phrases of the composition. You can regenerate them from the in-c-gen.py

   mkdir inc && python in-c-gen.py # makes all of the inc/00-53.mid files

## inc-seq24.mid

inc-seq24.mid contains all of the 00 to 53 phrases in a seq24 midi format, but it does load nicely into rosegarden.

## Origins

The score I sed was was transcribed by Shawn from https://moderndevice.com/author/shawn-3/.

My stance is that the score is Terry Riley's and Shawn's ownership of the transcription is not clear. His intent was freely redistribute but the score is obviously Terry Riley's. Terry Riley, "In C", 1964.

Anyways here's the header block of the file from https://moderndevice.com/documentation/terry-rileys-in-c-for-arduino-with-the-fluxamasynth/

## License

My generator code is under the same license as Music21

 This script Copyright (c) 2006-2018 Abram Hindle, Michael Scott Cuthbert and
 cuthbertLab. Music21 code (excluding content encoded in the corpus) is free
 and open-source software, licensed under the Lesser GNU Public License (LGPL)
 or the BSD License
 
 The music21 Toolkit
 
 Music21 is Copyright (c) 2006-2017, Michael Scott Cuthbert and cuthbertLab.
 Music21 code (excluding content encoded in the corpus) is free and
 open-source software, licensed under the Lesser GNU Public License (LGPL) or
 the BSD License.  The music21 Corpus
 
 The LGPL/BSD music21 software is distributed with a corpus of encoded
 compositions which are distributed with the permission of the encoders (and,
 where needed, the composers or arrangers) and where permitted under United
 States copyright law. Some encodings included in the corpus may not be used
 for commercial uses or have other restrictions: please see the licenses
 embedded in individual compositions or directories for more details.
 
 To the best of our knowledge, the music (if not the encodings) in the corpus
 are either out of copyright in the United States and/or are licensed for
 non-commercial use. These works, along with any works linked to in the
 virtual corpus, may or may not be free in your jurisdiction. If you believe
 this message to be in error regarding one or more works please contact
 Michael Cuthbert at the address provided on the contact page.
 
### The derivative score

I took the score from Shawn: https://moderndevice.com/author/shawn-3/.

In the header of his computer score he wrote:

   Terry Riley's In C
   
   This sketch implements Terry Riley's "In C" composition for 
   the Fluxamasynth Shield.. 
   For the score and more background visit:
   http://en.wikipedia.org/wiki/In_C
   http://imslp.org/wiki/In_C_(Riley,_Terry)
   
   http://moderndevice.com/product/fluxamasynth-shield/
   https://github.com/moderndevice/Fluxamasynth-Shield
   
   This code expects an analog input on A1 to control tempo
  
Please be respectful of Terry Riley and his work "In C", this code and midi is provided as a convienance for performers.
