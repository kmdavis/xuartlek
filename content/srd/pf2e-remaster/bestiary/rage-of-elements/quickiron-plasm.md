---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Quickiron Plasm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/large
statblock: inline
name: "Quickiron Plasm"
level: 4
source: "Rage of Elements"
aon_id: "creature-2647"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2647"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Quickiron Plasm"
level: "Creature 4"
size: "Large"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, magic scent"
skills:
  - name: "Skills"
    desc: "Athletics +12, Stealth +10"
abilityMods: [6, 2, 5, -4, 0, -2]
abilities_top:
  - name: "Magic Scent"
    desc: "The quickiron plasm can sense magical auras from up to 1 mile away as an imprecise sense."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +8; __Will__: +10"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ critical hits, bleed, paralyzed, poison, precision, sleep; __Resistances__ electricity 5"
abilities_mid:
  - name: "Biomagical Feedback"
    desc: "The quickiron plasm's conductive properties are dangerous to those in physical contact with it. When a creature grabbed by a quickiron plasm Casts a Spell, that creature takes 5 force damage per rank of the spell."
  - name: "Consume Magic"
    desc: "⬲"
  - name: "Trigger"
    desc: "The quickiron plasm succeeds at a saving throw against a spell"
  - name: "Effect"
    desc: "The quickiron plasm consumes energy from the spell, regaining 5 Hit Points per rank of the spell."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +12 (reach 10 feet) __Damage__ 2d6+6 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d6 bludgeoning, DC 22 Djezet Extraction When a quickiron plasm dies, most of the djezet making up its body becomes inert and useless. However, a skilled alchemist can sometimes extract trace amounts of the valuable skymetal from its remains. This is a 10-minute process that requires the Alchemical Crafting feat, a proficiency rank of expert or better in Crafting, and a successful DC 20 Crafting check. A successful attempt produces a single _djezet dose_ that remains potent for 1 hour before breaking down into a foul-smelling goo. The item has no value if sold due to its temporary nature."
sourcebook: "_Rage of Elements_, page 154."
```

```encounter-table
name: Quickiron Plasm
creatures:
  - 1: Quickiron Plasm
```
