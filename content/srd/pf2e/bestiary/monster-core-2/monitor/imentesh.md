---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Imentesh"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/large
statblock: inline
name: "Imentesh"
level: 10
source: "Monster Core 2"
aon_id: "creature-4519"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4519"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Imentesh"
level: "Creature 10"
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, entropy sense (imprecise) 60 feet"
languages: "Chthonian, Empyrean, Protean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +19, Deception +21, Diplomacy +19, Performance +21, Stealth +21, Thievery +17"
abilityMods: [7, 5, 5, 7, 3, 5]
abilities_top:
  - name: "Entropy Sense"
    desc: "(divine, prediction) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. _Veil of privacy_ prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +19; __Will__: +17 +1 status to all saves vs. magical"
hp: 175
health:
  - name: "HP"
    desc: "175 (fast healing 5); __Resistances__ precision 10, protean anatomy 15"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "(divine) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If blinded or deafened, the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "25 feet, fly 25 feet, swim 25 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 (Magical, reach 10 feet) __Damage__ 2d10+11 piercing plus warpwave strike"
  - name: "Melee"
    desc: "⬻ claw +23 (Agile, Magical, reach 10 feet) __Damage__ 2d6+11 slashing"
  - name: "Melee"
    desc: "⬻ tail +23 (Magical, reach 15 feet) __Damage__ 2d10+11 bludgeoning plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The imentesh takes the appearance of any Large or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal."
  - name: "Constrict"
    desc: "⬻ 1d10+11 bludgeoning, DC 29"
  - name: "Inflict Warpwave"
    desc: "⬻ (Divine) An imentesh inflicts a warpwave on a creature within 100 feet (DC 29 Fortitude save to resist)."
  - name: "Sneak Attack"
    desc: "An imentesh's Strikes deal an additional 2d6 precision damage to off-guard targets."
  - name: "Warpwave Strike"
    desc: "(Divine) Any creature struck and damaged by an imentesh's jaws Strike must succeed at a DC 29 Fortitude save or be subject to a warpwave. Mouthpieces Of Chaos While rarely found in the Universe, imenteshes frequent interplanar hubs of culture and commerce. Imenteshes act as diplomats on behalf of any chorus they claim allegiance to. They can offer safe travel through the Maelstrom or even act as guides through the Maelstrom's evershifting Borderlands."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __3rd__ Haste, Mending, Shrink Item, Slow - __4th__ Creation, Shatter, Translocate (at will), Unfettered Movement - __5th__ Crisis of Faith, Dispel Magic, Sending, Translocate - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 260."
```

```encounter-table
name: Imentesh
creatures:
  - 1: Imentesh
```
