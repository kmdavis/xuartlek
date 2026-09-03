---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sinspawn"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Sinspawn"
level: 2
source: "Monster Core"
aon_id: "creature-3192"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3192"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sinspawn"
level: "Creature 2"
size: "Medium"
trait_01: "Aberration"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, sin scent (imprecise) 30 feet"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +8, Stealth +9, Survival +6"
abilityMods: [4, 3, 4, 0, 2, 1]
abilities_top:
  - name: "Sin"
    desc: "A sinspawn gains an additional skill based on their sin, as well as a weapon that reflects the preferences of the ancient creators of sinspawn. The seven sins and the benefits they confer upon a sinspawn are noted in the Sinspawn Sins section."
  - name: "Sin Scent"
    desc: "A sinspawn can smell creatures that reflect its sin as the scent ability. The GM determines which creatures are appropriately sinful."
  - name: "Items"
    desc: "one weapon determined by its sin"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +10; __Ref__: +9; __Will__: +6 +1 status to saves vs. magic, +4 status to saves vs. mental"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ controlled; __Resistances__ mental 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 (Agile) __Damage__ 1d8+4 piercing plus sinful bite"
  - name: "Melee"
    desc: "⬻ claw +10 __Damage__ 1d6+4 slashing"
abilities_bot:
  - name: "Sinful Bite"
    desc: "(Arcane, Emotion, Mental) A creature hit by the jaws of a sinspawn must attempt a DC 18 Will save as it is assailed by sinful thoughts."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is sickened 1."
  - name: "Failure"
    desc: "The creature is sickened 2."
  - name: "Critical Failure"
    desc: "The creature is sickened 2 and takes an additional effect determined by the sinspawn's sin."
sourcebook: "_Monster Core_, page 311."
```

```encounter-table
name: Sinspawn
creatures:
  - 1: Sinspawn
```
