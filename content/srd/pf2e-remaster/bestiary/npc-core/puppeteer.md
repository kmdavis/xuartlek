---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Puppeteer"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Puppeteer"
level: 6
source: "NPC Core"
aon_id: "creature-3577"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3577"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Puppeteer"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Aklo, Common"
skills:
  - name: "Skills"
    desc: "Crafting +15, Occultism +13, Performance +13, Thievery +9"
abilityMods: [1, 2, 1, 4, 1, 4]
abilities_top:
  - name: "Puppets"
    desc: "The puppeteer has three animate puppets under their control—a smart puppet, a strong puppet, and a swift puppet. A puppet is a Tiny object that can be share a space with another creature. The usually begin combat in the puppeteer's space. A puppet has AC 23, Hardness 5, 20 Hit Points, and object immunities. If a puppet is destroyed, the puppeteer takes 15 nonlethal mental damage. A puppeteer can rebuild a puppet with 7 days of work. If the puppeteer dies while any of their puppets are still active, the active puppets become independent, but lose the will to fight in their grief."
  - name: "Items"
    desc: "_+1 dagger_, puppets"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +11; __Ref__: +14; __Will__: +15"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +14 (Agile, Finesse, Magical, versatile S) __Damage__ 1d4+7 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _dagger_ +14 (Agile, Magical, thrown 10 feet, versatile S) __Damage__ 1d4+7 piercing"
abilities_bot:
  - name: "Manipulate Puppets"
    desc: "⬺ (Concentrate, Manipulate, Occult) The puppeteer pulls at invisible strings to control their puppets. Each puppet Strides up to 30 feet. Each puppet can then make a Strike as described below. Each attack counts towards the puppeteer's multiple attack penalty, but their penalty does not increase until all attacks have been made."
  - name: "Smart Puppet"
    desc: "The smart puppet is covered in runes that give it occult power. It makes a ranged Strike against a creature within 30 feet at a +15 attack modifier. A successful Strike deals 2d6 mental damage."
  - name: "Strong Puppet"
    desc: "The strong puppet wields a tiny sword and shield. It makes a melee Strike against a creature whose space it shares at a +15 attack modifier. A successful Strike deals 2d8 slashing damage. In addition, the strong puppet gains a +1 circumstance bonus to AC for 1 round."
  - name: "Swift Puppet"
    desc: "The swift puppet wields two tiny daggers. It makes a melee Strike against a creature whose space it shares at a +15 attack modifier. A successful Strike deals 2d4 piercing damage. If the swift puppet hits a creature that was hit by another puppet this round, its Strike deals an additional 1d4 precision damage. Alternative Puppets This alternate set of villainous puppets Strikes with a +15 attack modifier."
  - name: "Fiend Puppet"
    desc: "The puppet makes a ranged Strike against a creature within 30 feet for 1d10 spirit damage, plus 1d4 spirit damage if the target is holy."
  - name: "Poisoner Puppet"
    desc: "The puppet makes a melee Strike with a tiny syringe of poison against a creature whose space it shares, dealing 1d4 piercing damage plus 1d6 persistent poison damage."
  - name: "Undead Puppet"
    desc: "The puppet makes a melee Strike against a creature whose space it shares, dealing 2d8 void damage and making the target frightened 1 (or frightened 2 on a critical hit)."
sourcebook: "_NPC Core_, page 129."
```

```encounter-table
name: Puppeteer
creatures:
  - 1: Puppeteer
```
