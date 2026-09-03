---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Octopus"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/huge
statblock: inline
name: "Giant Octopus"
level: 8
source: "Monster Core"
aon_id: "creature-3115"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3115"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Octopus"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [6, 3, 4, -4, 3, -2]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +17; __Will__: +15"
hp: 135
health:
  - name: "HP"
    desc: "135; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
speed: "15 feet, swim 40 feet; compression"
attacks:
  - name: "Melee"
    desc: "⬻ arm +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+9 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ beak +20 __Damage__ 2d8+9 piercing plus giant octopus venom"
abilities_bot:
  - name: "Compression"
    desc: "A giant octopus can move through a gap at least 2 feet wide without [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeezing]]and can Squeeze through a gap at least 1 foot wide."
  - name: "Constrict"
    desc: "⬻ 1d8+9 bludgeoning, DC 26"
  - name: "Giant Octopus Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], and off-guard (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage, clumsy 2, and off-guard (1 round)"
  - name: "Ink Cloud"
    desc: "⬻ The octopus emits a cloud of black ink in a 30-foot emanation. This cloud has no effect outside of water. Creatures inside the cloud are [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] and can't use their sense of smell. The cloud dissipates after 1 minute. The octopus can't use Ink Cloud again for 2d6 rounds."
  - name: "Jet"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The octopus moves up to 200 feet in a straight line through the water without triggering reactions."
  - name: "Writhing Arms"
    desc: "⬺ The giant octopus makes up to four Strikes with different arms, each against a different target. Each attack counts separately for the octopus's multiple attack penalty, but the penalty doesn't increase the until the octopus has made all the attacks. If the octopus subsequently uses the Grab action, it can Grab any number of creatures it hit with Writhing Arms."
sourcebook: "_Monster Core_, page 248."
```

```encounter-table
name: Giant Octopus
creatures:
  - 1: Giant Octopus
```
