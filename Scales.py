"""!
@brief Scales

Package for all kind of scales

"""


class ChromaticScale:
    """! @brief Chromatic scale
    This contains the chromatic scale in both directions(with sharp and flat notes).
    """

    SHARP_NOTES = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
    FLAT_NOTES = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")


## Global setting of which scale should be used.
chromaticScale = ChromaticScale.SHARP_NOTES
