---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Yarnspinner"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Yarnspinner"
level: 7
source: "NPC Core"
aon_id: "creature-3647"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3647"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Halfling Yarnspinner"
level: "Creature 7"
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; keen eyes"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Arcana +16, Deception +16, Diplomacy +16, Intimidation +14, History Lore +19, Occultism +17, Performance +19, Religion +15, Society +15"
abilityMods: [-1, 4, 0, 4, 3, 5]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the Seek action to find hidden or undetected creatures within 30 feet of them. Whenever the halfling targets a creature that is concealed or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Tale Specialist"
    desc: "For encounters involving storytelling, local history, or lore, the yarnspinner is a 10th-level challenge."
  - name: "Items"
    desc: "book of fables, Chain Shirt, _+1 halfling sling staff_ (20 bullets), _+1 shortsword_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +15; __Will__: +18"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Guidance Through Tales"
    desc: "⬲ (auditory, concentrate, linguistic, mental)"
  - name: "Trigger"
    desc: "An ally the yarnspinner can see fails a skill check"
  - name: "Effect"
    desc: "The yarnspinner offers a brief reminder about a legendary hero, granting their ally a +2 circumstance bonus to the triggering skill check, potentially turning the failure into a success."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _shortsword_ +16 (Agile, Finesse, Magical, versatile S) __Damage__ 1d6+3 piercing plus resonant weapons"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _halfling sling staff_ +16 (Magical, Propulsive, range increment 30 feet, reload 1) __Damage__ 1d10+3 bludgeoning plus resonant weapons"
abilities_bot:
  - name: "Mesmerizing Tale"
    desc: "⬺ (Auditory, Aura, Incapacitation, Linguistic, Mental, Occult) The yarnspinner weaves a long-winded but captivating narrative that enchants those nearby. Any creature that's in a 20-foot emanation or starts its turn in the aura must attempt a DC 24 Will save. The Mesmerizing Tale lasts until the end of the yarnspinner's next turn, but can be Sustained. The first time the yarnspinner Sustains the aura on subsequent rounds, the aura expands by 10 feet, to a maximum of 60 feet."
  - name: "Critical Success"
    desc: "The creature is unaffected, and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature becomes fascinated with the yarnspinner until the start of its next turn, and must spend all its actions to move closer to the yarnspinner and listen to the tale."
  - name: "Resonant Weapons"
    desc: "(Occult, Sonic) If the yarnspinner's Mesmerizing Tale aura is active or they have cast a spell within the last round, their Strikes with magic weapons deal an additional 2d10 sonic damage."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ Daze, Detect Magic, Figment, Light, Read Aura - __1st__ Illusory Disguise, Illusory Object, Mindlink, Ventriloquism (4 slots) - __2nd__ Invisibility, Laughing Fit, Revealing Light, Soothe (4 slots) - __3rd__ Haste, Heroism, Ring of Truth, Soothe (4 slots) - __4th__ Confusion, Honeyed Words, Translocate (3 slots)"
sourcebook: "_NPC Core_, page 192."
```

```encounter-table
name: Halfling Yarnspinner
creatures:
  - 1: Halfling Yarnspinner
```
