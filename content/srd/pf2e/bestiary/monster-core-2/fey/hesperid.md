---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hesperid"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/light
  - pf2e/creature/trait/nymph
  - pf2e/creature/trait/medium
statblock: inline
name: "Hesperid"
level: 9
source: "Monster Core 2"
aon_id: "creature-4491"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4491"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hesperid"
level: "Creature 9"
size: "Medium"
trait_01: "Fey"
trait_02: "Light"
trait_03: "Nymph"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], Utopian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +19, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +19, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +19, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +21, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [0, 6, 4, 4, 4, 6]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +21; __Will__: +19"
hp: 175
health:
  - name: "HP"
    desc: "175; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 10"
abilities_mid:
  - name: "Sunset Dependent"
    desc: "A hesperid is mystically bonded to a single remote location with a good view of the sunset—usually an island, coastal cliff, or valley. If they aren't at that location and able to see the sky at sunset on any given day, they become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1, increasing the value by 1 for each missed sunset and reducing by 1 only when they see a sunset. A hesperid can perform a 24-hour ritual to bond to a new location."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sunset ribbon +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d10+6 slashing plus 1d6 fire and 1d6 vitality"
  - name: "Ranged"
    desc: "⬻ sunset ray +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet) __Damage__ 2d12+6 fire plus 1d6 vitality"
abilities_bot:
  - name: "Create Golden Apple"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) While the hesperid is within their bonded location, they can spin golden light around an object they're holding or touching of up to 20 cubic feet in volume and up to 80 Bulk. Doing so condenses the object into a magic apple made of golden light with light Bulk. The golden apple reverts back to its original shape after a full day away from the hesperid's bonded location or when the hesperid [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismisses]] the effect."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/revealing-light|Revealing Light]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-3/holy-light|Holy Light]]"
sourcebook: "_Monster Core 2_, page 236."
```

```encounter-table
name: Hesperid
creatures:
  - 1: Hesperid
```
