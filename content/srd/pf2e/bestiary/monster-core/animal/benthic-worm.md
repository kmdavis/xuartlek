---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Benthic Worm"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Benthic Worm"
level: 15
source: "Monster Core"
aon_id: "creature-2872"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2872"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Benthic Worm"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Animal"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, tremorsense (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +20"
abilityMods: [10, -1, 8, -5, -1, -1]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +32; __Ref__: +20; __Will__: +23"
hp: 320
health:
  - name: "HP"
    desc: "320"
abilities_mid:
  - name: "Inexorable"
    desc: "The cave worm recovers from the [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]], and [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] conditions at the end of its turn. It's also immune to penalties to its Speeds and the [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] condition, and it ignores difficult terrain and greater difficult terrain."
  - name: "Slough Skin"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The cave worm would be affected by a condition or adverse effect (such as [[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|_cursed metamorphosis_]])"
  - name: "Effect"
    desc: "The cave worm negates the triggering condition or effect by sloughing an outer layer of its skin. Effects from [[srd/pf2e/compendium/rules-elements/traits/gm-core/artifact|artifacts]], deities, or a similarly powerful source can't be avoided in this way."
speed: "40 feet, burrow 40 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+16 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ stinger +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d6+16 piercing plus benthic worm venom"
  - name: "Melee"
    desc: "⬻ body +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+14 bludgeoning"
abilities_bot:
  - name: "Benthic Worm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 37 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 2]] (1 round)"
  - name: "Stage 2"
    desc: "4d6 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "6d6 poison damage and clumsy 2 (1 round)"
  - name: "Breach"
    desc: "⬺ The benthic worm Swims up to its swim Speed, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] vertically out of the water up to 30 feet, making a Strike against a creature at the apex of the jump (this lets it attack a creature within 45 feet of the water's surface). After the Strike, the worm splashes back down. It can use Improved Grab on this Strike and follow it up with Fast Swallow."
  - name: "Fast Swallow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The worm Grabs a creature"
  - name: "Effect"
    desc: "The worm uses Swallow Whole."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Huge, 3d8+10 bludgeoning, Rupture 27"
  - name: "Thrash"
    desc: "⬺ The worm attempts one Strike against each creature in its reach. It can Strike up to once with its jaws, up to once with its stinger, and any number of times with its body. Each attack counts toward the worm's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all the attacks."
sourcebook: "_Monster Core_, page 56."
```

```encounter-table
name: Benthic Worm
creatures:
  - 1: Benthic Worm
```
