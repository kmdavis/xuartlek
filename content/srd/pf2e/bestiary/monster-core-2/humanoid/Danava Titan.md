---
noteType: pf2eMonster
aliases: "Danava Titan"
tags:
  - pf2e/creature/level/23
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/titan
  - pf2e/creature/trait/water
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Danava Titan"
level: 23
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4583"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Danava Titan"
level: "Creature 23"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Rare"
trait_03: "Titan"
trait_04: "Water"
modifier: 41
perception:
  - name: "Perception"
    desc: "+41; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]], wavesense (imprecise) 100 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +39, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +43, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +46, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +43, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +41, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +43, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +41, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +43"
abilityMods: [11, 8, 10, 10, 8, 6]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+3 major striking]] [[srd/pf2e/compendium/equipment/weapons/club/Greatclub|greatclub]]_"
ac: 49
armorclass:
  - name: "AC"
    desc: "49; __Fort__: +41; __Ref__: +37; __Will__: +37 +4 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]"
hp: 470
health:
  - name: "HP"
    desc: "470; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
abilities_mid:
  - name: "Hadalic Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]]) Creatures that fail their Will save against the titan's impossible stature aura also experience the crushing depths and darkness of the ocean floor. Such creatures see as if in an area of [[srd/pf2e/compendium/spells/rank-2/Darkness|_darkness_]] (10th rank), and the titan can use their wavesense to detect such creatures as a precise sense, even if neither are in water. On a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]]."
  - name: "Impossible Stature"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] must succeed at a DC 46 Will save or its movement toward the titan is movement over [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Difficult Terrain|difficult terrain]] (greater difficult terrain on a critical failure) for 1 round."
  - name: "Relentless"
    desc: "The titan is as ever-moving as ocean waves. They're permanently [[srd/pf2e/compendium/rules-elements/Conditions#Quickened|quickened]] 1, and the extra action can be used only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]], Strike, or [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|Sustain]] a Spell, or as one of the actions necessary to cast [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|_dispel magic_]]."
  - name: "Roiling Rebuke"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 200 feet targets the titan with or includes the titan in the area of an attack, spell, or other effect"
  - name: "Effect"
    desc: "The titan makes a benthic wave Strike against the triggering creature. If the Strike hits, the titan [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Actions#Disrupting Actions|disrupts]] the triggering action."
speed: "50 feet, fly 50 feet, swim 40 feet; water walk"
attacks:
  - name: "Melee"
    desc: "⬻ _greatclub_ +43 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 40 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|shove]]) __Damage__ 4d10+20 bludgeoning plus 2d12 cold"
  - name: "Melee"
    desc: "⬻ foot +40 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]]) __Damage__ 4d8+20 bludgeoning plus 2d12 cold"
  - name: "Ranged"
    desc: "⬻ benthic wave +40 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], range 200 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]]) __Damage__ 4d6+20 bludgeoning plus 2d12 cold"
abilities_bot:
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 46"
  - name: "Wide Cleave"
    desc: "⬺ The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made. Danava Pillars Some danavas, known as danava pillars, are custodians of a fundamental concept like life or knowledge—each, a crux of the universe. Destroying a danava pillar forcibly shreds their bonds and risks unraveling a portion of reality, with potentially disastrous effects."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38 - __9th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]] (at will), [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-7/Eclipse Burst|Eclipse Burst]] (×3), [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×3), [[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|Hydraulic Push]] (×3), [[srd/pf2e/compendium/spells/rank-4/Hydraulic Torrent|Hydraulic Torrent]] (×3) - __10th__ [[srd/pf2e/compendium/spells/rank-9/Implosion|Implosion]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-2/Water Walk|Water Walk]]"
  - name: "Rituals"
    desc: "DC 46 - __5th__ Resurrect (doesn't require secondary casters) - __6th__ [[srd/pf2e/compendium/spells/rituals/Binding Circle|Binding Circle]] - __8th__ [[srd/pf2e/compendium/spells/rituals/Control Weather|Control Weather]]"
sourcebook: "_Monster Core 2_, page 321."
```

```encounter-table
name: Danava Titan
creatures:
  - 1: Danava Titan
```
