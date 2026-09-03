---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mix Coatl"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/coatl
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
  - pf2e/creature/trait/couatl
statblock: inline
name: "Mix Coatl"
level: 8
source: "Monster Core 2"
aon_id: "creature-4298"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4298"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mix Coatl"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Coatl"
trait_03: "Holy"
trait_04: "Uncommon"
trait_05: "Couatl"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Common, Draconic, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Arcana +18, Athletics +18, Diplomacy +20, Nature +21, Occultism +18, Society +16, Stealth +17, Survival +15"
abilityMods: [6, 3, 4, 4, 5, 4]
abilities_top:
  - name: "Star Child"
    desc: "The mix coatl is difficult to discern against starry skies. They can Hide in the air at night without cover or concealment."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +14; __Ref__: +15; __Will__: +19"
hp: 135
health:
  - name: "HP"
    desc: "135"
speed: "15 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (Magical) __Damage__ 2d10+9 piercing plus mix coatl venom and Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d10+4 bludgeoning, DC 26"
  - name: "Gift of Knowledge"
    desc: "When a mix coatl casts _rewrite memory_ on a willing creature, the mix coatl can Sustain the spell to rewrite these memories for up to 60 continuous minutes. A mix coatl can grant knowledge of a particular skill to the target as part of the spell. The mix coatl chooses Engineering Lore, Farming Lore, Fishing Lore, Hunting Lore, or Mercantile Lore. The target becomes permanently trained in the chosen skill. A creature can benefit from Gift of Knowledge only once."
  - name: "Mix Coatl Venom"
    desc: "(Holy, poison) To unholy creatures, this is a curse instead of a poison and deals spirit damage instead of poison damage"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage, stunned 1, and stupefied 1 (1 round)"
  - name: "Stage 3"
    desc: "2d8 poison damage, stunned 1, and stupefied 2 (1 round)"
  - name: "Wrap in Coils"
    desc: "⬻"
  - name: "Requirements"
    desc: "The mix coatl has a Medium or smaller creature grabbed or restrained in their jaws"
  - name: "Effect"
    desc: "The mix coatl moves the creature into their coils, freeing their jaws to make attacks, and then uses Constrict against the creature. The mix coatl can hold as many creatures in their coils as will fit in their space."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ Guidance, Light, Ignition, Stabilize - __1st__ Create Water, Mending - __2nd__ Invisibility (self only), Speak with Animals - __3rd__ Heal, Mind Reading (at will) - __4th__ Fireball, Speak with Plants - __6th__ Rewrite Memory (at will) - __7th__ Interplanar Teleport (self only)"
sourcebook: "_Monster Core 2_, page 74."
```

```encounter-table
name: Mix Coatl
creatures:
  - 1: Mix Coatl
```
