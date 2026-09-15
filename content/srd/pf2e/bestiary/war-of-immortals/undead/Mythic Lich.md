---
noteType: pf2eMonster
aliases: "Mythic Lich"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Mythic Lich"
level: 12
source: "War of Immortals"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3402"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Mythic Lich"
level: "Creature 12"
size: "Medium"
trait_01: "Mythic"
trait_02: "Rare"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +17, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +20"
abilityMods: [0, 4, 0, 6, 4, 3]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/consumables/Invisibility Potion|invisibility potion]]_, _[[srd/pf2e/compendium/spells/rank-6/Teleport|_scroll of teleport_]]_, _[[srd/pf2e/compendium/equipment/staves/Staff of Fire|greater staff of fire]]_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 [[srd/pf2e/books/war-of-immortals/mythic-rules/Mythic Monster Templates#Basic Mythic Abilities|mythic resilience]] (Ref and Will)"
hp: 190
health:
  - name: "HP"
    desc: "190 ([[srd/pf2e/compendium/gm/creature-families/Lich|rejuvenation]], void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, physical 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]] bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 60 feet, DC 29 **Counterspell ⬲ :"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared**"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Recharge Spell_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The mythic lich regains one spell._Remove a Condition_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The mythic lich ends one condition affecting it."
  - name: "Drain Soul Cage"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The lich taps into their _soul cage's_ power to cast any arcane spell up to 6th rank, even if the spell being cast is not one of the lich's prepared spells. The lich's _soul cage_ doesn't need to be present for the lich to use this ability."
  - name: "Siphon Life"
    desc: "A lich's form draws forth life from those who come into contact with it. When the lich damages a living creature with an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]] attack, the lich gains 5 temporary Hit Points and the creature must succeed at a DC 34 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]]. If the lich is [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] at the start of its turn, each creature grabbing or restraining it must succeed at a Fortitude save or become drained 1. If the lich siphons a creature's life again, the drained value increase by 1, to a maximum of drained 4."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted. Mythic Soul Cages Though a standard _soul cage_ appears in _Monster Core_, a truly powerful mythic lich is likely to have a _soul cage_ that is much more spectacular and unusual in nature. The mightiest mythic lich might bind a fearsome and nearly immortal creature to serve as its _soul cage_, or a majestic fortress, or even an entire island."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/False Vitality|False Vitality]], [[srd/pf2e/compendium/spells/rank-2/Resist Energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/Fire Shield|Fire Shield]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]] (×2), [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-5/Wall of Ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]]"
sourcebook: "_War of Immortals_, page 172."
```

```encounter-table
name: Mythic Lich
creatures:
  - 1: Mythic Lich
```
