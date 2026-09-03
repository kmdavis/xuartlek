---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Greater Chimera"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Greater Chimera"
level: 13
source: "Howl of the Wild"
aon_id: "creature-3257"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3257"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Greater Chimera"
level: "Creature 13"
size: "Huge"
trait_01: "Beast"
trait_02: "Rare"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27"
abilityMods: [8, 4, 5, -2, 3, 1]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +23; __Will__: +20"
hp: 235
health:
  - name: "HP"
    desc: "235"
abilities_mid:
  - name: "Multiple Reactions"
    desc: "A greater chimera gains 2 extra reactions each round that it can use only to make Reactive Strikes. It must use a different head for each reaction, and it can't use more than one on the same triggering action. If it loses one of its heads, it also loses one of these extra reactions."
  - name: "Three-Headed"
    desc: "Any ability that would sever a greater chimera's head (such as a critical hit with a [[srd/pf2e/compendium/equipment/runes/vorpal|_vorpal_]] weapon) severs one head at random. Losing a head doesn't kill a chimera (as long as it has at least one head left), but it does prevent it from making Strikes with the lost head or using any abilities granted by the head."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 3d8+8 slashing"
abilities_bot:
  - name: "Three-Headed Strike"
    desc: "⬺ The greater chimera makes a Strike with each of its heads, each at a –2 penalty and targeting a different creature. These Strikes count as only one attack for the greater chimera's multiple attack penalty, and the penalty doesn't increase until after it has made all three attacks."
sourcebook: "_Howl of the Wild_, page 133."
```

```encounter-table
name: Greater Chimera
creatures:
  - 1: Greater Chimera
```
