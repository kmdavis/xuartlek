---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Twins of Rowan"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Twins of Rowan"
level: 13
source: "Rage of Elements"
aon_id: "creature-2680"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2680"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Twins of Rowan"
level: "Creature 13"
size: "Huge"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; tremorsense (imprecise) 30 feet"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +21"
abilityMods: [5, 4, 8, 2, 3, 4]
abilities_top:
  - name: "Shielded Eyes"
    desc: "A twins of rowan's protective mask shields them from blinding and dazzling effects."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +24; __Ref__: +17; __Will__: +27"
hp: 273
health:
  - name: "HP"
    desc: "273; __Immunities__ bleed, blindness, [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15"
abilities_mid:
  - name: "Beacon of the Rowan Guard"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/wood|wood]]) 40 feet. The lantern carried by the twins of rowan contains pure elemental life energy that resonates with and empowers all wood elementals. While within the emanation, a creature with the [[srd/pf2e/compendium/rules-elements/traits/player-core/elemental|elemental]] trait and either the [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]] trait or [[srd/pf2e/compendium/rules-elements/traits/player-core/wood|wood]] trait gains fast healing 10 and a +2 circumstance bonus to all attack and damage rolls. The aura can be counteracted with a DC 30 check to _dispel magic_; doing so deactivates the aura for 1d6 rounds."
speed: "35 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d8+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ stump +26 (Brutal, range increment 120 feet) __Damage__ 2d10+15 bludgeoning"
abilities_bot:
  - name: "Follow-Up Combo"
    desc: "⬺ The twins of rowan makes a rapier Strike, followed by two fist Strikes, all against the same target. These attacks all count toward the twins' multiple attack penalty, but the penalty doesn't increase until after the twins make their attacks."
  - name: "Lifespring Burst"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|Vitality]]) Once per day, the twins of rowan can strike the ground with their sword, releasing a 30-foot burst of life energy centered on the twins that deals 14d6 vitality damage (DC 30 basic Fortitude save); the twins of rowan is immune. The area affected by this burst then becomes greater difficult terrain as vibrant new plant life ruptures through it."
  - name: "Throw Stump"
    desc: "⬻ As Throw Rock but can also be used to throw stumps and logs. Scions of Life Rowan trees have a long association with protection; Shumunue accordingly chose rowan as the base for the powerful guardian twins. Their weapons and protective masks are grown separately from younger saplings fed with mineral-rich magic that makes their wood as strong and sharp as steel."
sourcebook: "_Rage of Elements_, page 211."
```

```encounter-table
name: Twins of Rowan
creatures:
  - 1: Twins of Rowan
```
