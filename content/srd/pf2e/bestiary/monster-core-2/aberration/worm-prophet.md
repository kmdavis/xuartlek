---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Worm Prophet"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Worm Prophet"
level: 12
source: "Monster Core 2"
aon_id: "creature-4572"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4572"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Worm Prophet"
level: "Creature 12"
size: "Medium"
trait_01: "Aberration"
trait_02: "Swarm"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, tremorsense (imprecise) 30 feet"
languages: "Aklo, Chthonian, Common, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Diplomacy +22, Intimidation +24, Performance +22, Religion +25, Stealth +22"
abilityMods: [5, 2, 4, 3, 7, 6]
abilities_top:
  - name: "Items"
    desc: "silver religious symbol (10), _+1 striking warhammer_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +20; __Ref__: +20; __Will__: +25"
hp: 160
health:
  - name: "HP"
    desc: "160; __Immunities__ precision, swarm mind, unconscious; __Resistances__ physical 10, poison 10, spirit 10; __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Discorporate"
    desc: "When the worm prophet is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the worm prophet can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the worm prophet permanently. The invertebrates have a collective pool of HP, typically equal to 40 HP, and the same AC, saves, immunities, resistances, and weaknesses as the worm prophet. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the worm prophet."
speed: "25 feet, burrow 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _warhammer_ +24 (Shove) __Damage__ 2d8+11 bludgeoning plus clinging remnants"
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, finesse, nonlethal, unarmed) __Damage__ 1d4+1 bludgeoning plus clinging remnants"
abilities_bot:
  - name: "A Thousand Mouths in Prayer"
    desc: "⬻ (Divine, healing) The worm prophet's constituent creatures whisper countless paeans to their gods. The worm prophet attempts to counteract (counteract modifier +24, counteract rank 6) an effect on a creature within 30 feet that's imposing one of the following conditions: blinded, clumsy, dazzled, deafened, enfeebled, frightened, persistent damage, sickened, slowed, or stupefied. Once the worm prophet successfully counteracts an effect in this way, it can't do so again for 1d4 rounds."
  - name: "Clinging Remnants"
    desc: "A worm prophet's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 3d4 persistent piercing damage."
  - name: "Draw Bugs"
    desc: "⬻ (Healing) The worm prophet draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 15 HP. At the GM's discretion, the skittering slayer doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Squirming Embrace"
    desc: "⬻ The worm prophet Strides. If they end their movement sharing a space with a creature, they deal 4d6 piercing damage to the creature, with a DC 32 basic Reflex save. The worm prophet can Burrow instead of Striding."
  - name: "Swarm Shape"
    desc: "⬻ (Concentrate) The worm prophet collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession. In this form, the worm prophet can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to Squeeze. They can use the same action to coalesce from their swarm shape back into their normal form."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ Daze, Detect Magic, Divine Lance, Message, Shield - __4th__ Divine Wrath, Fly, Talking Corpse - __5th__ Crisis of Faith, Heal, Spiritual Guardian - __6th__ Blessed Boundary, Dispel Magic, Vampiric Exsanguination"
sourcebook: "_Monster Core 2_, page 312."
```

```encounter-table
name: Worm Prophet
creatures:
  - 1: Worm Prophet
```
