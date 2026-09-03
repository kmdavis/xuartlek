---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rakkatak"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Rakkatak"
level: 5
source: "Rage of Elements"
aon_id: "creature-2690"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2690"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Rakkatak"
level: "Creature 5"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [4, 2, 5, -3, 2, -2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +11; __Will__: +9"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5"
abilities_mid:
  - name: "Exploding Guts"
    desc: "When the rakkatak is critically hit or critically fails a Fortitude save, one of its organs bursts. Roll 1d4 to determine what effect this has. __1.__ Trapped noxious gas rushes out. The rakkatak is pushed 10 feet away from the source of the triggering attack or effect. __2.__ Pus showers those nearby. Each creature in a 5-foot emanation is sickened 1. __3.__ The damage is severe. The rakkatak takes 1d6 persistent bleed damage. __4.__ Gelatinous rakkatak eggs explode forth and instantly hatch. Each creature in a 5-foot emanation takes 1d6 persistent piercing damage from the ravenous larvae."
speed: "5 feet, fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mouth +15 __Damage__ 2d8+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ leg +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d10+7 slashing"
abilities_bot:
  - name: "Predator's Stare"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The rakkatak turns its grotesque yet mesmerizing eyes upon one creature it can see within 30 feet. That creature must succeed at a DC 22 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the rakkatak. While fascinated, the creature must spend at least 1 action each round moving closer to the rakkatak as expediently as possible, and can't intentionally move away from it. The fascination ends after 1 minute or when the rakkatak uses Predator's Stare again, whichever comes first."
  - name: "Suck Innards"
    desc: "⬻"
  - name: "Requirements"
    desc: "A [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], or willing creature is within the rakkatak's reach"
  - name: "Effect"
    desc: "The rakkatak deals 3d6 damage to the target (DC 22 basic Fortitude save). If the creature takes at least 12 damage, the rakkatak regains 10 HP. Ashen Hunting Grounds Avoiding the blazing chaos and ifrit rule that typify much of the [[srd/pf2e/compendium/gm/planes#Plane of Fire|Plane of Fire]], rakkataks prefer ashen wastelands as their hunting grounds. They dig simple burrows just barely below the surface, called rakkatak hills. Within, they can doze and digest in peace or lay and tend their horrifying eggs."
sourcebook: "_Rage of Elements_, page 132."
```

```encounter-table
name: Rakkatak
creatures:
  - 1: Rakkatak
```
