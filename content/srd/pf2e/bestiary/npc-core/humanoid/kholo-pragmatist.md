---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kholo Pragmatist"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Kholo Pragmatist"
level: 1
source: "NPC Core"
aon_id: "creature-3652"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3652"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Kholo Pragmatist"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Kholo|Kholo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [2, 2, 1, 2, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Longspear, Sling (20 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +6; __Will__: +8"
hp: 22
health:
  - name: "HP"
    desc: "22"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]]) __Damage__ 1d8+2 piercing"
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Pack Attack"
    desc: "A kholo pragmatist deals 1d4 extra damage to any creature that's within reach of at least two of the kholo pragmatist's allies."
  - name: "Pragmatic Aid"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]])"
  - name: "Requirements"
    desc: "The kholo pragmatist is adjacent to a foe"
  - name: "Effect"
    desc: "The kholo pragmatist sets up an advantageous avenue of attack for an ally within 10 feet of the same foe and then Steps away from that foe. The foe is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the kholo pragmatist's ally's next attack."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
  - name: "Spear Parry"
    desc: "⬻"
  - name: "Requirements"
    desc: "The kholo pragmatist is wielding a longspear"
  - name: "Effect"
    desc: "The kholo pragmatist positions their spear defensively, gaining a +1 circumstance bonus to AC until the start of their next turn."
sourcebook: "_NPC Core_, page 196."
```

```encounter-table
name: Kholo Pragmatist
creatures:
  - 1: Kholo Pragmatist
```
