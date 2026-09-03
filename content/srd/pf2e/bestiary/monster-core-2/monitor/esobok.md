---
obsidianUIMode: preview
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
aon_id: "creature-4521"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4521"
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
    desc: "Perception +12; darkvision, lifesense 60 feet, scent (imprecise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +8, Intimidation +9, Religion +4, Stealth +8, Survival +10"
abilityMods: [3, 3, 4, -3, 3, 2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +8; __Will__: +8"
hp: 55
health:
  - name: "HP"
    desc: "55; __Immunities__ death effects, disease; __Resistances__ poison 5, void 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 (Magical) __Damage__ 1d10+3 piercing plus Grab and shepherd's touch"
  - name: "Melee"
    desc: "⬻ claw +12 (Agile, Magical) __Damage__ 1d6+3 slashing plus shepherd's touch"
abilities_bot:
  - name: "Pounce"
    desc: "⬻ The esobok Strides and then makes a Strike. If it began this action hidden, it remains hidden until after the Strike."
  - name: "Wrench Spirit"
    desc: "⬻ (Attack, Divine, Incapacitation)"
  - name: "Requirement"
    desc: "A creature is grabbed or restrained by the esobok's jaws"
  - name: "Effect"
    desc: "The esobok releases the target from the Grab but wrenches its spirit free as it does so. The creature must attempt a DC 20 Will save. Creatures without souls (such as most constructs) and creatures whose bodies and souls are one (such as most celestials, fiends, and monitors) who roll a failure or critical failure on the save get a success instead."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The target is stunned 1."
  - name: "Failure"
    desc: "The esobok wrenches the target's soul from its body into its jaws. Mindless undead creatures of level 2 or lower are destroyed, other undead creatures are stunned for 1 round, and all other creatures are paralyzed. At the end of each of its turns, a creature paralyzed by this effect can attempt a new save to end the effect. The paralysis ends automatically if the esobok attempts a jaws Strike or speaks"
  - name: "Critical Failure"
    desc: "As failure, but as long as a creature is stunned or paralyzed, it's also stupefied 2."
  - name: "Shepherd's Touch"
    desc: "An esobok’s Strikes affect incorporeal creatures with the effects of a _ghost touch_ property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to undead."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __2nd__ Invisibility (×3; self only)"
sourcebook: "_Monster Core 2_, page 262."
```

```encounter-table
name: Esobok
creatures:
  - 1: Esobok
```
