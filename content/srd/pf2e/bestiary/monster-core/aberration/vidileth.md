---
obsidianUIMode: preview
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
aon_id: "creature-2813"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2813"
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
    desc: "Perception +25; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], Alghollthu, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +29, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [6, 6, 8, 7, 5, 6]
abilities_top:
  - name: "Numbing Lights"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. The vidileth exudes dim light. Creatures within the light must attempt a DC 34 Will save each round, becoming [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] on a failure (or increase their stupefied value from numbing lights by 1, to a maximum of 4)."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +26; __Ref__: +22; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20"
speed: "10 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 3d8+12 piercing plus consume memories"
  - name: "Melee"
    desc: "⬻ claw +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d10+12 slashing plus shape flesh"
  - name: "Melee"
    desc: "⬻ tentacle +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 7d6 electricity plus thoughtlance"
abilities_bot:
  - name: "Change Shape"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "A vidileth takes on the appearance of a [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] of Large, Medium, or Small size or resumes its true form. While in humanoid form, the vidileth's Speed is 30 feet, and it loses its numbing lights aura and swim Speed. If the humanoid form assumed lacks the [[srd/pf2e/compendium/rules-elements/traits/player-core/aquatic|aquatic]] trait, the vidileth loses its own aquatic trait as well. In humanoid form, the vidileth can use weapons or make Strikes that work like its tentacle attack but use the reach of its current form. If the form has fangs or claws, the vidileth can also make such Strikes."
  - name: "Consume Memories"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) When the vidileth hits with a fangs Strike, the target must succeed at a DC 34 Will save or take 3d6 mental damage. The vidileth gains temporary Hit Points equal to the damage dealt and learns some of the creature's memories (subject to the GM's discretion)."
  - name: "Delayed Suggestion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) When a vidileth successfully casts [[srd/pf2e/compendium/spells/rank-6/dominate|_dominate_]] on a creature, a [[srd/pf2e/compendium/spells/rank-4/suggestion|_suggestion_]] spell triggers when the _dominate_ spell ends. This _suggestion_ usually causes the target to return to the vidileth, so the creature can cast _dominate_ again, but a vidileth can set the _suggestion_ to different orders if it wishes."
  - name: "Shape Flesh"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The vidileth's last action was a success with a claw Strike"
  - name: "Effect"
    desc: "The vidileth sloppily modifies the target's flesh. They must succeed at a DC 34 Fortitude save or permanently receive the veiled master's choice of [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 2]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 2]], or a –10 status penalty to Speed."
  - name: "Tentacle Flurry"
    desc: "⬺ The vidileth makes a tentacle Strike against each creature within its reach. Make only one attack roll, and roll damage once for all targets."
  - name: "Thoughtlance"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) A creature touched by the vidileth's tentacles must attempt a DC 34 Will save, becoming [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] on a failure or slowed 2 on a critical failure. Each time the affected creature ends its turn, its slowed value decreases by 1."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/hypnotize|Hypnotize]] (at will), [[srd/pf2e/compendium/spells/rank-3/levitate|Levitate]] (at will), [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]] (at will), [[srd/pf2e/compendium/spells/rank-2/water-breathing|Water Breathing]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-4/mirage|Mirage]] (at will), [[srd/pf2e/compendium/spells/rank-5/sending|Sending]] (at will), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (×3) - __6th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-5/illusory-scene|Illusory Scene]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] (×3) - __9th__ [[srd/pf2e/compendium/spells/rank-7/project-image|Project Image]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 37 - __3rd__ Geas (5th)"
sourcebook: "_Monster Core_, page 12."
```

```encounter-table
name: Vidileth
creatures:
  - 1: Vidileth
```
