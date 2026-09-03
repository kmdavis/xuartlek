---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sprite"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/sprite
  - pf2e/creature/trait/tiny
statblock: inline
name: "Sprite"
level: -1
source: "Monster Core"
aon_id: "creature-3210"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3210"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sprite"
level: "Creature -1"
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [-3, 4, 0, -2, 0, 2]
abilities_top:
  - name: "Luminous Fire"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) A sprite naturally sheds light like a [[srd/pf2e/compendium/equipment/adventuring-gear/torch|torch]]. The sprite can extinguish, rekindle, or change the color of this light by using an action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait. While this light is extinguished, the sprite's Strikes don't deal fire damage, and they can't use their luminous spark Strike."
  - name: "Items"
    desc: "Rapier"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +8; __Will__: +4"
hp: 7
health:
  - name: "HP"
    desc: "7; __Weaknesses__ cold iron 3"
speed: "10 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d6–3 piercing plus 1 fire"
  - name: "Ranged"
    desc: "⬻ luminous spark +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]], range 20 feet) __Damage__ 1d4 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/dizzying-colors|Dizzying Colors]]"
sourcebook: "_Monster Core_, page 322."
```

```encounter-table
name: Sprite
creatures:
  - 1: Sprite
```
