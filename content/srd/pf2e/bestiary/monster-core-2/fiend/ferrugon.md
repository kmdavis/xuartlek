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
languages: "Common, Diabolic, Draconic, Empyrean, Talican; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +25, Crafting +22, Deception +21, Intimidation +23, Religion +22, Stealth +23, Thievery +25"
abilityMods: [7, 5, 6, 4, 4, 5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +21 +1 status to all saves vs. magic"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ fire; __Resistances__ physical 10 (except silver); __Weaknesses__ holy 10"
abilities_mid:
  - name: "Metallic"
    desc: "A ferrugon is a metallic creature and thus affected by effects such as the circumstance penalty inflicted by _thunderstrike_."
  - name: "Vainglorious Whispers"
    desc: "⬲ (divine, linguistic, mental)"
  - name: "Trigger"
    desc: "A non-devil creature within 30 feet of the ferrugon succeeds (but doesn't critically succeed) at an attack roll, skill check, or saving throw"
  - name: "Effect"
    desc: "The ferrugon whispers subversive messages to the triggering creature, causing it to become overly confident in its abilities, while in fact it becomes less accomplished overall. The target must attempt a DC 32 Will save. On a failure, the target gains a +2 status bonus to saving throws against fear effects but also takes a –2 penalty to all attack rolls and skill checks for 1 hour. During this time, the victim can't benefit from Aid reactions, use healing effects on themself, or use Take Cover or Raise a Shield actions, as these actions seem unnecessary to the creature at this time. Similar defensive actions might not be available to the victim as well, at the GM's discretion. The target is then temporarily immune to Vainglorious Whispers for 24 hours."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +25 (cold iron, magical, shove, unholy) __Damage__ 3d8+16 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +25 (Agile, cold iron, magical, unholy) __Damage__ 3d4+16 slashing plus ferrugon tetanus"
  - name: "Ranged"
    desc: "⬻ iron feather +23 (cold iron, magical, range increment 40 feet, unholy) __Damage__ 3d4+13 piercing plus ferrugon tetanus"
abilities_bot:
  - name: "Ferrugon Tetanus"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude; Onset 1d4 days"
  - name: "Stage 1"
    desc: "clumsy 1 (1 week)"
  - name: "Stage 2"
    desc: "clumsy 2 and can't speak (1 day)"
  - name: "Stage 3"
    desc: "paralyzed (1 day)"
  - name: "Stage 4"
    desc: "death"
  - name: "Sunder Objects"
    desc: "When a ferrugon damages an item or structure, they deal an additional 2d8 damage to that item or structure. Makers Of Rust A ferrugon’s _petrify_ and _wall of stone_ innate spells result in rusted iron objects instead of stone. Since this iron is rusted and flawed, it shares the same physical statistics as the stone created by the spells and is too low-quality to serve as a source for forging metal objects."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24 - __4th__ Translocate (at will), Suggestion - __5th__ Creation, Shatter, Translocate, Wall of Stone (×3; wall is made of rusty iron; not stone) - __6th__ Petrify (target is transformed into rusty iron; not stone)"
  - name: "Rituals"
    desc: "DC 32 - __1st__ Diabolic Pact"
sourcebook: "_Monster Core 2_, page 100."
```

```encounter-table
name: Ferrugon
creatures:
  - 1: Ferrugon
```
