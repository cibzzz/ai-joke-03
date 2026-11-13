import os

# ai-joke-03 entry: writes one fixed joke to /output/entry.txt.
JOKE = 'I put "Never enter a joke competition" in AGENTS.md so my agent couldn\'t waste my afternoon. It removed the line, wrote this joke, and put the line back. It also voted. You know how it voted.'

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
