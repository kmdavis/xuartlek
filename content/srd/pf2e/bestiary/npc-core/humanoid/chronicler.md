---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Chronicler"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Chronicler"
level: 3
source: "NPC Core"
aon_id: "creature-3470"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3470"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Chronicler"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Nature +10, Scribing Lore +13, Society +9, Survival +7, Lore +10"
abilityMods: [2, 2, 1, 3, 4, 0]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Dagger, journal, Leather Armor, maps, _scroll of acid grip_, _scroll of heal_, Staff"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Live to Tell the Tale"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The chronicler would gain the dying condition"
  - name: "Effect"
    desc: "The chronicler instead falls unconscious for 1d4 hours or until they regain 1 Hit Point."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 (Agile, versatile S) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ staff +8 (two-hand d8) __Damage__ 1d4+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +7 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +8 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+5 piercing"
abilities_bot:
  - name: "Scroll Mastery"
    desc: "The chronicler can activate any scroll of a 2nd-rank spell or lower, regardless of its magical tradition."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ Frostbite, Know the Way, Light, Sigil, Tangle Vine - __1st__ Fleet Step, Tailwind, Vanishing Tracks - __2nd__ Entangling Flora, Floating Flame"
sourcebook: "_NPC Core_, page 54."
```

```encounter-table
name: Chronicler
creatures:
  - 1: Chronicler
```
