---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2791"
socialImage: og-image.png
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
    desc: "+7; darkvision, locate aeon"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Utopian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, Axis Lore +5, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +9"
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
    desc: "22; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 3"
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Electrical Burst"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|Electricity]]) The arbiter releases an electrical burst from its body that deals 3d6 electricity damage to all creatures in a 10-foot emanation, with a DC 17 basic Reflex save. The arbiter is then [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] for 24 hours."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Mending|Mending]] (×3), [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]]"
sourcebook: "_Monster Core_, page 8."
```

```encounter-table
name: Arbiter
creatures:
  - 1: Arbiter
```
