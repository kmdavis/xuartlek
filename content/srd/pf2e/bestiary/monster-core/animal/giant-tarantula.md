---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Tarantula"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Tarantula"
level: 6
source: "Monster Core"
aon_id: "creature-3208"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3208"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Tarantula"
level: "Creature 6"
size: "Large"
trait_01: "Animal"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [6, 1, 5, -5, 2, -4]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +13; __Will__: +10"
hp: 135
health:
  - name: "HP"
    desc: "135"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +17 __Damage__ 2d8+8 piercing plus giant tarantula venom"
  - name: "Melee"
    desc: "⬻ leg +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d12+8 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Giant Tarantula Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 23 Fortitude"
  - name: "Maximum Duration"
    desc: "8 rounds"
  - name: "Stage 1"
    desc: "1d10 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d12 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage, clumsy 2, and off-guard (1 round)"
  - name: "Stage 4"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] (1 round)"
  - name: "Hair Barrage"
    desc: "⬺ The tarantula flicks its legs, flinging spiky hairs in a 15-foot cone. This deals 4d6 piercing damage with a DC 25 basic Reflex save."
sourcebook: "_Monster Core_, page 321."
```

```encounter-table
name: Giant Tarantula
creatures:
  - 1: Giant Tarantula
```
