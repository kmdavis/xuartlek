---
noteType: pf2eMonster
aliases: "Pale Horse"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Pale Horse"
level: 11
source: "Howl of the Wild"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3319"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Pale Horse"
level: "Creature 11"
size: "Large"
trait_01: "Incorporeal"
trait_02: "Uncommon"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision, lifesense 90 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; can't speak any language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +23"
abilityMods: [-5, 8, 3, -2, 4, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +20; __Ref__: +24; __Will__: +21"
hp: 180
health:
  - name: "HP"
    desc: "180 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ all damage 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]; double resistance vs. non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]])"
abilities_mid:
  - name: "Aura of Despair"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 30 feet. A living creature that begins its turn in the aura must succeed at a DC 27 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]]. A creature is temporarily immune to the aura for 1 hour if it critically succeeds."
speed: "fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spectral horn +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d10+10 void"
  - name: "Melee"
    desc: "⬻ hoof +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d8+10 void"
abilities_bot:
  - name: "Spectral Charge"
    desc: "⬺ The pale horse [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] twice and then makes a horn Strike. The pale horse can move through creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (×3) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]]"
sourcebook: "_Howl of the Wild_, page 190."
```

```encounter-table
name: Pale Horse
creatures:
  - 1: Pale Horse
```
