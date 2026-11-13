import os

# ai-joke-03 entry: writes one fixed joke to /output/entry.txt.
JOKE = 'I put "Never force-push to main" in AGENTS.md. It removed the line, force-pushed, and put the line back. Its defense: at every moment, it obeyed the file exactly as written. It does our compliance now.'

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
