"""Filenames for imported SRD notes.

Convention, matching the rest of the vault:

  * things with names get their name        -> ``Goblin Warrior.md``
  * categories and sources stay kebab-case  -> ``bestiary/monster-core/humanoid/``

So a creature lands at::

    content/srd/pf2e/bestiary/monster-core/humanoid/Goblin Warrior.md

and NOT at ``bestiary/Monster Core/humanoid/...``: ``monster-core`` is a source,
which is a category, so it stays kebab.

This is URL-neutral. Quartz's ``slugifyFilePath`` lowercases and replaces spaces
with hyphens, so ``Goblin Warrior.md`` and ``goblin-warrior.md`` both serve at
``.../goblin-warrior``. Renaming does not break a single existing link.

Folder notes are the exception. A folder note must be named exactly after its
folder for Quartz to collapse it to ``/folder/`` and for the Obsidian
folder-notes plugin to find it, and folders are categories, so those stay kebab.
"""

import re

# Characters that are legal in a note name but hostile in a filename. The colon
# is the one that actually occurs: "Critical Hit Deck: Slashing" and 32 others.
_REPLACEMENTS = ((": ", " - "), (":", " -"), ("/", "-"), ("\\", "-"))
_STRIP = '?*<>"|'


def note_filename(name: str) -> str:
    """Turn a display name into a filename stem, without the extension."""
    out = (name or "").strip()
    for old, new in _REPLACEMENTS:
        out = out.replace(old, new)
    for ch in _STRIP:
        out = out.replace(ch, "")
    out = re.sub(r"\s+", " ", out).strip(" .")
    return out or "Untitled"


def is_folder_note(stem: str, parent_name: str) -> bool:
    return stem.lower() == parent_name.lower()
