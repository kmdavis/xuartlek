---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Fortune Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Fortune Dragon"
level: 14
source: "Monster Core"
aon_id: "creature-2945"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2945"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Fortune Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Dwarven"
skills:
  - name: "Skills"
    desc: "Accounting Lore +28, Acrobatics +27, Arcana +28, Athletics +27, Crafting +28, Diplomacy +24, Mercantile Lore +28, Thievery +27"
abilityMods: [7, 7, 6, 8, 4, 4]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +27; __Will__: +24 +2 status to all saves vs. arcane"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ drained, paralyzed, sleep"
abilities_mid:
  - name: "Aura of Disruption"
    desc: "(arcane, aura) 120 feet. The dragon radiates disruptive energies that allow them to feed on magic. When a spell is counteracted or disrupted within the aura, the dragon regains one expended spontaneous spell slot and gains 25 temporary Hit Points that last for 1 minute."
  - name: "Capture Spell"
    desc: "⬲ (arcane)"
  - name: "Trigger"
    desc: "The dragon succeeds or critically succeeds on a saving throw against a spell"
  - name: "Effect"
    desc: "The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 7, counteract modifier +28). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "70 feet, fly 140 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 (Magical, reach 15 feet) __Damage__ 3d10+13 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ claw +27 (Agile, Magical, reach 10 feet) __Damage__ 3d6+13 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ tail +25 (Magical, reach 20 feet) __Damage__ 3d10+13 bludgeoning plus 1d6 force"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "⬺ (Arcane, Force) The dragon unleashes a spray of magic-disrupting energies that deals 13d6 force damage in a 40-foot cone (DC 36 basic Reflex save) Creatures that fail become stupefied 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Disruptive Breath or regain one expended spontaneous spell slot."
  - name: "Share the Wealth"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body is covered in riches (this is typically the case when the dragon is first encountered)"
  - name: "Effect"
    desc: "The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing 9d10 bludgeoning damage with a DC 35 basic Reflex save to all creatures in a 40-foot emanation. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body isn't covered in riches and the dragon is adjacent to their hoard"
  - name: "Effect"
    desc: "The dragon Strides or Burrows through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 33 Reflex save or be pushed 10 feet (or pushed 20 feet and knocked prone on a critical failure)."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 36, attack +28 - __Cantrips (7th)__ Detect Magic, Read Aura - __7th__ Chain Lightning, Fireball, Force Barrage, Slither, Unfettered Movement, Warp Mind (2 slots)"
sourcebook: "_Monster Core_, page 118."
```

```encounter-table
name: Adult Fortune Dragon
creatures:
  - 1: Adult Fortune Dragon
```
