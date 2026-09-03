---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grothlut"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/medium
statblock: inline
name: "Grothlut"
level: 3
source: "Monster Core"
aon_id: "creature-2997"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2997"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Grothlut"
level: "Creature 3"
size: "Medium"
trait_01: "Aberration"
trait_02: "Mindless"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11"
abilityMods: [4, -2, 4, -5, 0, -3]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +5; __Will__: +7"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]"
abilities_mid:
  - name: "Disgusting Demise"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) When the grothlut is reduced to 0 Hit Points, its digestive organs rupture, unleashing alchemical acid and poison upon all creatures in a 30-foot emanation. Each creature in the area must succeed at a DC 19 Fortitude save or take 2d6 acid damage and become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (double damage and sickened 2 on a critical failure)."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d10+8 slashing"
  - name: "Ranged"
    desc: "⬻ digestive spew +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], range increment 15 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]]) __Damage__ 2d6 acid damage plus 1d6 acid splash damage"
abilities_bot:
  - name: "Piteous Moan"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) 60 feet. Each non-grothlut creature that enters or starts its turn within the area must succeed at a DC 17 Will saving throw or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (sickened 2 on a critical failure). The creature then becomes temporarily immune for 1 minute. The grothlut can Dismiss this aura. A grothlut usually does not begin moaning until it senses the presence of a non-grothlut creature, and it usually stops once it doesn't sense any more such creatures."
sourcebook: "_Monster Core_, page 152."
```

```encounter-table
name: Grothlut
creatures:
  - 1: Grothlut
```
