---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Apothecary"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Apothecary"
level: -1
source: "NPC Core"
aon_id: "creature-3479"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3479"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Apothecary"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +5, Medicine +10, Nature +8"
abilityMods: [0, 1, 1, 3, 3, 1]
abilities_top:
  - name: "Medical Specialist"
    desc: "For encounters involving making medicine or alchemical contests, the apothecary is a 3rd-level challenge."
  - name: "Medical Wisdom"
    desc: "The apothecary can identify the effect of any alchemical composition or medical ingredient using only their senses. This typically takes 1 minute."
  - name: "Items"
    desc: "lesser acid flask (2), Dagger, minor elixir of life (2), Healer's Toolkit, leather apron (functions as padded armor), mortar and pestle"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +8; __Ref__: +3; __Will__: +5 +1 circumstance to all saves vs. poisons"
hp: 8
health:
  - name: "HP"
    desc: "8; __Resistances__ poison 2"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone pestle +4 __Damage__ 1d6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ acid flask +5 (range increment 20 feet, Splash) __Damage__ 1 acid plus 1d6 persistent acid and 1 splash acid"
sourcebook: "_NPC Core_, page 60."
```

```encounter-table
name: Apothecary
creatures:
  - 1: Apothecary
```
