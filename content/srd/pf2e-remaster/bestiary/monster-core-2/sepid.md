---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sepid"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Sepid"
level: 14
source: "Monster Core 2"
aon_id: "creature-4342"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4342"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sepid"
level: "Creature 14"
size: "Large"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; greater darkvision"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Arcana +20, Athletics +28, Deception +23, Intimidation +26, Religion +20, Stealth +23"
abilityMods: [8, 5, 8, 4, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+2 striking falchion_"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +28; __Ref__: +23; __Will__: +20 +1 status to all saves vs. magic"
hp: 350
health:
  - name: "HP"
    desc: "350; __Weaknesses__ cold iron 10, holy 10"
abilities_mid:
  - name: "Blatant Liar"
    desc: "While all divs delight in lying, sepids are compulsive and predictable liars who always do the opposite of what they claim they'll do. If a sepid is ever forced or compelled to tell the truth, they take 4d8 mental damage."
  - name: "Deflecting Lie"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature hits the sepid with a ranged Strike or a ranged spell attack"
  - name: "Effect"
    desc: "The sepid lies in an attempt to divert the attack. They roll a Deception check against the triggering creature's Perception DC. On a success, if the triggering attack roll was a success, it becomes a failure, and if the triggering attack roll was a critical hit, it becomes a normal success."
  - name: "Reactive Strike"
    desc: "⬲ A sepid gains an extra reaction each round that they can use only to make a Reactive Strike."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _falchion_ +30 (Forceful, magical, sweep, unholy) __Damage__ 2d10+16 slashing plus 1d6 mental"
  - name: "Melee"
    desc: "⬻ claw +28 (Agile, magical, unholy) __Damage__ 3d6+16 slashing plus 1d6 mental"
abilities_bot:
  - name: "Rain of Debris"
    desc: "⬺ (Divine, unholy) The sepid calls forth a vicious, torrential hail of stone, wood, metal, and similar debris in a 40-foot emanation, dealing 10d6 bludgeoning damage and 5d6 spirit damage. Each creature in the area other than the sepid must attempt a DC 31 basic Reflex saving throw. The sepid can't use Rain of Debris again for 1d4 rounds. Sepid Deceptions Given that sepids always do the opposite of what they say they will, it might seem difficult for these divs to deceive anyone, which is far from the truth. Often, sepids avoid making statements about their own intentions and instead give orders or speak in analogies, riddles, and anecdotes, allowing those they manipulate to parse out their rationales with clever forms of deception."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __Cantrips (7th)__ Detect Magic - __3rd__ Translate (at will; self only) - __4th__ Darkness (at will), Fly, Translocate (at will) - __7th__ Dispel Magic, Paralyze, Veil of Privacy (at will; self only)"
  - name: "Rituals"
    desc: "DC 34 - __1st__ Div Pact - __2nd__ Create Undead (no secondary caster required)"
sourcebook: "_Monster Core 2_, page 113."
```

```encounter-table
name: Sepid
creatures:
  - 1: Sepid
```
