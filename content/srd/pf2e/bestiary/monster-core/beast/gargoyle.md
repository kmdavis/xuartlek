---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gargoyle"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/medium
statblock: inline
name: "Gargoyle"
level: 4
source: "Monster Core"
aon_id: "creature-3001"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3001"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gargoyle"
level: "Creature 4"
size: "Medium"
trait_01: "Beast"
trait_02: "Earth"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common, Petran"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +9, Stealth +12"
abilityMods: [3, 2, 3, -2, 2, -2]
abilities_top:
  - name: "Recall Knowledge - Beast"
    desc: "(Arcana, Nature): DC 19"
  - name: "Unspecific Lore"
    desc: ": DC 17"
  - name: "Specific Lore"
    desc: ": DC 14 Gargoyle Medium Beast Earth"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +10; __Will__: +10"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ bleed; __Resistances__ physical 5 (except adamantine)"
abilities_mid:
  - name: "Clawed Feet"
    desc: "⬲ (attack)"
  - name: "Trigger"
    desc: "The gargoyle is Flying, and a creature moves into an adjacent square below it"
  - name: "Effect"
    desc: "The gargoyle makes a claw Strike against the triggering creature."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+3 piercing"
  - name: "Melee"
    desc: "⬻ claw +13 (Agile) __Damage__ 2d6+3 slashing"
abilities_bot:
  - name: "Statue"
    desc: "⬻ (Concentrate) Until the next time it acts, the gargoyle appears to be a statue. It has an automatic result of 32 on Deception checks and DCs to pass as a statue. Gargoyle Religion Although gargoyles roosting at a religious site eventually gravitate towards that god's ethos and frequently become followers, other gargoyle wings reconsecrate crumbling temples to their own gods. Most such wings hold up a demon lord or one of the lords of the Plane of Earth as their creator and patron."
sourcebook: "_Monster Core_, page 155."
```

```encounter-table
name: Gargoyle
creatures:
  - 1: Gargoyle
```
