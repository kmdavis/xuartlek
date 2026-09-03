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
languages: "Aklo, Alghollthu, Common, Sakvroth, Thalassic; _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +27, Athletics +24, Deception +28, Intimidation +26, Lore +29, Occultism +29, Society +27, Stealth +24"
abilityMods: [6, 6, 8, 7, 5, 6]
abilities_top:
  - name: "Numbing Lights"
    desc: "(aura, light, visual) 30 feet. The vidileth exudes dim light. Creatures within the light must attempt a DC 34 Will save each round, becoming stupefied 1 on a failure (or increase their stupefied value from numbing lights by 1, to a maximum of 4)."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +26; __Ref__: +22; __Will__: +24 +2 status to all saves vs. magic"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ controlled, electricity, mental; __Resistances__ cold 20"
speed: "10 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +28 (Magical, reach 10 feet, versatile S) __Damage__ 3d8+12 piercing plus consume memories"
  - name: "Melee"
    desc: "⬻ claw +28 (Agile, Magical, reach 20 feet) __Damage__ 3d10+12 slashing plus shape flesh"
  - name: "Melee"
    desc: "⬻ tentacle +28 (Agile, Electricity, Magical, reach 20 feet) __Damage__ 7d6 electricity plus thoughtlance"
abilities_bot:
  - name: "Change Shape"
    desc: "⭓ (Concentrate, Occult, Polymorph)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "A vidileth takes on the appearance of a humanoid of Large, Medium, or Small size or resumes its true form. While in humanoid form, the vidileth's Speed is 30 feet, and it loses its numbing lights aura and swim Speed. If the humanoid form assumed lacks the aquatic trait, the vidileth loses its own aquatic trait as well. In humanoid form, the vidileth can use weapons or make Strikes that work like its tentacle attack but use the reach of its current form. If the form has fangs or claws, the vidileth can also make such Strikes."
  - name: "Consume Memories"
    desc: "(Mental, Occult) When the vidileth hits with a fangs Strike, the target must succeed at a DC 34 Will save or take 3d6 mental damage. The vidileth gains temporary Hit Points equal to the damage dealt and learns some of the creature's memories (subject to the GM's discretion)."
  - name: "Delayed Suggestion"
    desc: "(Occult) When a vidileth successfully casts _dominate_ on a creature, a _suggestion_ spell triggers when the _dominate_ spell ends. This _suggestion_ usually causes the target to return to the vidileth, so the creature can cast _dominate_ again, but a vidileth can set the _suggestion_ to different orders if it wishes."
  - name: "Shape Flesh"
    desc: "⬻ (Curse, Occult, Manipulate)"
  - name: "Requirements"
    desc: "The vidileth's last action was a success with a claw Strike"
  - name: "Effect"
    desc: "The vidileth sloppily modifies the target's flesh. They must succeed at a DC 34 Fortitude save or permanently receive the veiled master's choice of clumsy 2, enfeebled 2, or a –10 status penalty to Speed."
  - name: "Tentacle Flurry"
    desc: "⬺ The vidileth makes a tentacle Strike against each creature within its reach. Make only one attack roll, and roll damage once for all targets."
  - name: "Thoughtlance"
    desc: "(Curse, Occult) A creature touched by the vidileth's tentacles must attempt a DC 34 Will save, becoming slowed 1 on a failure or slowed 2 on a critical failure. Each time the affected creature ends its turn, its slowed value decreases by 1."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __3rd__ Hypnotize (at will), Levitate (at will), Mind Reading (at will), Water Breathing (at will) - __5th__ Illusory Object (at will), Mirage (at will), Sending (at will), Translocate (×3) - __6th__ Dominate (×3) - __7th__ Illusory Disguise (at will) - __8th__ Illusory Scene (at will), Suggestion (×3) - __9th__ Project Image (at will) - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 37 - __3rd__ Geas (5th)"
sourcebook: "_Monster Core_, page 12."
```

```encounter-table
name: Vidileth
creatures:
  - 1: Vidileth
```
