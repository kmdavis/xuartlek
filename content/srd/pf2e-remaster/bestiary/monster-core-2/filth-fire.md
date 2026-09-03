---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Filth Fire"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Filth Fire"
level: 4
source: "Monster Core 2"
aon_id: "creature-4387"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4387"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Filth Fire"
level: "Creature 4"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, smoke vision"
languages: "Pyric; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +9"
abilityMods: [1, 5, 4, -2, 3, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +13; __Will__: +9"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ burning lash +13 (Finesse) __Damage__ 2d6+3 bludgeoning plus 1d6 persistent fire"
  - name: "Ranged"
    desc: "⬻ ember ball +13 (Fire, range increment 20 feet) __Damage__ 1d6+3 bludgeoning plus 1d6 persistent fire"
abilities_bot:
  - name: "Noxious Burst"
    desc: "⬺ Toxic materials and churning rubbish within the filth fire's body explode in one of three ways. The filth fire chooses the effect, but it can't make the same choice twice in a row."
  - name: "Fiery Beam"
    desc: "(fire, primal) The filth fire expels a 30-foot line of flame that deals 3d6 fire damage with a DC 21 basic Reflex save."
  - name: "Shrapnel Blast"
    desc: "(primal) The filth fire shoots jagged rubbish out in a 5-foot emanation that deals 2d12 piercing damage with a DC 21 basic Reflex save."
  - name: "Toxic Fumes"
    desc: "(poison, primal) The filth fire belches a 15-foot cone of toxic smoke that deals 2d6 poison damage (DC 21 basic Fortitude save). A creature that fails is also sickened 1 (sickened 2 on a critical failure)."
sourcebook: "_Monster Core 2_, page 148."
```

```encounter-table
name: Filth Fire
creatures:
  - 1: Filth Fire
```
