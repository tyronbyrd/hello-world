import pygame
import webbrowser
from tkinter import Tk, Label, Entry, scrolledtext, Button
from tkinter.ttk import Style
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.generators import Sine
from tkinter.constants import END


class MusicalCryptogramGenerator:
    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Mapping of note values to frequencies (Hz)
        self.NOTE_FREQS = {
            'C0': 16.35,
            'C#0/Db0': 17.32,
            'D0': 18.35,
            'D#0/Eb0': 19.45,
            'E0': 20.60,
            'F0': 21.83,
            'F#0/Gb0': 23.12,
            'G0': 24.50,
            'G#0/Ab0': 25.96,
            'A0': 27.50,
            'A#0/Bb0': 29.14,
            'B0': 30.87,
            'C1': 32.70,
            'C#1/Db1': 34.65,
            'D1': 36.71,
            'D#1/Eb1': 38.89,
            'E1': 41.20,
            'F1': 43.65,
            'F#1/Gb1': 46.25,
            'G1': 49.00,
            'G#1/Ab1': 51.91,
            'A1': 55.00,
            'A#1/Bb1': 58.27,
            'B1': 61.74,
            'C2': 65.41,
            'C#2/Db2': 69.30,
            'D2': 73.42,
            'D#2/Eb2': 77.78,
            'E2': 82.41,
            'F2': 87.31,
            'F#2/Gb2': 92.50,
            'G2': 98.00,
            'G#2/Ab2': 103.83,
            'A2': 110.00,
            'A#2/Bb2': 116.54,
            'B2': 123.47,
            'C3': 130.81,
            'C#3/Db3': 138.59,
            'D3': 146.83,
            'D#3/Eb3': 155.56,
            'E3': 164.81,
            'F3': 174.61,
            'F#3/Gb3': 185.00,
            'G3': 196.00,
            'G#3/Ab3': 207.65,
            'A3': 220.00,
            'A#3/Bb3': 233.08,
            'B3': 246.94,
            'C4': 261.63,
            'C#4/Db4': 277.18,
            'D4': 293.66,
            'D#4/Eb4': 311.13,
            'E4': 329.63,
            'F4': 349.23,
            'F#4/Gb4': 369.99,
            'G4': 392.00,
            'G#4/Ab4': 415.30,
            'A4': 440.00,
            'A#4/Bb4': 466.16,
            'B4': 493.88,
            'C5': 523.25,
            'C#5/Db5': 554.37,
            'D5': 587.33,
            'D#5/Eb5': 622.25,
            'E5': 659.25,
            'F5': 698.46,
            'F#5/Gb5': 739.99,
            'G5': 783.99,
            'G#5/Ab5': 830.61,
            'A5': 880.00,
            'A#5/Bb5': 932.33,
            'B5': 987.77,
            'C6': 1046.50,
            'C#6/Db6': 1108.73,
            'D6': 1174.66,
            'D#6/Eb6': 1244.51,
            'E6': 1318.51,
            'F6': 1396.91,
            'F#6/Gb6': 1479.98,
            'G6': 1567.98,
            'G#6/Ab6': 1661.22,
            'A6': 1760.00,
            'A#6/Bb6': 1864.66,
            'B6': 1975.53,
            'C7': 2093.00,
            'C#7/Db7': 2217.46,
            'D7': 2349.32,
            'D#7/Eb7': 2489.02,
            'E7': 2637.02,
            'F7': 2793.83,
            'F#7/Gb7': 2959.96,
            'G7': 3135.96,
            'G#7/Ab7': 3322.44,
            'A7': 3520.00,
            'A#7/Bb7': 3729.31,
            'B7': 3951.07,
            'C8': 4186.01,
            'C#8/Db8': 4434.92,
            'D8': 4698.63,
            'D#8/Eb8': 4978.03,
            'E8': 5274.04,
            'F8': 5587.65,
            'F#8/Gb8': 5919.91,
            'G8': 6271.93,
            'G#8/Ab8': 6644.88,
            'A8': 7040.00,
            'A#8/Bb8': 7458.62,
            'B8': 7902.13,
            '_': 0.00,  # Add a blank space entry with value 0.00
        }

        # Initialize Tkinter
        self.root = Tk()
        self.root.title("Musical Cryptogram Generator v.10.0")
        self.root.geometry("390x300")
        self.root.configure(bg="#229b75")
        self.style = Style()
        self.style.configure('TButton', foreground='black', background='#4bae75', font=('Arial', 12, "bold"))

        # Define GUI widgets
        self.input_label = Label(self.root, text="Enter your input string:")
        self.input_label.place(x=30, y=11)
        self.input_entry = Entry(self.root)
        self.input_entry.place(x=190, y=9)
        self.process_button = Button(self.root, text="Translate!", command=self.translate_and_render)

        self.process_button.place(x=140, y=40)
        self.playback_button = Button(self.root, text="Playback!", command=self.play_sound_from_notes)
        self.playback_button.place(x=140, y=70)
        self.result_label = Label(self.root, text="Result:")
        self.result_label.configure(bg="#229b75")
        self.result_label.place(x=169, y=105)
        self.result_text = scrolledtext.ScrolledText(self.root, width=50, height=10, wrap="word")
        self.result_text.place(x=10, y=130)
        self.icon_image = Image.open('icon.png')
        self.icon_image = self.icon_image.resize((24, 24), resample=Image.BICUBIC)
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)
        self.icon_button = Button(self.root, image=self.icon_photo, command=self.open_webpage)
        self.icon_button.place(x=176, y=260)

        # Initialize playback notes
        self.playback_notes = []

    def get_note_value(self, letter):
        # Implement get_note_value function
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if letter.isalpha():
            if letter.upper() in alphabet:
                # lets try deleting the below + 1 (that worked)
                return alphabet.index(letter.upper())

    def get_note_name(self, note_value):
        # Implement get_note_name function
        if note_value is None:
            return ' '

        octaves = ['4', '5', '6', '7', '8', '9', '10', '11']
        notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

        octave_index = ((note_value) // 7)
        note_index = ((note_value) % 7)

        return f"{notes[note_index]}{octaves[octave_index]}"

    def convert_to_musical_cryptogram(self, input_string):
        # Implement convert_to_musical_cryptogram function
        notes = []
        for letter in input_string:
            if letter == ' ':
                notes.append('_')  # Add a blank space as a rest with the value 00.00
            else:
                note_value = self.get_note_value(letter)  # Corrected
                note_name = self.get_note_name(note_value)  # Corrected
                notes.append(note_name)
        return notes

    def notes_to_text_notes(self, notes):
        # Implement notes_to_text_notes function
        text_notes = []
        for note in notes:
            if note == '_':
                text_notes.append('   ')  # Add three spaces for a rest
            # write a module here that if note = CHAR/NUM format text_notes.appendf"{note} minus the # and + superscript #.
            elif note[0].isalpha() and note[-1].isdigit():
                SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
                note = note.translate(SUP)
                text_notes.append(note)
            # otherwise just handle normally by appending each note
            else:
                text_notes.append(f"{note}")
        return ''.join(text_notes)

    def generate_sine_wave(self, frequency, duration):
        # Implement generate_sine_wave function
        duration_ms = int(duration * 1000)  # Convert duration to milliseconds
        samples = [Sine(frequency).to_audio_segment(duration_ms)]
        return sum(samples)

    def play_notes(self, note_list, duration):
        # Implement play_notes function
        audio = AudioSegment.silent(duration=0)
        for note in note_list:
            if note == '_':
                rest_duration = int(duration * 1000)
                rest = AudioSegment.silent(duration=rest_duration)
                audio += rest
            else:
                note, octave = note[:-1], note[-1]
                frequency = self.NOTE_FREQS.get(f"{note}{octave}")  # Corrected
                if frequency:
                    note_audio = self.generate_sine_wave(frequency, duration)  # Corrected
                    audio += note_audio
                else:
                    print(f"Invalid note: {note}{octave}")

        audio.export("output.wav", format="wav")

    def process_input_string(self):
        # Implement process_input_string function
        input_text1 = self.input_entry.get()
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        input_text = ''.join(filter(whitelist.__contains__, input_text1))
        musical_cryptogram = self.convert_to_musical_cryptogram(input_text)
        text_notes = self.notes_to_text_notes(musical_cryptogram)
        self.result_text.delete('1.0', END)  # Corrected
        self.result_text.insert(END, text_notes)  # Corrected
        self.playback_notes = musical_cryptogram

    def play_sound_from_notes(self):
        # Implement play_sound_from_notes function
        # FIXME: No fixes needed but adjust this value below to adjust bpm! 1 = 1 second
        duration = 1  # Adjust the duration as needed -
        self.play_notes(self.playback_notes, duration)  # Corrected

        # Use pygame to play the exported audio file
        pygame.mixer.music.load("output.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def translate_and_render(self):
        self.process_input_string()
        #self.play_sound_from_notes()

    def open_webpage(self):
        webbrowser.open("https://hyperfollow.com/EponymousSparrow?_gl=1*5hadnh*_ga*MjI5NTY1NDE3LjE2ODY3NzAxMzI.*_ga_PQXYYERT25*MTY4ODM4ODAwOC4zLjEuMTY4ODM4ODUyMi42MC4wLjA.&_ga=2.120660431.69287412.1688387995-229565417.1686770132")

    def run(self):
        self.root.mainloop()

# Usage example:
if __name__ == "__main__":
    musical_cryptogram_generator = MusicalCryptogramGenerator()
    musical_cryptogram_generator.run()
