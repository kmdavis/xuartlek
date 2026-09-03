---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hryngar Sharpshooter"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/hryngar
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/duergar
statblock: inline
name: "Hryngar Sharpshooter"
level: 0
source: "Monster Core"
aon_id: "creature-3061"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3061"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hryngar Sharpshooter"
level: "Creature 0"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Hryngar"
trait_03: "Humanoid"
trait_04: "Duergar"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision"
languages: "Common, Dwarven, Sakvroth"
skills:
  - name: "Skills"
    desc: "Athletics +3, Stealth +5"
abilityMods: [1, 3, 3, 0, 2, -2]
abilities_top:
  - name: "Items"
    desc: "Chain Shirt, Crossbow (3 bola bolts and 10 bolts), Light Mace"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +7; __Will__: +4 +2 status to saves vs. magic"
hp: 18
health:
  - name: "HP"
    desc: "18"
abilities_mid:
  - name: "Light Blindness"
    desc: ""
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light mace +5 (Agile, Finesse, Shove) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +7 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing or bola bolt"
abilities_bot:
  - name: "Bola Bolt"
    desc: "This shot deals no damage, but on a hit, the target must succeed at a DC 16 Reflex save or be knocked prone and become immobilized until it is freed with a successful DC 15 check to Escape. This check can be attempted either by the target or a creature adjacent to the target."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 12 - __Cantrips (1st)__ Sigil - __2nd__ Blood Vendetta, Paranoia"
sourcebook: "_Monster Core_, page 202."
```

```encounter-table
name: Hryngar Sharpshooter
creatures:
  - 1: Hryngar Sharpshooter
```
