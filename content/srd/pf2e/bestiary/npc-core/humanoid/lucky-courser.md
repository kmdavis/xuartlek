---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lucky Courser"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/catfolk
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Lucky Courser"
level: 8
source: "NPC Core"
aon_id: "creature-3625"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3625"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Lucky Courser"
level: "Creature 8"
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
languages: "Amurrun, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +16, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [2, 4, 3, 1, 2, 2]
abilities_top:
  - name: "Warning Ears"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Trigger"
    desc: "The lucky courser rolls initiative using Perception or [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]]"
  - name: "Effect"
    desc: "Their expressive ears twitch in alarm, granting allies within 10 feet a +2 circumstance bonus to initiative rolls."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/crossbow/arbalest|arbalest]]_ (20 cold iron bolts, 20 dawnsilver bolts), +1 whip, Leather Armor"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +18; __Will__: +14"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Guide to Fortune"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Trigger"
    desc: "The lucky courser or an ally within 10 feet fails a Reflex save, [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] check, or [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check"
  - name: "Effect"
    desc: "The triggering creature rerolls the save or check and uses the better result."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _whip_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+12 slashing"
  - name: "Melee"
    desc: "⬻ claw+19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+12 slashing"
  - name: "Ranged"
    desc: "⬻ _arbalest_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 110 feet, reload 1) __Damage__ 2d10+6 piercing"
abilities_bot:
  - name: "Elusive Hunter"
    desc: "The lucky courser can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] and [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneak]] in any natural terrain and in lesser cover from allies."
  - name: "Feline Skirmish"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The lucky courser can Interact to reload their arbalest, Step, and Strike, taking the actions in any order. The Step ignores difficult terrain."
  - name: "Head Shot"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The lucky courser [[srd/pf2e/compendium/rules-elements/actions/player-core#Create a Diversion|Creates a Diversion]] and then Strikes. The target is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] until the end of the lucky courser's next turn on a successful Strike (or [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] on a critical hit)."
sourcebook: "_NPC Core_, page 173."
```

```encounter-table
name: Lucky Courser
creatures:
  - 1: Lucky Courser
```
