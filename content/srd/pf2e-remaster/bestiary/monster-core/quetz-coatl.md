---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Quetz Coatl"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/coatl
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
  - pf2e/creature/trait/couatl
statblock: inline
name: "Quetz Coatl"
level: 10
source: "Monster Core"
aon_id: "creature-2882"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2882"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Quetz Coatl"
level: "Creature 10"
size: "Large"
trait_01: "Beast"
trait_02: "Coatl"
trait_03: "Holy"
trait_04: "Uncommon"
trait_05: "Couatl"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Common, Empyrean, Sussuran, Utopian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Arcana +19, Athletics +19, Diplomacy +22, Nature +22, Occultism +19, Religion +22, Survival +16"
abilityMods: [7, 3, 5, 6, 5, 5]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +19; __Ref__: +19; __Will__: +21"
hp: 175
health:
  - name: "HP"
    desc: "175"
speed: "15 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 (Holy, Magical) __Damage__ 2d10+13 piercing plus quetz coatl venom and Grab"
abilities_bot:
  - name: "Greater Constrict"
    desc: "⬻ 2d10+7 bludgeoning, DC 29"
  - name: "Quetz Coatl Venom"
    desc: "(Holy, Poison) To unholy creatures, this is a curse instead of a poison and deals spirit damage instead of poison damage"
  - name: "Saving Throw"
    desc: "DC 29 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d8 poison damage, enfeebled 1, and off-guard (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison damage, enfeebled 2, and off-guard (1 round)"
  - name: "Radiant Wings"
    desc: "⬺ (Divine, Incapacitation, Light, Mental, Visual) The quetz coatl spreads their multicolored wings and radiant plumage. Each enemy in a 30-foot emanation must attempt a DC 29 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to Radiant Wings for 24 hours."
  - name: "Success"
    desc: "The creature is dazzled for 1 round."
  - name: "Failure"
    desc: "The creature is dazzled for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, plus if the creature is unholy, it is also stunned 3."
  - name: "Wrap in Coils"
    desc: "⬻"
  - name: "Requirements"
    desc: "The quetz coatl has a Medium or smaller creature grabbed or restrained in its jaws"
  - name: "Effect"
    desc: "The quetz coatl moves the creature into its coils, freeing its fangs to make attacks, then uses Greater Constrict against the creature. The quetz coatl can hold as many creatures in its coils as will fit in its space."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ Light, Telekinetic Hand, Vitality Lash - __3rd__ Mind Reading (at will) - __4th__ Charm, Vapor Form - __5th__ Breath of Life, Cleanse Affliction, Divine Wrath - __7th__ Interplanar Teleport (self only)"
sourcebook: "_Monster Core_, page 65."
```

```encounter-table
name: Quetz Coatl
creatures:
  - 1: Quetz Coatl
```
