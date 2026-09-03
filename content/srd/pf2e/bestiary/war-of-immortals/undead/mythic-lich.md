---
obsidianUIMode: preview
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
aon_id: "creature-3402"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3402"
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
    desc: "Perception +20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +17, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +20"
abilityMods: [0, 4, 0, 6, 4, 3]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/consumables/invisibility-potion|invisibility potion]]_, _[[srd/pf2e/compendium/spells/rank-6/teleport|_scroll of teleport_]]_, _[[srd/pf2e/compendium/equipment/staves/staff-of-fire-major|greater staff of fire]]_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 [[srd/pf2e/books/war-of-immortals/mythic-rules/mythic-monster-templates#Basic Mythic Abilities|mythic resilience]] (Ref and Will)"
hp: 190
health:
  - name: "HP"
    desc: "190 ([[srd/pf2e/compendium/gm/creature-families/lich|rejuvenation]], void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, physical 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]] bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet, DC 29 **Counterspell ⬲ :"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared**"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Recharge Spell_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The mythic lich regains one spell._Remove a Condition_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
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
    desc: "A lich's form draws forth life from those who come into contact with it. When the lich damages a living creature with an [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]] attack, the lich gains 5 temporary Hit Points and the creature must succeed at a DC 34 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]. If the lich is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] at the start of its turn, each creature grabbing or restraining it must succeed at a Fortitude save or become drained 1. If the lich siphons a creature's life again, the drained value increase by 1, to a maximum of drained 4."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted. Mythic Soul Cages Though a standard _soul cage_ appears in _Monster Core_, a truly powerful mythic lich is likely to have a _soul cage_ that is much more spectacular and unusual in nature. The mightiest mythic lich might bind a fearsome and nearly immortal creature to serve as its _soul cage_, or a majestic fortress, or even an entire island."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/message|Message]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/fleet-step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/false-vitality|False Vitality]], [[srd/pf2e/compendium/spells/rank-2/resist-energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-1/force-barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/locate|Locate]], [[srd/pf2e/compendium/spells/rank-3/vampiric-feast|Vampiric Feast]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/fire-shield|Fire Shield]], [[srd/pf2e/compendium/spells/rank-4/fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|Howling Blizzard]] (×2), [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-5/wall-of-ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/chain-lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/vampiric-exsanguination|Vampiric Exsanguination]]"
sourcebook: "_War of Immortals_, page 172."
```

```encounter-table
name: Mythic Lich
creatures:
  - 1: Mythic Lich
```
