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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "Accounting Lore +37, [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +36, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +37, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +34, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +37, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +32, Mercantile Lore +37, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +36"
abilityMods: [9, 9, 8, 10, 5, 5]
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +31; __Ref__: +34; __Will__: +32 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Aura of Disruption"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 120 feet. The dragon radiates disruptive energies that allow them to feed on magic. When a spell is counteracted or disrupted within the aura, the dragon regains one expended spontaneous spell slot and gains 35 temporary Hit Points that last for 1 minute."
  - name: "Capture Spell"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]])"
  - name: "Trigger"
    desc: "The dragon succeeds or critically succeeds on a saving throw against a spell"
  - name: "Effect"
    desc: "The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 10, counteract modifier +37). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "80 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d10+15 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d6+15 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ tail +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 4d10+15 bludgeoning plus 1d6 force"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/force|Force]]) The dragon unleashes a spray of magic-disrupting energies that deals 18d6 force damage in a 60-foot cone (DC 45 basic Reflex save) Creatures that fail become [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Disruptive Breath again for 1d4 rounds."
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
    desc: "The dragon Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrows]] through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 38 Reflex save or be pushed 10 feet (or pushed 20 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] on a critical failure)."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 45, attack +37 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]] - __10th__ [[srd/pf2e/compendium/spells/rank-6/chain-lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-1/force-barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-9/implosion|Implosion]], [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]], [[srd/pf2e/compendium/spells/rank-5/slither|Slither]], [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]], [[srd/pf2e/compendium/spells/rank-7/warp-mind|Warp Mind]] (3 slots)"
sourcebook: "_Monster Core_, page 118."
```

```encounter-table
name: Ancient Fortune Dragon
creatures:
  - 1: Ancient Fortune Dragon
```
