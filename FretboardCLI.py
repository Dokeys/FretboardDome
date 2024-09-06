"""!
@ brief Fretboard CLI

Module to print the fretboard.
"""

from Fretboard import fretboard
from rich.console import Console
from rich.control import Control


console = Console()

printFretboardLine = 3


def printOnFret(
    string: int, fret: int, stringToPrint: str, highlight: bool = False
) -> None:
    line = printFretboardLine
    console.print(Control.move_to(x=0, y=line))
    stringLine = line + 6 - string
    if fret == 0:
        console.print(Control.move_to(x=1, y=stringLine))
    elif fret == 1:
        console.print(Control.move_to(x=6, y=stringLine))
    else:
        console.print(Control.move_to(x=fret * 7 - 2, y=stringLine))

    if string % 2 != 0:
        backgroundColor = "red"
    else:
        backgroundColor = "dark_red"

    if highlight is False:
        console.print(stringToPrint, style=f"black on {backgroundColor}")
    else:
        console.print(stringToPrint, style=f"green on {backgroundColor} blink")

    console.print(Control.move_to(x=0, y=printFretboardLine + 8))


def printEmptyFretboard() -> None:
    """! Draw fretboard without notes"""
    line = printFretboardLine
    console.print(Control.move_to(x=0, y=line - 1))
    console.print("🎼 Fretboard:")
    console.print(Control.move_to(x=0, y=line))
    console.print(
        "    0     1      2      3      4   O  5      6  oo  7      8   O  9      10     11",
        style="grey69",
        highlight=False,
    )
    for stringNumber in range(len(fretboard.strings)):
        if stringNumber % 2 == 0:
            style = "grey69 on red"
        else:
            style = "grey69 on dark_red"

        console.print(
            "   ||     |      |      |      |      |      |      |      |      |      |      | ",
            style=style,
        )


def printFretboardNotes(highlightNotes: list = None) -> None:
    """! Draw all fretboard notes"""
    for stringNumber in range(len(fretboard.strings)):
        for fretNumber in range(0, 12):
            currentNote = fretboard.strings[stringNumber][fretNumber]
            highlight = False
            if highlightNotes != None and currentNote in highlightNotes:
                highlight = True
            printOnFret(
                string=stringNumber,
                fret=fretNumber,
                stringToPrint=currentNote,
                highlight=highlight,
            )


def printFretboard(highlightNotes: list = None) -> None:
    """! Print fretboard with notes"""
    printEmptyFretboard()
    printFretboardNotes(highlightNotes)


def moveFretboardLine(newLine: int) -> None:
    global printFretboardLine
    printFretboardLine = newLine
