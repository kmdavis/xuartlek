---
obsidianUIMode: preview
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
aon_id: "creature-3579"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3579"
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
    desc: "Perception +22"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Deception +23, Diplomacy +23, Intimidation +23, Music Lore +21, Occultism +19, Performance +30, Society +21"
abilityMods: [2, 4, 1, 2, 3, 5]
abilities_top:
  - name: "Bardic Lore"
    desc: "The maestro can Recall Knowledge on any subject with a +19 modifier."
  - name: "Performing Specialist"
    desc: "For encounters involving acting, music, or storytelling, the maestro is a 15th-level challenge."
  - name: "Items"
    desc: "_+1 striking composite shortbow_ (30 arrows), _+1 leather armor_, lyre (_moderate maestro's instrument_), _+1 striking rapier_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +24; __Will__: +21 +1 circumstance bonus to saves vs. auditory, illusion, linguistic, sonic, or visual"
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
    desc: "⬻ _rapier_ +24 (deadly 1d8, Disarm, Finesse, Magical) __Damage__ 2d6+10 piercing plus resonating weaponry"
  - name: "Melee"
    desc: "⬻ fist +23 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +24 (deadly d10, Magical, Propulsive, range increment 60 feet, reload 0) __Damage__ 2d6+9 piercing plus resonating weaponry"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 30, 1 Focus Point - __Cantrips (6th)__ Courageous Anthem, Dirge of Doom - __6th__ Counter Performance"
  - name: "Resonating Weaponry"
    desc: "The maestro funnels musical energy from their compositions into attacks, dealing additional 1d6 sonic damage with their weapon Strikes on any turn they cast a composition spell."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 30, attack +22 - __Cantrips (6th)__ Light, Figment, Message, Summon Instrument, Telekinetic Projectile - __4th__ Fly, Shatter, Translocate (3 slots) - __5th__ Illusory Scene, Truespeech, Wave of Despair (3 slots) - __6th__ Spirit Blast, Vibrant Pattern (2 slots)"
sourcebook: "_NPC Core_, page 130."
```

```encounter-table
name: Maestro
creatures:
  - 1: Maestro
```
