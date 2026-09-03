---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Oregorger"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/large
statblock: inline
name: "Oregorger"
level: 11
source: "Rage of Elements"
aon_id: "creature-2653"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2653"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Oregorger"
level: "Creature 11"
size: "Large"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, rust vision"
languages: "Talican"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +25"
abilityMods: [8, 2, 7, -1, 3, 3]
abilities_top:
  - name: "Rust Vision"
    desc: "An oregorger ignores the concealed condition from rust clouds."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +17; __Will__: +20"
hp: 245
health:
  - name: "HP"
    desc: "245; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ acid 10, electricity 10"
abilities_mid:
  - name: "Caustic Rust"
    desc: "(acid, aura) 5 feet. The oregorger continually leaks tiny fragments of partially digested rust into the air around it. Any creature that ends its turn in the aura takes 2d6 acid damage with a DC 27 basic Reflex save. A creature that critically fails is also sickened 1."
speed: "30 feet, burrow 20 feet, fly 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ adamantine bite +23 (reach 10 feet) __Damage__ 2d12+12 piercing plus devour metal"
  - name: "Melee"
    desc: "⬻ claw +23 (Agile) __Damage__ 2d6+12 slashing"
abilities_bot:
  - name: "Devour Metal"
    desc: "Any time the oregorger scores a critical hit with an adamantine bite attack, it deals the same amount of damage to any metal armor worn by the target, automatically bypassing any Hardness lower than 10. If a creature uses the Shield Block reaction with a metal shield against an oregorger's adamantine bite, the shield is automatically broken, but no other item takes damage from that attack. Unattended metal items automatically take full damage from an oregorger's adamantine bite attack, ignoring their Hardness if it's lower than 10."
  - name: "Searing Spew"
    desc: "⬺ (Acid) The oregorger belches forth a cloud of caustic, rusted debris from its maw, filling a cube adjacent to itself that's 10 feet on each side. Any creature in this area takes 6d6 acid damage and 6d6 slashing damage (DC 30 basic Reflex). The ground under the cloud is difficult terrain for 1 hour, after which the shrapnel crumbles to dust. The oregorger can't use Searing Spew again for 1d4 rounds, but the ability recharges if the oregorger damages an item with devour metal."
sourcebook: "_Rage of Elements_, page 158."
```

```encounter-table
name: Oregorger
creatures:
  - 1: Oregorger
```
