---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sedacthy Scout"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/sedacthy
  - pf2e/creature/trait/medium
statblock: inline
name: "Sedacthy Scout"
level: 2
source: "Monster Core"
aon_id: "creature-3178"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3178"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sedacthy Scout"
level: "Creature 2"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Sedacthy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, wavesense 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]; sea speech"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [4, 4, 1, 0, 1, 3]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]] can be understood by any animal that has a swim Speed or the [[srd/pf2e/compendium/rules-elements/traits/player-core/amphibious|amphibious]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/aquatic|aquatic]] trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently [[srd/pf2e/compendium/rules-elements/conditions#Helpful|helpful]]."
  - name: "Items"
    desc: "Spear"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spear +10 __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ jaws +10 __Damage__ 1d4+4 piercing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+4 slashing"
  - name: "Ranged"
    desc: "⬻ spear +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Shared Feast"
    desc: "⬺ The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
  - name: "Wriggling Rush"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The scout takes a Stride action and a [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]] action, in either order. They ignore difficult terrain from mud, quicksand, and similar terrain during this movement."
sourcebook: "_Monster Core_, page 300."
```

```encounter-table
name: Sedacthy Scout
creatures:
  - 1: Sedacthy Scout
```
