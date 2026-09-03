---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grim Reaper"
tags:
  - pf2e/creature/level/21
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/medium
statblock: inline
name: "Grim Reaper"
level: 21
source: "Monster Core"
aon_id: "creature-3036"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3036"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Grim Reaper"
level: "Creature 21"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Unique"
modifier: 41
perception:
  - name: "Perception"
    desc: "Perception +41; darkvision, see the unseen, status sight, _truesight_"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +43, Athletics +38, Deception +40, Intimidation +43, Religion +39, Society +36, Stealth +43"
abilityMods: [8, 10, 8, 5, 7, 8]
abilities_top:
  - name: "Status Sight"
    desc: "The Grim Reaper automatically knows the Hit Points, conditions, afflictions, and emotions of all creatures it can see."
  - name: "Items"
    desc: "Scythe"
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +37; __Ref__: +41; __Will__: +38 +1 status to all saves vs. magic"
hp: 320
health:
  - name: "HP"
    desc: "320 (death's grace, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ all damage 15"
abilities_mid:
  - name: "Aura of Misfortune"
    desc: "(aura, divine, misfortune) 20 feet. Living creatures in the aura must roll twice on all d20 rolls and use the lower result."
  - name: "Death's Grace"
    desc: "The Grim Reaper can choose whether or not it counts as undead for effects that affect undead differently. Even if it does not count as undead, the Grim Reaper still never counts as a living creature."
  - name: "Void Healing"
    desc: "The Grim Reaper can choose whether or not it takes vitality damage."
  - name: "Lurking Death"
    desc: "⬲ (divine, teleportation)"
  - name: "Trigger"
    desc: "A creature within 100 feet makes a ranged attack or uses an action that has the concentrate, manipulate, or move trait"
  - name: "Effect"
    desc: "The Grim Reaper teleports to a square adjacent to the triggering creature and makes a melee Strike against it. If the Strike hits, the Grim Reaper disrupts the triggering action."
speed: "50 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ keen scythe +40 (Agile, deadly 3d10, Magical, reach 10 feet, Trip) __Damage__ 4d10+23 slashing plus death strike and energy drain"
abilities_bot:
  - name: "Death Strike"
    desc: "(Death) A creature critically hit by any of the Grim Reaper's attacks or that critically fails against any of its spells must succeed at a DC 47 Fortitude save or die."
  - name: "Energy Drain"
    desc: "When the Grim Reaper hits and deals damage with its scythe, it regains 20 Hit Points, and the target must succeed at a DC 43 Fortitude save or become doomed 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of doomed 3)."
  - name: "Final Death"
    desc: "A creature killed by the Grim Reaper can't be brought back to life by any means short of divine intervention."
  - name: "Infuse Weapon"
    desc: "(Divine) Any scythe gains the agile trait, can't be disarmed, and becomes a _+3 major striking keen scythe_ while the Grim Reaper wields it. If the Grim Reaper Strikes a creature with a weakness to any specific type of damage, the scythe's damage counts as that type of damage, in addition to slashing."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47, attack +37 - __7th__ Interplanar Teleport - __10th__ Execute (×4) - __Constant (2nd)__ See the Unseen - __Constant (3rd)__ Haste - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core_, page 184."
```

```encounter-table
name: Grim Reaper
creatures:
  - 1: Grim Reaper
```
