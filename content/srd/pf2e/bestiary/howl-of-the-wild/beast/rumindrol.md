---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rumindrol"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Rumindrol"
level: 15
source: "Howl of the Wild"
aon_id: "creature-3303"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3303"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Rumindrol"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Rare"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; motion sense 120 feet, no vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +25"
abilityMods: [9, 6, 7, -1, 5, -1]
abilities_top:
  - name: "Motion Sense"
    desc: "A rumindrol can sense nearby motion through vibration and air movement."
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +30; __Ref__: +26; __Will__: +23"
hp: 295
health:
  - name: "HP"
    desc: "295; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
abilities_mid:
  - name: "Dreadful Resonance"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]]) 60 feet. Each creature that enters or starts its turn in the emanation must succeed at a DC 36 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (enfeebled 2 on a critical failure) and take 3d8 sonic damage."
  - name: "Enthralling Call"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 1 mile. Each non-rumindrol creature that enters or starts its turn within the emanation must succeed at a DC 26 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]]. The creature then becomes temporarily immune to this effect for 1 day (1 hour on a critical failure). Any creature fascinated in this way will attempt to find the source of the rumindrol's cry, mindlessly wandering towards it."
speed: "20 feet, burrow 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+15 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ leg +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+15 slashing"
  - name: "Ranged"
    desc: "⬻ focused resonance +30 (range increment 120 feet) __Damage__ 3d10+15 sonic"
abilities_bot:
  - name: "Entropic Cry"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]]) The rumindrol focuses its sonic emanations on a creature it's aware of within the area of its enthralling call aura. The target must attempt a DC 31 Fortitude save."
  - name: "Critical Success"
    desc: "The creature becomes temporarily immune to Entropic Cry for 1 hour."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]."
  - name: "Failure"
    desc: "The target is sickened 2."
  - name: "Critical Failure"
    desc: "The target is sickened 2, [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]], and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]]."
  - name: "Fast Swallow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The rumindrol Grabs a creature"
  - name: "Effect"
    desc: "The rumindrol uses Swallow Whole."
  - name: "Inexorable"
    desc: "The rumindrol recovers from the [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]], and [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] conditions at the end of its turn. It's also immune to penalties to its Speeds and the immobilized condition, and it ignores difficult terrain and greater difficult terrain."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Huge, 3d10+9 bludgeoning, Rupture 30"
  - name: "Thrash"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) The rumindrol attempts individual Strikes against each creature in its reach. It can attempt up to one jaws Strike and any number of leg Strikes. Each attack counts toward the rumindrol's multiple attack penalty, but the penalty doesn't increase until after it makes all the attacks."
  - name: "Trample"
    desc: "⬽ Huge or smaller, leg, DC 36"
sourcebook: "_Howl of the Wild_, page 176."
```

```encounter-table
name: Rumindrol
creatures:
  - 1: Rumindrol
```
