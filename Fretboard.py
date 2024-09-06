"""!
@brief Fretboard

Module for fretboard settings.

Design goals:
- keep this module flexible so that it is possible to use other tuning or instruments like a mandolin.

"""

from Scales import chromaticScale


class Fretboard:
    def __init__(self, chromaticScale: list) -> None:
        self.tuning = ("E", "A", "D", "G", "B", "E")
        self.chromaticScale = chromaticScale
        self.strings = self._getStringNotes(self.tuning, chromaticScale)

    def _getStringNotes(self, tuning: list, chromaticScale: list) -> list[list]:
        strings = []
        for string in tuning:
            noteNumber = 0
            for note in chromaticScale:
                if note == string:
                    break
                noteNumber += 1

            fretNotes = []
            for fret in range(12):
                currentNoteNumber = noteNumber + fret
                if currentNoteNumber >= 12:
                    currentNoteNumber = currentNoteNumber - 12
                fretNotes.append(chromaticScale[currentNoteNumber])
            strings.append(fretNotes)

        return strings


fretboard = Fretboard(chromaticScale)
