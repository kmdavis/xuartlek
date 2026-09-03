---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Skullcrushers"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Orc Skullcrushers"
level: 7
source: "NPC Core"
aon_id: "creature-3665"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3665"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Orc Skullcrushers"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Athletics +17, Intimidation +15, Stealth +16, Survival +13"
abilityMods: [4, 3, 4, 0, 2, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +16; __Will__: +13"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Resistances__ void 8; __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Chant of Dominance"
    desc: "⬻ (Divine, Holy, Spirit)"
  - name: "Effect"
    desc: "Orc war drummers lead the other skullcrushers in a holy chant extolling their superiority in battle. Any creature damaged by the skullcrushers this turn also takes 1d6 persistent spirit damage."
  - name: "Crush Skulls"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The skullcrushers smash their mauls and clubs against each enemy in a 5-foot emanation, with a DC 22 basic Reflex save. The damage depends on the number of actions. ⬻ 1d12 bludgeoning damage ⬺ 1d12+8 bludgeoning damage ⬽ 2d12+8 bludgeoning damage"
  - name: "Sacred Salvo"
    desc: "⬺ (Divine, Vitality) The skullcrushers fling a fusillade of sling bullets enchanted with life energy intended to destroy undead. This barrage is a 10-foot burst within 50 feet that deals 3d6 bludgeoning damage plus 1d6 vitality damage to undead, with a DC 22 basic Reflex save. When the troop is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
sourcebook: "_NPC Core_, page 207."
```

```encounter-table
name: Orc Skullcrushers
creatures:
  - 1: Orc Skullcrushers
```
