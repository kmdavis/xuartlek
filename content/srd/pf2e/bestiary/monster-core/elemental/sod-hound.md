---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sod Hound"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Sod Hound"
level: 3
source: "Monster Core"
aon_id: "creature-2977"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2977"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sod Hound"
level: "Creature 3"
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; crystal sense (imprecise) 60 feet, darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [4, -1, 3, -4, 2, -1]
abilities_top:
  - name: "Crystal Sense"
    desc: "A sod hound can sense crystals or gems within 60 feet as if using the scent ability."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +12; __Ref__: +6; __Will__: +7"
hp: 44
health:
  - name: "HP"
    desc: "44; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "30 feet, burrow 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d10+6 piercing plus Knockdown"
abilities_bot:
  - name: "Earth Glide"
    desc: "The sod hound can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through any earthen matter, including rock. When it does so, the sod hound moves at its full burrow Speed, leaving no tunnels or signs of its passing."
sourcebook: "_Monster Core_, page 142."
```

```encounter-table
name: Sod Hound
creatures:
  - 1: Sod Hound
```
