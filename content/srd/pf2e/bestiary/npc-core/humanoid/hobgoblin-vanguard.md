---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin Vanguard"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hobgoblin Vanguard"
level: 8
source: "NPC Core"
aon_id: "creature-3650"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3650"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hobgoblin Vanguard"
level: "Creature 8"
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Athletics +18, Crafting +17, Intimidation +16, Survival +16"
abilityMods: [5, 2, 3, 2, 1, 1]
abilities_top:
  - name: "Items"
    desc: "alchemical grenades, Alchemist's Toolkit, Full Plate, _+1 striking maul_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +13; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _maul_ +19 (Magical, Shove) __Damage__ 2d12+8 bludgeoning plus Knockdown"
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ alchemical grenade +16 (range increment 20 feet, Splash) __Damage__ 2d8 acid, cold, electricity, or fire plus 2 persistent damage and 2 splash damage of the same type"
abilities_bot:
  - name: "Shock and Awe"
    desc: "⬲ (Emotion, Mental, Visual)"
  - name: "Trigger"
    desc: "The hobgoblin vanguard critically hits a creature with an alchemical grenade Strike"
  - name: "Effect"
    desc: "The hobgoblin vanguard attempts to Demoralize the creature with a mere look. If the target creature was reduced to 0 Hit Points by the triggering Strike, the hobgoblin vanguard can instead attempt to Demoralize all opponents within 30 feet, rolling once and comparing the result to each target's Will DC."
sourcebook: "_NPC Core_, page 195."
```

```encounter-table
name: Hobgoblin Vanguard
creatures:
  - 1: Hobgoblin Vanguard
```
