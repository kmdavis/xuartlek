---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bogwid"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Bogwid"
level: 5
source: "Monster Core"
aon_id: "creature-2859"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2859"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bogwid"
level: "Creature 5"
size: "Medium"
trait_01: "Aberration"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +13, Intimidation +11, Stealth +10"
abilityMods: [5, 4, 4, -4, -2, 1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +15; __Ref__: +12; __Will__: +8"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Revolting Aura"
    desc: "(aura, olfactory) 20 feet. A creature entering the aura or beginning their turn in the aura must succeed at a DC 20 Fortitude save or become sickened 1 (or sickened 2 on a critical failure). A creature that succeeds is temporarily immune to the aura for 1 minute."
speed: "25 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +15 __Damage__ 2d8+8 bludgeoning plus bogwid fever"
  - name: "Ranged"
    desc: "⬻ larval spit +14 (range increment 10 feet) __Damage__ 2d8 persistent bleed plus ravenous young"
abilities_bot:
  - name: "Bogwid Fever"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Onset"
    desc: "1 day"
  - name: "Stage 1"
    desc: "enfeebled 1 (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 2, and the DC to recover from persistent bleed is increased by 2 (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 3, and the DC to recover from persistent bleed is increased by 5 (1 day)"
  - name: "Stage 4"
    desc: "enfeebled 4, the DC to recover from persistent bleed is increased by 5, and you take 1d8 persistent bleed damage every 1d4 hours (1 day)"
  - name: "Ravenous Young"
    desc: "The larvae launched from the bogwid attach themselves to the target and begin to feed. Once a larva is attached, the target becomes drained 1. While the larva remains attached, the target cannot recover from persistent bleed. To remove the larva, the target can attempt a DC 21 Escape check. Additionally, any area damage dealt to the target destroys all attached larvae. Swamp Bodies While a bogwid does not have a lair and does not carry any treasure, a bogwid's presence is often foreshadowed by the discovery of bodies with large gaping holes in their chests. Though these will often just come in the form of crocodiles and other large predators, a lucky adventurer might just stumble upon the corpse of a much less lucky adventurer."
sourcebook: "_Monster Core_, page 46."
```

```encounter-table
name: Bogwid
creatures:
  - 1: Bogwid
```
