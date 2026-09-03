---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phistophilus"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Phistophilus"
level: 10
source: "Monster Core"
aon_id: "creature-2909"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2909"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phistophilus"
level: "Creature 10"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; greater darkvision"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Empyrean, Sakvroth; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +19, Deception +23, Diplomacy +21, Intimidation +21, Legal Lore +25, Religion +19, Society +19, Stealth +18, Athletics +19"
abilityMods: [3, 4, 4, 7, 5, 5]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +18; __Will__: +23 +1 status to all saves vs. magic"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ fire, ward contract; __Resistances__ physical 10 (except silver), poison 10; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Ward Contract"
    desc: "A signed contract carried by a living contract devil (including draped over their horns) is immune to damage from all creatures other than that contract devil. A contract devil is immune to mental effects that would make them destroy, nullify, or alter a contract."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ binding contract +23 (Agile, Disarm, Magical, reach 10 feet, Trip, Unholy) __Damage__ 3d6+11 slashing plus Grab and infernal wound"
  - name: "Melee"
    desc: "⬻ horn +21 (Magical) __Damage__ 3d10+11 piercing plus infernal wound"
abilities_bot:
  - name: "Draft Contract"
    desc: "⬽ (Divine, Manipulate) The contract devil produces an infernal contract for a single living mortal. This contract can grant a wide range of abilities and effects, akin to the power of a _wish_ ritual but fulfilled to the letter by the contract devil. To receive any of those benefits, the mortal must willingly sign its true name to the contract. At that point, the mortal's soul is bound to the contract devil and Hell. While the contract is in effect, the victim can't be restored to life except by _wish_ or similar magic. If the mortal is restored to life by those means, the contract devil knows which mortal came to life and can locate the creature or creatures who restored the mortal to life for 1 year, gaining the effects of a _locate_ spell with unlimited range. Avoiding the terms of an infernal contract is difficult and often dangerous."
  - name: "Infernal Investment"
    desc: "A contract devil can cast a 10th-rank innate _scrying_ spell at will, but only to target a creature with which they have a contract. The target automatically critically fails its save."
  - name: "Infernal Wound"
    desc: "(Divine) The wounds from a contract devil's Strikes resist healing. A spellcaster or item attempting to use healing magic on a creature suffering first attempts to counteract infernal wound (DC 29). If it is not counteracted, the healing has no effect. Infernal Contracts The diabolic contracts created by contract devils are not the only ways a devil can engage a mortal in a binding agreement, but they are the most convenient. Other devils must perform complex rituals or jump through bureaucratic hoops to organize a contract with a mortal, and in most cases the easiest solution for devils in this situation is to simply enlist the aid of a contract devil"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31 - __Cantrips (7th)__ Detect Magic - __3rd__ Mind Reading (at will) - __4th__ Peaceful Bubble, Silence, Translocate (at will) - __5th__ Fireball, Illusory Scene, Lightning Bolt, Locate (at will), Mind Probe, Sending (at will), Translocate - __7th__ Interplanar Teleport - __10th__ Scrying (at will; see infernal investment) - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 31 - __1st__ Diabolic Pact"
sourcebook: "_Monster Core_, page 90."
```

```encounter-table
name: Phistophilus
creatures:
  - 1: Phistophilus
```
