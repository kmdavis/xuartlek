---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Taldan Cave Squirrel"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Taldan Cave Squirrel"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3315"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3315"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Taldan Cave Squirrel"
level: "Creature 5"
size: "Medium"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 60 feet, tremorsense (imprecise)"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +12, Survival +13"
abilityMods: [4, 4, 5, -4, 1, 2]
abilities_top:
  - name: "Studded Cheeks"
    desc: "The cave squirrel can store up to six gems in its cheeks. It typically begins combat with all six, and it loses a gem each time it uses gem spit."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +15; __Will__: +9"
hp: 95
health:
  - name: "HP"
    desc: "95"
abilities_mid:
  - name: "Defensive Scream"
    desc: "⬲ (auditory)"
  - name: "Trigger"
    desc: "The cave squirrel rolls initiative or has taken damage before initiative"
  - name: "Effect"
    desc: "The cave squirrel lets out an earpiercing shriek, alerting any other cave squirrels in the area to its plight. It uses Screaming Force."
speed: "30 feet, burrow 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 (Agile) __Damage__ 2d6+4 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +13 (Agile) __Damage__ 2d8+4 slashing"
  - name: "Ranged"
    desc: "⬻ gem spit +15 (range 20 feet) __Damage__ 2d8+6 bludgeoning plus concussive gem"
abilities_bot:
  - name: "Concussive Gem"
    desc: "On a critical hit on a gem spit Strike, the target must succeed at a DC 22 Fortitude save or become stunned 1."
  - name: "Forage for Gems"
    desc: "⬺ The cave squirrel dives underground in search of gems. The cave squirrel Burrows up to its Speed. It must end its movement back on the surface. During its burrow, it happens upon 1d4 cheap gems (such as salt or quartz), which it stuffs in its cheeks, up to its maximum of 6."
  - name: "Natural Speed"
    desc: "A cave squirrel isn't affected by difficult terrain from earth or stone."
  - name: "Screaming Force"
    desc: "⬻ (Auditory, Sonic) The cave squirrel lets out a terrible scream. Non–cave squirrel creatures within 30 feet must succeed at a DC 22 Fortitude save or take 2d10 sonic damage. On a critical failure, a creature is deafened for 1 minute. The cave squirrel can't use Screaming Force again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 186."
```

```encounter-table
name: Taldan Cave Squirrel
creatures:
  - 1: Taldan Cave Squirrel
```
