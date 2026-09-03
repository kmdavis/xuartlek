---
obsidianUIMode: preview
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
aon_id: "creature-4311"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4311"
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
    desc: "Perception +29; greater darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/lore|Netherworld Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/lore|Void Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +27"
abilityMods: [8, 4, 6, 6, 6, 7]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +25; __Ref__: +25; __Will__: +31"
hp: 310
health:
  - name: "HP"
    desc: "310 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10, [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]] 10"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) 40 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 4d6 void damage with a DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save. If it fails, it's also [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 as long as it remains in the sunlight."
speed: "40 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ horn +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+12 bludgeoning plus 1d10 cold and 2d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]]"
  - name: "Melee"
    desc: "⬻ arm spike +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+12 piercing plus 1d10 cold"
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
    desc: "The sykever snatches the item and pierces it with their arm spikes. The item becomes [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]] and falls to the ground in the sykever's space. Items that are already broken aren't further damaged, and an item with 14 or higher [[srd/pf2e/books/player-core/chapter-6-equipment/shields#Hardness|Hardness]] is unaffected."
  - name: "Draining Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The sykever fixes their nightmarish gaze on one creature they can see, who must attempt a DC 36 Will save. Regardless of the result, the target is temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 2 for 1 round if the sykever is in bipedal stance or clumsy 2 for 1 round if the sykever is in quadrupedal stance."
  - name: "Failure"
    desc: "As success, but the effect lasts 1 minute."
  - name: "Critical Failure"
    desc: "As success, but enfeebled 3 or [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 3, and the effect lasts 10 minutes."
  - name: "Horned Rush"
    desc: "⬻"
  - name: "Requirements"
    desc: "The sykever is in their quadrupedal stance"
  - name: "Effect"
    desc: "The sykever Strides and then makes a horn Strike. The Bound One Hidden beneath the necromantic colleges of Yled in the nation of Geb are a trio of sykevers held in magical stasis alongside an ancient darvakka known only as the Bound One. This creature, ensnared by Geb himself, serves as an unending pool of void energy, immensely useful for magical experiments and empowering other undead servitors around the nation. The four darvakkas await the day Geb calls upon them once more."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (at will), [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (×3) - __6th__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __7th__ [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×3), [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]]; [[srd/pf2e/compendium/gm/planes#The Void|the Void]]; or [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]] only), [[srd/pf2e/compendium/spells/rank-3/paralyze|Paralyze]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-4/fly|Fly]]"
sourcebook: "_Monster Core 2_, page 85."
```

```encounter-table
name: Sykever
creatures:
  - 1: Sykever
```
