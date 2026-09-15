---
noteType: pf2eMonster
aliases: "Vidileth"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Vidileth"
level: 14
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2813"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vidileth"
level: "Creature 14"
size: "Large"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "+25; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], Alghollthu, [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +29, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +27, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +24"
abilityMods: [6, 6, 8, 7, 5, 6]
abilities_top:
  - name: "Numbing Lights"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. The vidileth exudes dim light. Creatures within the light must attempt a DC 34 Will save each round, becoming [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] on a failure (or increase their stupefied value from numbing lights by 1, to a maximum of 4)."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +26; __Ref__: +22; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 20"
speed: "10 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 3d8+12 piercing plus consume memories"
  - name: "Melee"
    desc: "⬻ claw +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d10+12 slashing plus shape flesh"
  - name: "Melee"
    desc: "⬻ tentacle +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 7d6 electricity plus thoughtlance"
abilities_bot:
  - name: "Change Shape"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "A vidileth takes on the appearance of a [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]] of Large, Medium, or Small size or resumes its true form. While in humanoid form, the vidileth's Speed is 30 feet, and it loses its numbing lights aura and swim Speed. If the humanoid form assumed lacks the [[srd/pf2e/compendium/rules-elements/traits/player-core/Aquatic|aquatic]] trait, the vidileth loses its own aquatic trait as well. In humanoid form, the vidileth can use weapons or make Strikes that work like its tentacle attack but use the reach of its current form. If the form has fangs or claws, the vidileth can also make such Strikes."
  - name: "Consume Memories"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) When the vidileth hits with a fangs Strike, the target must succeed at a DC 34 Will save or take 3d6 mental damage. The vidileth gains temporary Hit Points equal to the damage dealt and learns some of the creature's memories (subject to the GM's discretion)."
  - name: "Delayed Suggestion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) When a vidileth successfully casts [[srd/pf2e/compendium/spells/rank-6/Dominate|_dominate_]] on a creature, a [[srd/pf2e/compendium/spells/rank-4/Suggestion|_suggestion_]] spell triggers when the _dominate_ spell ends. This _suggestion_ usually causes the target to return to the vidileth, so the creature can cast _dominate_ again, but a vidileth can set the _suggestion_ to different orders if it wishes."
  - name: "Shape Flesh"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The vidileth's last action was a success with a claw Strike"
  - name: "Effect"
    desc: "The vidileth sloppily modifies the target's flesh. They must succeed at a DC 34 Fortitude save or permanently receive the veiled master's choice of [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 2]], [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled 2]], or a –10 status penalty to Speed."
  - name: "Tentacle Flurry"
    desc: "⬺ The vidileth makes a tentacle Strike against each creature within its reach. Make only one attack roll, and roll damage once for all targets."
  - name: "Thoughtlance"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) A creature touched by the vidileth's tentacles must attempt a DC 34 Will save, becoming [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] on a failure or slowed 2 on a critical failure. Each time the affected creature ends its turn, its slowed value decreases by 1."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Hypnotize|Hypnotize]] (at will), [[srd/pf2e/compendium/spells/rank-3/Levitate|Levitate]] (at will), [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will), [[srd/pf2e/compendium/spells/rank-2/Water Breathing|Water Breathing]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-4/Mirage|Mirage]] (at will), [[srd/pf2e/compendium/spells/rank-5/Sending|Sending]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (×3) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-5/Illusory Scene|Illusory Scene]] (at will), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (×3) - __9th__ [[srd/pf2e/compendium/spells/rank-7/Project Image|Project Image]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 37 - __3rd__ Geas (5th)"
sourcebook: "_Monster Core_, page 12."
```

```encounter-table
name: Vidileth
creatures:
  - 1: Vidileth
```
