---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Monk Cadre"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Monk Cadre"
level: 14
source: "Battlecry!"
aon_id: "creature-3928"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3928"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Monk Cadre"
level: "Creature 14"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +28, Athletics +28, Stealth +25"
abilityMods: [8, 5, 2, 2, 4, 1]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +28; __Ref__: +26; __Will__: +25"
hp: 270
health:
  - name: "HP"
    desc: "270 (4 segments); __Weaknesses__ area damage 15, splash damage 15"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "35 feet, climb 20 feet; troop movement"
abilities_bot:
  - name: "Coordinated Maneuvers"
    desc: "⬺ The monk cadre is practiced at putting their foes off-balance. The monks choose Disarm, Grapple, Reposition, or Trip and attempt an Athletics check to perform that action, comparing the result to the appropriate DC (Fortitude for Grapple and Reposition, Reflex for Disarm and Trip) of each enemy within a 5-foot emanation. This can result in a different degree of success for each target."
  - name: "Pummeling Punches"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The monks perform well-timed coordinated melee attacks against all enemies in a 5-foot emanation, with a DC 31 basic Reflex save. The damage depends on the number of actions. ⬻ 2d8 bludgeoning damage ⬺ 4d8+8 bludgeoning damage ⬽ 4d8+16 bludgeoning damage"
  - name: "Qi Blast"
    desc: "(Force, Occult) The monks channel their qi into an explosion of energy that affects all creatures in a 10- foot burst within 60 feet. This explosion deals 6d6 force Qi Blast damage with a DC 31 basic Reflex save. When the monk cadre is reduced to 2 segments, this area decreases to a 5-foot burst."
sourcebook: "_Battlecry!_, page 186."
```

```encounter-table
name: Monk Cadre
creatures:
  - 1: Monk Cadre
```
