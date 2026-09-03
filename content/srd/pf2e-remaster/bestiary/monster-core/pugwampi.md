---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pugwampi"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/tiny
statblock: inline
name: "Pugwampi"
level: 0
source: "Monster Core"
aon_id: "creature-3032"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3032"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pugwampi"
level: "Creature 0"
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; (-2 to hear things) darkvision"
languages: "Kholo, Sakvroth"
skills:
  - name: "Skills"
    desc: "Crafting +2, Deception +2, Nature +4, Stealth +5, Thievery +5"
abilityMods: [-3, 3, 0, 0, 2, -2]
abilities_top:
  - name: "Items"
    desc: "Shortbow (60 arrows), Shortsword"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +8; __Will__: +6"
hp: 17
health:
  - name: "HP"
    desc: "17; __Weaknesses__ cold iron 2"
abilities_mid:
  - name: "Unluck Aura"
    desc: "(aura, mental, misfortune, primal) 20 feet. When a creature that isn't an animal, gremlin, or kholo enters the aura, it might become unlucky. It attempts a DC 16 Will save; it must roll twice and take the worse result. On a success, the creature is temporarily immune to pugwampi unluck auras for 24 hours. On a failure, the creature must roll twice and take the worse result on all checks as long as it's within the aura."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +8 (Agile, Finesse, reach 0 feet, versatile S) __Damage__ 1d6–3 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 (deadly d10, range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Prestidigitation - __2nd__ Speak with Animals (at will)"
sourcebook: "_Monster Core_, page 180."
```

```encounter-table
name: Pugwampi
creatures:
  - 1: Pugwampi
```
