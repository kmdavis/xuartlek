---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boggard Warrior"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/boggard
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Boggard Warrior"
level: 2
source: "Monster Core"
aon_id: "creature-2857"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2857"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Boggard Warrior"
level: "Creature 2"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Boggard"
trait_03: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Boggard"
skills:
  - name: "Skills"
    desc: "Athletics +8, Intimidation +5, Stealth +6"
abilityMods: [4, 0, 4, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Club, Javelin (3), Studded Leather Armor"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +5; __Will__: +8"
hp: 38
health:
  - name: "HP"
    desc: "38"
speed: "20 feet, swim 25 feet; swamp passage"
attacks:
  - name: "Melee"
    desc: "⬻ club +10 __Damage__ 1d6+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ tongue +10 (reach 10 feet) __Damage__ tongue grab"
  - name: "Ranged"
    desc: "⬻ javelin +6 (thrown 30 feet) __Damage__ 1d6+4 piercing"
  - name: "Ranged"
    desc: "⬻ club +6 (thrown 10 feet) __Damage__ 1d6+6 bludgeoning"
abilities_bot:
  - name: "Swamp Passage"
    desc: "A boggard ignores difficult terrain caused by swamp terrain features."
  - name: "Terrifying Croak"
    desc: "⬻ (Auditory, Emotion, Fear, Mental) The boggard unleashes a terrifying croak. Any non-boggard within 30 feet becomes frightened 1 unless they succeed at a DC 18 Will save; those who critically succeed are temporarily immune for 1 minute."
  - name: "Tongue Grab"
    desc: "If the boggard hits a creature with their tongue, that creature becomes grabbed by the boggard. Unlike with a normal Grab, the creature isn't immobilized, but it can't move beyond the reach of the boggard's tongue. A creature can sever the tongue by hitting AC 15 and dealing at least 3 slashing damage. Though this doesn't deal any damage to the boggard, it prevents them from using their tongue Strike until they regrow their tongue, which takes a week."
sourcebook: "_Monster Core_, page 44."
```

```encounter-table
name: Boggard Warrior
creatures:
  - 1: Boggard Warrior
```
