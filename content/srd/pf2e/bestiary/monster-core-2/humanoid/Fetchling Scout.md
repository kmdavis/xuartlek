---
noteType: pf2eMonster
aliases: "Fetchling Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fetchling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/medium
statblock: inline
name: "Fetchling Scout"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4400"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fetchling Scout"
level: "Creature 1"
size: "Medium"
trait_01: "Fetchling"
trait_02: "Humanoid"
trait_03: "Shadow"
modifier: 5
perception:
  - name: "Perception"
    desc: "+5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +3, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +7"
abilityMods: [1, 4, 2, 0, 0, 2]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/Armor#Chain Shirt|Chain Shirt]], [[srd/pf2e/compendium/equipment/weapons/knife/Dagger|Dagger]]"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Shadow Blending"
    desc: "When the fetchling scout is [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] as a result of [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Perception and Detection#Dim Light|dim light]], the flat check to target them has a DC of 7, not 5."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Shadow Stride"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shadow|shadow]])"
  - name: "Requirements"
    desc: "The fetchling is in [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Perception and Detection#Dim Light|dim light]]"
  - name: "Effect"
    desc: "The fetchling Strides. They have a +10-foot status bonus to their Speed during this [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]]. The DC from shadow blending increases to 11 during this Stride, and the fetchling remains [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] by dim light until the end of the movement, even if they leave dim light during the Stride."
  - name: "Sneak Attack"
    desc: "The fetchling scout's Strikes deal an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 15 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]]"
sourcebook: "_Monster Core 2_, page 156."
```

```encounter-table
name: Fetchling Scout
creatures:
  - 1: Fetchling Scout
```
