---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Iron Warden"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Iron Warden"
level: 13
source: "Monster Core"
aon_id: "creature-3068"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3068"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Iron Warden"
level: "Creature 13"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30"
abilityMods: [8, -1, 4, -5, 0, -5]
abilities_top:
  - name: "Shield Arm"
    desc: "The iron warden has a shield built into its arm, that it can use as a steel shield (+2 to AC and Hardness 5). Because it's a part of the iron warden, all damage in excess of its Hardness is dealt only to the iron warden."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +19; __Will__: +22"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 15 (except [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]]), spells 15 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] and spells that cause rust)"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲ (see shield arm)"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+12 bludgeoning"
abilities_bot:
  - name: "Breathe Poison"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The iron warden exhales poisonous gas in a 10-foot burst centered on the corner of one of the iron warden's squares. The gas persists until the start of the warden's next turn. Any creature in the area (or that later enters the area) is exposed to the iron warden's poison. The warden can't Breathe Poison again for 1d4 rounds."
  - name: "Inexorable March"
    desc: "⬻ The iron warden Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can attempt to bar the way by succeeding at a DC 37 Fortitude save. On a critical success, the resisting creature takes no damage; otherwise, it's damaged as if hit by the iron warden's fist."
  - name: "Iron Warden Poison"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) Any [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] value from this poison is reduced by 1 every hour"
  - name: "Saving Throw"
    desc: "DC 33 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "2d6 poison and drained 1 (1 round)"
  - name: "Stage 2"
    desc: "4d6 poison and drained 2 (1 round)"
  - name: "Stage 3"
    desc: "8d6 poison and drained 3 (1 round) Iron Scrap An iron warden can be melted down for scrap or traded to [[srd/pf2e/bestiary/monster-core/giant/fire-giant|fire giants]] to be repurposed into armor for a Large creature."
sourcebook: "_Monster Core_, page 207."
```

```encounter-table
name: Iron Warden
creatures:
  - 1: Iron Warden
```
