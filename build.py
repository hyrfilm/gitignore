#!/usr/bin/env python3
"""
build.py - Regenerate the LANGUAGES table in `gitignore` from templates/.

Each templates/<flag>.gitignore is an ordinary gitignore file. Its first line
is a header of the form "# Label: help text" that becomes the section heading
written to .gitignore and the --help text for --<flag>. Blank lines and
comments are dropped; every other line becomes a pattern.

Run ./build.py after adding or editing a template.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, "templates")
SCRIPT = os.path.join(HERE, "gitignore")
BEGIN = "# BEGIN GENERATED (from templates/, run ./build.py)"
END = "# END GENERATED"
# Option names already taken by the gitignore script itself.
RESERVED = {"help", "list", "undo", "patterns"}

# "defaults" first, the rest alphabetical.
def order(flag):
    return (flag != "defaults", flag)


def read_template(path):
    flag = os.path.basename(path)[: -len(".gitignore")]
    with open(path) as f:
        lines = f.read().splitlines()
    header = lines[0] if lines else ""
    m = re.match(r"#\s*(.+?)\s*:\s*(.+)", header)
    if m:
        label, help_text = m.group(1), m.group(2)
        lines = lines[1:]
    else:
        label = flag.capitalize()
        help_text = f"Add {label} ignores"
    patterns = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and line not in patterns:
            patterns.append(line)
    return flag, label, help_text, patterns


def render(entries):
    out = [BEGIN, "LANGUAGES = {"]
    for flag, label, help_text, patterns in entries:
        q = json.dumps
        out.append(f"    {q(flag)}: Lang({q(label)}, {q(help_text)}, [")
        out.extend(f"        {q(p)}," for p in patterns)
        out.append("    ]),")
    out.append("}")
    out.append(END)
    return "\n".join(out)


def main():
    files = sorted(
        (f for f in os.listdir(TEMPLATES) if f.endswith(".gitignore")),
        key=lambda f: order(f[: -len(".gitignore")]),
    )
    entries = [read_template(os.path.join(TEMPLATES, f)) for f in files]
    for flag, *_ in entries:
        if flag in RESERVED:
            sys.exit(f"templates/{flag}.gitignore: --{flag} clashes with a built-in option")

    with open(SCRIPT) as f:
        src = f.read()
    start = src.index(BEGIN)
    end = src.index(END) + len(END)
    new = src[:start] + render(entries) + src[end:]

    if new == src:
        print("gitignore is up to date.")
        return
    with open(SCRIPT, "w") as f:
        f.write(new)
    print(f"Regenerated LANGUAGES in gitignore from {len(entries)} template(s):")
    for flag, label, _, patterns in entries:
        print(f"  --{flag:9} {label:11} {len(patterns)} pattern(s)")


if __name__ == "__main__":
    if not os.path.isdir(TEMPLATES):
        sys.exit(f"No templates directory at {TEMPLATES}")
    main()
