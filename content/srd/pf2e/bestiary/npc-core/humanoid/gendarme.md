---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gendarme"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gendarme"
level: 8
source: "NPC Core"
aon_id: "creature-3563"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3563"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gendarme"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +16, Legal Lore +14"
abilityMods: [4, 1, 4, 0, 3, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 composite longbow_ (20 arrows), _+1 striking flail_, _+1 gauntlet_, Half Plate"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +14; __Will__: +17 (nerves of steel)"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Nerves of Steel"
    desc: "When the gendarme succeeds against a fear effect, they get a critical success instead."
  - name: "Reactive Strike"
    desc: "⬲ The gendarme can Disarm instead of Striking."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _flail_ +19 (Disarm, Magical, Sweep, Trip) __Damage__ 2d6+10 bludgeoning plus Improved Knockdown"
  - name: "Melee"
    desc: "⬻ _gauntlet_ +19 (Agile, Free-Hand, Magical) __Damage__ 1d4+10 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +16 (deadly d10, Magical, Propulsive, range increment 100 feet, volley 30 feet) __Damage__ 1d8+8 piercing __Stop in the Name of the Law!__ ⬺ (Incapacitation, Linguistic) The gendarme Strides twice and then Demoralizes. On a success, the target is slowed with a value equal to its frightened value until it is no longer frightened."
abilities_bot:
  - name: "Shoot Down"
    desc: "⬺ The gendarme carefully makes a ranged Strike. If the Strike deals damage, the target must succeed at a DC 26 Reflex saving throw or fall prone."
sourcebook: "_NPC Core_, page 117."
```

```encounter-table
name: Gendarme
creatures:
  - 1: Gendarme
```
