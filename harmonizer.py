from constants import *
import random as rand

class harmonizer():
    def __init__(self, voices: int, key: int) -> None:
        self.voices = [0 for _ in range(voices)]
        self.numvoices = voices
        self.key = key
        self.currchord = None
        self.currchordfunction = None

    def harmonize(self, note: int) -> list[int]:
        """Given a note, return the constituent notes of the corresponding chord"""
        pass

    def reset(self) -> None:
        pass


class majorCounterPointHarmonizer(harmonizer):
    def __init__(self, voices: int, key: int) -> None:
        super().__init__(voices, key)

    def harmonize(self, note: int) -> list[int]:
        """Given a note, return a chord key major in n voices following counterpoint"""
        note = (note - self.key) % 12
        if self.currchord is None:
            function = "tonic"
        else:
            function = chord_to_function[self.currchord]

        # Case received accidental
        if note not in note_to_scale:
            return self.voices

        self.currchord = self.get_next_chord(note, function)
        self.build_chord()
        return self.voices

    def get_next_chord(self, note, function):
        probdict = chord_from_note_and_function[(note, function)]

        roll = rand.random()
        for key in probdict:
            roll -= probdict[key]
            if roll <= 0:
                return key

    def build_chord(self):
        # Case this is the first chord
        notes = chords_in_semitones[self.currchord]
        # As many octaves of that chord as fit in our voices
        target_notes = [note for note in notes]
        i = 0
        while len(target_notes) < self.numvoices:
            # May not double leading tone or 3rd of chord
            if notes[i % len(notes)] != 11 and i % len(notes) != 1:
                target_notes.append(notes[i] + (12 * (i % len(notes))))
            i += 1

        if sum(self.voices) == 0:
            self.voices = target_notes
            return

        # counterpoint case:
        # TODO: REWRITE ALL OF THIS BUT BETTER
        new_voices = []
        target_notes = [note % 12 for note in target_notes]
        for voice in self.voices:
            octave_offset = voice // 12
            currvoice = voice % 12
            # If we have no other options, this voice is coerced to the remaining chord tone
            if len(target_notes) == 1:
                new_voices.append(target_notes[0] + octave_offset * 12)
            # Rule 1: pedal if possible
            elif currvoice in target_notes:
                target_notes.remove(voice)
                new_voices.append(voice)
            # Rule 2: tendency tones
            elif currvoice + 1 in target_notes:
                target_notes.remove(voice + 1)
                new_voices.append(voice + 1)
            elif currvoice - 1 in target_notes:
                target_notes.remove(voice - 1)
                new_voices.append(voice - 1)
            # Rule 3: consonant leaps
            else:
                closest = min(target_notes, key=lambda x: abs(x - voice))
                target_notes.remove(closest)
                new_voices.append(closest)


        self.voices = new_voices

class powerChordHarmonizer(harmonizer):
    def __init__(self, voices, key):
        super().__init__(voices, key)

    def harmonize(self, note: int) -> list[int]:
        newchord = []
        notes = [0, 4, 7]
        octaveoffset = 0
        for index in range(len(self.voices)):
            newchord.append(notes[index % 3] + 12 * octaveoffset + (note%12))
            if index >= 3 and index % 3 == 0:
                octaveoffset += 1
        self.voices = newchord
        return newchord

class minorCounterPointHarmonizer(majorCounterPointHarmonizer):
    def __init__(self, voices, key):
        super().__init__(voices, key)

    def turn_minor(self, voices) -> (list[int], str):
        newvoices = []
        for note in self.voices:
            offset = note // 12
            rawnote = note % 12
            newvoices.append(min_to_majNote[rawnote] + 12*offset)

        return newvoices

    def harmonize(self, note: int) -> list[int]:
        self.currchord = maj_to_minChord.get(self.currchord)
        rawvoices = super().harmonize(note)
        minorvoices = self.turn_minor(rawvoices)
        self.currchord = min_to_majChord.get(self.currchord)
        self.voices = minorvoices
        return minorvoices





