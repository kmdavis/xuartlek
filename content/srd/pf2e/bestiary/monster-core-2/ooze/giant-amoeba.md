---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Amoeba"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/small
statblock: inline
name: "Giant Amoeba"
level: 1
source: "Monster Core 2"
aon_id: "creature-4496"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4496"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Amoeba"
level: "Creature 1"
size: "Small"
trait_01: "Amphibious"
trait_02: "Mindless"
trait_03: "Ooze"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; motion sense 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Athletics +6, Stealth +3"
abilityMods: [3, -2, 2, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A giant amoeba can sense nearby creatures through vibration and air or water movement."
ac: 8
armorclass:
  - name: "AC"
    desc: "8; __Fort__: +7; __Ref__: +3; __Will__: +5"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ acid, bleed, critical hits, mental, precision, unconscious, visual; __Weaknesses__ slashing 5"
speed: "10 feet, climb 10 feet, swim 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +9 __Damage__ 1d6 acid plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d4 bludgeoning plus 1d4 acid, DC 17"
  - name: "Envelop"
    desc: "⬽"
  - name: "Requirements"
    desc: "The giant amoeba begins its turn with a target its size or smaller grabbed"
  - name: "Effect"
    desc: "The giant amoeba maintains the Grab and extends pseudopods to surround the creature and pull it inside the amoeba's body. This thereafter has the same effect as if the amoeba had Engulfed the creature (DC 17, 1d6 acid, Escape DC 17, Rupture 3)."
  - name: "Weak Acid"
    desc: "A giant amoeba's acid damages only organic material—not metal, stone, or other inorganic substances. Amoebas Large And Small Giant amoebas and amoeba swarms are usually found near each other, as the two oozes are part of the same life cycle. When a giant amoeba grows large enough, it can spontaneously split apart into two separate amoeba swarms, and when an amoeba swarm feeds enough, its individual components can fuse together into a single creature."
sourcebook: "_Monster Core 2_, page 241."
```

```encounter-table
name: Giant Amoeba
creatures:
  - 1: Giant Amoeba
```
