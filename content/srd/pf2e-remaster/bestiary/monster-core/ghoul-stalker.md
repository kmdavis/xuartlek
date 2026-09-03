---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghoul Stalker"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/ghoul
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ghoul Stalker"
level: 1
source: "Monster Core"
aon_id: "creature-3009"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3009"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ghoul Stalker"
level: "Creature 1"
size: "Medium"
trait_01: "Ghoul"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +8, Stealth +7, Survival +5"
abilityMods: [1, 4, 1, 1, 2, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +9; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Stench"
    desc: "(aura, olfactory) 10 feet, DC 14"
speed: "25 feet, burrow 5 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 (Finesse) __Damage__ 1d8+1 piercing"
  - name: "Melee"
    desc: "⬻ claw +9 (Agile, Finesse) __Damage__ 1d6+1 slashing plus Grab"
abilities_bot:
  - name: "Consume Flesh"
    desc: "⬻ (Manipulate) 1d6 HP"
  - name: "Ghoul Whispers"
    desc: "⬻ (Auditory, Linguistic, Occult) DC 17"
  - name: "Grave Knowledge"
    desc: "(Occult) +7 skill modifier"
  - name: "Swift Leap"
    desc: "⬻ (move)"
sourcebook: "_Monster Core_, page 163."
```

```encounter-table
name: Ghoul Stalker
creatures:
  - 1: Ghoul Stalker
```
