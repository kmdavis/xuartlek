---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lomori Sprout"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/tiny
statblock: inline
name: "Lomori Sprout"
level: 3
source: "Rage of Elements"
aon_id: "creature-2684"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2684"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Lomori Sprout"
level: "Creature 3"
size: "Tiny"
trait_01: "Aeon"
trait_02: "Plant"
trait_03: "Rare"
trait_04: "Wood"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Muan, Rasu, Utopian"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +7, Crafting +10, Gardening Lore +11, Nature +10, Stealth +11"
abilityMods: [0, 4, 3, 0, 3, 1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +11; __Will__: +8"
hp: 50
health:
  - name: "HP"
    desc: "50; __Weaknesses__ fire 3, void 3"
abilities_mid:
  - name: "Scurry"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature the lomori sprout can observe attacks the sprout"
  - name: "Effect"
    desc: "After the attack resolves, the lomori sprout can Stride up to their speed. This movement doesn't trigger reactions from the triggering creature."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬺ grass lash +9 (Disarm, Finesse, reach 5 feet) __Damage__ 2d6 slashing plus Knockdown"
abilities_bot:
  - name: "Take Root"
    desc: "⬺"
  - name: "Requirements"
    desc: "The lomori sprout is on the ground"
  - name: "Effect"
    desc: "The lomori sprout plants themself in the ground. Grasping roots erupt from the ground in a 5-foot burst within 60 feet of the lomori sprout, dealing 4d4 bludgeoning damage (DC 20 basic Reflex save) to creatures in the area; on a failed save, a creature gains the immobilized condition until it Escapes (DC 20). The roots also make the area difficult terrain for 1 minute, after which they decompose into fertile mulch; the area is no longer difficult terrain, and any creatures still immobilized by the roots automatically Escape."
  - name: "Greater Forest Passage"
    desc: "The lomori sprout ignores difficult terrain and greater difficult terrain from plants and fungi. Get Off My Lawn! Lomori sprouts are industrious yet skittish, halting their work only to hide from intruders—if they can be bothered to stop at all. They're ceaseless in their efforts, often working together in large groups to tend vast swaths of land. Nothing rouses a lomori sprout to violence faster than damaging their garden or other creations."
sourcebook: "_Rage of Elements_, page 215."
```

```encounter-table
name: Lomori Sprout
creatures:
  - 1: Lomori Sprout
```
