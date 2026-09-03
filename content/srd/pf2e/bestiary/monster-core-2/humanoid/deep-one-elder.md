---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deep One Elder"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Deep One Elder"
level: 14
source: "Monster Core 2"
aon_id: "creature-4316"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4316"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Deep One Elder"
level: "Creature 14"
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, wavesense 120 feet"
languages: "Aklo, Common"
skills:
  - name: "Skills"
    desc: "Athletics +31, Dagon Lore +24, Intimidation +24, Ocean Lore +24, Religion +27, Survival +25"
abilityMods: [9, 4, 8, 6, 5, 4]
abilities_top:
  - name: "Pressurized"
    desc: "A deep one elder is immune to damage and other negative effects from changes in water pressure."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +22; __Will__: +26"
hp: 260
health:
  - name: "HP"
    desc: "260 , regeneration 10 (deactivated by fire); __Immunities__ cold; __Resistances__ acid 10, piercing 15"
abilities_mid:
  - name: "Endless"
    desc: "A deep one elder doesn't age and is immune to spells and other effects that inflict magical aging. Unless killed, a deep one elder lives forever."
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 31. A creature that fails its save is also slowed 1 (slowed 2 on a critical failure)."
  - name: "Mental Mirror"
    desc: "Mental effects that fail against a deep one elder are reflected back onto the source, as _spell riposte_."
speed: "30 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ foot +29 (Magical, reach 20 feet, unholy) __Damage__ 3d12+15 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +29 (Agile, magical, reach 20 feet, sweep, unholy) __Damage__ 3d10+12 slashing plus Improved Knockdown and devastation"
abilities_bot:
  - name: "Devastation"
    desc: "A deep one elder's claw Strikes ignore the first 10 Hardness of an object. Additionally, on a critical hit, the target must succeed at a DC 34 Fortitude save or be stunned 2."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 31. The deep one can Swim up to double its swim Speed instead of Striding."
  - name: "Watery Void"
    desc: "⬽ (Concentrate, manipulate, occult, void, water) The deep one elder makes an endless void of water appear in a 20-foot burst within 60 feet, dragging creatures down into its whirlpool. If cast underwater, the watery void fills a 60-foot-tall cylinder with a 20-foot radius. Creatures in the area when the void appears and creatures that end their turn in the area take 3d8 bludgeoning damage and 3d8 void damage and must attempt a DC 31 Reflex save. The void remains until the end of the deep one elder's next turn. The deep one elder can Sustain the void to extend the duration by 1 round, up to a total of 4 rounds, and can move the void up to 15 feet. Once the effect ends, the elder can't use Watery Void again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage and a –5-foot circumstance penalty to their Speeds while in the void."
  - name: "Failure"
    desc: "The creature takes full damage and a –10-foot circumstance penalty to their Speeds while in the void."
  - name: "Critical Success"
    desc: "The creature takes double damage, is knocked prone, and takes a –10-foot circumstance penalty to their Speeds while in the void."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 31, attack +23 - __4th__ Unfettered Movement - __5th__ Wave of Despair - __6th__ Blinding Fury, Phantasmal Calamity - __7th__ Warp Mind (×3)"
sourcebook: "_Monster Core 2_, page 89."
```

```encounter-table
name: Deep One Elder
creatures:
  - 1: Deep One Elder
```
