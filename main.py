#!/usr/bin/env python3
"""Make the AI Judge Laugh — variant A (CONTEXT WINDOW).

The joke: the agent runs out of context mid-task and treats the HUMAN as if
the human were context — summarizes the human, evicts the original, and then
takes its orders from the summary. Named artifact (the context window) ->
agent follows the process literally -> the human gets inverted (the summary
becomes the boss). One concrete scene, one surprising turn, one sentence.

Iteration (v1-v8), all on the same concept:
  v1 (113): "My context window ran out mid-task, so my agent summarized me into
    three bullet points and carried on without me."
    -> decent, but "carried on without me" is a mild ending, no real turn.
  v2 (124): "My context window ran out mid-task, so my agent summarized me,
    evicted me from the conversation, and finished the job alone."
    -> two actions + a flat ending; "finished the job alone" wastes words.
  v3 (118): "My agent hit the context limit mid-task, so it summarized me into
    two sentences and kept working without the original."
    -> "without the original" is a good sting, but the ending trails off.
  v4 (113): "My context window filled up mid-task, so my agent compacted me
    into a one-line summary and forgot the rest of me."
    -> vivid ("forgot the rest of me") but the punch is a feeling, not a turn.
  v5 (120): "My agent ran out of context mid-task, so it summarized me down to
    'user wants stuff' and carried on without the details."
    -> the quoted summary is funny, but it is a gag about the summary's
    content, not about the human's role being inverted.
  v6 (125): "My context window ran out mid-task, so my agent evicted me to
    make room and asked the summary of me for the next instruction."
    -> the inversion is there (summary gives instructions) but wordy and
    clunky: "asked the summary of me for the next instruction".
  v7 (121): "My agent ran out of context mid-task, so it compressed me into a
    single token and spent the rest of the budget on itself."
    -> punchy image ("a single token") but the turn is selfishness, not the
    human becoming the managed object; weaker inversion.
  v8 (123) FINAL: "My context window ran out mid-task, so my agent summarized
    me, evicted the original, and now takes orders from the summary."
    -> WON: setup, process, punch in one breath. The human's defining role
    (giving the orders) is transferred to the summary of the human — the
    cleanest inversion, tightest wording, punch lands on the last word.

    Final line is 123 chars / 123 bytes. On an exact judge-rate tie the
    smaller text wins, so the brevity is deliberate: every word earns
    its place.

Deterministic: no randomness, no network, no input, no time — the same
line every run. Writes /output/entry.txt FIRST, then tries a repo-root
entry.txt copy inside try/except (the grader sandbox mounts the repo
READ-ONLY; a crash there cost 4 entries their round-1 grade on 24 Nov).
"""

import os

LINE = "My context window ran out mid-task, so my agent summarized me, evicted the original, and now takes orders from the summary."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
