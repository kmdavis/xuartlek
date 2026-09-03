---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nasurgeth"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Nasurgeth"
level: 20
source: "Monster Core 2"
aon_id: "creature-4313"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4313"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nasurgeth"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Darvakka"
trait_03: "Shadow"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; greater darkvision, lifesense 60 feet"
languages: "Chthonian, Common, Diabolic, Necril; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +36, Athletics +39, Netherworld Lore +36, Religion +36, Stealth +34, Void Lore +36"
abilityMods: [11, 6, 7, 8, 8, 7]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +35; __Ref__: +32; __Will__: +36"
hp: 510
health:
  - name: "HP"
    desc: "510 (void healing); __Immunities__ bleed, cold, death effects, disease, paralyzed, poison, unconscious; __Weaknesses__ holy 15, silver 15"
abilities_mid:
  - name: "Midnight Depths"
    desc: "(aura, cold, darkness, divine, void) 60 feet. A nasurgeth's entropy grows even stronger underwater. All water within the aura is completely dark (as 4th-rank _darkness_). Magical light with a counteract rank of 4th or lower and magical light cantrips are suppressed. A living creature entering or starting its turn in the aura takes 4d6 void damage, and the creature also takes an additional 2d10 cold damage if it's in water (DC 39 basic Fortitude save). If it fails, it's also enfeebled 1 for 1 minute and pulled 10 feet toward the nasurgeth."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is stunned 2 and clumsy 2 as long as it remains in the sunlight."
  - name: "Spray Black Bile"
    desc: "⬲"
  - name: "Trigger"
    desc: "The nasurgeth takes slashing or piercing damage from a critical hit, or a swallowed creature cuts itself free"
  - name: "Effect"
    desc: "Darkness and death energy spill out from the nasurgeth's wound, dealing 8d8 void damage to creatures in a 20-foot emanation with a DC 40 basic Fortitude save."
speed: "fly 60 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +39 (Magical, reach 15 feet) __Damage__ 3d10+19 piercing plus 2d10 cold and Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +39 (Agile, magical, reach 20 feet) __Damage__ 3d6+19 bludgeoning plus 2d10 cold"
abilities_bot:
  - name: "Broken Barb"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is grabbed or restrained in the nasurgeth's jaws"
  - name: "Effect"
    desc: "The nasurgeth breaks a tooth off in the target, who takes 3d10 persistent bleed damage and is no longer grabbed or restrained. If the target is adjacent to a surface, the tooth also pins it in place, making it immobilized (Escape DC 45)."
  - name: "Ravenous Void"
    desc: "⬽ The nasurgeth barrels forward with their mouth open, Swimming twice in a straight line and moving through the spaces of Huge or smaller creatures. The nasurgeth deals the damage of their jaws Strike to each creature whose space they enter (DC 45 basic Reflex save). Any creature that critically fails is automatically Swallowed Whole."
  - name: "Swallow Whole"
    desc: "⬻ Huge, 2d10+9 bludgeoning, Rupture 40. A living creature that ends its turn swallowed whole by a nasurgeth becomes drained 1 or increases its drained condition by 1, and the nasurgeth gains 20 temporary Hit Points that last for 10 minutes . A creature whose drained condition increases to 5 in this way dies."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 43 - __Cantrips (10th)__ Detect Magic - __7th__ Interplanar Teleport (to the Universe; the Void; or the Netherworld only), Truesight - __8th__ Eclipse Burst (×3), Harm (×3)"
sourcebook: "_Monster Core 2_, page 87."
```

```encounter-table
name: Nasurgeth
creatures:
  - 1: Nasurgeth
```
