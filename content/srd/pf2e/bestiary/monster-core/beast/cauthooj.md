---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cauthooj"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/medium
statblock: inline
name: "Cauthooj"
level: 12
source: "Monster Core"
aon_id: "creature-2870"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2870"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cauthooj"
level: "Creature 12"
size: "Medium"
trait_01: "Beast"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; thoughtsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25"
abilityMods: [6, 4, 7, -3, 2, 0]
abilities_top:
  - name: "Thoughtsense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The cauthooj senses all non-[[srd/pf2e/compendium/rules-elements/traits/player-core/mindless|mindless]] creatures at the listed range."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +20; __Will__: +18"
hp: 215
health:
  - name: "HP"
    desc: "215; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 15"
abilities_mid:
  - name: "Hop-Dodge"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]])"
  - name: "Trigger"
    desc: "The cauthooj is the target of a melee Strike and is adjacent to another enemy that is also within the reach of the melee Strike"
  - name: "Effect"
    desc: "The cauthooj nimbly hops aside, redirecting the triggering Strike against the adjacent enemy. The cauthooj Strides up to half its Speed, and this movement does not trigger reactions."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+12 piercing"
abilities_bot:
  - name: "Staccato Strike"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) With subtle alterations in the pitch and tone of its song, the cauthooj directs one creature confused by its Warbling Song to make a Strike. This works like other Strikes made by [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] creatures, except that the cauthooj chooses the target. If no target is in reach or range, or the creature is unable to Strike for any other reason, this ability has no effect."
  - name: "Warbling Song"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The cauthooj gives a strange, ululating cry that causes nearby creatures to lash out violently and without control. Each creature within a 120-foot emanation that can hear the cauthooj must attempt a DC 32 Will save to resist the effect."
  - name: "Critical Success"
    desc: "The target is unaffected and is temporarily immune for 1 minute."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round."
  - name: "Critical Failure"
    desc: "The target is confused for 1 round and immediately attacks itself (in the normal fashion for attacking oneself while confused). This Strike doesn't give the creature a flat check to recover from the confusion. Cauthooj Lairs Cauthoojs make their lairs in small caverns, alcoves, and similar out-of-theway places, but claim large stretches of territory and wander many miles from their lairs in search of food. They often hunt in plains, prairies, and other large, open expanses. Shiny Collections Like magpies, cauthoojs are attracted to shiny baubles, and they often pick up choice treasures from their victims, depositing these trinkets in large piles in their lairs. Not all that glitters is gold, however, and adventurers will find as many colorful bits of string, broken mirror shards, and pieces of costume jewelry as they find coins, magic weapons, and other valuable treasures."
sourcebook: "_Monster Core_, page 53."
```

```encounter-table
name: Cauthooj
creatures:
  - 1: Cauthooj
```
