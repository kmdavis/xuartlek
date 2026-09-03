---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zyss Serpentfolk"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Zyss Serpentfolk"
level: 2
source: "Monster Core"
aon_id: "creature-3181"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3181"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zyss Serpentfolk"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
trait_03: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "Aklo, Common, Sakvroth; telepathy 00 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Arcana +8, Deception +9, Occultism +8, Society +8"
abilityMods: [-1, 4, -2, 4, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, Shortbow (30 arrows)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +4; __Ref__: +8; __Will__: +8 (+4 status vs. mental) +1 status to all saves vs. magic"
hp: 25
health:
  - name: "HP"
    desc: "25; __Resistances__ poison 5"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Zyss serpentfolk recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +10 (Finesse) __Damage__ 1d6+1 piercing plus serpentfolk venom"
  - name: "Melee"
    desc: "⬻ dagger +10 (Agile, Finesse, versatile S) __Damage__ 1d4+1 piercing plus serpentfolk venom"
  - name: "Ranged"
    desc: "⬻ shortbow +10 (deadly d10, range increment 60 feet) __Damage__ 1d6+2 piercing plus serpentfolk venom"
abilities_bot:
  - name: "Serpentfolk Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 18 - __1st__ Illusory Disguise (at will), Ventriloquism (at will) - __2nd__ Blur (self only; at will) - __4th__ Suggestion"
sourcebook: "_Monster Core_, page 302."
```

```encounter-table
name: Zyss Serpentfolk
creatures:
  - 1: Zyss Serpentfolk
```
