---
noteType: pf2eMonster
aliases: "Ghost Ape"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Ghost Ape"
level: 4
source: "Howl of the Wild"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3272"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Ghost Ape"
level: "Creature 4"
size: "Large"
trait_01: "Beast"
trait_02: "Ethereal"
trait_03: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [5, 2, 3, -1, 4, 2]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +10; __Will__: +12"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 2d8+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 1d10+5 bludgeoning"
abilities_bot:
  - name: "Ghost Stance"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Stance|Stance]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The ghost ape phases partially out of existence, its form blurring and becoming difficult to pinpoint. While in this stance, they are [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] to any creature that isn't adjacent to them. They can't use this concealment to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneak]]. They also gain resistance 5 to physical damage. If the ghost ape takes force damage, this stance ends and they can't reenter it for 1d3 rounds."
  - name: "Phantom Step"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|Teleportation]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The ghost ape moves quickly, passing through the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]]. They teleport up to a distance equal to twice their Speed within their line of sight."
  - name: "Terrifying Display"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The ghost ape beats their chest in a terrifying display. Creatures within 30 feet must succeed a DC 20 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]] (or frightened 2 on a critical failure). While a creature is frightened by this ability, it's [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the ape. On a success, the creature is temporarily immune for 1 minute."
sourcebook: "_Howl of the Wild_, page 146."
```

```encounter-table
name: Ghost Ape
creatures:
  - 1: Ghost Ape
```
