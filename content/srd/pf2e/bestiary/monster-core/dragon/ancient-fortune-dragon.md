---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Fortune Dragon"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Fortune Dragon"
level: 19
source: "Monster Core"
aon_id: "creature-2946"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2946"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Fortune Dragon"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Dwarven, Petran"
skills:
  - name: "Skills"
    desc: "Accounting Lore +37, Acrobatics +36, Arcana +37, Athletics +34, Crafting +37, Diplomacy +32, Mercantile Lore +37, Thievery +36"
abilityMods: [9, 9, 8, 10, 5, 5]
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +31; __Ref__: +34; __Will__: +32 +2 status to all saves vs. arcane"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ drained, paralyzed, sleep"
abilities_mid:
  - name: "Aura of Disruption"
    desc: "(arcane, aura) 120 feet. The dragon radiates disruptive energies that allow them to feed on magic. When a spell is counteracted or disrupted within the aura, the dragon regains one expended spontaneous spell slot and gains 35 temporary Hit Points that last for 1 minute."
  - name: "Capture Spell"
    desc: "⬲ (arcane)"
  - name: "Trigger"
    desc: "The dragon succeeds or critically succeeds on a saving throw against a spell"
  - name: "Effect"
    desc: "The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 10, counteract modifier +37). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "80 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 (Magical, reach 20 feet) __Damage__ 4d10+15 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ claw +34 (Agile, Magical, reach 15 feet) __Damage__ 4d6+15 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ tail +32 (Magical, reach 25 feet) __Damage__ 4d10+15 bludgeoning plus 1d6 force"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "⬺ (Arcane, Force) The dragon unleashes a spray of magic-disrupting energies that deals 18d6 force damage in a 60-foot cone (DC 45 basic Reflex save) Creatures that fail become stupefied 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Disruptive Breath or regain one expended spontaneous spell slot."
  - name: "Drain Hoard"
    desc: "⬻"
  - name: "Requirements"
    desc: "The dragon is within 60 feet of their hoard"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The dragon draws power out of the magic items in their hoard, regaining all their expended spontaneous spell slots."
  - name: "Share the Wealth"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body is covered in riches (this is typically the case when the dragon is first encountered)"
  - name: "Effect"
    desc: "The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing 18d6 bludgeoning damage with a DC 40 basic Reflex save to all creatures in a 50-foot emanation. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body isn't covered in riches and the dragon is adjacent to their hoard"
  - name: "Effect"
    desc: "The dragon Strides or Burrows through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 38 Reflex save or be pushed 10 feet (or pushed 20 feet and knocked prone on a critical failure)."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 45, attack +37 - __Cantrips (10th)__ Detect Magic, Read Aura - __10th__ Chain Lightning, Fireball, Force Barrage, Implosion, Quandary, Slither, Unfettered Movement, Warp Mind (3 slots)"
sourcebook: "_Monster Core_, page 118."
```

```encounter-table
name: Ancient Fortune Dragon
creatures:
  - 1: Ancient Fortune Dragon
```
