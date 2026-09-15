---
noteType: pf2eMonster
aliases: "Raktavarna"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/rakshasa
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Raktavarna"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3160"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Raktavarna"
level: "Creature 1"
size: "Tiny"
trait_01: "Rakshasa"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7"
abilityMods: [1, 4, 2, 1, 1, 2]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +6 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]] magic"
hp: 20
health:
  - name: "HP"
    desc: "20; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 3"
abilities_mid:
  - name: "Knowledge of Delusion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A creature that fails a [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] check or a Perception check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] on a rakshasa is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] until the end of its next turn."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]]) __Damage__ 1d6+1 piercing plus raktavarna venom"
abilities_bot:
  - name: "Betraying Bite"
    desc: "A raktavarna gains a +2 bonus to Strikes against any creature that is holding it."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The raktavarna takes on the appearance of a Tiny inanimate object. If, while transformed, the raktavarna takes any action other than the purely mental (such as [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]]), they immediately revert to their original form. Until then, they can use [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonate]] the object."
  - name: "Designate Master"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Exploration|Exploration]]) The raktavarna spends 10 minutes on an invocation alongside another creature. That creature becomes the raktavarna's master until the raktavarna dies or Dismisses the effect. The master gains the Master's Eyes activity as long as the bond lasts."
  - name: "Master's Eyes"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Scrying|Scrying]]) The master observes the world through the raktavarna's eyes instead of their own, using the raktavarna's Perception and darkvision. This lasts until the end of the master's next turn, but the master can Sustain the activity. This ability functions at any range, even on different planes of existence. If the raktavarna dies while their master is using this ability, the master is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 5]]."
  - name: "Raktavarna Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage and stupefied 2 (1 round)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/Command|Command]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]]"
sourcebook: "_Monster Core_, page 286."
```

```encounter-table
name: Raktavarna
creatures:
  - 1: Raktavarna
```
