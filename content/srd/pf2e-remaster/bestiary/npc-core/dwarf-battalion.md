---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf Battalion"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Dwarf Battalion"
level: 6
source: "NPC Core"
aon_id: "creature-3628"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3628"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dwarf Battalion"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "Common, Dwarven"
skills:
  - name: "Skills"
    desc: "Athletics +15, Survival +13, Warfare Lore +11"
abilityMods: [5, 1, 4, 0, 3, -1]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +16; __Ref__: +11; __Will__: +13"
hp: 105
health:
  - name: "HP"
    desc: "105 (4 segments); __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Dwarven Doughtiness"
    desc: "Dwarves are often calm and collected in the face of imminent danger. At the end of the battalion's turn, reduce its frightened condition by 2 instead of 1."
  - name: "Troop Defenses"
    desc: ""
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Bombing Barrage"
    desc: "⬺ The dwarf battalion draws alchemical bombs, then hurls them at distant foes. This volley is a 10-foot burst within 60 feet that deals 3d6 damage with a DC 21 basic Reflex save. The damage is either acid, fire, or electricity damage, depending on which type of bombs the battalion used. When the dwarf battalion is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Coordinated Pummel"
    desc: "Frequency once per round; Effect The dwarf battalion unleashes a storm of warhammer blows against each enemy in a 5-foot emanation (DC 21 basic Reflex save). The damage depends on the number of actions. ⬻ 1d8 bludgeoning damage ⬺ 2d8+5 bludgeoning damage ⬽ 3d8+5 bludgeoning damage"
  - name: "Dwarven War Song"
    desc: "⬻ (Auditory, Concentrate, Emotion, Fear, Mental) The battalion joins together to sing a traditional song of battle. Each enemy in a 30-foot emanation must succeed at a DC 23 Will save or be frightened 1 (or frightened 2 on a critical failure). Each enemy is then temporarily immune for 10 minutes. __Shields Up!__ ⬲ The battalion raises their steel shields. It gains a +2 circumstance bonus to AC and Reflex saves until the start of its next turn."
sourcebook: "_NPC Core_, page 175."
```

```encounter-table
name: Dwarf Battalion
creatures:
  - 1: Dwarf Battalion
```
