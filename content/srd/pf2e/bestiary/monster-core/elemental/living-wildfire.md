---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Wildfire"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Living Wildfire"
level: 5
source: "Monster Core"
aon_id: "creature-2982"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2982"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Living Wildfire"
level: "Creature 5"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13"
abilityMods: [3, 4, 2, -2, 3, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The living wildfire ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +15; __Will__: +10"
hp: 80
health:
  - name: "HP"
    desc: "80 (explosion); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] 5"
abilities_mid:
  - name: "Explosion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) When the living wildfire dies, it explodes, dealing 3d6 fire damage to each creature in a 10-foot emanation (DC 19 basic Reflex save)."
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+6 fire plus 2d4 persistent fire"
  - name: "Ranged"
    desc: "⬻ fire mote +15 (range increment 60 feet) __Damage__ 2d6+3 fire"
abilities_bot:
  - name: "Spreading Flames"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Requirements"
    desc: "The living wildfire's last action was a Strike that dealt fire damage"
  - name: "Effect"
    desc: "The fire flares, dealing 3d6 fire damage to each creature adjacent to that target with a DC 19 basic Reflex save."
sourcebook: "_Monster Core_, page 144."
```

```encounter-table
name: Living Wildfire
creatures:
  - 1: Living Wildfire
```
