---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Levaloch"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Levaloch"
level: 7
source: "Monster Core 2"
aon_id: "creature-4327"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4327"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Levaloch"
level: "Creature 7"
size: "Large"
trait_01: "Construct"
trait_02: "Devil"
trait_03: "Fiend"
trait_04: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; greater darkvision"
languages: "Diabolic, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +17, Intimidation +14, Religion +14"
abilityMods: [6, 3, 4, 2, 3, 1]
abilities_top:
  - name: "Hellstrider"
    desc: "A levaloch ignores the effects of non-magical difficult terrain. They take no damage from caltrops or from damaging terrain that deals physical, acid, or cold damage. A levaloch can move through liquids up to 5 feet deep at their full Speed."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +14; __Will__: +12 +1 status to all saves vs. magic"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, fire, healing, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void; __Resistances__ physical 5 (except silver); __Weaknesses__ holy 5"
abilities_mid:
  - name: "Phalanx Fighter"
    desc: "All devils of equal or lower level adjacent to a levaloch gain a +1 circumstance bonus to their AC as the levaloch shields them from harm."
  - name: "Stable Stance"
    desc: "A levaloch gains a +2 circumstance bonus to their Fortitude DC against being Shoved and to other saving throws to resist being moved against their will."
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +19 (Magical, unholy) __Damage__ 2d8+12 piercing plus merciless thrust"
  - name: "Ranged"
    desc: "⬻ _trident_ +16 (Magical, thrown 20 feet, unholy) __Damage__ 2d8+12 piercing"
  - name: "Ranged"
    desc: "⬻ _barbed net_ +16 (Magical, range increment 20 feet) __Damage__ barbed net"
abilities_bot:
  - name: "Barbed Net"
    desc: "When a levaloch hits a creature with their barbed net, the net wraps around the target, which becomes clumsy 1 and takes a –10-foot circumstance penalty to its Speeds. If the Strike was a critical success, the target is also immobilized. When a creature Escapes (DC 22), or if the Strike misses, the net crumbles into rust. Each time a creature attempts to Escape, it takes 1d6 slashing damage from the net's barbs, regardless of whether the attempt succeeds."
  - name: "Forge Weapon"
    desc: "⬻ (Manipulate) A levaloch reforges part of their barbed iron substance into a new _+1 striking trident_ or barbed net. Their previous trident crumbles to rust. When the levaloch is destroyed, any tridents or barbed nets they created crumble to rust."
  - name: "Merciless Thrust"
    desc: "When a levaloch hits a creature that has the clumsy, enfeebled, immobilized, or restrained conditions with a melee trident Strike, the Strike deals an additional 2d6 damage. Hellforged Construct Levalochs are strange amalgamations of devil and automaton, never requiring food or rest. The engravings on their iron plates indicate their hellish allegiance to a certain archdevil, infernal duke, malebranche, or Queen of the Night."
spellcasting:
  - name: "Rituals"
    desc: "DC 22 - __1st__ Diabolic Pact"
sourcebook: "_Monster Core 2_, page 99."
```

```encounter-table
name: Levaloch
creatures:
  - 1: Levaloch
```
