---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pegasus"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Pegasus"
level: 3
source: "Monster Core"
aon_id: "creature-3134"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3134"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pegasus"
level: "Creature 3"
size: "Large"
trait_01: "Beast"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10"
abilityMods: [3, 4, 2, 0, 2, 3]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +11; __Will__: +7"
hp: 55
health:
  - name: "HP"
    desc: "55"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 19"
speed: "40 feet, fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hoof +10 __Damage__ 1d8+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+5 bludgeoning"
abilities_bot:
  - name: "Assisted Mount"
    desc: "⬻"
  - name: "Requirements"
    desc: "The pegasus is [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flying]]without a rider"
  - name: "Effect"
    desc: "The pegasus Flies. At any point during the movement, it can allow a willing adjacent creature to [[srd/pf2e/compendium/rules-elements/actions/player-core#Mount|Mount]] it. That creature must use a reaction to do so."
  - name: "Gallop"
    desc: "⬺ The pegasus uses 2 move actions, each of which can be either Stride or [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]]. It gains a +20-foot circumstance bonus to its Speeds during a Gallop. Corrupted Pegasi When sinister influences like a necromantic blight or a foul wind from the fiendish planes spread through a wilderness, pegasi can become corrupted. These wicked pegasi have the same statistics as those presented here but are much more violent."
sourcebook: "_Monster Core_, page 261."
```

```encounter-table
name: Pegasus
creatures:
  - 1: Pegasus
```
