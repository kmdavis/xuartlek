---
noteType: pf2eMonster
aliases: "Sykever"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Sykever"
level: 15
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4311"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sykever"
level: "Creature 15"
size: "Huge"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 29
perception:
  - name: "Perception"
    desc: "+29; greater darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/Lore|Netherworld Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +27, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/Lore|Void Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/Lore|Warfare Lore]] +27"
abilityMods: [8, 4, 6, 6, 6, 7]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +25; __Ref__: +25; __Will__: +31"
hp: 310
health:
  - name: "HP"
    desc: "310 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 10, [[srd/pf2e/compendium/equipment/materials/Silver|silver]] 10"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) 40 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 4d6 void damage with a DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save. If it fails, it's also [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]] 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]] 2 as long as it remains in the sunlight."
speed: "40 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ horn +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+12 bludgeoning plus 1d10 cold and 2d8 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed]]"
  - name: "Melee"
    desc: "⬻ arm spike +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+12 piercing plus 1d10 cold"
abilities_bot:
  - name: "Change Posture"
    desc: "⬻ The sykever changes between their bipedal and quadrupedal stance. In their bipedal stance, the sykever can use all the abilities in their stat block except Horned Rush. In their quadrupedal stance, the sykever has a Speed of 80 feet but can't make arm spike Strikes, [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]], cast spells, or use Crush Item."
  - name: "Crush Item"
    desc: "⬲"
  - name: "Trigger"
    desc: "The sykever gets a critical success to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]]"
  - name: "Requirements"
    desc: "The sykever is in their bipedal stance"
  - name: "Effect"
    desc: "The sykever snatches the item and pierces it with their arm spikes. The item becomes [[srd/pf2e/compendium/rules-elements/Conditions#Broken|broken]] and falls to the ground in the sykever's space. Items that are already broken aren't further damaged, and an item with 14 or higher [[srd/pf2e/books/player-core/chapter-6-equipment/Shields#Hardness|Hardness]] is unaffected."
  - name: "Draining Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) The sykever fixes their nightmarish gaze on one creature they can see, who must attempt a DC 36 Will save. Regardless of the result, the target is temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]] 2 for 1 round if the sykever is in bipedal stance or clumsy 2 for 1 round if the sykever is in quadrupedal stance."
  - name: "Failure"
    desc: "As success, but the effect lasts 1 minute."
  - name: "Critical Failure"
    desc: "As success, but enfeebled 3 or [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]] 3, and the effect lasts 10 minutes."
  - name: "Horned Rush"
    desc: "⬻"
  - name: "Requirements"
    desc: "The sykever is in their quadrupedal stance"
  - name: "Effect"
    desc: "The sykever Strides and then makes a horn Strike. The Bound One Hidden beneath the necromantic colleges of Yled in the nation of Geb are a trio of sykevers held in magical stasis alongside an ancient darvakka known only as the Bound One. This creature, ensnared by Geb himself, serves as an unending pool of void energy, immensely useful for magical experiments and empowering other undead servitors around the nation. The four darvakkas await the day Geb calls upon them once more."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]] (at will), [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×3) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]] - __7th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (×3), [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]]; [[srd/pf2e/compendium/gm/Planes#The Void|the Void]]; or [[srd/pf2e/compendium/gm/Planes#The Netherworld|the Netherworld]] only), [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]]"
sourcebook: "_Monster Core 2_, page 85."
```

```encounter-table
name: Sykever
creatures:
  - 1: Sykever
```
