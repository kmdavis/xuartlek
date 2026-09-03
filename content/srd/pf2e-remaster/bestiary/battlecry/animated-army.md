---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Army"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Animated Army"
level: 8
source: "Battlecry!"
aon_id: "creature-3899"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3899"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Animated Army"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Troop"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +18"
abilityMods: [6, 0, 6, -5, 0, -5]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +14; __Will__: +13 construct armor"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Weaknesses__ area damage 8, splash damage 8; __Hardness__ 10"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, the animated statues of the animated army have Hardness. This Hardness reduces any damage the animated army takes by an amount equal to the Hardness. Once an animated army is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 23."
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Battering Fists"
    desc: "(Magical)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The animated army makes a melee attack against each enemy in a 5-foot emanation (DC 23 basic Reflex save). The damage dealt depends on the number of actions. ⬻ 1d8+2 bludgeoning damage ⬺ 2d8+8 bludgeoning damage ⬽ 3d8+10 bludgeoning damage"
sourcebook: "_Battlecry!_, page 173."
```

```encounter-table
name: Animated Army
creatures:
  - 1: Animated Army
```
