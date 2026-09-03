---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hārakasura"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/asura
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Hārakasura"
level: 7
source: "Monster Core 2"
aon_id: "creature-4086"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4086"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hārakasura"
level: "Creature 7"
size: "Medium"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Common, Diabolic; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +19, Intimidation +15, Performance +15, Religion +15, Stealth +15"
abilityMods: [6, 4, 4, 2, 2, 4]
abilities_top:
  - name: "Items"
    desc: "Kukri (4)"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +17; __Will__: +13"
hp: 130
health:
  - name: "HP"
    desc: "130; __Immunities__ curses; __Weaknesses__ holy 5 (see glorious visage)"
abilities_mid:
  - name: "Dual Mind"
    desc: "⬲"
  - name: "Trigger"
    desc: "The hārakasura fails a saving throw against a mental effect"
  - name: "Effect"
    desc: "The hārakasura shunts the effect into one of their minds, rendering them temporarily insensible. They change their result to a success, but one of their bodies hangs limply until the end of their next turn. During this time, the hārakasura is clumsy 2; takes a –10-foot circumstance penalty to their Speed; and can't use Dual Mind, Dance of Destruction, or Reactive Strike."
  - name: "Reactive Strike"
    desc: "⬲ The hārakasura gains an additional reaction at the beginning of each of their turns that they can use only for a Reactive Strike."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +18 (Agile, Trip, Unholy) __Damage__ 1d6+9 slashing plus 2d6 persistent bleed and 1d4 spirit"
  - name: "Melee"
    desc: "⬻ claw +18 (Agile, Unholy) __Damage__ 1d6+9 slashing and 1d4 spirit"
abilities_bot:
  - name: "Dance of Destruction"
    desc: "⬻"
  - name: "Requirements"
    desc: "The hārakasura's last action was a Strike that dealt damage"
  - name: "Effect"
    desc: "The hārakasura Strides up to 10 feet and Strikes."
  - name: "Glorious Visage"
    desc: "⬻ The asura sanctifies themselves as either holy or unholy, gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 5 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Wound Thief"
    desc: "⬻ (Divine) The hārakasura touches an adjacent creature that is taking persistent bleed damage. If the hārakasura has the holy trait, it ends the persistent bleed effect immediately and restores 2d6 Hit Points to the target; this is a healing and vitality effect. If the hārakasura has the unholy trait, it causes the target to immediately take damage equal to its persistent bleed value, and the hārakasura gains temporary Hit Points equal to the damage taken until the start of its next turn."
sourcebook: "_Monster Core 2_, page 43."
```

```encounter-table
name: Hārakasura
creatures:
  - 1: Hārakasura
```
