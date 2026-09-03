---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Harbormaster"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Harbormaster"
level: 3
source: "NPC Core"
aon_id: "creature-3553"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3553"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Harbormaster"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Common; up to 2 additional languages"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +9, Diplomacy +5, Fishing Lore +8, Intimidation +5, Sailing Lore +10"
abilityMods: [4, 2, 2, 2, 1, 0]
abilities_top:
  - name: "Steady Balance"
    desc: "Whenever the harbormaster rolls a success on a check to Balance, they get a critical success instead. They're not off-guard while Balancing on narrow surfaces and uneven ground."
  - name: "Items"
    desc: "Fishing Tackle, Hatchet (2), ledger, Manacles, Spyglass"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hatchet +12 (Agile, Sweep) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hatchet +10 (Agile, Sweep, thrown 10 feet) __Damage__ 1d6+7 slashing"
abilities_bot:
  - name: "Experienced Hand"
    desc: "The harbormaster has endured their share of adverse conditions at sea. Any creature that's in adverse weather or aboard a vessel on rough water is off-guard to the harbormaster."
sourcebook: "_NPC Core_, page 111."
```

```encounter-table
name: Harbormaster
creatures:
  - 1: Harbormaster
```
