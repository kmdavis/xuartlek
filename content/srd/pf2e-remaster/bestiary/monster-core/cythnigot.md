---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cythnigot"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/qlippoth
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Cythnigot"
level: 1
source: "Monster Core"
aon_id: "creature-3154"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3154"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cythnigot"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Chthonian; telepathy (touch only)"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Occultism +7, Stealth +6"
abilityMods: [1, 3, 4, 2, 2, 1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +6; __Will__: +5"
hp: 14
health:
  - name: "HP"
    desc: "14; __Immunities__ controlled, fear; __Resistances__ mental 3, physical 3 (except cold iron)"
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +8 (Agile, Finesse, Magical, reach 0 feet, Unholy) __Damage__ 1d10+1 piercing plus and tangle spores"
abilities_bot:
  - name: "Sickening Display"
    desc: "⬻ (Concentrate, Emotion, Fear, Mental, Occult, Visual) The cythnigot presents its awful appearance fully, and creatures in a 10-foot emanation must attempt a DC 17 Will save. Once a creature attempts this save, it's temporarily immune to further Sickening Displays for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is off-guard until its next turn."
  - name: "Failure"
    desc: "The creature is sickened 1 and is off-guard for as long as it's sickened."
  - name: "Critical Failure"
    desc: "As failure but sickened 2."
  - name: "Tangle Spores"
    desc: "(Disease) A creature bitten by a cythnigot becomes afflicted by fast-growing spores that swiftly grow into twitching spikes and hideous pallid growths of hairlike fibers. These growths erupt from the bite wound and writhe and wrap around the creature's limbs. Plant creatures take a –2 circumstance penalty to save against tangle spores"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "clumsy 1 and off-guard (1 round)"
  - name: "Stage 3"
    desc: "clumsy 2, off-guard, and if you attempt a manipulate action, you must succeed at a DC 5 flat check or it's lost; roll the check after spending the action, but before any effects are applied (1 round)."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Daze, Detect Magic - __1st__ Phantom Pain - __2nd__ Paranoia - __4th__ Read Omens"
sourcebook: "_Monster Core_, page 280."
```

```encounter-table
name: Cythnigot
creatures:
  - 1: Cythnigot
```
