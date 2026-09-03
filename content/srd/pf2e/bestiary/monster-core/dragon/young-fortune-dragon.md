---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Fortune Dragon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Fortune Dragon"
level: 10
source: "Monster Core"
aon_id: "creature-2944"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2944"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Fortune Dragon"
level: "Creature 10"
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "Accounting Lore +22, [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +19, Mercantile Lore +22, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +21"
abilityMods: [5, 5, 4, 6, 3, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +21; __Will__: +19 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Capture Spell"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]])"
  - name: "Trigger"
    desc: "The dragon succeeds or critically succeeds on a saving throw against a spell"
  - name: "Effect"
    desc: "The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 5, counteract modifier +20). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "60 feet, fly 100 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+11 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d6+11 piercing plus 1d6 force"
  - name: "Melee"
    desc: "⬻ tail +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+11 bludgeoning plus 1d6 force"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/force|Force]]) The dragon unleashes a spray of magic-disrupting energies that deals 9d6 force damage in a 30-foot cone (DC 30 basic Reflex save) Creatures that fail become [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Disruptive Breath or regain one expended spontaneous spell slot."
  - name: "Share the Wealth"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body is covered in riches (this is typically the case when the dragon is first encountered)"
  - name: "Effect"
    desc: "The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing 6d10 bludgeoning damage with a DC 29 basic Reflex save to all creatures in a 30-foot emanation. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon's body isn't covered in riches and the dragon is adjacent to their hoard"
  - name: "Effect"
    desc: "The dragon Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrows]] through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 27 Reflex save or be pushed 10 feet (or pushed 20 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] on a critical failure)."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 30, attack +22 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-1/force-barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-5/slither|Slither]], [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]] (1 slot)"
sourcebook: "_Monster Core_, page 116."
```

```encounter-table
name: Young Fortune Dragon
creatures:
  - 1: Young Fortune Dragon
```
