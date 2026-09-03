---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Pyro"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Pyro"
level: 1
source: "Monster Core"
aon_id: "creature-3026"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3026"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goblin Pyro"
level: "Creature 1"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, Fire Lore +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [0, 4, 2, 0, -1, 3]
abilities_top:
  - name: "Items"
    desc: "Torch"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "⬲"
  - name: "Trigger"
    desc: "A goblin ally ends a move action adjacent to the goblin"
  - name: "Effect"
    desc: "The goblin Steps."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ torch +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) __Damage__ 1d4 bludgeoning plus 1 fire"
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 16, attack +6 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/tangle-vine|Tangle Vine]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/breathe-fire|Breathe Fire]], [[srd/pf2e/compendium/spells/rank-1/grease|Grease]] (3 slots)"
sourcebook: "_Monster Core_, page 175."
```

```encounter-table
name: Goblin Pyro
creatures:
  - 1: Goblin Pyro
```
