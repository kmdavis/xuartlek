---
noteType: pf2eMonster
aliases: "Orc Commander"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Commander"
level: 2
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3132"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Orc Commander"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Orcish|Orcish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +5"
abilityMods: [4, 2, 1, -1, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Greatclub, Hide Armor, Javelin (6)"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +6; __Will__: +7"
hp: 32
health:
  - name: "HP"
    desc: "32"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatclub +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 1d10+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Battle Cry"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) Bellowing mightily, the orc commander gives themself and all orc allies within 60 feet a +1 status bonus to attack and damage rolls until the start of the orc commander's next turn."
sourcebook: "_Monster Core_, page 259."
```

```encounter-table
name: Orc Commander
creatures:
  - 1: Orc Commander
```
