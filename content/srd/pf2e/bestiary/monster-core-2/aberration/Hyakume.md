---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4444"
socialImage: og-image.png
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
    desc: "+29; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; telepathy 100 feet (page 362)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +30, [[srd/pf2e/compendium/rules-elements/skills/Lore|Bardic Lore]] +28, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +30, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +25, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +25, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +30, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +27, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +28, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +25"
abilityMods: [4, 6, 4, 9, 6, 4]
abilities_top:
  - name: "Light Blindness"
    desc: ""
  - name: "Lore Master"
    desc: "A hyakume can use their [[srd/pf2e/compendium/rules-elements/skills/Lore|Bardic Lore]] skill to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] on any topic, and they know any languages common to an area they have spent a day or more in."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +23; __Ref__: +25; __Will__: +29 +2 status to all saves vs. magic"
hp: 275
health:
  - name: "HP"
    desc: "275; __Immunities__ [[srd/pf2e/compendium/spells/rank-4/Confusion|_confusion_]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d10+10 bludgeoning plus scatterbrain palm"
abilities_bot:
  - name: "Eye Probe"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Up to six of the hyakume's eyes detach from the hyakume's body. Each eye has AC 26, HP 1, and a fly speed of 40 feet. The hyakume can see through all of their eye probes. They can move the probes all in separate directions using a single [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|Sustain]] action. A hyakume can have no more than six eye probes active at a time; using this ability to create more causes the eye or eyes farthest away to shrivel and die. The hyakume can deliver touch spells through their eye probes and can make melee spell attacks through them. In addition, the hyakume can Steal Memories through an eye probe using a single action by touching the target with the eye."
  - name: "Scatterbrain Palm"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) A creature hit by the hyakume's fist Strike must attempt a DC 36 Will save. The creature is then temporarily immune until start of its next turn."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] 1."
  - name: "Failure"
    desc: "The creature is stunned 2."
  - name: "Critical Failure"
    desc: "The creature is stunned 3 and the hyakume can use Steal Memories on the target as part of this action."
  - name: "Steal Memories"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) The hyakume reaches out with their mind and attempts to steal memories from a creature within 30 feet. The target must succeed at a DC 40 Will saving throw or become [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 2 and have some of its memories stolen. The hyakume learns some of the target's memories (chosen by the GM), which are then lost to the target. Memory Thieves Hyakume jealously hoard knowledge in the form of memories, their own or stolen. They stalk temples and libraries, memorizing hundreds of texts before obliterating them all. Hyakume have earned a mistaken reputation as nocturnal guardians of shrines and other archives of wisdom. Though they can occasionally thwart thieves and tomb raiders, they do so only to keep the repository's knowledge for themselves."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40, attack +32 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]] (at will), [[srd/pf2e/compendium/spells/rank-3/Hypercognition|Hypercognition]] (at will), [[srd/pf2e/compendium/spells/rank-3/Ring of Truth|Ring of Truth]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (×2), [[srd/pf2e/compendium/spells/rank-1/Mindlink|Mindlink]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×2), [[srd/pf2e/compendium/spells/rank-8/Disappearance|Disappearance]], [[srd/pf2e/compendium/spells/rank-8/Hidden Mind|Hidden Mind]]"
sourcebook: "_Monster Core 2_, page 196."
```

```encounter-table
name: Hyakume
creatures:
  - 1: Hyakume
```
