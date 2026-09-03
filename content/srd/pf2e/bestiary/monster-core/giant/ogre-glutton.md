---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ogre Glutton"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Ogre Glutton"
level: 4
source: "Monster Core"
aon_id: "creature-3119"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3119"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ogre Glutton"
level: "Creature 4"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [6, -1, 4, -2, 0, -2]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Greataxe"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +14; __Ref__: +7; __Will__: +6"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+8 slashing"
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 1d8+8 piercing plus Grab and glutton's feast"
abilities_bot:
  - name: "Glutton's Feast"
    desc: "If the ogre glutton damages a living creature with their jaws Strike, they gain 1d4 temporary Hit Points for 1 minute."
  - name: "Glutton's Rush"
    desc: "⬺ The ogre glutton Strides twice and makes a jaws Strike. If they damage a living creature with this Strike, the temporary Hit Points they receive from glutton's feast is increased to 2d4."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Small, 2d4+4 bludgeoning, Rupture 14"
sourcebook: "_Monster Core_, page 250."
```

```encounter-table
name: Ogre Glutton
creatures:
  - 1: Ogre Glutton
```
