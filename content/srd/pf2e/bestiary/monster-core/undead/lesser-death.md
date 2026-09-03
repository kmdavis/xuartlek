---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lesser Death"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Lesser Death"
level: 16
source: "Monster Core"
aon_id: "creature-3037"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3037"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lesser Death"
level: "Creature 16"
size: "Medium"
trait_01: "Rare"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; darkvision, [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|_see the unseen_]], status sight, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +30, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +30, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +35"
abilityMods: [6, 9, 6, 4, 6, 6]
abilities_top:
  - name: "Status Sight"
    desc: "a lesser death automatically knows the Hit Points, conditions, afflictions, and emotions of all creatures it can see."
  - name: "Items"
    desc: "Scythe"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +30; __Ref__: +33; __Will__: +32 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 255
health:
  - name: "HP"
    desc: "255 (death's grace, void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Aura of Misfortune"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]]) 20 feet. Living creatures in the aura must roll twice on all d20 rolls and use the lower result."
  - name: "Death's Grace"
    desc: "A lesser death can choose whether or not it counts as [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]] for effects that affect undead differently. Even if it does not count as undead, the lesser death still never counts as a living creature."
  - name: "Void Healing"
    desc: "A lesser death can choose whether or not it takes vitality damage."
  - name: "Lurking Death"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "A creature within 60 feet makes a ranged attack or uses an action that has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] trait"
  - name: "Effect"
    desc: "The lesser death teleports to a square adjacent to the triggering creature and makes a melee Strike against it. If the Strike hits, the lesser death disrupts the triggering action."
speed: "50 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ keen scythe +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 3d10+14 slashing plus 1d12 void"
abilities_bot:
  - name: "Infuse Weapon"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) Any scythe gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|agile]] trait, can't be disarmed, and becomes a _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/runes/keen|keen]] scythe_ while the lesser death wields it."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core_, page 185."
```

```encounter-table
name: Lesser Death
creatures:
  - 1: Lesser Death
```
