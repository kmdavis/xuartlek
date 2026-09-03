---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tikbalang"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Tikbalang"
level: 9
source: "Monster Core 2"
aon_id: "creature-4580"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4580"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tikbalang"
level: "Creature 9"
size: "Medium"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [5, 4, 4, -1, 3, 6]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +17; __Will__: +14"
hp: 197
health:
  - name: "HP"
    desc: "197; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 10"
abilities_mid:
  - name: "Believe the Lie"
    desc: "The tikbalang takes a –2 circumstance penalty to saves against illusion spells and to their Will DC against checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]] to them."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ hoof +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+8 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The tikbalang takes on the appearance of any Medium or Large humanoid. This doesn't change the tikbalang's Speed or their attack and damage modifiers with their Strikes."
  - name: "Flailing Thrash"
    desc: "⬺ The tikbalang makes two fist Strikes, with each Strike dealing an extra 1d6 damage against creatures grabbing or [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the tikbalang. The multiple attack penalty doesn't increase until after both attacks."
  - name: "Unnatural Leap"
    desc: "⬻ The tikbalang jumps up to their Speed horizontally, or half that vertically. Golden Strand Why do adventurers go through the trouble of wrestling a tikbalang? Hidden among the luxurious ebony mane of the creature is a single strand of golden hair. Anyone who successfully Grabs the tikbalang can [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] (DC 29) the strand and Interact to pluck it from their head. Made of actual gold, this strand (worth 150 gp) holds magic particularly well and is highly sought after for creating magic items. A tikbalang regrows their plucked golden strand in a year."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29 - __4th__ [[srd/pf2e/compendium/spells/rank-3/hypnotize|Hypnotize]], [[srd/pf2e/compendium/spells/rank-4/mirage|Mirage]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]] (once per week)"
sourcebook: "_Monster Core 2_, page 319."
```

```encounter-table
name: Tikbalang
creatures:
  - 1: Tikbalang
```
