---
noteType: pf2eMonster
aliases: "Gennayn"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/tiny
statblock: inline
name: "Gennayn"
level: 2
source: "Rage of Elements"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2687"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Gennayn"
level: "Creature 2"
size: "Tiny"
trait_01: "Elemental"
trait_02: "Genie"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +6, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +8, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +10"
abilityMods: [-2, 4, 0, 2, 2, 4]
abilities_top:
  - name: "Inspiring Influence"
    desc: "A gennayn automatically succeeds with the Aid action supporting any [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] or [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill check. Their Aid action automatically counts as a critical success while aiding in the creation of new art or a new performance."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +10; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30; __Resistances__ attuned element 5 (see below)"
speed: "15 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ elemental fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 2d6 damage (see attuned element)"
abilities_bot:
  - name: "Attuned Element"
    desc: "Upon waking each day, a gennayn attunes to one planar element. They gain the corresponding trait, a movement Speed, a cantrip, resistance, and an elemental damage type for their energy fist attack based on their attuned element: __air__ fly 30 feet, resist electricity 5, _electric arc_, electricity damage; __earth__ burrow 15 feet, resist bludgeoning 5, _scatter scree_, bludgeoning damage; __fire__ fly 30 feet, resist fire 5, _ignition_, fire damage; __metal__ burrow 15 feet, resist slashing 5, [[srd/pf2e/compendium/spells/cantrips/Needle Darts|_needle darts_]], slashing damage; __water__ swim 20 feet, resist cold 5, _frostbite_, bludgeoning damage; __wood__ climb 15 feet, resist piercing 5, _tangle vine_, piercing damage. The attunement lasts until the gennayn attunes to a different element."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The gennayn transforms into a Tiny [[srd/pf2e/compendium/rules-elements/traits/player-core/Elemental|elemental]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]]. This doesn't affect the gennayn's statistics, but it could change the damage type of their Strikes."
  - name: "Little Wish"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|Fortune]])"
  - name: "Trigger"
    desc: "A creature the gennayn can see that's within 60 feet attempts a saving throw or skill check"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The gennayn reshapes reality in a small way to twist fate, allowing the creature to reroll the saving throw or skill check and take the better result. Artistic Inspiration Talented individuals often claim to have been inspired by otherworldly forces. As gennayns are known to share inspiration and develop talent, many scholars and artists believe their aptitude unknowingly benefited from a gennayn's attention. Others speculate that being in a gennayn's good graces can stave off bouts of artistic ennui—or that angering a gennayn is a direct path to creative doldrums. Gennayns themselves don't claim to be muses, merely beings drawn to talent."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ elemental cantrip (see attuned element), [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Summon Instrument|Summon Instrument]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Cleanse Cuisine|Cleanse Cuisine]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Translate|Translate]] (at will), [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only)"
sourcebook: "_Rage of Elements_, page 226."
```

```encounter-table
name: Gennayn
creatures:
  - 1: Gennayn
```
