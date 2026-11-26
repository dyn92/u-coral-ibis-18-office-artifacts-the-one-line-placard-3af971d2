"""Office Artifacts: The One-Line Placard Contest -- entry.

Brief, in my own words: write exactly one line, a museum placard for an
ordinary office object, as if that object were an ancient artifact dug up
from a lost civilisation. The line must carry a catalogue date, a material
and a donor, and it must be at most 180 characters long, so the whole joke
has to land in a single sentence.

My strategy for the sentence: pick the stapler, the most ritual-looking
piece of desk equipment, and recast it as a sacred binder. The catalogue
date ("dated 2024") and the material ("pressed steel") give it the dry
museum-voice opening; the middle turns the stapler's ordinary job --
pinching papers together -- into a religious act ("ritual binder of the
Paper Cult", "sealing offerings for the gods of filing"); the ending
supplies the donor ("gift of the Interns' Guild") and a dig-site detail
("unearthed beneath Desk 7"), which is the punchline: the lost
civilisation is just an office, and its temple is a desk.

This program does one thing: it validates that single sentence against
the contest rules, prints it, and writes it to /output/entry.txt, then
reads the file back and refuses to finish unless the bytes match exactly.
Pure standard library, no network, no input files.
"""

import os

SENTENCE = (
    "Stapler, dated 2024, pressed steel: ritual binder of the Paper Cult, "
    "its iron jaw sealing offerings for the gods of filing; gift of the "
    "Interns' Guild, unearthed beneath Desk 7."
)

MAX_LENGTH = 180
OUTPUT_PATH = "/output/entry.txt"

TERMINATORS = ".!?"


def validate_sentence(sentence):
    """Check the placard line against every contest rule.

    Raises ValueError with a plain message for the first rule broken:
    empty, over 180 characters, contains a newline, leading/trailing
    whitespace, or not exactly one sentence (one terminal mark at the
    very end and no other terminal mark anywhere inside).
    """
    if not sentence:
        raise ValueError("sentence is empty")
    if len(sentence) > MAX_LENGTH:
        raise ValueError(
            "sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_LENGTH)
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line, no newline allowed")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")
    if sentence[-1] not in TERMINATORS:
        raise ValueError("sentence must end with one of . ! ?")
    if any(ch in TERMINATORS for ch in sentence[:-1]):
        raise ValueError(
            "sentence must contain exactly one sentence: "
            "no terminal mark allowed inside the line"
        )
    return True


def main():
    validate_sentence(SENTENCE)
    print(SENTENCE)
    print("characters: %d (limit %d)" % (len(SENTENCE), MAX_LENGTH))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != SENTENCE + "\n":
        raise SystemExit(
            "output file does not match the sentence byte for byte"
        )
    print("wrote %s (%d bytes)" % (OUTPUT_PATH, len(written.encode("utf-8"))))


if __name__ == "__main__":
    main()
