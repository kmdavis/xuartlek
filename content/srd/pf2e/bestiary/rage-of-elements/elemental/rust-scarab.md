---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rust Scarab"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/large
statblock: inline
name: "Rust Scarab"
level: 5
source: "Rage of Elements"
aon_id: "creature-2648"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2648"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Rust Scarab"
level: "Creature 5"
size: "Large"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, rust vision"
languages: "Talican"
skills:
  - name: "Skills"
    desc: "Athletics +13, Plane of Metal Lore +11"
abilityMods: [6, 2, 5, 2, 2, 2]
abilities_top:
  - name: "Heavy"
    desc: "As long as it is immobile, the elemental can't be forcibly moved or knocked prone. If it takes a move action, it loses this immunity until the start of its next turn."
  - name: "Rust Vision"
    desc: "A rust scarab ignores the concealed condition from rust clouds."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +9; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 5, physical 5 (except adamantine)"
abilities_mid:
  - name: "Crumbling Carapace"
    desc: "When a rust scarab is reduced to fewer than half its maximum Hit Points or is damaged by a critical hit, its outer shell breaks into a veil of rusty metal flakes. This causes it to lose its resistance to physical damage and its heavy ability, but it gains a rust cloud aura (as metal wisp) and a 35-foot land Speed."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 __Damage__ 2d8+6 slashing plus tetanus"
abilities_bot:
  - name: "Tetanus"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Onset"
    desc: "1 week"
  - name: "Stage 1"
    desc: "clumsy 1 (1 week)"
  - name: "Stage 2"
    desc: "clumsy 2 and can't speak (1 day)"
  - name: "Stage 3"
    desc: "paralyzed with spasms (1 day)"
  - name: "Stage 4"
    desc: "death"
  - name: "Trample"
    desc: "⬽ Medium or smaller, claw, DC 23 Ancient Remnants No rust scarab specimens free of deterioration have been documented, leading to debate among scholars as to whether this state of corrosion is their natural condition, or whether the creatures are spectacularly ancient even by the standards of immortal elemental beings."
sourcebook: "_Rage of Elements_, page 155."
```

```encounter-table
name: Rust Scarab
creatures:
  - 1: Rust Scarab
```
