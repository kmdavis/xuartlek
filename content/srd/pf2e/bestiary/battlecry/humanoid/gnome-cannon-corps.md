---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnome Cannon Corps"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Gnome Cannon Corps"
level: 7
source: "Battlecry!"
aon_id: "creature-3919"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3919"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Gnome Cannon Corps"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision"
languages: "Common, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Arcana +17, Crafting +15"
abilityMods: [0, 4, 2, 6, 2, 1]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +15; __Will__: +18"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Arcane Explosion"
    desc: "⬽ (Arcane, Force) Aiming the gnome cannons toward the enemy, loading them, and firing them requires the troop's full attention. The cannons fire a 15- foot burst of bright magic within 200 feet that deals 2d12+2 force damage (DC 22 basic Reflex save). A creature that fails their save is also dazzled for 1 round; this is a light and visual effect. The area of the explosion seems to twist and ripple for 1 minute afterward. A creature that attempts to move through the space must succeed at a DC 22 Will save or treat the area as difficult terrain; this is an illusion and visual effect."
  - name: "Cannon Vent"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The gnome engineers vent the cannons' energy in a blast that hits all creatures in a 5-foot emanation (DC 22 basic Reflex save). The damage depends on the number of actions. ⬻ 1d6+2 fire damage ⬺ 2d6+8 fire damage ⬽ 3d6+10 fire damage"
  - name: "Direct Hit"
    desc: "⬺ The gnomes fire a more mundane round from one of their cannons at a single target within 60 feet, who takes 3d10+6 bludgeoning damage (DC 22 basic Reflex save). On a failed save, the creature is also pushed 5 feet away from the troop."
sourcebook: "_Battlecry!_, page 182."
```

```encounter-table
name: Gnome Cannon Corps
creatures:
  - 1: Gnome Cannon Corps
```
