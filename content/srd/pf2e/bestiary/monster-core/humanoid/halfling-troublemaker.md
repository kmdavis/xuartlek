---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Troublemaker"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Troublemaker"
level: 1
source: "Monster Core"
aon_id: "creature-3045"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3045"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Halfling Troublemaker"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +3, Deception +5, Stealth +7, Thievery +7"
abilityMods: [1, 4, 1, 0, 3, 3]
abilities_top:
  - name: "Items"
    desc: "Filcher's Fork, Leather Armor"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ filcher's fork +9 (Agile, Backstabber, deadly d6, Finesse, thrown 20 feet) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ filcher's fork +9 (Agile, Backstabber, deadly d6, Finesse, thrown 20 feet) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Graffiti Egg"
    desc: "⬻ the halfling troublemaker throws an egg filled with paint, glitter, and confetti at a creature within 30 feet. The target must succeed a DC 17 Reflex saving throw or become dazzled for 1 round (or 1 minute on a critical failure)."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the Seek action to find hidden or undetected creatures within 30 feet of it. Whenever the halfling targets a creature that is concealed or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Sneak Attack"
    desc: "The troublemaker deals an extra 1d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core_, page 192."
```

```encounter-table
name: Halfling Troublemaker
creatures:
  - 1: Halfling Troublemaker
```
