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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +14"
abilityMods: [4, 1, 4, 0, 3, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_ (20 arrows), _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/flail/flail|flail]]_, _+1 [[srd/pf2e/compendium/equipment/weapons/brawling/gauntlet|gauntlet]]_, Half Plate"
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
    desc: "⬲ The gendarme can [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] instead of Striking."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _flail_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 2d6+10 bludgeoning plus Improved Knockdown"
  - name: "Melee"
    desc: "⬻ _gauntlet_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d4+10 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+8 piercing __Stop in the Name of the Law!__ ⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]]) The gendarme Strides twice and then [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralizes]]. On a success, the target is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] with a value equal to its [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] value until it is no longer frightened."
abilities_bot:
  - name: "Shoot Down"
    desc: "⬺ The gendarme carefully makes a ranged Strike. If the Strike deals damage, the target must succeed at a DC 26 Reflex saving throw or fall [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
sourcebook: "_NPC Core_, page 117."
```

```encounter-table
name: Gendarme
creatures:
  - 1: Gendarme
```
