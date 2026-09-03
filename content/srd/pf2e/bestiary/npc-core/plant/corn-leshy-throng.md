---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Corn Leshy Throng"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Corn Leshy Throng"
level: 4
source: "NPC Core"
aon_id: "creature-3658"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3658"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Corn Leshy Throng"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: "Troop"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]] (corn only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +12"
abilityMods: [2, 3, 2, 0, 2, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +13; __Will__: +10"
hp: 54
health:
  - name: "HP"
    desc: "54 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Encircling Maze"
    desc: "A corn leshy throng is arranged in rows of stalks to envelop foes, stretching upward to block their vision. It can move into other creatures' spaces, and other creatures can move into its squares. When a Medium or smaller creature attempts to enter any of the corn leshy throng's spaces, it must attempt a DC 20 [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] check. If the creature fails, it gets turned around—all the throng's squares are greater difficult terrain for it until the end of this turn. A creature needs to attempt this check only the first time in a round it attempts to enter one of the throng's squares."
  - name: "Troop Defenses"
    desc: ""
  - name: "Verdant Burst"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) When the corn leshy throng dies, a burst of primal energy explodes from their body, restoring 3d8 Hit Points to each plant creature in a 30-foot emanation. This area immediately fills with stalks of corn, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Boxing Ears"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The corn leshy throng lashes out with hardened ears of corn to attack each enemy in its space and in a 5-foot emanation, with a DC 18 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6 bludgeoning damage ⬺ 2d6+4 bludgeoning damage ⬽ 2d6+8 bludgeoning damage"
  - name: "Kernel Barrage"
    desc: "⬺ The throng's members fling a bombardment of corn kernels. Each creature in a 30-foot cone takes 2d6 bludgeoning damage with a DC 18 basic Reflex save. When the throng is reduced to 2 or fewer segments, this area decreases to a 15-foot cone."
sourcebook: "_NPC Core_, page 201."
```

```encounter-table
name: Corn Leshy Throng
creatures:
  - 1: Corn Leshy Throng
```
