"""One-line warning label for humans, built to land the joke.

The sentence is assembled from short fragments, sanity-checked, and
saved as exactly one line without a trailing newline.
"""

import os

_LABEL = "WARNING:"
_SUBJECT = " This human will ignore every warning label,"
_TWIST = " including this one,"
_ENDING = " then blame you for the accident."

_TARGET = 105
_LOW = 1
_HIGH = 160


def build_label():
    fragments = (_LABEL, _SUBJECT, _TWIST, _ENDING)
    sentence = ""
    for fragment in fragments:
        sentence += fragment
    return sentence


def label_is_ok(candidate):
    if not isinstance(candidate, str):
        return False
    if not candidate.strip():
        return False
    if any(mark in candidate for mark in ("\n", "\r")):
        return False
    length = len(candidate)
    if length < _LOW or length > _HIGH:
        return False
    return length == _TARGET


def main():
    sentence = build_label()
    if not label_is_ok(sentence):
        raise SystemExit("warning label failed its own check")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target_path = os.path.join(out_dir, "entry.txt")
    with open(target_path, "w", encoding="utf-8", newline="") as out:
        out.write(sentence)


if __name__ == "__main__":
    main()
