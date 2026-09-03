---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tempest Incarnate"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Tempest Incarnate"
level: 19
source: "NPC Core"
aon_id: "creature-3586"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3586"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tempest Incarnate"
level: "Creature 19"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29"
languages: "Common, Sussuran, Thalassic"
skills:
  - name: "Skills"
    desc: "Acrobatics +35, Intimidation +37, Nature +34, Stealth +35, Survival +31"
abilityMods: [2, 5, 3, 1, 4, 6]
abilities_top:
  - name: "Wind Rider"
    desc: "A tempest incarnate ignores penalties and difficult terrain from strong winds. When flying, they don't need to Fly each round to avoid falling."
  - name: "Items"
    desc: "_+2 greater resilient explorer's clothing_, _+2 greater striking handwraps of mighty blows_"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +30; __Ref__: +34; __Will__: +31"
hp: 360
health:
  - name: "HP"
    desc: "360; __Resistances__ cold 15, electricity 20; __Weaknesses__ earthbound vulnerability"
abilities_mid:
  - name: "Hurricane Cloak"
    desc: "(air, aura, primal) 10 feet. A creature that enters the area must succeed at a DC 38 Athletics check (if on the ground) or Acrobatics check to Maneuver in Flight (if flying) or end its movement. A creature that critically fails is also knocked back 5 feet and falls prone. Creatures making ranged projectile and thrown attacks that pass through the area must succeed on a DC 5 flat check or the attack fails. Massive projectiles, such as thrown boulders, are not affected. A tempest incarnate can activate or deactivate this ability with a single action that has the concentrate trait."
  - name: "Earthbound Vulnerability"
    desc: "A tempest incarnate who is hit by or fails a saving throw against an effect that prevents them from flying (such as _earthbind_ or Felling Strike) takes 20 mental damage in addition to the usual effects."
speed: "25 feet, fly 60 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ _fist_ +32 (Agile, Finesse, Magical, Nonlethal, Unarmed) __Damage__ 3d4+8 bludgeoning plus 3d12 electricity and Push 10 feet"
abilities_bot:
  - name: "Intimidating Storm"
    desc: "(Emotion, Fear, Mental) A creature that fails a saving throw against a _cataclysm_ or _wrathful storm_ spell cast by the tempest incarnate becomes frightened 2 (or frightened 3 on a critical failure). A creature can only be frightened once by each casting of _wrathful storm_."
  - name: "Swiftness"
    desc: "The tempest incarnate's movement doesn't trigger reactions."
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 44, attack +37 - __Cantrips (10th)__ Caustic Blast, Electric Arc, Frostbite, Know the Way, Sigil - __1st__ Air Bubble, Gust of Wind (4 slots) - __2nd__ Mist, Water Breathing - __3rd__ Haste, Wall of Wind (4 slots) - __4th__ Hydraulic Torrent, Unfettered Movement (4 slots) - __5th__ Control Water, Environmental Endurance (4 slots) - __6th__ Field of Life, Truesight (4 slots) - __7th__ Fly, Unfettered Pack (4 slots) - __8th__ Arctic Rift, Chain Lightning (4 slots) - __9th__ Detonate Magic (items that grant flight only), Wrathful Storm (4 slots) - __10th__ Cataclysm (1 slot)"
sourcebook: "_NPC Core_, page 136."
```

```encounter-table
name: Tempest Incarnate
creatures:
  - 1: Tempest Incarnate
```
