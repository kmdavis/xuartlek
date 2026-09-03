---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urveth"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Urveth"
level: 18
source: "Monster Core 2"
aon_id: "creature-4312"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4312"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urveth"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; greater darkvision, lifesense 60 feet"
languages: "Chthonian, Common, Diabolic, Necril; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +29, Athletics +35, Netherworld Lore +31, Religion +32, Stealth +31, Void Lore +31"
abilityMods: [10, 5, 8, 5, 6, 6]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +32; __Ref__: +29; __Will__: +34"
hp: 460
health:
  - name: "HP"
    desc: "460 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 15; __Weaknesses__ holy 15, silver 15"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "(aura, divine, void) 60 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 5d6 void damage with a DC 38 basic Fortitude save. If it fails, it's also enfeebled 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is stunned 2 and clumsy 2 as long as it remains in the sunlight."
  - name: "Reactive Strike"
    desc: "⬲ claw only. An urveth gains 3 extra reactions each round that they can use only to make Reactive Strikes."
speed: "25 feet, burrow 60 feet, fly"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +36 (Magical, reach 15 feet) __Damage__ 3d10+14 slashing plus 2d10 cold and Improved Grab"
  - name: "Melee"
    desc: "⬻ claw +36 (Agile, magical, reach 15 feet) __Damage__ 3d6+14 slashing plus 2d10 cold"
  - name: "Melee"
    desc: "⬻ stinger +36 (Poison, magical, reach 20 feet) __Damage__ 3d6+14 piercing plus 2d10 cold and urveth venom"
abilities_bot:
  - name: "Frenzy"
    desc: "⬺ The urveth makes two claw Strikes and one stinger Strike in any order."
  - name: "Swallow Whole"
    desc: "⬻ Huge, 2d10+5 bludgeoning, Rupture 35. A living creature that ends its turn swallowed whole by an urveth becomes drained 1 or increases its drained condition by 1, and the urveth gains 10 temporary Hit Points. A creature whose drained condition increases to 5 in this way dies."
  - name: "Urveth Venom"
    desc: "(Poison) Saving Throw DC 37 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 void damage and 2d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "3d6 void damage, 2d6 poison damage, and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "3d6 void damage, 2d6 poison damage, and enfeebled 4 (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40 - __Cantrips (9th)__ Detect Magic - __4th__ Darkness (at will) - __8th__ Harm (×3), Eclipse Burst, Interplanar Teleport (to the Universe; the Void; or the Netherworld only), Truesight - __Constant (9th)__ Fly"
sourcebook: "_Monster Core 2_, page 86."
```

```encounter-table
name: Urveth
creatures:
  - 1: Urveth
```
