# hello-world
Practicing the github flow and submitting an artifact for uni portfolio

This is a simple python program which creates musical cyptograms, that is, takes plain text and converts it to musical notes following a simple rule. 

Alphabetic letters are taken in, and then using a dictionary, are converted into musical notes following the logic A = C4, B = D4, C = E4... and so on. 
As the letters modulate through the notes A-G they go up in octave, giving Z = G7. The note values are taken from an international tone scale. 

Usage is simple: type in any text into the 'enter your input' field and then press translate, then playback; and listen to your sound. 
There is additionally a BPM slider where you can adust the beats per minute to go faster or slower. 

There is an extra easter egg for poking the bird.

This code runs on pygame and uses the pydub library to render .wav's into the project folder as output. 


The necessary pip installations are:

pip install pygame
pip install pillow
pip install tk
pip install pydub

Enjoy!

