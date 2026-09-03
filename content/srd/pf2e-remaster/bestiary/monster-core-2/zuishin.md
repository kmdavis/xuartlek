---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zuishin"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/kami
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/medium
statblock: inline
name: "Zuishin"
level: 10
source: "Monster Core 2"
aon_id: "creature-4455"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4455"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Zuishin"
level: "Creature 10"
size: "Medium"
trait_01: "Kami"
trait_02: "Spirit"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Common, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +22, Intimidation +19, Medicine +21, Nature +21, Stealth +21"
abilityMods: [6, 7, 5, 1, 5, 3]
abilities_top:
  - name: "Ward"
    desc: "(divine) Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. A zuishin's ward is a specific gate, doorway, or shrine."
  - name: "Items"
    desc: "_+1 breastplate_, _+1 composite longbow_, _+1 katana_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +19; __Ref__: +23; __Will__: +17"
hp: 180
health:
  - name: "HP"
    desc: "180; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _holy katana_ +23 (deadly d8, holy, magical, two-hand d10, versatile P) __Damage__ 2d6+9 slashing plus 1d4 spirit"
  - name: "Ranged"
    desc: "⬻ _holy composite longbow_ +24 (deadly d10, holy, magical, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 2d8+9 piercing plus 1d4 spirit"
abilities_bot:
  - name: "Healing Arrow"
    desc: "⬺ (Divine, healing) The zuishin blesses an arrow with healing magic. They expend a _breath of life_, _cleanse affliction_, _heal_, or _sure footing_ spell and make a _composite longbow_ Strike against an ally. A critical failure has no effect, but on any other result the ally is affected by the spell rather than taking damage from the Strike."
  - name: "Holy Weaponry"
    desc: "(Divine, holy) Any weapon becomes a _striking holy weapon_ while the zuishin wields it. A zuishin creates arrows out of nothing as part of their attacks with any bow they wield. Attracting A Kami Different cultures have different beliefs about the best way to attract a kami spirit, such as a zuishin. Societies that strive to preserve the natural world—like elven tree-cities and small villages that balance their own population with those of other local creatures—are the most likely to be graced by a kami’s presence."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __3rd__ Heal (×2), Share Life - __4th__ Cleanse Affliction, Sure Footing - __5th__ Breath of Life, Dispel Magic, Heal, Translocate (×3)"
sourcebook: "_Monster Core 2_, page 206."
```

```encounter-table
name: Zuishin
creatures:
  - 1: Zuishin
```
