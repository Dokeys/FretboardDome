"""!
@brief Fretboard CLI

Main command line module for FretboardDome.
"""

import FretboardCLI
from Fretboard import fretboard
from Scales import chromaticScale
from rich.console import Console
from rich.control import Control
from enum import Enum
import sys
import random


console = Console()


class UserSelection(Enum):
    PRINT_FRETBOARD = "1"
    RANDOM_NOTE_FIND_TRAINER = "2"
    PLACE_TO_NOTE_TRAINER = "3"


def printTitle() -> None:
    console.print(Control.clear())
    console.print(Control.move_to(x=0, y=0))
    console.print("🎸 Guitar Fretboard Trainer 🎸")
    console.print("")


def printSelection() -> None:
    console.print(
        f"{UserSelection.PRINT_FRETBOARD.value}",
        style="blue",
        highlight=False,
        end="",
    )
    console.print(" - Print fretboard")

    console.print(
        f"{UserSelection.RANDOM_NOTE_FIND_TRAINER.value}",
        style="blue",
        highlight=False,
        end="",
    )
    console.print(" - Random note find trainer")

    console.print(
        f"{UserSelection.PLACE_TO_NOTE_TRAINER.value}",
        style="blue",
        highlight=False,
        end="",
    )
    console.print(" - Fretboard place to note trainer")

    console.print(
        f"q",
        style="blue",
        highlight=False,
        end="",
    )
    console.print(" - Exit")


def userSelection() -> UserSelection:
    printSelection()
    userInput = input("Input number:")
    if userInput == "q":
        sys.exit(1)
    selection = UserSelection(userInput)

    return selection


def randomNoteFindTrainer() -> None:
    while True:
        console.print(Control.clear())
        console.print(Control.move_to(x=0, y=0))
        noteToFind = random.choice(chromaticScale)
        console.print(f"Find note: {noteToFind}")
        userInput = input("Enter q to quit:")
        if userInput == "q":
            break
        FretboardCLI.printFretboard(highlightNotes=[noteToFind])


def placeToNoteTrainer() -> None:
    while True:
        FretboardCLI.printEmptyFretboard()
        searchString = random.randint(0, 5)
        searchFret = random.randint(0, 11)
        searchNote = fretboard.strings[searchString][searchFret]
        FretboardCLI.printOnFret(
            string=searchString, fret=searchFret, stringToPrint="🎵"
        )
        userInput = input(
            f"Enter note on string {searchString + 1}, fret {searchFret}:"
        )
        if userInput == "q":
            break
        if userInput.upper() == searchNote:
            console.print(f"✅ Note {userInput.upper()} is correct.", style="green")
        else:
            FretboardCLI.printEmptyFretboard()
            for stringNumber in range(len(fretboard.strings)):
                for fretNumber in range(0, 12):
                    if fretboard.strings[stringNumber][fretNumber] == searchNote:
                        FretboardCLI.printOnFret(
                            string=stringNumber,
                            fret=fretNumber,
                            stringToPrint=searchNote,
                            highlight=True,
                        )

            console.print(
                f"❌ Wrong input, searched note was {searchNote}.", style="red"
            )
        userInput = input("Enter q for quit or enter for next:")
        if userInput == "q":
            break


def runCLI() -> None:
    while True:
        printTitle()
        selection = userSelection()
        if selection == UserSelection.PRINT_FRETBOARD:
            FretboardCLI.printFretboard()
        elif selection == UserSelection.RANDOM_NOTE_FIND_TRAINER:
            randomNoteFindTrainer()
        elif selection == UserSelection.PLACE_TO_NOTE_TRAINER:
            placeToNoteTrainer()
