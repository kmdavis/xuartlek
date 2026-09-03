---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fire Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/small
statblock: inline
name: "Fire Scamp"
level: 1
source: "Monster Core"
aon_id: "creature-2987"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2987"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Fire Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7"
abilityMods: [0, 4, 0, -2, 0, 2]
abilities_top:
  - name: "Smoke Vision"
    desc: "The fire scamp ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +3; __Ref__: +9; __Will__: +7"
hp: 16
health:
  - name: "HP"
    desc: "16 (fast healing 2 (while touching fire)); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 3"
speed: "20 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6 piercing and 1d4 fire"
abilities_bot:
  - name: "Flame Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) The fire scamp breathes flames in a 15- foot cone that deals 2d4 fire damage to each creature within the area (DC 17 basic Reflex save). Creatures that fail the save also take 1d4 persistent fire damage. The fire scamp can't use Flame Breath again for 1d4 rounds."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 15 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/light|Light]]"
sourcebook: "_Monster Core_, page 147."
```

```encounter-table
name: Fire Scamp
creatures:
  - 1: Fire Scamp
```
