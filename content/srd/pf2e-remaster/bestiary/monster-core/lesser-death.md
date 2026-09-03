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
    desc: "Perception +32; darkvision, _see the unseen_, status sight, _truesight_"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +28, Deception +30, Intimidation +32, Religion +30, Society +26, Stealth +35"
abilityMods: [6, 9, 6, 4, 6, 6]
abilities_top:
  - name: "Status Sight"
    desc: "a lesser death automatically knows the Hit Points, conditions, afflictions, and emotions of all creatures it can see."
  - name: "Items"
    desc: "Scythe"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +30; __Ref__: +33; __Will__: +32 +1 status to all saves vs. magic"
hp: 255
health:
  - name: "HP"
    desc: "255 (death's grace, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Aura of Misfortune"
    desc: "(aura, divine, misfortune) 20 feet. Living creatures in the aura must roll twice on all d20 rolls and use the lower result."
  - name: "Death's Grace"
    desc: "A lesser death can choose whether or not it counts as undead for effects that affect undead differently. Even if it does not count as undead, the lesser death still never counts as a living creature."
  - name: "Void Healing"
    desc: "A lesser death can choose whether or not it takes vitality damage."
  - name: "Lurking Death"
    desc: "⬲ (divine, teleportation)"
  - name: "Trigger"
    desc: "A creature within 60 feet makes a ranged attack or uses an action that has the concentrate, manipulate, or move trait"
  - name: "Effect"
    desc: "The lesser death teleports to a square adjacent to the triggering creature and makes a melee Strike against it. If the Strike hits, the lesser death disrupts the triggering action."
speed: "50 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ keen scythe +32 (Agile, deadly 2d10, Magical, reach 10 feet, Trip) __Damage__ 3d10+14 slashing plus 1d12 void"
abilities_bot:
  - name: "Infuse Weapon"
    desc: "(Divine) Any scythe gains the agile trait, can't be disarmed, and becomes a _+2 greater striking keen scythe_ while the lesser death wields it."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __2nd__ See the Unseen - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core_, page 185."
```

```encounter-table
name: Lesser Death
creatures:
  - 1: Lesser Death
```
