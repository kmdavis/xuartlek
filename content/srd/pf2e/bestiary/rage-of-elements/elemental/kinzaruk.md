---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kinzaruk"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/medium
statblock: inline
name: "Kinzaruk"
level: 3
source: "Rage of Elements"
aon_id: "creature-2646"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2646"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Kinzaruk"
level: "Creature 3"
size: "Medium"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [3, 4, 1, -4, 0, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +8; __Ref__: +11; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 5"
speed: "fly 10 feet (can't ascend more than 5 feet off the ground)"
attacks:
  - name: "Melee"
    desc: "⬻ razor's edge +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d10+3 slashing"
abilities_bot:
  - name: "Fold Form"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The kinzaruk swiftly unfolds and refolds its body into a new shape chosen from the options of _animal form_. This grants it the movement Speeds and Strikes of the chosen form, but none of the other benefits. Its attack bonus is unchanged, and its damage bonus is +3. The kinzaruk can return to its natural form by taking this action again, and automatically returns if it falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]."
sourcebook: "_Rage of Elements_, page 154."
```

```encounter-table
name: Kinzaruk
creatures:
  - 1: Kinzaruk
```
