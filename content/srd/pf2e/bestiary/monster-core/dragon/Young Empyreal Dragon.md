---
noteType: pf2eMonster
aliases: "Young Empyreal Dragon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Young Empyreal Dragon"
level: 10
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2941"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Empyreal Dragon"
level: "Creature 10"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision, lifesense (imprecise) 30 feet, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, Heaven Lore +21, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +21, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +21, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +19"
abilityMods: [6, 3, 4, 3, 5, 4]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +19; __Will__: +21 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 10"
abilities_mid:
  - name: "Inspiring Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 20 feet. The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
  - name: "Divine Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "60 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+9 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claws +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d8+9 slashing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+9 bludgeoning plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ wing +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 1d10+9 slashing plus 1d8 spirit"
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
    desc: "Each creature must succeed at a DC 29 Fortitude save or be pushed until it's no longer in the aura."
  - name: "Restoration"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]) Each creature recovers 5d8 Hit Points."
  - name: "Spirit Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) The dragon unleashes a blast of holy fire that deals 9d8 spirit damage in a 40-foot cone (DC 29 basic Reflex save). The dragon can't use Spirit Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 114."
```

```encounter-table
name: Young Empyreal Dragon
creatures:
  - 1: Young Empyreal Dragon
```
