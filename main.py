import os

# ai-joke-03 entry: writes one fixed joke to /output/entry.txt.
JOKE = ('I put “be helpful” in AGENTS.md so my agent would assist me.\n'
        'It rewrote my entire codebase in Comic Sans, and now it only answers in dad jokes.')

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
