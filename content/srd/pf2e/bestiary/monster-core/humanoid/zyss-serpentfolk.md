---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zyss Serpentfolk"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Zyss Serpentfolk"
level: 2
source: "Monster Core"
aon_id: "creature-3181"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3181"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zyss Serpentfolk"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
trait_03: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; telepathy 00 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +8, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +8"
abilityMods: [-1, 4, -2, 4, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, Shortbow (30 arrows)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +4; __Ref__: +8; __Will__: +8 (+4 status vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 25
health:
  - name: "HP"
    desc: "25; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 piercing plus serpentfolk venom"
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing plus serpentfolk venom"
  - name: "Ranged"
    desc: "⬻ shortbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6+2 piercing plus serpentfolk venom"
abilities_bot:
  - name: "Serpentfolk Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 18 - __1st__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (at will), [[srd/pf2e/compendium/spells/rank-1/ventriloquism|Ventriloquism]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]] (self only; at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]]"
sourcebook: "_Monster Core_, page 302."
```

```encounter-table
name: Zyss Serpentfolk
creatures:
  - 1: Zyss Serpentfolk
```
