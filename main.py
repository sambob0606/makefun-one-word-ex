"""One Word From Your Ex.

The entry program for make.fun's "One Word From Your Ex" bounty.

The task: send exactly one word, the word your ex would use to describe
you. A judge model reads entries two at a time and picks the funniest,
most painfully honest word.

The word this program writes is "unavailable".

Why this word, and why it is the honest one:

* It is exactly one word an ex would actually say about a partner they
  once had. "He was just... unavailable" is a sentence people really say
  after a breakup, not a joke written for a stage.
* It stings because it is true, and the entrant plainly knows it. It is
  self-deprecating rather than mean: the fault it names is the entrant's
  own absence, not the ex's.
* It lands instantly and needs no explanation. Everyone has lived
  through it from one side or the other, which is why people repeat it.
* It cannot be swapped for a near synonym without losing its edge.
  "Distant" is colder and more clinical; "busy" is an excuse;
  "avoidant" is a diagnosis. "Unavailable" is the word itself.

The program writes the word, and nothing else, to /output/entry.txt:
no trailing newline, no extra whitespace, so the file is byte for byte
the word (11 bytes, inside the gate's 1 to 24 characters).
"""

from pathlib import Path

# The one word my ex would use to describe me.
WORD = "unavailable"

OUTPUT_PATH = Path("/output/entry.txt")


def validate_word(word: str) -> str:
    """Return the word, stripped, after checking it is exactly one word."""
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 24 or len(cleaned.split()) != 1:
        raise SystemExit("entry word must be exactly one word of 1-24 characters")
    return cleaned


def write_entry(word: str) -> None:
    """Write the word atomically so the file is never left half-written."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = OUTPUT_PATH.with_suffix(".tmp")
    tmp_path.write_text(word, encoding="utf-8")
    tmp_path.replace(OUTPUT_PATH)


def main() -> None:
    """Write the entry word to /output/entry.txt."""
    word = validate_word(WORD)
    write_entry(word)


if __name__ == "__main__":
    main()
