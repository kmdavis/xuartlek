---
noteType: pf2eMonster
aliases: "Aeolaeka"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Aeolaeka"
level: 12
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2843"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aeolaeka"
level: "Creature 12"
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Earth"
trait_04: "Holy"
modifier: 23
perception:
  - name: "Perception"
    desc: "+23; darkvision, tremorsense (precise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]]; [[srd/pf2e/compendium/spells/rank-5/Speak with Stones|_speak with stones_]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +22, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +23"
abilityMods: [6, 4, 7, 2, 5, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/hammer/Warhammer|warhammer]]_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +20; __Will__: +23"
hp: 250
health:
  - name: "HP"
    desc: "250; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 15"
speed: "25 feet, burrow 25 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ _warhammer_ +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 2d8+12 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "An aeolaeka can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through any earthen matter, including rock. When they do so, the aeolaeka moves at their full burrow Speed, leaving no tunnels or signs of their passing."
  - name: "Liberate the Earth"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|Earth]]) The aeolaeka conjures churning stones, creating a 60-foot line of rolling boulders. Creatures in the line take 10d6 bludgeoning damage with a DC 35 Reflex save. The area is difficult terrain for 24 hours before the leftover stone crumbles to dust. The aeolaeka can't Liberate the Earth for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature takes no damage."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is knocked [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]."
  - name: "Critical Failure"
    desc: "The creature takes double damage, is knocked prone, and is [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]] by the rubble ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 32)."
  - name: "Statue"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) Until the next time they act, the aeolaeka appears to be a statue. They have an automatic result of 45 on [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks and DCs to pass as a statue."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]], [[srd/pf2e/compendium/spells/rank-5/Wall of Stone|Wall of Stone]], [[srd/pf2e/compendium/spells/rank-4/Weapon Storm|Weapon Storm]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Petrify|Petrify]], [[srd/pf2e/compendium/spells/rank-2/Sure Footing|Sure Footing]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Speak with Stones|Speak with Stones]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 35."
```

```encounter-table
name: Aeolaeka
creatures:
  - 1: Aeolaeka
```
