---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ugothol"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Ugothol"
level: 4
source: "Monster Core"
aon_id: "creature-2812"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2812"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ugothol"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Alghollthu, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +9"
abilityMods: [4, 3, 3, 0, 2, 3]
abilities_top:
  - name: "Assume Form"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The ugothol spends 10 minutes reshaping its appearance to take on the shape of any Small or Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]]. It gains a +4 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to pass as that creature."
  - name: "Items"
    desc: "Longsword, studded leather"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +9; __Will__: +12 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ bludgeoning 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longsword +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d8+6 slashing"
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+6 slashing plus Grab"
abilities_bot:
  - name: "Blood Nourishment"
    desc: "⬻ The ugothol uses its three-pronged tongue to drink the blood of an adjacent [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] or [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] creature. The creature gains [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]."
  - name: "Compression"
    desc: "When the ugothol successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeezes]], it moves through the tight space at full speed. Narrow confines are not difficult terrain for an ugothol."
  - name: "Revert Form"
    desc: "⭓"
  - name: "Requirements"
    desc: "The ugothol is in an assumed form"
  - name: "Effect"
    desc: "The ugothol resumes its true form. Until the start of its next turn, it gains a +2 status bonus to attack rolls, damage rolls, saving throws, and skill checks."
  - name: "Sneak Attack"
    desc: "The ugothol deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19 - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 12."
```

```encounter-table
name: Ugothol
creatures:
  - 1: Ugothol
```
