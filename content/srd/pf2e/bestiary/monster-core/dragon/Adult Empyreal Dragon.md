---
noteType: pf2eMonster
aliases: "Adult Empyreal Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Empyreal Dragon"
level: 14
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2942"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Empyreal Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
modifier: 27
perception:
  - name: "Perception"
    desc: "+27; darkvision, lifesense (imprecise) 30 feet, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +25, Heaven Lore +26, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +24"
abilityMods: [8, 4, 6, 4, 7, 5]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +24; __Will__: +26 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 10"
abilities_mid:
  - name: "Inspiring Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 20 feet. The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
  - name: "Divine Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "70 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d10+11 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claws +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+11 slashing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ tail +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d10+11 bludgeoning plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ wing +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+11 slashing plus 1d8 spirit"
abilities_bot:
  - name: "Direct Halo"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]]) The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Spirit Breath whenever they score a critical hit with a Strike."
  - name: "Halo Pulse"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) The dragon chooses one effect to impose on creatures in their inspiring presence aura. The dragon can't use Halo Pulse again for 1d4 rounds."
  - name: "Repulsion"
    desc: "Each creature must succeed at a DC 34 Fortitude save or be pushed until it's no longer in the aura."
  - name: "Restoration"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]) Each creature recovers 7d8 Hit Points."
  - name: "Spirit Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) The dragon unleashes a blast of holy fire that deals 12d8 spirit damage in a 50-foot cone (DC 34 basic Reflex save). The dragon can't use Spirit Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26 - __5th__ [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (at will; self only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 115."
```

```encounter-table
name: Adult Empyreal Dragon
creatures:
  - 1: Adult Empyreal Dragon
```
