---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Lucky Draw"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Halfling Lucky Draw"
level: 8
source: "Battlecry!"
aon_id: "creature-3921"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3921"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Halfling Lucky Draw"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Deception +18, Diplomacy +16, Occultism +16, Performance +18, Stealth +16"
abilityMods: [0, 4, 1, 3, 1, 6]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +13; __Ref__: +16; __Will__: +19"
hp: 135
health:
  - name: "HP"
    desc: "135 (4 segments); __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Bad Deal"
    desc: "⬺ (Auditory, Linguistic, Emotion, Mental, Misfortune, Occult) The halflings mock and taunt their enemies with quick Harrow readings that predict doom. The troop chooses a number of creatures equal to the number of its remaining segments within 60 feet. Each target must attempt a DC 23 Will save. On a failure, the target must roll their next attack roll, saving throw, or skill check twice and use the worse result."
  - name: "False Cuts"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The halflings feint with their cards and then lash out with their daggers in a coordinated melee attack against enemies in a 5-foot emanation, with a DC 23 basic Reflex save. The damage depends on the number of actions. ⬻ 1d4 piercing or slashing damage and 1d4 precision damage ⬺ 2d4+7 piercing or slashing damage and 2d4 precision damage ⬽ 3d4+10 piercing or slashing damage and 2d4 precision damage"
  - name: "Troop Harrowing"
    desc: "(Mental, Occult) When the halfling lucky draw Casts a Spell that targets a single creature, some of the constituent members can perform a focused Harrow reading on the target as part of Casting the Spell. The lucky draw attempts an Occultism skill check against the target's Will DC. On a success, the target takes a –1 status penalty to their saving throw or AC against the spell (–2 on a critical success). If the lucky draw critically fails this check, their reading portends bad news for the halflings and they become frightened 2."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 23, attack +20 - __Cantrips (4th)__ Daze, Figment, Telekinetic Projectile - __3rd__ Force Barrage, Paralyze, Slow (3 slots) - __4th__ Confusion, Force Barrage (2 slots)"
sourcebook: "_Battlecry!_, page 182."
```

```encounter-table
name: Halfling Lucky Draw
creatures:
  - 1: Halfling Lucky Draw
```
