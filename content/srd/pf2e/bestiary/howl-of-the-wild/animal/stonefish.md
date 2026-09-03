---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stonefish"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/tiny
statblock: inline
name: "Stonefish"
level: 0
source: "Howl of the Wild"
aon_id: "creature-3274"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3274"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Stonefish"
level: "Creature 0"
size: "Tiny"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [2, 3, 2, -5, 1, -1]
abilities_top:
  - name: "Camouflage"
    desc: "The stonefish can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] in its natural environment even if it doesn't have [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Cover|cover]]."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +6; __Will__: +3"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Defensive Spines"
    desc: "When a creature moves into a space with one or more stonefish, that creature takes 1d4 piercing damage and is exposed to stonefish venom."
speed: "swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ spines +6 __Damage__ 1d4+2 piercing plus stonefish venom"
abilities_bot:
  - name: "Stonefish Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "3 hours"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] (1 round)"
  - name: "Stage 2"
    desc: "clumsy 2 (10 minutes)"
  - name: "Stage 3"
    desc: "3d6 poison and clumsy 2 (1 hour)"
sourcebook: "_Howl of the Wild_, page 148."
```

```encounter-table
name: Stonefish
creatures:
  - 1: Stonefish
```
