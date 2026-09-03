---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Assassin"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Assassin"
level: 8
source: "NPC Core"
aon_id: "creature-3434"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3434"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Assassin"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +14, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +14"
abilityMods: [3, 5, 2, 2, 2, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/composite-shortbow|composite shortbow]]_ (20 arrows), lesser darkvision elixir, [[srd/pf2e/compendium/equipment/alchemical-items/giant-centipede-venom-equipment-3334|Giant Centipede Venom]] (4), [[srd/pf2e/compendium/equipment/consumables/invisibility-potion|_invisibility potion_]], Leather Armor, Lethargy Poison (3), _+1 [[srd/pf2e/compendium/equipment/weapons/sword/rapier|rapier]]_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +12; __Ref__: +19; __Will__: +14"
hp: 130
health:
  - name: "HP"
    desc: "130"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The assassin isn't [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to creatures of 8th level or lower that are [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]], flanking, or using surprise attack."
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The assassin is targeted with a melee or ranged attack by an attacker it can see"
  - name: "Effect"
    desc: "The assassin gains a +2 circumstance bonus to AC against the triggering attack."
speed: "25 feet, swift sneak"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d6+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 2d6+7 piercing"
abilities_bot:
  - name: "Assassin's Poison"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The assassin is wielding a piercing or slashing weapon and has a free hand"
  - name: "Effect"
    desc: "The assassin applies a poison to the weapon. That poison's DC is increased to 24 if it was lower."
  - name: "Quick Draw"
    desc: "⬻ The assassin Interacts to draw a weapon, then Strikes with that weapon."
  - name: "Sneak Attack"
    desc: "The assassin deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the assassin."
  - name: "Swift Sneak"
    desc: "The assassin can move their full Speed when [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaking]]."
sourcebook: "_NPC Core_, page 23."
```

```encounter-table
name: Assassin
creatures:
  - 1: Assassin
```
