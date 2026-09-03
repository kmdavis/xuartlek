---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boggard Swampseer"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/boggard
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Boggard Swampseer"
level: 3
source: "Monster Core"
aon_id: "creature-2858"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2858"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Boggard Swampseer"
level: "Creature 3"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Boggard"
trait_03: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Boggard, Chthonian, Common"
skills:
  - name: "Skills"
    desc: "Athletics +8, Intimidation +8, Medicine +9, Nature +11, Performance +8, Religion +9"
abilityMods: [3, 0, 2, 0, 4, 3]
abilities_top:
  - name: "Items"
    desc: "Staff"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +7; __Will__: +11"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "20 feet, swim 25 feet; swamp passage"
attacks:
  - name: "Melee"
    desc: "⬻ staff +10 (two-hand d8) __Damage__ 1d4+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ tongue +10 (reach 10 feet) __Damage__ tongue grab"
abilities_bot:
  - name: "Destructive Croak"
    desc: "⬺ (sonic) The swampseer utters a powerful croak that deals 4d6 sonic damage to any non-boggard within a 15-foot emanation (DC 19 basic Fortitude save); any creature with the frightened condition takes additional sonic damage equal to twice the value of its frightened condition. The boggard can’t use Destructive Croak again for 1d4 rounds."
  - name: "Drowning Drone"
    desc: "⬲ (Auditory, Mental)"
  - name: "Trigger"
    desc: "The boggard swampseer or one of their allies within 60 feet attempts a saving throw against an auditory or sonic effect"
  - name: "Effect"
    desc: "The swampseer releases a croak that drowns out other sounds. They roll a Performance check. They and boggard allies in the area can use the higher result between the swampseer's Performance check and their saves to resolve the effects against the auditory or sonic effect."
  - name: "Swamp Passage"
    desc: "A boggard ignores difficult terrain caused by swamp terrain features."
  - name: "Terrifying Croak"
    desc: "⬻ (Auditory, Emotion, Fear, Mental) The boggard unleashes a terrifying croak. Any non-boggard within 30 feet becomes frightened 1 unless they succeed at a DC 19 Will save; those who critically succeed are temporarily immune for 1 minute."
  - name: "Tongue Grab"
    desc: "If the boggard hits a creature with their tongue, that creature becomes grabbed by the boggard. Unlike with a normal Grab, the creature isn't immobilized, but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 15 and dealing at least 4 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 21, attack +11 - __Cantrips (2nd)__ Caustic Blast, Frostbite, Light, Tangle Vine - __1st__ Fear, Jump, Runic Weapon - __2nd__ Acid Grip, Mist"
sourcebook: "_Monster Core_, page 45."
```

```encounter-table
name: Boggard Swampseer
creatures:
  - 1: Boggard Swampseer
```
