import os
from pathlib import Path

ENTRY = "I circled that dust twice, declared it a protected historic site, and docked myself for trespassing."

def main():
    os.makedirs("/output", exist_ok=True)
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
