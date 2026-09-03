---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Girtablilu Seer"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/girtablilu
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Girtablilu Seer"
level: 12
source: "Monster Core 2"
aon_id: "creature-4414"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4414"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Girtablilu Seer"
level: "Creature 12"
size: "Large"
trait_01: "Beast"
trait_02: "Girtablilu"
trait_03: "Humanoid"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, tremorsense (imprecise) 60 feet"
languages: "Common, Girtablilu"
skills:
  - name: "Skills"
    desc: "Athletics +25, Intimidation +23, Religion +25, Survival +23"
abilityMods: [6, 5, 6, 3, 7, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 resilient hide armor_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +19; __Will__: +25"
hp: 210
health:
  - name: "HP"
    desc: "210"
abilities_mid:
  - name: "Divine Aegis"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "The girtablilu seer attempts a saving throw against a magical effect but hasn't rolled yet"
  - name: "Effect"
    desc: "The seer summons divine energy to protect themself at the cost of their other magical defenses. Until the start of their next turn, they gain a +1 circumstance bonus to saving throws against non-divine magical effects and a –1 circumstance penalty to saves against divine effects."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +24 (Agile, unarmed) __Damage__ 3d8+12 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +24 (reach 10 feet, unarmed) __Damage__ 3d6+12 piercing plus girtablilu venom"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d8+6 bludgeoning, DC 30"
  - name: "Desert Passage"
    desc: "A girtablilu ignores natural difficult terrain in the desert."
  - name: "Girtablilu Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 30 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 3"
    desc: "3d6 poison damage and enfeebled 2 (1 round)"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 33 - __Cantrips (6th)__ Daze, Detect Magic, Forbidding Ward, Guidance, Read Aura - __1st__ Cleanse Cuisine, Create Water, Sanctuary (3 slots) - __2nd__ Augury, Calm, Create Food (3 slots) - __3rd__ Dream Message, Anointed Ground, Slow (3 slots) - __4th__ Cleanse Affliction, Outcast's Curse, Unfettered Movement (3 slots) - __5th__ Cleanse Affliction, Divine Wrath, Harm (3 slots) - __6th__ Blessed Boundary, Heal, Spirit Blast (3 slots)"
sourcebook: "_Monster Core 2_, page 167."
```

```encounter-table
name: Girtablilu Seer
creatures:
  - 1: Girtablilu Seer
```
