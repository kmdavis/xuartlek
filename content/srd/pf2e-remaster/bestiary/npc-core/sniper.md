---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sniper"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sniper"
level: 5
source: "NPC Core"
aon_id: "creature-3525"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3525"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Sniper"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +11, Medicine +11, Stealth +15, Survival +11"
abilityMods: [2, 4, 1, 1, 4, 0]
abilities_top:
  - name: "Silencer"
    desc: "A silencer is an uncommon item worth 1 sp. It has light Bulk and can be attached to a firearm in 1 minute; the sniper typically already has one attached before going into combat. The first time a shot is fired through it, the silencer is consumed and reduces the report to a quiet noise. A silencer doesn't work on scatter firearms."
  - name: "Items"
    desc: "Arquebus (20 cartridges), Dagger, Silencer (4)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +15; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +15 (Agile, Finesse, versatile S +15) __Damage__ 1d4+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Finesse, Nonlethal, unarmed +15) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arquebus +15 (range 150 feet, Concussive, fatal d12, Kickback, reload 1) __Damage__ 1d8+6 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +15 (Agile, thrown 10 feet, versatile S +15) __Damage__ 1d4+8 piercing"
abilities_bot:
  - name: "Concussive Shot"
    desc: "⬺ The sniper makes an arquebus Strike against a creature within the weapon's first range increment. On a success, the creature must succeed at a DC 21 Fortitude save or be stunned 1 (stunned 2 on a critical failure)."
  - name: "Full Bore"
    desc: "⬺ The sniper makes an arquebus Strike against two creatures that are adjacent to each other. The attack ignores any lesser cover one target provides the other. Roll damage once, and apply it to each creature the sniper hits. This counts as two attacks when determining the sniper's multiple attack penalty."
  - name: "Sniper's Edge"
    desc: "The sniper's ranged Strikes deal 2d6 extra precision damage to off-guard creatures."
  - name: "Surprise Attack"
    desc: "All enemy creatures that have not yet acted in combat are off-guard to the sniper. Outfitting A Sniper The weapons and armor of a sniper vary depending on how they wish to get the job done. Though this one uses an arquebus, many snipers choose to use longbows if gunpowder isn't an option or if they prefer more subtle means of killing. Snipers usually forgo wearing the colors of their company in favor of hues that best match their surroundings. They usually only carry a small insignia for identification purposes, and their position is usually on a need-to-know basis."
sourcebook: "_NPC Core_, page 90."
```

```encounter-table
name: Sniper
creatures:
  - 1: Sniper
```
