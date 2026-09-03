---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wight Battalion"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/wight
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Wight Battalion"
level: 9
source: "Battlecry!"
aon_id: "creature-3942"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3942"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Wight Battalion"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Troop"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Wight"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +20, Intimidation +18, Stealth +18"
abilityMods: [6, 2, 4, 0, 3, 2]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +15; __Will__: +18"
hp: 150
health:
  - name: "HP"
    desc: "150 (4 segments, fueled by spite, void healing); __Weaknesses__ area damage 7, splash damage 7"
abilities_mid:
  - name: "Final Grudge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The wight battalion is about to lose a segment due to Hit Point damage"
  - name: "Effect"
    desc: "The wights strike out as they fall. Each enemy in a 5-foot emanation takes 2d4 piercing damage (DC 25 basic Reflex save). This occurs before the battalion loses a segment."
  - name: "Fueled by Spite"
    desc: "Each time a creature loses Hit Points due to the wight battalion's corrupting spite curse, the battalion gains 6 temporary Hit Points that last for 1 round."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Corrupting Spite"
    desc: "(Curse, Divine, Void) The wight battalion's attacks inflict a curse that makes a creature grow weak and spiteful. A living humanoid that dies while under this curse rises as a wight after 1d4 rounds, controlled by the wight battalion that inflicted the curse. This new wight can't inflict corrupting spite and is clumsy 2. If the creating wight battalion dies or after roughly a month of existence, the new wight becomes autonomous and becomes a normal wight"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Stage 1"
    desc: "drained 1 (1 round)"
  - name: "Stage 2"
    desc: "drained 2 and doesn't treat any creatures as allies (1 round)"
  - name: "Stage 3"
    desc: "As stage 2, except drained 3 (1 round)"
  - name: "Stage 4"
    desc: "As stage 2, except drained 4 (1 round)."
  - name: "Hateful Daggers"
    desc: "The wights coordinate melee attacks with the daggers they were buried with. Each enemy within a 5-foot emanation attempts a DC 25 basic Reflex save. The damage depends on the number of actions. On a failed save, the creature is also exposed to corrupting spite. ⬻ 2d4 piercing damage ⬺ 4d4+8 piercing damage ⬽ 4d4+14 piercing damage"
sourcebook: "_Battlecry!_, page 194."
```

```encounter-table
name: Wight Battalion
creatures:
  - 1: Wight Battalion
```
