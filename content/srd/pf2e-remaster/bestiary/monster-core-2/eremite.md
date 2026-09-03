---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eremite"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Eremite"
level: 20
source: "Monster Core 2"
aon_id: "creature-4611"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4611"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Eremite"
level: "Creature 20"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; greater darkvision, painsight, _truesight_"
languages: "Common, Diabolic, Shadowtongue; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +33, Deception +38, Diplomacy +36, Intimidation +40, Medicine +36, Religion +34, Stealth +36, Torture Lore +36"
abilityMods: [9, 6, 7, 6, 6, 10]
abilities_top:
  - name: "Painsight"
    desc: "(divine) A velstrac automatically knows whether a creature it sees has any of the doomed, dying, and wounded conditions as well as the value of those conditions."
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +37; __Ref__: +32; __Will__: +34 +1 status to all saves vs. magic"
hp: 375
health:
  - name: "HP"
    desc: "375 , regeneration 25 (deactivated by holy or silver); __Immunities__ cold, fear, nonlethal; __Weaknesses__ holy 20, silver 20"
abilities_mid:
  - name: "Ignore Pain"
    desc: "An eremite's actions can't be disrupted due to damage or Strikes (such as Reactive Strike)."
  - name: "Paralytic Perfection"
    desc: "(aura, divine, fear, incapacitation, mental, visual) 30 feet. When a creature ends its turn in the aura, it feels compelled to offer pieces of its own flesh to the eremite. The creature must succeed at a DC 40 Will save or become paralyzed for 1 round."
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +39 (Magical, unholy) __Damage__ 4d8+19 piercing plus 2d6 persistent bleed and exquisite pain"
  - name: "Melee"
    desc: "⬻ claw +39 (Agile, magical, unholy) __Damage__ 3d6+19 slashing plus 2d6 persistent bleed, exquisite pain, and Improved Grab"
abilities_bot:
  - name: "Evisceration"
    desc: "⬻ (Attack)"
  - name: "Requirements"
    desc: "The eremite has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The eremite excises flesh or bone from a creature they've grabbed or restrained. The target takes 6d10 persistent bleed damage."
  - name: "Exquisite Pain"
    desc: "An eremite's knowledge of pressure points and pain centers is unsurpassed. A creature hit by an eremite's melee Strikes must succeed at a DC 40 Fortitude save or be stunned 2 (stunned 4 on a critical failure). A creature that critically succeeds is temporarily immune for 24 hours."
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, mental, visual) The eremite stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against paralytic perfection. In addition, if the creature was already paralyzed, on a failed save, its unnatural longing causes it to become doomed 1. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the eremite's next turn."
  - name: "Graft Flesh"
    desc: "⬻"
  - name: "Requirements"
    desc: "The eremite holds a piece of flesh they collected via Evisceration"
  - name: "Effect"
    desc: "The eremite attaches the stolen flesh to themself. They either regain 100 Hit Points; reduce the value of their clumsy, drained, enfeebled, or stupefied condition by 3; or reduce the stage of any affliction affecting them by 3."
  - name: "Shadow Traveler"
    desc: "(Divine) When an eremite uses _interplanar teleport_, they arrive at exactly their intended destination."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42 - __Cantrips (9th)__ Stabilize - __7th__ Interplanar Teleport (to the Netherworld or the Universe only), Planar Seal, Shadow Blast, Translocate (at will), Warp Mind - __9th__ Blessed Boundary, Harm (×2), Heal (×2), Seize Soul, Shadow Blast - __Constant (9th)__ Truesight"
sourcebook: "_Monster Core 2_, page 348."
```

```encounter-table
name: Eremite
creatures:
  - 1: Eremite
```
