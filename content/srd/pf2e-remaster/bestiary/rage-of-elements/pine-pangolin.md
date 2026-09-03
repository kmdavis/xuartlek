---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pine Pangolin"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Pine Pangolin"
level: 7
source: "Rage of Elements"
aon_id: "creature-2676"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2676"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Pine Pangolin"
level: "Creature 7"
size: "Medium"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
skills:
  - name: "Skills"
    desc: "Nature +15, Survival +18, Athletics +17"
abilityMods: [4, 0, 5, 1, 2, 1]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +10; __Will__: +18"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ axes 5, fire 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +17 (Agile) __Damage__ 2d12+3 piercing"
  - name: "Melee"
    desc: "⬻ tongue +17 __Damage__ 2d8+3 bludgeoning plus Grab"
abilities_bot:
  - name: "Roll Up"
    desc: "⬻ (Move) The pine pangolin falls prone, closes up its scales, and rolls into a ball. While Rolled Up, the pangolin gains resistance 10 to physical damage and total immunity to falling damage from heights of 50 feet or less. The only action the pine pangolin can take is to Stand, and the effects of Roll Up end once the pangolin Stands."
  - name: "Secrete Tar"
    desc: "⬻ (Plant) The pine pangolin secretes a brown, sticky tar within a 5-foot emanation, making those squares difficult terrain for 1 minute. Each creature that enters or starts its turn in a tarred square must succeed at a DC 25 Fortitude save or become immobilized until it Escapes. On a critical failure, the creature falls prone; prone creatures take a –2 circumstance penalty to their checks to Escape the tar. The pine pangolin is immune to the effects of its own tar. More Wooded Origins Pine pangolins grow in clusters of two to five individuals on giant trees, protected by a cozy layer of tar until their scales harden enough for their first drop. Snapdrakes are handcrafted for kizidhar nobility, often serving as loyal guards. Nobody knows where painted stags come from, as all who have tried to investigate have been eaten."
sourcebook: "_Rage of Elements_, page 208."
```

```encounter-table
name: Pine Pangolin
creatures:
  - 1: Pine Pangolin
```
