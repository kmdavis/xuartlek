---
noteType: pf2eMonster
aliases: "Vermlek"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Vermlek"
level: 3
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4317"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vermlek"
level: "Creature 3"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8"
abilityMods: [3, 1, 4, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sword/Longsword|Longsword]]"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +11; __Ref__: +8; __Will__: +6"
hp: 55
health:
  - name: "HP"
    desc: "55; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]] 5"
abilities_mid:
  - name: "Recoil from Wasted Opportunities"
    desc: "Vermleks can't stand the sight of a good meal presented and then swiftly taken away. Whenever a [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]] creature within sight of the vermlek has its dying condition removed, the vermlek takes 1d6 mental damage."
speed: "25 feet, burrow 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d8+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ longsword +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d8+4 slashing"
abilities_bot:
  - name: "Abandon Body"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The vermlek is Inhabiting a Body"
  - name: "Effect"
    desc: "The vermlek crawls out of the body they are inhabiting, devouring much of the body's remaining flesh and regaining 10 Hit Points in the process. The corpse they leave behind is little more than a husk."
  - name: "Inhabit Body"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The vermlek isn't already Inhabiting a Body"
  - name: "Effect"
    desc: "The vermlek crawls into the body of an adjacent Medium humanoid that has been dead for no more than 1 week, consuming the bulk of the victim's skeleton and internal organs as they do so and cramming themself into the cavity. As long as they Inhabit a Body, the vermlek loses their bite attack, can wield weapons like a humanoid, gains a +3 circumstance bonus to AC, and gains a +3 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks to Impersonate the creature they are inhabiting."
  - name: "Unsettling Movement"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) Whenever the vermlek Abandons a Body or Inhabits a Body, all creatures within 30 feet who can see the vermlek must succeed at a DC 19 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] 1. On a critical failure, the creature is frightened 1 and [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1. Regardless of the result, creatures are immune to the same vermlek's unsettling movement for 24 hours. Telltale Desecration Coroners and priests in demon-infested lands know immediately that they're dealing with a vermlek when they're brought a corpse that is little more than a sack of skin."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 19 - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]]"
sourcebook: "_Monster Core 2_, page 90."
```

```encounter-table
name: Vermlek
creatures:
  - 1: Vermlek
```
