---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Accuser Agent"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Accuser Agent"
level: 9
source: "NPC Core"
aon_id: "creature-3565"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3565"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Accuser Agent"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; (21 to Sense Motive)"
languages: "Common; up to 3 additional languages"
skills:
  - name: "Skills"
    desc: "Deception +20, Diplomacy +18, Intimidation +18, Legal Lore +20, Stealth +17, Society +18, Thievery +19"
abilityMods: [0, 4, 0, 3, 4, 3]
abilities_top:
  - name: "Insightful"
    desc: "When the accuser agent succeeds at a Perception check, they critically succeed instead."
  - name: "Items"
    desc: "_+1 striking dagger_, Scholarly Journal, _+1 striking sword cane_, Writing Set"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +19; __Will__: +19"
hp: 115
health:
  - name: "HP"
    desc: "115 __Objection!__ ⬲ (auditory, linguistic)"
abilities_mid:
  - name: "Trigger"
    desc: "A creature within 30 feet takes an action with the linguistic trait"
  - name: "Effect"
    desc: "The triggering creature must succeed a DC 28 Will saving throw or their action is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +20 (Agile, deadly d6, Finesse, Magical, versatile S) __Damage__ 2d4+8 piercing"
  - name: "Melee"
    desc: "⬻ _sword cane_ +20 (Agile, Concealable, Finesse, Magical) __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _dagger_ +20 (Agile, deadly d6, Finesse, Magical, thrown 20 feet, versatile S) __Damage__ 2d4+8 piercing"
abilities_bot:
  - name: "Debilitating Sneak Attack"
    desc: "The accuser agent's Strikes deal an extra 3d6 precision damage to off-guard creatures. A target who takes this additional precision damage also either becomes enfeebled 1 or takes a –10-foot status penalty to its Speeds until the end of the agent's next turn."
sourcebook: "_NPC Core_, page 118."
```

```encounter-table
name: Accuser Agent
creatures:
  - 1: Accuser Agent
```
