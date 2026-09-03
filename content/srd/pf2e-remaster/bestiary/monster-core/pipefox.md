---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pipefox"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/tiny
statblock: inline
name: "Pipefox"
level: 2
source: "Monster Core"
aon_id: "creature-3138"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3138"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pipefox"
level: "Creature 2"
size: "Tiny"
trait_01: "Beast"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Common, Draconic; _translate_"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Arcana +9, Athletics +7, Occultism +9, Society +9, Stealth +8"
abilityMods: [3, 4, 3, 4, 1, 3]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +8; __Ref__: +11; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 (Finesse, reach 0 feet) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Master of Tongues"
    desc: "Even if the pipefox does not speak a creature's language, it can rapidly pick up on inflection, root words, and body language. If the pipefox interacts or observes a creature for at least 10 minutes and that creature can speak a language, it can communicate basic concepts to that creature."
  - name: "Rapid Erudition"
    desc: "⬻ (Concentrate)"
  - name: "Requirements"
    desc: "The pipefox saw a cantrip cast within the last minute"
  - name: "Effect"
    desc: "The pipefox can cast the cantrip it saw as an innate arcane spell for 1 minute. Hoarders of Knowledge Nothing is as valuable to a pipefox as knowledge. They often fill their space with the books and tools they've secretly collected over the years. While these books are often on seemingly mundane topics, it is not uncommon to find a magic scroll or two hidden away in a pipefox's home."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 18, attack +8 - __2nd__ Invisibility (at will; self only Cantrips) - __Constant (2nd)__ Translate"
sourcebook: "_Monster Core_, page 265."
```

```encounter-table
name: Pipefox
creatures:
  - 1: Pipefox
```
