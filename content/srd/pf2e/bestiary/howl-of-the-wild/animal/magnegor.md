---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Magnegor"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Magnegor"
level: 6
source: "Howl of the Wild"
aon_id: "creature-3297"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3297"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Magnegor"
level: "Creature 6"
size: "Huge"
trait_01: "Animal"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision"
skills:
  - name: "Skills"
    desc: "Athletics +15, Intimidation +13, Survival +15"
abilityMods: [5, 2, 4, -4, 2, -2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +17; __Ref__: +11; __Will__: +14"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Metal Allergy"
    desc: "When a magnegor takes damage from a metal weapon or an effect with the metal trait, it takes 5 additional damage and must succeed at a DC 5 flat check or become sickened 1. The value of the sickened condition increases each time the magnegor fails such a check, to a maximum of 3."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +17 (reach 10 feet) __Damage__ 2d8+5 piercing"
abilities_bot:
  - name: "Excavating Spines"
    desc: "(Earth) The magnegor inadvertently digs a 10-foot-deep continuous trench in any square it Wallows through, as long as the ground in that space isn't made of stone, rock, or some other surface too hard to excavate. The trench is greater difficult terrain. At the GM's discretion, any excavated square can reveal a deposit of sedimentary rock filled with metal ore that has Hardness 7 and 28 Hit Points."
  - name: "Magnetized Coat"
    desc: "When a magnegor comes within 30 feet of a metal object or a deposit of metal ore, its thousands of wiry hairs stand on end, pointing towards the metal and creating a magnetic field. Metal items of light or negligible Bulk that touch the magnegor's coat adhere to it magnetically, requiring an Interact action to be pried free. Creatures wearing or primarily composed of metal treat all squares in a 10-foot radius around the magnegor as difficult terrain, unless they are moving directly towards it."
  - name: "Wallow"
    desc: "⬽ (Move)"
  - name: "Requirements"
    desc: "The magnegor is prone"
  - name: "Effect"
    desc: "The magnegor rolls on its spine-covered back, up to its Speed, furrowing the earth and crushing any Large or smaller creatures in its path. This deals 4d10 piercing damage with a DC 24 basic Reflex save; on a failed save, a creature wearing metal armor or made of metal is restrained by the magnegor's magnetized coat (Escape DC 24). For each metal object or piece of equipment a restrained creature chooses to leave stuck to the magnegor, it gains a +1 circumstance bonus to its attempts to Escape. A creature that relinquishes all its metal Escapes automatically. The magnegor can move at its full Speed while it has a creature restrained in this way, bringing the creature along."
sourcebook: "_Howl of the Wild_, page 168."
```

```encounter-table
name: Magnegor
creatures:
  - 1: Magnegor
```
