---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Megaprimatus"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Megaprimatus"
level: 8
source: "Monster Core"
aon_id: "creature-2828"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2828"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Megaprimatus"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19"
abilityMods: [7, 2, 5, -4, 1, 2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +16; __Will__: +13"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d8+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+10 piercing"
abilities_bot:
  - name: "Mangling Rend"
    desc: "⬺ A megaprimatus makes two fist Strikes against the same target. If both hit, the attack deals an additional 2d6 bludgeoning damage, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], and the target takes a –20-foot status penalty to all Speeds until the end of its next turn."
  - name: "Terrifying Display"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The megaprimatus beats its chest in a terrifying display. Creatures within 50 feet must attempt a DC 27 Will save. While a creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] by this ability, it is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the megaprimatus and to gorillas."
  - name: "Critical Success"
    desc: "No effect and temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is frightened 1."
  - name: "Critical Failure"
    desc: "The creature is frightened 2 and [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] until the end of its next turn."
sourcebook: "_Monster Core_, page 23."
```

```encounter-table
name: Megaprimatus
creatures:
  - 1: Megaprimatus
```
