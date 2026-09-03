---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nursery Crawler"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/small
statblock: inline
name: "Nursery Crawler"
level: 3
source: "Rage of Elements"
aon_id: "creature-2672"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2672"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Nursery Crawler"
level: "Creature 3"
size: "Small"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [4, 3, 3, -2, 1, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +4; __Will__: +12"
hp: 48
health:
  - name: "HP"
    desc: "48; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
speed: "20 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ root +9 __Damage__ 1d8+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ seed +8 (range increment 20 feet) __Damage__ 1d6+3 piercing plus germinate"
abilities_bot:
  - name: "Germinate"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/plant|Plant]]) A creature hit by the nursery crawler's seed Strike must, on its turn, spend an Interact action to remove the seed; any seeds still implanted at the end of the creature's turn begin to sprout, dealing 1d6 persistent bleed damage and rendering the seeded creature [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. Removing a seed after it's sprouted deals 1d4 piercing damage; removing it before it begins to sprout does no damage. Removed seeds that land in viable soil sprout immediately and grow into new saplings after 1 hour."
sourcebook: "_Rage of Elements_, page 206."
```

```encounter-table
name: Nursery Crawler
creatures:
  - 1: Nursery Crawler
```
