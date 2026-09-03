---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin Battalion"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Hobgoblin Battalion"
level: 6
source: "NPC Core"
aon_id: "creature-3649"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3649"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hobgoblin Battalion"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +12"
abilityMods: [5, 0, 3, 0, 2, 2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +12; __Will__: +14"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments); __Weaknesses__ area damage 8, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 8"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Coordinated Strikes"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The battalion thrusts their spears at each enemy in a 5-foot emanation with a DC 21 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+2 slashing damage ⬺ 2d6+5 slashing damage ⬽ 3d12+7 slashing damage"
  - name: "Focused Volley"
    desc: "⬺ The hobgoblin battalion's archers draw or reload their crossbows, then launch a ranged attack in the form of a volley. This volley is a 10-foot burst within 120 feet that deals 2d8 piercing damage with a DC 21 basic Reflex save. When the hobgoblin battalion is reduced to 2 or fewer segments, this area is reduced to a 5-foot burst."
  - name: "Perfect Formation"
    desc: "⬻ The battalion raises a perfect guard against explosions. It gains a +2 item bonus to AC and a +2 status bonus to Reflex saves until the start of its next turn."
sourcebook: "_NPC Core_, page 194."
```

```encounter-table
name: Hobgoblin Battalion
creatures:
  - 1: Hobgoblin Battalion
```
