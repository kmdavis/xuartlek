---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stone Bulwark"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Stone Bulwark"
level: 11
source: "Monster Core"
aon_id: "creature-3213"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3213"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Stone Bulwark"
level: "Creature 11"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +26"
abilityMods: [7, -1, 4, -5, 0, -5]
abilities_top:
  - name: "Serpentstone Breath"
    desc: "⬺ (earth, incapacitation, primal) The bulwark breathes a 60- foot cone of green gas. Each creature in the area must attempt a DC 34 Fortitude save. The bulwark can't use Serpentstone Breath again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature's body hardens, causing it to become slowed 1 for 1 round."
  - name: "Failure"
    desc: "The creature becomes petrified for 1 minute. It can attempt a new save at the end of each of its turns."
  - name: "Critical Failure"
    desc: "The creature becomes petrified permanently."
  - name: "Recall Knowledge - Construct"
    desc: "(Arcana, Crafting): DC 30"
  - name: "Unspecific Lore"
    desc: ": DC 28"
  - name: "Specific Lore"
    desc: ": DC 25 Stone Bulwark Uncommon Large Construct Mindless"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +18; __Will__: +19"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Resistances__ physical 10 (except adamantine), spells 10 (except cold, earth, or water)"
abilities_mid:
  - name: "Statuary Aura"
    desc: "(arcane, aura, earth) 20 feet. Rocks of marble magically arise from the ground in the aura. They protect the bulwark's allies, giving each of them standard cover. These stones can be used for Throw Rock. This aura automatically activates at the start of the stone bulwark's first turn in combat and deactivates at the end of combat."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 (Magical, reach 10 feet) __Damage__ 2d10+13 bludgeoning and binding stone"
  - name: "Ranged"
    desc: "⬻ rock +22 (Brutal, Magical, range increment 120 feet) __Damage__ 2d6+11 bludgeoning and binding stone"
abilities_bot:
  - name: "Binding Stone"
    desc: "(Arcane, Earth) Any creature hit by the stone bulwark's fist or rock Strike is affected by a DC 30 _earthbind_ spell."
  - name: "Inexorable March"
    desc: "⬻ The stone bulwark Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can attempt to bar the way by succeeding at a DC 34 Fortitude save. On a critical success, the resisting creature takes no damage; otherwise it is damaged as if hit by the construct's fist."
  - name: "Throw Rock"
    desc: "⬻ Stone Slabs Depending on the material from which it is made and the care that went into crafting it, a destroyed stone bulwark may be worth as much as an immaculately sculpted marble pillar or as little as a pile of rubble."
sourcebook: "_Monster Core_, page 324."
```

```encounter-table
name: Stone Bulwark
creatures:
  - 1: Stone Bulwark
```
