---
noteType: pf2eMonster
aliases: "Maestro"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Maestro"
level: 11
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3579"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Maestro"
level: "Creature 11"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +23, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +23, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/Lore|Music Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +19, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +30, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +21"
abilityMods: [2, 4, 1, 2, 3, 5]
abilities_top:
  - name: "Bardic Lore"
    desc: "The maestro can [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] on any subject with a +19 modifier."
  - name: "Performing Specialist"
    desc: "For encounters involving acting, music, or storytelling, the maestro is a 15th-level challenge."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/Composite Shortbow|composite shortbow]]_ (30 arrows), _+1 [[srd/pf2e/compendium/equipment/Armor#Leather Armor|leather armor]]_, lyre (_[[srd/pf2e/compendium/equipment/held-items/Maestro's Instrument|moderate maestro's instrument]]_), _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/Rapier|rapier]]_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +24; __Will__: +21 +1 circumstance bonus to saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]"
hp: 180
health:
  - name: "HP"
    desc: "180"
abilities_mid:
  - name: "Resolve"
    desc: "When the maestro rolls a success on a Will save, they get a critical success instead."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly 1d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d6+10 piercing plus resonating weaponry"
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 2d6+9 piercing plus resonating weaponry"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 30, 1 Focus Point - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Dirge of Doom|Dirge of Doom]] - __6th__ [[srd/pf2e/compendium/spells/focus/Counter Performance|Counter Performance]]"
  - name: "Resonating Weaponry"
    desc: "The maestro funnels musical energy from their compositions into attacks, dealing additional 1d6 sonic damage with their weapon Strikes on any turn they cast a [[srd/pf2e/compendium/rules-elements/traits/player-core/Composition|composition]] spell."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 30, attack +22 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Summon Instrument|Summon Instrument]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-2/Shatter|Shatter]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (3 slots) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Illusory Scene|Illusory Scene]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]], [[srd/pf2e/compendium/spells/rank-5/Wave of Despair|Wave of Despair]] (3 slots) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Spirit Blast|Spirit Blast]], [[srd/pf2e/compendium/spells/rank-6/Vibrant Pattern|Vibrant Pattern]] (2 slots)"
sourcebook: "_NPC Core_, page 130."
```

```encounter-table
name: Maestro
creatures:
  - 1: Maestro
```
