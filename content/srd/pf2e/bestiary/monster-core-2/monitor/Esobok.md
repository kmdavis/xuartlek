---
noteType: pf2eMonster
aliases: "Esobok"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Esobok"
level: 3
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4521"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Esobok"
level: "Creature 3"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; darkvision, lifesense 60 feet, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +4, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +10"
abilityMods: [3, 3, 4, -3, 3, 2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +8; __Will__: +8"
hp: 55
health:
  - name: "HP"
    desc: "55; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d10+3 piercing plus Grab and shepherd's touch"
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d6+3 slashing plus shepherd's touch"
abilities_bot:
  - name: "Pounce"
    desc: "⬻ The esobok Strides and then makes a Strike. If it began this action hidden, it remains hidden until after the Strike."
  - name: "Wrench Spirit"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]])"
  - name: "Requirement"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] by the esobok's jaws"
  - name: "Effect"
    desc: "The esobok releases the target from the Grab but wrenches its spirit free as it does so. The creature must attempt a DC 20 Will save. Creatures without souls (such as most [[srd/pf2e/compendium/rules-elements/traits/player-core/Construct|constructs]]) and creatures whose bodies and souls are one (such as most celestials, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiends]], and [[srd/pf2e/compendium/rules-elements/traits/player-core/Monitor|monitors]]) who roll a failure or critical failure on the save get a success instead."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]]."
  - name: "Failure"
    desc: "The esobok wrenches the target's soul from its body into its jaws. [[srd/pf2e/compendium/rules-elements/traits/player-core/Mindless|Mindless]] [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] creatures of level 2 or lower are destroyed, other undead creatures are stunned for 1 round, and all other creatures are [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]]. At the end of each of its turns, a creature paralyzed by this effect can attempt a new save to end the effect. The paralysis ends automatically if the esobok attempts a jaws Strike or speaks"
  - name: "Critical Failure"
    desc: "As failure, but as long as a creature is stunned or paralyzed, it's also [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 2]]."
  - name: "Shepherd's Touch"
    desc: "An esobok’s Strikes affect [[srd/pf2e/compendium/rules-elements/traits/gm-core/Incorporeal|incorporeal]] creatures with the effects of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]]."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×3; self only)"
sourcebook: "_Monster Core 2_, page 262."
```

```encounter-table
name: Esobok
creatures:
  - 1: Esobok
```
