---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zephyr Hawk"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Zephyr Hawk"
level: 3
source: "Monster Core"
aon_id: "creature-2973"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2973"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zephyr Hawk"
level: "Creature 3"
size: "Small"
trait_01: "Air"
trait_02: "Elemental"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [2, 4, 1, -4, 0, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +13; __Will__: +7"
hp: 36
health:
  - name: "HP"
    desc: "36; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wing +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+4 slashing"
abilities_bot:
  - name: "Circling Attack"
    desc: "⬺ The zephyr hawk Flies up to half its Speed, makes two wing Strikes, then Flies up to half its Speed again to return to its original location. The second half of this movement doesn't trigger reactions. Both attacks count toward the zephyr hawk's multiple attack penalty, but the penalty doesn't increase until after it makes both attacks."
sourcebook: "_Monster Core_, page 140."
```

```encounter-table
name: Zephyr Hawk
creatures:
  - 1: Zephyr Hawk
```
