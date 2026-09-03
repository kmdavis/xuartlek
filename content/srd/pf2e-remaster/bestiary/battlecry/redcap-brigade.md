---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Redcap Brigade"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Redcap Brigade"
level: 10
source: "Battlecry!"
aon_id: "creature-3935"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3935"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Redcap Brigade"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Fey"
trait_02: "Troop"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +22, Intimidation +22, Nature +17"
abilityMods: [4, 6, 4, 2, 2, 3]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +18; __Ref__: +22; __Will__: +17"
hp: 165
health:
  - name: "HP"
    desc: "165 (4 segments, fast healing 20); __Weaknesses__ area damage 10, cold iron 10, divine revulsion, splash damage 10"
abilities_mid:
  - name: "Divine Revulsion"
    desc: "(emotion, fear, mental) If a redcap brigade sees a creature brandish a religious symbol of a deity (which requires an Interact action by that creature) or cast a divine spell while wearing a religious symbol, the troop must attempt a DC 26 Will save. They then become temporarily immune to all brandished religious symbols for 10 minutes."
  - name: "Critical Success"
    desc: "The troop is unaffected."
  - name: "Success"
    desc: "The troop is frightened 1."
  - name: "Failure"
    desc: "The troop is frightened 2."
  - name: "Critical Failure"
    desc: "The troop is frightened 3."
  - name: "Troop Defenses"
    desc: ""
speed: "50 feet; troop movement"
abilities_bot:
  - name: "Blood Soak"
    desc: "⭓"
  - name: "Trigger"
    desc: "The redcap brigade loses its first segment, causes another troop to lose its first segment, or is otherwise exposed to copious amounts of blood; Effect The redcap brigade gains a status bonus to damage rolls for 1 minute. The bonus is +2 if they spend one action on Bloody Reaping, +6 if they spend two actions, or +8 if they spend 3 actions. They gain a +4 status bonus to damage rolls with Bowl Over and Stomp."
  - name: "Bloody Reaping"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The redcaps in the brigade wildly swing their halberds and sickles at each enemy in a 10-foot emanation, with a DC 26 basic Reflex save. The damage depends on the number of actions. ⬻ 1d10+2 slashing ⬺ 2d10+9 slashing ⬽ 3d10+10 slashing"
  - name: "Bowl Over and Stomp"
    desc: "⬺ The redcap brigade Strides; they can pass through spaces of Medium or smaller creatures, but can't end their movement in them. All enemies whose spaces the redcap brigade passed through take 4d8 bludgeoning damage and must attempt a DC 26 Fortitude save. Bowl Over and Stomp damages each creature only once."
  - name: "Critical Success"
    desc: "The creature takes no damage."
  - name: "Success"
    desc: "The creature takes half damage. If it is prone, it also takes 1d6 persistent bleed damage."
  - name: "Failure"
    desc: "The creature takes full damage, is knocked prone, and takes 2d6 persistent bleed damage."
  - name: "Critical Failure"
    desc: "The creature takes double damage, is knocked prone, and takes 2d6 persistent bleed damage."
  - name: "Deadly Swipes"
    desc: "⬲"
  - name: "Trigger"
    desc: "The redcap brigade drops a creature to 0 Hit Points with Bloody Reaping"
  - name: "Effect"
    desc: "The redcap brigade performs an additional one-action Bloody Reaping, ignoring the once per round frequency limitation. This does not deal damage to the triggering creature."
sourcebook: "_Battlecry!_, page 189."
```

```encounter-table
name: Redcap Brigade
creatures:
  - 1: Redcap Brigade
```
