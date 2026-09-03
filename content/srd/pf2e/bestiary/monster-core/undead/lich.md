---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lich"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Lich"
level: 12
source: "Monster Core"
aon_id: "creature-3082"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3082"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lich"
level: "Creature 12"
size: "Medium"
trait_01: "Rare"
trait_02: "Undead"
trait_03: "Unholy"
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
    desc: "[[srd/pf2e/compendium/equipment/consumables/invisibility-potion|_invisibility potion_]], [[srd/pf2e/compendium/spells/rank-6/teleport|_scroll of teleport_]], [[srd/pf2e/compendium/equipment/staves/staff-of-fire-major|_greater staff of fire_]]"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]"
hp: 190
health:
  - name: "HP"
    desc: "190 (void healing, rejuvenation); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, physical 10 (except magical bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet, DC 29"
  - name: "Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Drain Soul Cage"
    desc: "⭓ 6th rank"
  - name: "Siphon Life"
    desc: "DC 34"
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/message|Message]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/fleet-step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/false-vitality|False Vitality]], [[srd/pf2e/compendium/spells/rank-2/resist-energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-1/force-barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-3/locate|Locate]], [[srd/pf2e/compendium/spells/rank-3/vampiric-feast|Vampiric Feast]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/fire-shield|Fire Shield]], [[srd/pf2e/compendium/spells/rank-4/fly|Fly]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|Howling Blizzard]] (×2), [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-5/wall-of-ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/chain-lightning|Chain Lightning]], [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/vampiric-exsanguination|Vampiric Exsanguination]]"
sourcebook: "_Monster Core_, page 219."
```

```encounter-table
name: Lich
creatures:
  - 1: Lich
```
