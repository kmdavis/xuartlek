---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vanara Disciple"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/vanara
  - pf2e/creature/trait/medium
statblock: inline
name: "Vanara Disciple"
level: 1
source: "Monster Core 2"
aon_id: "creature-4604"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4604"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vanara Disciple"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Uncommon"
trait_03: "Vanara"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], Vanara"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [1, 4, 0, 1, 3, 0]
abilities_top:
  - name: "Prehensile Tail"
    desc: "The vanara can use their long, flexible tail to perform [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interact]] actions requiring a free hand, even if both hands are otherwise occupied. Their tail can't perform actions that require fingers or significant manual dexterity, including any action that would require a check to accomplish, and they can't use it to hold items."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/club/bo-staff|Bo Staff]], [[srd/pf2e/compendium/equipment/weapons/dart/javelin|javelins]] (3)"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +5; __Ref__: +9; __Will__: +8"
hp: 16
health:
  - name: "HP"
    desc: "16"
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 1d6+1 bludgeoning"
  - name: "Melee"
    desc: "⬻ bo staff +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]]) __Damage__ 1d8+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Flurry of Blows"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The vanara disciple makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses."
  - name: "Spring Up"
    desc: "⬺"
  - name: "Requirements"
    desc: "The vanara disciple is [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]"
  - name: "Effect"
    desc: "The vanara [[srd/pf2e/compendium/rules-elements/actions/player-core#Stand|Stands]], then can immediately [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Step]] twice. The Stand action doesn't trigger reactions."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 13 - __1st__ [[srd/pf2e/compendium/spells/rank-1/pest-form|Pest Form]] (monkey only)"
sourcebook: "_Monster Core 2_, page 342."
```

```encounter-table
name: Vanara Disciple
creatures:
  - 1: Vanara Disciple
```
