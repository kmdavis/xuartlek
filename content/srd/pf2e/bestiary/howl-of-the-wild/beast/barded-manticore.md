---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Barded Manticore"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Barded Manticore"
level: 18
source: "Howl of the Wild"
aon_id: "creature-3300"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3300"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Barded Manticore"
level: "Creature 18"
size: "Large"
trait_01: "Beast"
trait_02: "Rare"
modifier: 33
perception:
  - name: "Perception"
    desc: "Perception +33; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Mwangi|Mwangi]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +35, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +29, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +32, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +31"
abilityMods: [9, 5, 6, 1, 5, 6]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +32; __Ref__: +30; __Will__: +29"
hp: 440
health:
  - name: "HP"
    desc: "440; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 15"
abilities_mid:
  - name: "Spell Reflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An opponent casts a spell that targets the manticore and requires a saving throw"
  - name: "Effect"
    desc: "The manticore gains a +4 circumstance bonus to the saving throw. If they critically succeed at the save, they can choose a creature within 30 feet that was not originally targeted by the spell. That creature becomes a new target of the spell, who must attempt its own save against the same DC."
speed: "40 feet, fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+15 piercing plus 1d12 electricity"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+15 slashing plus 1d12 electricity"
  - name: "Ranged"
    desc: "⬻ spike +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 40 feet) __Damage__ 3d8+15 piercing"
abilities_bot:
  - name: "Arrange Scales"
    desc: "⬻ The barded manticore flexes the muscles under their scales to temporarily gain better protection. The manticore gains a +2 circumstance bonus to AC and resistance 15 to their choice of bludgeoning, piercing, or slashing damage. These benefits last until the beginning of the manticore's next turn or they use Arrange Scales again."
  - name: "Metallic Coating"
    desc: "A barded manticore's [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]] attacks (including spikes) count as adamantine, cold iron, [[srd/pf2e/compendium/equipment/weapons/dawnsilver-weapon-high-grade|dawnsilver]], and silver."
  - name: "Paired Spikes"
    desc: "⬻ The barded manticore flings two spikes from their tail, targeting up to two creatures within 20 feet of each other. They make a separate ranged Strike against each creature, which counts as a single Strike for the barded manticore's multiple attack penalty, and the penalty doesn't increase until they've made both Strikes. If the manticore targeted only one creature and hits, that creature takes normal damage for a single spike, but also gains weakness 15 to electricity damage until the spikes are removed with an Interact action. Ingot Salvage The scales of a deceased barded manticore can be salvaged, granting several metal ingots (typically 1 [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine ingot]], 5 [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron ingots]], 1 [[srd/pf2e/compendium/equipment/materials/dawnsilver-object-high-grade|dawnsilver ingot]], and 5 [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver ingots]]). Its innate spells are etched onto the metal covering its tail, usually dawnsilver, which can be used as magical writing to [[srd/pf2e/compendium/rules-elements/actions/player-core#Learn a Spell|Learn a Spell]] for those spells."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 40, attack +35 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/detect-metal|Detect Metal]], [[srd/pf2e/compendium/spells/cantrips/needle-darts|Needle Darts]], [[srd/pf2e/compendium/spells/cantrips/tangle-vine|Tangle Vine]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/one-with-stone|One with Stone]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/impaling-spike|Impaling Spike]] (at will), [[srd/pf2e/compendium/spells/rank-3/lightning-bolt|Lightning Bolt]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/field-of-razors|Field of Razors]], [[srd/pf2e/compendium/spells/rank-6/tangling-creepers|Tangling Creepers]] - __8th__ [[srd/pf2e/compendium/spells/rank-6/chain-lightning|Chain Lightning]] - __9th__ [[srd/pf2e/compendium/spells/rank-9/wrathful-storm|Wrathful Storm]]"
sourcebook: "_Howl of the Wild_, page 173."
```

```encounter-table
name: Barded Manticore
creatures:
  - 1: Barded Manticore
```
