---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hyakume"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Hyakume"
level: 15
source: "Monster Core 2"
aon_id: "creature-4444"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4444"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hyakume"
level: "Creature 15"
size: "Large"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision"
languages: "Aklo, Common; telepathy 100 feet (page 362)"
skills:
  - name: "Skills"
    desc: "Arcana +30, Bardic Lore +28, Crafting +30, Deception +27, Medicine +25, Nature +25, Occultism +30, Religion +27, Society +28, Thievery +25"
abilityMods: [4, 6, 4, 9, 6, 4]
abilities_top:
  - name: "Light Blindness"
    desc: ""
  - name: "Lore Master"
    desc: "A hyakume can use their Bardic Lore skill to Recall Knowledge on any topic, and they know any languages common to an area they have spent a day or more in."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +23; __Ref__: +25; __Will__: +29 +2 status to all saves vs. magic"
hp: 275
health:
  - name: "HP"
    desc: "275; __Immunities__ _confusion_; __Resistances__ mental 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +27 (Agile, finesse, magical, reach 10 feet) __Damage__ 3d10+10 bludgeoning plus scatterbrain palm"
abilities_bot:
  - name: "Eye Probe"
    desc: "⬽ (Occult)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Up to six of the hyakume's eyes detach from the hyakume's body. Each eye has AC 26, HP 1, and a fly speed of 40 feet. The hyakume can see through all of their eye probes. They can move the probes all in separate directions using a single Sustain action. A hyakume can have no more than six eye probes active at a time; using this ability to create more causes the eye or eyes farthest away to shrivel and die. The hyakume can deliver touch spells through their eye probes and can make melee spell attacks through them. In addition, the hyakume can Steal Memories through an eye probe using a single action by touching the target with the eye."
  - name: "Scatterbrain Palm"
    desc: "(Incapacitation, mental, occult) A creature hit by the hyakume's fist Strike must attempt a DC 36 Will save. The creature is then temporarily immune until start of its next turn."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is stunned 1."
  - name: "Failure"
    desc: "The creature is stunned 2."
  - name: "Critical Failure"
    desc: "The creature is stunned 3 and the hyakume can use Steal Memories on the target as part of this action."
  - name: "Steal Memories"
    desc: "⬽ (Emotion, mental, occult) The hyakume reaches out with their mind and attempts to steal memories from a creature within 30 feet. The target must succeed at a DC 40 Will saving throw or become stupefied 2 and have some of its memories stolen. The hyakume learns some of the target's memories (chosen by the GM), which are then lost to the target. Memory Thieves Hyakume jealously hoard knowledge in the form of memories, their own or stolen. They stalk temples and libraries, memorizing hundreds of texts before obliterating them all. Hyakume have earned a mistaken reputation as nocturnal guardians of shrines and other archives of wisdom. Though they can occasionally thwart thieves and tomb raiders, they do so only to keep the repository's knowledge for themselves."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40, attack +32 - __Cantrips (8th)__ Daze, Detect Magic, Read Aura - __4th__ Fly (at will), Hypercognition (at will), Ring of Truth (at will) - __7th__ Dispel Magic (×2), Mindlink (at will) - __8th__ Charm (×2), Disappearance, Hidden Mind"
sourcebook: "_Monster Core 2_, page 196."
```

```encounter-table
name: Hyakume
creatures:
  - 1: Hyakume
```
