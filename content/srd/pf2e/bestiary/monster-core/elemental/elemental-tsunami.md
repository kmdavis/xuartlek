---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elemental Tsunami"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Elemental Tsunami"
level: 11
source: "Monster Core"
aon_id: "creature-2992"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2992"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elemental Tsunami"
level: "Creature 11"
size: "Huge"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +23"
abilityMods: [6, 6, 6, 0, 3, 0]
abilities_top:
  - name: "Waterbound"
    desc: "When not touching water, the elemental tsunami is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] and can't use reactions."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +22; __Will__: +19"
hp: 195
health:
  - name: "HP"
    desc: "195; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Vortex"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) 50 feet. Water in the area that is in the same body of water as the elemental tsunami is difficult terrain for [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swimming]]creatures that don't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] trait."
speed: "35 feet, swim 100 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wave +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+12 bludgeoning plus Push or Pull 10 feet"
abilities_bot:
  - name: "Drench"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]]) The elemental puts out all fires in a 20-foot emanation. It extinguishes all non-magical fires automatically and attempts to counteract magical fires (+20 counteract modifier)."
  - name: "Surge"
    desc: "⬺ The elemental tsunami momentarily expands to fill the area of its vortex. Creatures within the aura take 5d12+6 bludgeoning damage with a DC 31 basic Fortitude save. A creature that fails this save is pushed 20 feet. The elemental tsunami then shrinks to its normal space and can't Surge again for 1d4 rounds."
sourcebook: "_Monster Core_, page 149."
```

```encounter-table
name: Elemental Tsunami
creatures:
  - 1: Elemental Tsunami
```
