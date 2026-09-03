---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sage"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sage"
level: 6
source: "NPC Core"
aon_id: "creature-3593"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3593"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Sage"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common; up to 4 additional languages"
skills:
  - name: "Skills"
    desc: "Arcana +12, Diplomacy +13, Medicine +12, Nature +14, Occultism +12, Religion +12, Society +14"
abilityMods: [2, 2, 1, 4, 3, 0]
abilities_top:
  - name: "Items"
    desc: "religious symbol, _+1 staff_"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +10; __Ref__: +12; __Will__: +16"
hp: 86
health:
  - name: "HP"
    desc: "86"
abilities_mid:
  - name: "Timely Advice"
    desc: "⬲ (auditory, concentrate, linguistic, mental)"
  - name: "Trigger"
    desc: "An ally is about to attempt an attack roll or skill check and has not yet rolled"
  - name: "Effect"
    desc: "The sage gives the ally a savvy piece of advice, providing valuable insight. The ally gains a +2 circumstance bonus to the triggering roll."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +13 (Magical, two-hand d8) __Damage__ 1d4+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Sage's Analysis"
    desc: "⬻ (Concentrate) The sage studies a creature, attempting an Arcana, Nature, Occultism, Religion, or Society check against the creature's Recall Knowledge DC. On a success, the sage gains a +2 circumstance bonus to attack rolls and AC against that creature and deals an additional 2d6 damage to the creature with weapon attacks. These benefits last for 1 minute or until the sage uses this ability again."
sourcebook: "_NPC Core_, page 141."
```

```encounter-table
name: Sage
creatures:
  - 1: Sage
```
