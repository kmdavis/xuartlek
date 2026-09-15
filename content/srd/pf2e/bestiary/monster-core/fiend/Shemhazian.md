---
noteType: pf2eMonster
aliases: "Shemhazian"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Shemhazian"
level: 16
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2900"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shemhazian"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "+30; darkvision, scent (imprecise) 60 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +31, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +25, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +27, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +30"
abilityMods: [9, 5, 7, 0, 6, 3]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +26; __Will__: +27 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 350
health:
  - name: "HP"
    desc: "350; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Paralyzing Gaze"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. A non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Demon|demon]] creature that ends its turn in the aura must attempt a DC 35 Fortitude save. If it fails, it's [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] for 1 round, and if it critically fails, it is [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] for 1 round."
  - name: "Succor Vulnerability"
    desc: "A shemhazian's mutilation is a part of them, and they can't bear to see it reversed. The first time each round that a creature heals from damage the shemhazian dealt on their last turn, the demon takes 3d6 mental damage."
  - name: "Tail Whip"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the shemhazian's tail leaves a square during a [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] action it's using"
  - name: "Effect"
    desc: "The shemhazian attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] the triggering creature. On a success, the creature also takes damage as if the shemhazian had hit with a tail Strike, and if the creature was flying, it falls 30 feet."
speed: "35 feet, climb 20 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d12+17 piercing plus enfeebling bite"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d8+17 slashing"
  - name: "Melee"
    desc: "⬻ pincer +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d8+17 bludgeoning plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d8+17 slashing"
abilities_bot:
  - name: "Enfeebling Bite"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) If the shemhazian's jaws Strike damages a creature, the target is enfeebled 3 for 24 hours. The target can attempt a DC 37 Fortitude save to reduce this to enfeebled 1 (or be unaffected on a critical success)."
  - name: "Focused Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The shemhazian focuses their gaze on a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Demon|demon]] creature they can see within 30 feet. If that creature isn't already [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] by the shemhazian's paralyzing gaze, it must attempt a save against the shemhazian's paralyzing gaze. If that creature is slowed, it must succeed at a DC 35 Fortitude save or be [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] for 1 round. A shemhazian can't use this ability against the same creature more than once per round."
  - name: "Rend"
    desc: "⬻ claw"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Clairvoyance|Clairvoyance]] (×3), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Scouting Eye|Scouting Eye]] (×3), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 37 - __1st__ [[srd/pf2e/compendium/spells/rituals/Demonic Pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 81."
```

```encounter-table
name: Shemhazian
creatures:
  - 1: Shemhazian
```
