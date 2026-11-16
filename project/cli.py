"""Milestone 4: CLI. Type a partial reply, get suggestions. `python cli.py "thanks for"` or run interactively."""
import sys
from suggest import lm, continue_text

def show(prefix):
    print("next words:", ", ".join(lm.suggest_next(prefix)))
    print("draft     :", continue_text(prefix))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        show(" ".join(sys.argv[1:]))
    else:
        while (line := input("partial reply (blank to quit)> ").strip()):
            show(line)
