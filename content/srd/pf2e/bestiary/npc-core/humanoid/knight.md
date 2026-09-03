---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Knight"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Knight"
level: 7
source: "NPC Core"
aon_id: "creature-3423"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3423"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Knight"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +15"
abilityMods: [4, 3, 3, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/sword/bastard-sword|bastard sword]]_, [[srd/pf2e/compendium/equipment/armor#Full Plate|full plate]] with livery, Spear (3), Steel Shield (Hardness 5, 20 HP, BT 10)"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +14; __Ref__: +14; __Will__: +13"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Knight's Courage"
    desc: "Any time the knight gains the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition, they reduce its value by 1."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲ The knight can Shield Block for an adjacent ally, preventing that ally from taking damage instead of themself."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bastard sword_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d12]]) __Damage__ 1d8+10 slashing"
  - name: "Melee"
    desc: "⬻ spear +17 __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ gauntlet +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spear +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+10 piercing"
abilities_bot:
  - name: "Intimidating Strike"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fighter|Fighter]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The knight makes a melee Strike. If it hits and deals damage, the target is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]], or frightened 2 on a critical hit."
  - name: "Rearming Advance"
    desc: "⬻ The knight Strides or Steps. During this movement, they can Interact to swap from wielding their bastard sword in two hands to wielding it in one hand and wielding their shield in the other, or vice versa. This Interact action doesn't trigger reactions that can be triggered by [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]] actions."
  - name: "Warding Shift"
    desc: "⬻"
  - name: "Requirements"
    desc: "The knight is adjacent to a willing ally"
  - name: "Effect"
    desc: "The knight moves an adjacent willing ally 5 feet in any direction and can Step into the space the ally vacated. Knighthood While most are knighted after years of training under an established knight, there are other ways to earn the title. It might be presented as a tournament prize, a reward for prowess in battle, or an honor bestowed upon adventurers for aiding a grateful noble. Knighthood is the fastest way to join the ranks of nobility outside of marriage and bestows land and properties along with a rise in station."
sourcebook: "_NPC Core_, page 16."
```

```encounter-table
name: Knight
creatures:
  - 1: Knight
```
