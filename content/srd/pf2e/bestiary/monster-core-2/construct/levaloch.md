---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Levaloch"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Levaloch"
level: 7
source: "Monster Core 2"
aon_id: "creature-4327"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4327"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Levaloch"
level: "Creature 7"
size: "Large"
trait_01: "Construct"
trait_02: "Devil"
trait_03: "Fiend"
trait_04: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +14"
abilityMods: [6, 3, 4, 2, 3, 1]
abilities_top:
  - name: "Hellstrider"
    desc: "A levaloch ignores the effects of non-magical difficult terrain. They take no damage from caltrops or from damaging terrain that deals physical, acid, or cold damage. A levaloch can move through liquids up to 5 feet deep at their full Speed."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +14; __Will__: +12 +1 status to all saves vs. magic"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/damage-rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 5 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Phalanx Fighter"
    desc: "All devils of equal or lower level adjacent to a levaloch gain a +1 circumstance bonus to their AC as the levaloch shields them from harm."
  - name: "Stable Stance"
    desc: "A levaloch gains a +2 circumstance bonus to their Fortitude DC against being [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shoved]] and to other saving throws to resist being moved against their will."
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d8+12 piercing plus merciless thrust"
  - name: "Ranged"
    desc: "⬻ _trident_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d8+12 piercing"
  - name: "Ranged"
    desc: "⬻ _barbed net_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 20 feet) __Damage__ barbed net"
abilities_bot:
  - name: "Barbed Net"
    desc: "When a levaloch hits a creature with their barbed net, the net wraps around the target, which becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 and takes a –10-foot circumstance penalty to its Speeds. If the Strike was a critical success, the target is also [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]]. When a creature [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 22), or if the Strike misses, the net crumbles into rust. Each time a creature attempts to Escape, it takes 1d6 slashing damage from the net's barbs, regardless of whether the attempt succeeds."
  - name: "Forge Weapon"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) A levaloch reforges part of their barbed iron substance into a new _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/spear/trident|trident]]_ or barbed net. Their previous trident crumbles to rust. When the levaloch is destroyed, any tridents or barbed nets they created crumble to rust."
  - name: "Merciless Thrust"
    desc: "When a levaloch hits a creature that has the [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]], [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] conditions with a melee trident Strike, the Strike deals an additional 2d6 damage. Hellforged Construct Levalochs are strange amalgamations of devil and automaton, never requiring food or rest. The engravings on their iron plates indicate their hellish allegiance to a certain archdevil, infernal duke, malebranche, or Queen of the Night."
spellcasting:
  - name: "Rituals"
    desc: "DC 22 - __1st__ [[srd/pf2e/compendium/spells/rituals/diabolic-pact|Diabolic Pact]]"
sourcebook: "_Monster Core 2_, page 99."
```

```encounter-table
name: Levaloch
creatures:
  - 1: Levaloch
```
