---
noteType: pf2eMonster
aliases: "Jinx Eater"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tengu
  - pf2e/creature/trait/medium
statblock: inline
name: "Jinx Eater"
level: 4
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3671"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Jinx Eater"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Tengu; plus two others"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +10, [[srd/pf2e/compendium/rules-elements/skills/Lore|Sailing Lore]] +12"
abilityMods: [2, 4, 1, 1, 1, 2]
abilities_top:
  - name: "Items"
    desc: "bottle, Leather Armor, [[srd/pf2e/compendium/equipment/weapons/sword/Tengu Gale Blade|Tengu Gale Blade]]"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +14; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65"
abilities_mid:
  - name: "Eat Fortune"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]] effect"
  - name: "Effect"
    desc: "The tengu negates the attempt to manipulate fate and fortune. Eat Fortune gains the opposing trait, and the triggering effect is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Actions#Disrupting Actions|disrupted]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tengu gale blade +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d6+4 slashing"
  - name: "Melee"
    desc: "⬻ beak +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Jinxed Call"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The jinx eater gives an eerie croak. Each non-[[srd/pf2e/compendium/rules-elements/traits/player-core-2/Tengu|tengu]] in a 30-foot emanation must succeed at a DC 21 Will save or be [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 1]] for 1 round (or 1 minute on a critical failure). Regardless of the results, each creature is then temporarily immune to Jinxed Call for 1 minute."
  - name: "Sneak Attack"
    desc: "The jinx eater deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 212."
```

```encounter-table
name: Jinx Eater
creatures:
  - 1: Jinx Eater
```
