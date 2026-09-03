---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Infantry"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Clockwork Infantry"
level: 11
source: "Battlecry!"
aon_id: "creature-3907"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3907"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Clockwork Infantry"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Troop"
trait_05: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +23"
abilityMods: [7, 3, 5, -5, 5, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 27, standby"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +21; __Will__: +18"
hp: 195
health:
  - name: "HP"
    desc: "195 (4 segments); __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poisoned, sickened, unconscious, vitality, void; __Resistances__ physical 8 (except adamantine or orichalcum); __Weaknesses__ area damage 10, electricity 10, splash damage 10, orichalcum 10"
abilities_mid:
  - name: "Reactive Sweep"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy within a 10-foot emanation uses a manipulate action or a move action, makes a ranged attack, or leaves a square in the area during a move action it's using"
  - name: "Effect"
    desc: "The clockwork infantry lashes out with their halberds. The triggering enemy takes 2d10+10 damage (DC 27 basic Reflex save). If the enemy critically fails this saving throw and the trigger was a manipulate action, the damage disrupts that action."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Halberd Sweep"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The clockwork infantry engages in a coordinated melee attack against each enemy in a 10-foot emanation, with a DC 27 basic Reflex save. The damage depends on the number of actions. ⬻ 1d10+2 piercing or slashing damage ⬺ 2d10+10 piercing or slashing damage ⬽ 3d10+12 piercing or slashing damage"
  - name: "Raise Defenses"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The clockwork soldiers of the infantry extend external plates on mechanical actuators to defend the troop or an adjacent creature. The creature gains a +2 circumstance bonus to AC until the start of the infantry's next turn, or until it is no longer adjacent to the infantry, whichever comes first."
sourcebook: "_Battlecry!_, page 176."
```

```encounter-table
name: Clockwork Infantry
creatures:
  - 1: Clockwork Infantry
```
