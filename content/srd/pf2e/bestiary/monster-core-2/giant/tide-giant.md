---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tide Giant"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Tide Giant"
level: 13
source: "Monster Core 2"
aon_id: "creature-4412"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4412"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tide Giant"
level: "Creature 13"
size: "Large"
trait_01: "Amphibious"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Water"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; low-light vision"
languages: "Common, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +27, Nature +21, Survival +23"
abilityMods: [8, 6, 6, 0, 4, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 striking returning trident_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +25; __Will__: +21"
hp: 250
health:
  - name: "HP"
    desc: "250; __Resistances__ fire 10"
abilities_mid:
  - name: "Cloak of High Tide"
    desc: "(aura, primal, water) 10 feet. Elemental water magic ebbs and flows into a tide giant. At the start of each of the giant's turns in combat, their cloak of high tide automatically activates if it's inactive or ends if it's already active. Any creature other than a tide giant that enters or starts its turn in the aura while it's active regains 5 HP; this is a healing vitality effect, and a creature can benefit from it only once per round. When active, the cloak appears as a magical, flowing cloak of seafoam that billows from the tidal giant's shoulders and the back of their limbs. The cloak is inactive when the tide giant isn't in combat."
speed: "30 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trident +28 (Magical, reach 10 feet) __Damage__ 2d8+14 piercing"
  - name: "Melee"
    desc: "⬻ fist +27 (Agile, nonlethal, reach 10 feet, unarmed) __Damage__ 2d4+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ trident +26 (Magical, thrown 20 feet) __Damage__ 2d8+14 piercing"
abilities_bot:
  - name: "Blood Tide"
    desc: "⬺ (Primal, water) The tide giant Swims, or Swims twice if their cloak of high tide is active. Holding out their trident, they slash those they pass, dealing 2d8 piercing damage and 2d6 persistent bleed damage (DC 24 basic Reflex save) to each enemy the giant moves within 10 feet of during their movement. Each creature can be affected only once during a single use of Blood Tide."
  - name: "Tine and Tide"
    desc: "⬺ (Primal, water) A wave blasts from the giant's trident in a 15-foot cone or a 5-foot burst within 100 feet. If the giant's cloak of high tide is active, this is a 30-foot cone or a 10-foot burst. Each creature in the area takes 9d8 bludgeoning damage with a DC 33 basic Reflex save. On The Beach Despite being able to dwell entirely underwater, tide giants favor building their homes near beaches to advantageously use land and sea as they wish. Their bungalows are open to the elements. They’re also quite cluttered, with treasures that washed ashore heaped in disorganized piles of driftwood, fish skeletons, seashells, broken bottles, and more."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33 - __5th__ Control Water"
sourcebook: "_Monster Core 2_, page 165."
```

```encounter-table
name: Tide Giant
creatures:
  - 1: Tide Giant
```
