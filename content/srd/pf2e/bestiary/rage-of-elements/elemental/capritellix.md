---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Capritellix"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Capritellix"
level: 17
source: "Rage of Elements"
aon_id: "creature-2641"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2641"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Capritellix"
level: "Creature 17"
size: "Huge"
trait_01: "Elemental"
trait_02: "Metal"
trait_03: "Rare"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision"
languages: "Talican; plus one language for each of their mouths; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +31, Athletics +29, Deception +32, Diplomacy +32, Intimidation +32, Performance +32, Plane of Metal Lore +30, Society +30"
abilityMods: [6, 8, 8, 7, 5, 9]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +31; __Ref__: +29; __Will__: +30"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 10, physical 10 (except adamantine)"
abilities_mid:
  - name: "Whirling Hands"
    desc: "⭓"
  - name: "Trigger"
    desc: "A creature starts its turn in the capritellix's melee reach"
  - name: "Effect"
    desc: "The capritellix makes a metal hand Strike against the creature."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ metal hand +33 (Agile, Finesse, Magical, reach 15 feet) __Damage__ 3d8+14 bludgeoning plus 1d12 electricity, plentiful metals, and Push 20 feet"
  - name: "Ranged"
    desc: "⬻ eye beam +33 (Electricity, Magical, range 120 feet) __Damage__ 4d12 electricity"
abilities_bot:
  - name: "Dual Beams"
    desc: "⬺ The capritellix makes two eye beam Strikes against different creatures. Their multiple attack penalty doesn't increase until after both Strikes."
  - name: "Plentiful Metals"
    desc: "Each of the capritellix's levitating hands is made of a different precious metal. Each time a capritellix makes a metal hand Strike, they choose whether the hand they use is adamantine, cold iron, dawnsilver, orichalcum, silver, or any other solid precious metal."
  - name: "Shift Mood"
    desc: "⬻ The capritellix rotates the segments of their face, changing their personality and demeanor. Until they Shift their Mood again, the capritellix gains a +4 status bonus to a certain skill and to their Will DC against that skill, as well as a specific occult innate spell they can cast at will (9th rank, DC 38)."
  - name: "Angry"
    desc: "Intimidation, _dominate_"
  - name: "Gregarious"
    desc: "Performance, _uncontrollable dance_"
  - name: "Serene"
    desc: "Diplomacy, _suggestion_"
  - name: "Sly"
    desc: "Deception, _warp mind_ Recycled Remains When horribly damaged or weary, capritellixes travel to a communal necropolis, much like a fabled elephant graveyard. Thousands of metallic hands reach up from the landscape, clawing at the sky, and severed discs that used to make up capritellixes pile up in endless heaps. Other elementals sometimes salvage these disparate parts and assemble them into a new capritellix—a unique individual with a brand-new identity."
sourcebook: "_Rage of Elements_, page 151."
```

```encounter-table
name: Capritellix
creatures:
  - 1: Capritellix
```
