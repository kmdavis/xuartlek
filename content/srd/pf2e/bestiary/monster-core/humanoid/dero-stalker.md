---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dero Stalker"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/dero
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Dero Stalker"
level: 2
source: "Monster Core"
aon_id: "creature-2902"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2902"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dero Stalker"
level: "Creature 2"
size: "Small"
trait_01: "Dero"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Aklo, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Medicine +5, Stealth +8, Thievery +8"
abilityMods: [2, 4, 3, 0, -1, 1]
abilities_top:
  - name: "Items"
    desc: "Club, cytillesh toolkit (see sidebar), Hand Crossbow (20 bolts), Lethargy Poison (2 doses), Rope (50 feet)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +10; __Will__: +3"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ confused"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A dero stalker takes 4 damage for every hour they're exposed to sunlight."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +8 __Damage__ 1d6+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ club +10 (thrown 10 feet) __Damage__ 1d6+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6 piercing plus lethargy poison"
abilities_bot:
  - name: "Dero Medicine"
    desc: "⬻ (Healing, Manipulate)"
  - name: "Requirements"
    desc: "The dero is wearing a cytillesh toolkit and has a hand free"
  - name: "Effect"
    desc: "The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine."
  - name: "Exploit Lethargy"
    desc: "A creature afflicted with lethargy poison is off-guard to the dero stalker, and the stalker can choose to add the nonlethal trait to their attacks against the creature without taking the normal penalty."
  - name: "Sneak Attack"
    desc: "A dero stalker deals 1d6 extra precision damage to creatures who are off-guard."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Daze, Light, Read Aura"
sourcebook: "_Monster Core_, page 84."
```

```encounter-table
name: Dero Stalker
creatures:
  - 1: Dero Stalker
```
