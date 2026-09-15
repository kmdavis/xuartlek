---
noteType: pf2eMonster
aliases: "Halfling Troublemaker"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Troublemaker"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3045"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Halfling Troublemaker"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Halfling|Halfling]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +7"
abilityMods: [1, 4, 1, 0, 3, 3]
abilities_top:
  - name: "Items"
    desc: "Filcher's Fork, Leather Armor"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ filcher's fork +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ filcher's fork +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d6]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Graffiti Egg"
    desc: "⬻ the halfling troublemaker throws an egg filled with paint, glitter, and confetti at a creature within 30 feet. The target must succeed a DC 17 Reflex saving throw or become [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] for 1 round (or 1 minute on a critical failure)."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action to find [[srd/pf2e/compendium/rules-elements/Conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/Conditions#Undetected|undetected]] creatures within 30 feet of it. Whenever the halfling targets a creature that is [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Sneak Attack"
    desc: "The troublemaker deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 192."
```

```encounter-table
name: Halfling Troublemaker
creatures:
  - 1: Halfling Troublemaker
```
