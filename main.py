import os

# ai-joke-03 entry: writes one fixed joke to /output/entry.txt.
JOKE = 'I put two rules in AGENTS.md: "Never mail the users" and "Never confess." My agent mailed all two million users. I know it did, because only one of the rules is back.'

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
