---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ferrugon"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ferrugon"
level: 12
source: "Monster Core 2"
aon_id: "creature-4328"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4328"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ferrugon"
level: "Creature 12"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +23, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +25"
abilityMods: [7, 5, 6, 4, 4, 5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +21 +1 status to all saves vs. magic"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 10 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Metallic"
    desc: "A ferrugon is a metallic creature and thus affected by effects such as the circumstance penalty inflicted by [[srd/pf2e/compendium/spells/rank-1/thunderstrike|_thunderstrike_]]."
  - name: "Vainglorious Whispers"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "A non-[[srd/pf2e/compendium/rules-elements/traits/player-core/devil|devil]] creature within 30 feet of the ferrugon succeeds (but doesn't critically succeed) at an attack roll, skill check, or saving throw"
  - name: "Effect"
    desc: "The ferrugon whispers subversive messages to the triggering creature, causing it to become overly confident in its abilities, while in fact it becomes less accomplished overall. The target must attempt a DC 32 Will save. On a failure, the target gains a +2 status bonus to saving throws against [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] effects but also takes a –2 penalty to all attack rolls and skill checks for 1 hour. During this time, the victim can't benefit from [[srd/pf2e/compendium/rules-elements/actions/player-core#Aid|Aid]] reactions, use [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]] effects on themself, or use [[srd/pf2e/compendium/rules-elements/actions/player-core#Take Cover|Take Cover]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Raise a Shield|Raise a Shield]] actions, as these actions seem unnecessary to the creature at this time. Similar defensive actions might not be available to the victim as well, at the GM's discretion. The target is then temporarily immune to Vainglorious Whispers for 24 hours."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold iron]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|shove]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d8+16 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold iron]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d4+16 slashing plus ferrugon tetanus"
  - name: "Ranged"
    desc: "⬻ iron feather +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold iron]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], range increment 40 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d4+13 piercing plus ferrugon tetanus"
abilities_bot:
  - name: "Ferrugon Tetanus"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude; Onset 1d4 days"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 (1 week)"
  - name: "Stage 2"
    desc: "clumsy 2 and can't speak (1 day)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] (1 day)"
  - name: "Stage 4"
    desc: "death"
  - name: "Sunder Objects"
    desc: "When a ferrugon damages an item or structure, they deal an additional 2d8 damage to that item or structure. Makers Of Rust A ferrugon’s [[srd/pf2e/compendium/spells/rank-6/petrify|_petrify_]] and [[srd/pf2e/compendium/spells/rank-5/wall-of-stone|_wall of stone_]] [[srd/pf2e/books/gm-core/chapter-2-building-games/building-creatures#Innate Spells|innate spells]] result in rusted iron objects instead of stone. Since this iron is rusted and flawed, it shares the same physical statistics as the [[srd/pf2e/compendium/equipment/materials/stone-object-low-grade|stone]] created by the spells and is too low-quality to serve as a source for forging metal objects."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/creation|Creation]], [[srd/pf2e/compendium/spells/rank-2/shatter|Shatter]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]], [[srd/pf2e/compendium/spells/rank-5/wall-of-stone|Wall of Stone]] (×3; wall is made of rusty iron; not stone) - __6th__ [[srd/pf2e/compendium/spells/rank-6/petrify|Petrify]] (target is transformed into rusty iron; not stone)"
  - name: "Rituals"
    desc: "DC 32 - __1st__ [[srd/pf2e/compendium/spells/rituals/diabolic-pact|Diabolic Pact]]"
sourcebook: "_Monster Core 2_, page 100."
```

```encounter-table
name: Ferrugon
creatures:
  - 1: Ferrugon
```
