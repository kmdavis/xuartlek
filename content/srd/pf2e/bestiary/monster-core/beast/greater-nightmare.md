---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Greater Nightmare"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Greater Nightmare"
level: 11
source: "Monster Core"
aon_id: "creature-3106"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3106"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Greater Nightmare"
level: "Creature 11"
size: "Huge"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "Chthonian, Daemonic, Diabolic"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +24, Intimidation +22, Survival +20"
abilityMods: [7, 4, 5, 2, 5, 3]
abilities_top:
  - name: "Smoke"
    desc: "(aura) 15 feet. The nightmare continually exhales black smoke. Creatures within the aura are concealed to those outside it, and creatures outside the aura are concealed to creatures within it. Nightmares and their riders can see through this smoke. A creature that begins its turn in the area must succeed at a DC 28 Fortitude save or be sickened 2. It's then temporarily immune to being sickened by the smoke for 1 minute. This is an inhaled poison, and the nightmare and its rider are immune to it."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +25; __Ref__: +24; __Will__: +21"
hp: 200
health:
  - name: "HP"
    desc: "200; __Resistances__ fire 15"
speed: "60 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 (Magical, Unholy, reach 10 feet) __Damage__ 3d10+13 piercing"
  - name: "Melee"
    desc: "⬻ hoof +24 (Agile, Fire, Magical, Unholy) __Damage__ 2d8+10 bludgeoning plus 2d6 fire"
abilities_bot:
  - name: "Flaming Gallop"
    desc: "⬺ (Divine, Fire, Unholy) The nightmare Strides or Fliesup to triple its Speed. Its hooves burst with intense flame, dealing 6d6 fire damage with a DC 30 basic Reflex save to each creature other than the nightmare's rider that the nightmare moves adjacent to during its gallop. Each creature can be affected only once during a single use of Flaming Gallop."
  - name: "Trample"
    desc: "⬽ Large or smaller, hoof, DC 30"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __7th__ Interplanar Teleport (self and rider only)"
sourcebook: "_Monster Core_, page 238."
```

```encounter-table
name: Greater Nightmare
creatures:
  - 1: Greater Nightmare
```
