---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Scavenger"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Scavenger"
level: 4
source: "NPC Core"
aon_id: "creature-3641"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3641"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Goblin Scavenger"
level: "Creature 4"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Crafting +12, Society +8, Stealth +11, Survival +10, Thievery +9"
abilityMods: [1, 3, 2, 2, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Big Boom Gun (10 rounds), bundle of fireworks, dogslicer, Leather Armor"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +11; __Will__: +13"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Finders Keepers"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet drops an item"
  - name: "Requirements"
    desc: "The goblin scavenger has a hand free"
  - name: "Effect"
    desc: "The goblin scavenger Strides up to their speed to an adjacent square and Interacts to pick up the item. The movement triggers reactions as normal, but the Interact action to pick up the item does not."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dogslicer +12 (Agile, Backstabber, Finesse) __Damage__ 2d6+3 slashing"
  - name: "Melee"
    desc: "⬻ jaws +12 (Unarmed) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ big boom gun +14 (cobbled; fatal d12; modular B, or S; range 20 feet; reload 1) __Damage__ 2d6+2 modular"
abilities_bot:
  - name: "Fireworks Barrage"
    desc: "⬺ (Manipulate)"
  - name: "Requirement"
    desc: "The goblin scavenger has a free hand"
  - name: "Effect"
    desc: "The goblin scavenger draws a bundle of fireworks and launches them toward a point within 60 feet, where they explode, dealing 1d10 fire damage and 1d10 sonic damage in a 10-foot burst. Every creature in the area must attempt a DC 21 Reflex save."
  - name: "Critical Success"
    desc: "The creature is unaffected. The goblin scavenger realizes that's because a firework fell at their feet and takes 2 fire damage when it explodes in their face."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is dazzled and deafened for 1 round."
  - name: "Critical Failure"
    desc: "As failure, except the creature is also stunned 1."
  - name: "One Person's Junk"
    desc: "The goblin scavenger intuitively knows how to make use of junk. When they use a weapon with the goblin trait or an improvised weapon, they do an additional die of damage (already included in the Strikes above)."
sourcebook: "_NPC Core_, page 186."
```

```encounter-table
name: Goblin Scavenger
creatures:
  - 1: Goblin Scavenger
```
