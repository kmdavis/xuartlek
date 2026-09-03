---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Smuggler"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Smuggler"
level: 6
source: "NPC Core"
aon_id: "creature-3646"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3646"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Halfling Smuggler"
level: "Creature 6"
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; keen eyes"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +11, Deception +14, Intimidation +14, Society +10, Stealth +15, Thievery +16, Underworld Lore +14"
abilityMods: [3, 4, 2, 0, 1, 2]
abilities_top:
  - name: "Grease Some Palms"
    desc: "A smuggler is adept at navigating official channels and makes network contacts in order to keep their goods moving. They gain a +2 circumstance bonus to Make an Impression and Request with members of the local bureaucracy."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the Seek action to find hidden or undetected creatures within 30 feet of them. Whenever the halfling targets a creature that is concealed or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Items"
    desc: "Arsenic, Disguise Kit, lesser elixir of life, _+1 filcher's fork_, fine clothes, Leather Armor, Sling, lesser smoke ball, Thieves' Toolkit"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +16; __Will__: +13"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _filcher's fork_ +17 (Agile, Backstabber, deadly d6, Finesse, Magical) __Damage__ 1d4+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _filcher's fork_ +17 (Agile, Backstabber, deadly d6, Magical, thrown 20 feet) __Damage__ 1d4+9 piercing"
  - name: "Ranged"
    desc: "⬻ sling +16 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d4+7 bludgeoning"
abilities_bot:
  - name: "Distracting Escape"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "Smugglers succeed by making a move only after they've diverted others' attention. The smuggler Creates a Diversion. If the smuggler became hidden to at least one creature, the smuggler can then Sneak."
  - name: "Hidden Pockets"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The smuggler Interacts to draw an item of light Bulk concealed in one of their hidden pockets. The pockets can store up to four objects of light Bulk. For most smugglers, these items are arsenic, a lesser elixir of life, a lesser smoke ball, and a thieves' toolkit. The smuggler can refill the pockets over the course of 1 minute."
  - name: "Sneak Attack"
    desc: "The smuggler deals an extra 2d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 191."
```

```encounter-table
name: Halfling Smuggler
creatures:
  - 1: Halfling Smuggler
```
