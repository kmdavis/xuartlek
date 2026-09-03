---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nightgaunt"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/dream
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Nightgaunt"
level: 4
source: "Monster Core 2"
aon_id: "creature-4488"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4488"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nightgaunt"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
trait_02: "Dream"
trait_03: "Uncommon"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; all-around vision (page 360), darkvision, thoughtsense (precise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [5, 3, 2, -2, 2, 0]
abilities_top:
  - name: "Thoughtsense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) A nightgaunt senses all nonmindless creatures at the listed range."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +13; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5"
abilities_mid:
  - name: "Faceless"
    desc: "The nightgaunt has no face, but they can still see in all directions as if their entire body were an eye. They have no need to breathe, and they're immune to all inhaled toxins and other [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]] effects."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+7 plus Grab"
  - name: "Melee"
    desc: "⬻ tail +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ tickle"
abilities_bot:
  - name: "Clutches"
    desc: "A nightgaunt can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at full Speed while it has a Medium or smaller creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its claws, carrying that creature along with it."
  - name: "Tickle"
    desc: "The nightgaunt can use its tail to tickle a foe with horrible efficiency. A creature hit by its tail Strike must attempt a DC 21 Fortitude save; if the creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the nightgaunt, it uses the outcome one degree of success worse than the result it rolled."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature is overcome with laughter and can't perform reactions for 1 round."
  - name: "Failure"
    desc: "As success, and the creature is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
  - name: "Critical Failure"
    desc: "As success, and the creature is sickened 2 and can't speak for 1 round. Emotion Eaters Nightgaunts feed on emotions via touch, preferring unique cocktails formed of conflicting emotions, especially despair, horror, or nervous laughter. Such feeding has little lasting impact on their food source, but a nightgaunt can only feed on a given creature once. As a result, they tend to satiate themselves fully before seeking out different prey."
sourcebook: "_Monster Core 2_, page 234."
```

```encounter-table
name: Nightgaunt
creatures:
  - 1: Nightgaunt
```
