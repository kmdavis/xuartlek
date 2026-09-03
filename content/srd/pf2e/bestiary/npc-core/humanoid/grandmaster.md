---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grandmaster"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Grandmaster"
level: 17
source: "NPC Core"
aon_id: "creature-3503"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3503"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Grandmaster"
level: "Creature 17"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; lifesense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/lore|Martial Arts Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25"
abilityMods: [6, 4, 3, 1, 5, 1]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/runes/returning|returning]] [[srd/pf2e/compendium/equipment/weapons/dart/shuriken|shuriken]]_, _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/worn-items/handwraps-of-mighty-blows-3-major-striking|handwraps of mighty blows]]_, _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/weapons/sword/temple-sword|temple sword]]_, _[[srd/pf2e/compendium/equipment/worn-items/bands-of-force-major|bands of force]]_"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +28; __Ref__: +32; __Will__: +27"
hp: 310
health:
  - name: "HP"
    desc: "310"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _temple sword_ +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 3d8+14 slashing"
  - name: "Melee"
    desc: "⬻ _fist_ +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 3d6+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _shuriken_ +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 3d4+14 piercing"
abilities_bot:
  - name: "Disrupt Qi"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/void|Void]]) The grandmaster attempts an [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]] Strike against a living creature. On a hit, the creature takes 3d6 persistent void damage and is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 2]] until the persistent damage ends."
  - name: "Flurry of Blows"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The grandmaster makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. The grandmaster can substitute any number of the attacks with temple sword Strikes or attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Reposition]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]]."
  - name: "Forbidden Palm"
    desc: "⬽"
  - name: "Requirements"
    desc: "The grandmaster has at least 1 Focus Point"
  - name: "Effect"
    desc: "The grandmaster casts [[srd/pf2e/compendium/spells/focus/touch-of-death|_touch of death_]] (spending 1 Focus Point as normal). Any time the target attempts a Fortitude save against this touch of death, the grandmaster takes 40 damage and is permanently [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]]. If the target gets a critical success, it's [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]; if it gets a success or failure the stunned condition it gains is increased by 1, and any damage it takes is increased by 40."
  - name: "One-Millimeter Punch"
    desc: "The grandmaster makes a single, carefully controlled unarmed Strike that deals 2 additional dice of damage, or 4 additional dice if the grandmaster spent 3 actions. If this damages the target, the grandmaster can choose to make the target attempt a DC 38 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is pushed back 5 feet."
  - name: "Failure"
    desc: "The target is pushed back 10 feet."
  - name: "Critical Failure"
    desc: "The target is pushed back 10 feet for each action the grandmaster spent on One-Millimeter Punch."
  - name: "Powerful Fists"
    desc: "The grandmaster's fist Strikes don't take penalties when making lethal attacks, and the grandmaster's fist Strikes are treated as adamantine, cold iron, and silver."
spellcasting:
  - name: "Monk Focus Spells"
    desc: "DC 38, attack +34, 3 Focus Points - __8th__ [[srd/pf2e/compendium/spells/focus/harmonize-self|Harmonize Self]], [[srd/pf2e/compendium/spells/focus/qi-blast|Qi Blast]], [[srd/pf2e/compendium/spells/focus/touch-of-death|Touch of Death]], [[srd/pf2e/compendium/spells/focus/wind-jump|Wind Jump]]"
sourcebook: "_NPC Core_, page 74."
```

```encounter-table
name: Grandmaster
creatures:
  - 1: Grandmaster
```
