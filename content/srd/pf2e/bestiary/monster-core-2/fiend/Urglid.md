---
noteType: pf2eMonster
aliases: "Urglid"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Urglid"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4321"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urglid"
level: "Creature 13"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision, tremorsense (imprecise) 60 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +22, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +27, [[srd/pf2e/compendium/rules-elements/skills/Lore|Outer Rifts Lore]] +24, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +24, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +22, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +27"
abilityMods: [8, 4, 5, 4, 3, 4]
abilities_top:
  - name: "Consecration Vulnerability"
    desc: "Dedicated to the desecration of graves, an urglid takes 3d6+6 mental damage each round they're within the area of an effect with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Consecration|consecration]] trait. In addition, the demon's [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Immunity, Weakness, and Resistance#Weakness|weakness]] to [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] increases to 30 for 1 round the first time they take damage from [[srd/pf2e/compendium/equipment/consumables/Holy Water|holy water]] each turn."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +26; __Ref__: +20; __Will__: +20 +1 status to all saves vs. magic"
hp: 290
health:
  - name: "HP"
    desc: "290; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 10"
speed: "30 feet, burrow 40 feet, climb 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d10+16 slashing"
  - name: "Melee"
    desc: "⬻ leg +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d12+16 bludgeoning"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 32 - __1st__ [[srd/pf2e/compendium/spells/rituals/Demonic Pact|Demonic Pact]]"
  - name: "Earth Glide"
    desc: "The urglid can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through any earthen matter, including rock. When they do so, the urglid moves at their full burrow Speed, leaving no tunnels or signs of its passing unless they choose to do so."
  - name: "Gravechoke"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Olfactory|olfactory]]) The urglid emits a putrid pulse that targets all living creatures within a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]]. Each creature in this area that fails a DC 30 Fortitude save becomes [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 (sickened 2 on a critical failure)."
  - name: "Ravenous Earth"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) With a single, devious thought, the urglid causes a mound of grave soil to well up at a creature's feet. That creature must succeed at a DC 30 Reflex save or become [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 30). The restrained creature then begins sinking below the ground into a spontaneously formed grave. A creature restrained by this ability for 3 rounds is buried 6 feet deep in the ground and begins suffocating within 1 minute. A buried creature must be dug up to be freed (see [[srd/pf2e/books/gm-core/chapter-2-building-games/Environment#Burial|Burial]]). A creature that is slain by Ravenous Earth rises as a [[srd/pf2e/compendium/gm/creature-families/Ghoul|ghoul]] the next midnight. Kabriri's Excavators While many loathe urglids for their ravenous appetite for burial and wanton destruction, priests of [[srd/pf2e/compendium/deities/demon-lords/Kabriri|Kabriri]] insist that the demon lord blessed and oversaw their creation, trusting the fiends with digging the labyrinthine network of tunnels that connects Everglut with [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]]. It's no surprise, then, that where there's an urglid, there's possibly a pathway to the [[srd/pf2e/compendium/gm/Planes#Outer Rifts|Outer Rifts]]—and plenty of ghouls."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Magic Passage|Magic Passage]] (at will), [[srd/pf2e/compendium/spells/rank-5/Wall of Stone|Wall of Stone]] (×3) - __8th__ [[srd/pf2e/compendium/spells/rank-8/Earthquake|Earthquake]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 94."
```

```encounter-table
name: Urglid
creatures:
  - 1: Urglid
```
