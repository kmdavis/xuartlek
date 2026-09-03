---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arbiter"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/tiny
statblock: inline
name: "Arbiter"
level: 1
source: "Monster Core"
aon_id: "creature-2791"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2791"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Arbiter"
level: "Creature 1"
size: "Tiny"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, locate aeon"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, Axis Lore +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [1, 4, 2, 0, 2, 1]
abilities_top:
  - name: "Locate Aeon"
    desc: "An arbiter can always sense the direction of the nearest non-arbiter aeon on the plane, but it can't sense the range to the aeon."
  - name: "Items"
    desc: "Shortsword"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +7 +1 status to all saves vs. magic"
hp: 22
health:
  - name: "HP"
    desc: "22; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 3"
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Electrical Burst"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]]) The arbiter releases an electrical burst from its body that deals 3d6 electricity damage to all creatures in a 10-foot emanation, with a DC 17 basic Reflex save. The arbiter is then [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] for 24 hours."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/command|Command]], [[srd/pf2e/compendium/spells/rank-1/mending|Mending]] (×3), [[srd/pf2e/compendium/spells/rank-1/sanctuary|Sanctuary]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]]"
sourcebook: "_Monster Core_, page 8."
```

```encounter-table
name: Arbiter
creatures:
  - 1: Arbiter
```
