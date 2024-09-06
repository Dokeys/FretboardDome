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
import click

UP_KEY = "àH"
DOWN_KEY = "àP"

console = Console()
selection = 0


class UserSelection(Enum):
    PRINT_FRETBOARD = 0
    RANDOM_NOTE_FIND_TRAINER = 1
    PLACE_TO_NOTE_TRAINER = 2
    EXIT = 3


def printTitle() -> None:
    console.print(Control.clear())
    console.print(Control.move_to(x=0, y=0))
    console.print("🎸 FretboardDome - The Fretboard Trainer 🎸")
    console.print("")


def getStyleForSelection(currentSelection: UserSelection) -> str:
    if selection == currentSelection.value:
        style = "blue"
    else:
        style = ""

    return style


def printSelection() -> None:
    console.print(Control.move_to(x=0, y=3))

    console.print(
        "   Print fretboard", style=getStyleForSelection(UserSelection.PRINT_FRETBOARD)
    )
    console.print(
        "   Random note find trainer",
        style=getStyleForSelection(UserSelection.RANDOM_NOTE_FIND_TRAINER),
    )
    console.print(
        "   Fretboard place to note trainer",
        style=getStyleForSelection(UserSelection.PLACE_TO_NOTE_TRAINER),
    )
    console.print("   Exit", style=getStyleForSelection(UserSelection.EXIT))

    console.print(Control.move_to(x=0, y=3 + selection))
    console.print("➡")

    console.print(Control.move_to(x=0, y=10))


def userSelection() -> UserSelection:
    global selection
    pressedKey = ""
    while True:
        printTitle()
        printSelection()
        pressedKey = click.getchar()
        if pressedKey == "q":
            sys.exit(1)
        elif pressedKey == UP_KEY:
            selection -= 1
        elif pressedKey == DOWN_KEY:
            selection += 1
        elif pressedKey == "\n" or pressedKey == "\r":  # enter
            return UserSelection(selection)

        if selection < 0:
            selection = 0
        elif selection > len(UserSelection) - 1:
            selection = len(UserSelection) - 1


def printFretboard() -> None:
    printTitle()
    FretboardCLI.moveFretboardLine(3)
    FretboardCLI.printEmptyFretboard()
    FretboardCLI.printFretboardNotes()

    console.print(Control.move_to(x=0, y=11))
    console.print("Press any key to go to menu.", style="grey42")
    input()


def randomNoteFindTrainer() -> None:
    while True:
        printTitle()
        console.print(Control.move_to(x=0, y=2))
        noteToFind = random.choice(chromaticScale)
        console.print(f"Find note {noteToFind} on your guitar.")
        FretboardCLI.moveFretboardLine(5)
        FretboardCLI.printEmptyFretboard()
        console.print(Control.move_to(x=0, y=13))
        console.print(
            "Press any key to show notes on fretboard or q to go o menu.",
            style="grey42",
        )
        if click.getchar() == "q":
            break
        FretboardCLI.printFretboardNotes(highlightNotes=[noteToFind])
        console.print(Control.move_to(x=0, y=13))
        console.print(
            "Press any key for next note or q to go to menu.              ",
            style="grey42",
        )
        if click.getchar() == "q":
            break


def placeToNoteTrainer() -> None:
    while True:
        printTitle()
        FretboardCLI.moveFretboardLine(3)
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
        console.print(Control.move_to(x=0, y=13))
        console.print(
            "Press any key for next note or q to go to menu.              ",
            style="grey42",
        )
        if click.getchar() == "q":
            break


def runCLI() -> None:
    while True:
        printTitle()
        selection = userSelection()
        if selection == UserSelection.PRINT_FRETBOARD:
            printFretboard()
        elif selection == UserSelection.RANDOM_NOTE_FIND_TRAINER:
            randomNoteFindTrainer()
        elif selection == UserSelection.PLACE_TO_NOTE_TRAINER:
            placeToNoteTrainer()
        elif selection == UserSelection.EXIT:
            console.print(Control.clear())
            console.print(Control.move_to(x=0, y=0))
            sys.exit(1)
