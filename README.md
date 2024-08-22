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


Debrief questions:


    How do I interpret user needs and implement them into a program? How does creating “user stories” help with this?

      A: I interpret user needs through a simple heuristic once passed to me when running a cafe in Washington State. "Make a sandwhich you would want to eat."
         Quite simply, I have spent my entire life using software. I remember which software applications felt nice and why they felt nice. I then try to 
         emulate what feels good about them by being a user of what I am making, in leiu of having a userbase. I also test on friends and iterate over their 
         experiences. 

         With one extra step of complexity, basically I take my experiences and make user stories. Examples of this might look like this:

           User Story: I can't change the speed of the output sound, which make this a novelty but not a tool.
           Change: Add a BPM slider. 

           User Story: I have a hard time reading the note and octave output quickly.
           Change: Make the numbers superscript.

           User Story: I enjoy the program but wish I had multiple busses, different wave types, panning, and note value adjustment.
           Change (another version): Have multiple wave types, multiple busses, panning, and note value adjustement. 

         And so on.

    How do I approach developing programs? What Agile processes do I hope to incorporate into my future development work?

      A: Despite working solo, I can still use things like timeboxing, information radiators, definition of done, and velocity tracking to make better use of 
         my time, track project statuses, forecase time it will take me to fulfill various tasks, and keep good coding practices through the projects I take on.
         Later, when working with other people, I can use all Scrum Agile principles which would probably be standard operating procedure in European Tech.

    What does it mean to be a good team member in software development?

      A: Communicating well, practicing self improvement and skillsharing, not being overly rigid in task assignment (no 'that's not my job'), and being 
         gregarious are examples of what makes a good team member in software development. Besides that, being punctual. 


