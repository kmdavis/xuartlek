---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leprechaun"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Leprechaun"
level: 2
source: "Monster Core 2"
aon_id: "creature-4463"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4463"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Leprechaun"
level: "Creature 2"
size: "Small"
trait_01: "Fey"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Deception +9, Gold Lore +7, Nature +7, Performance +9, Thievery +8"
abilityMods: [1, 4, 1, 3, 3, 4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +11; __Will__: +10"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +7 __Damage__ 1d6+3 bludgeoning"
abilities_bot:
  - name: "Create Object"
    desc: "⬺ (Manipulate, primal)"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The leprechaun produces an item out of their hat, from behind their jacket, from within a hole in a tree stump, or from any other unexpected location. This conjured item must be no more than 1 Bulk and must be made of relatively commonplace material (such as cloth, wood, stone, or even low-value metal like iron or lead). It can't rely on intricate artistry or complex moving parts, never fulfills a Cost or the like, and can't be made of precious materials or materials with a rarity of uncommon or higher. The created object is temporary and lasts for 1 hour or until the leprechaun creates a new item, whichever comes first."
  - name: "Leprechaun Magic"
    desc: "Leprechauns love to use their magic to beguile others, and after generations of doing so, they've developed a strong connection to such tricks. When a leprechaun uses their innate spells to deceive, trick, or humiliate a creature, the spell DC increases to 20 and the attack modifier to +12. Pots Of Gold While it's true that leprechauns typically return items they steal, they particularly love gold and often hoard gold coins and treasures in pots tucked away in hidden places. It's rumored that a person who finds a gold coin in the forest and returns it to the leprechaun who dropped it will be granted a wish as a reward. Unfortunately, this rumor is false—a deception perpetrated by leprechauns to trick others into bringing them even more gold for their pots."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18, attack +10 - __Cantrips (2nd)__ Figment, Light, Prestidigitation, Telekinetic Hand, Telekinetic Projectile - __1st__ Runic Weapon, Vanishing Tracks, Ventriloquism - __2nd__ Illusory Creature, Illusory Object, Invisibility (self only)"
sourcebook: "_Monster Core 2_, page 213."
```

```encounter-table
name: Leprechaun
creatures:
  - 1: Leprechaun
```
