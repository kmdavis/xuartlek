---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jotund Troll"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/mutant
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Jotund Troll"
level: 15
source: "Monster Core 2"
aon_id: "creature-4594"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4594"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Jotund Troll"
level: "Creature 15"
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Mutant"
trait_04: "Rare"
trait_05: "Troll"
trait_06: "Wood"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision"
languages: "Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +29, Intimidation +27"
abilityMods: [8, 4, 8, -1, 6, 4]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +31; __Ref__: +24; __Will__: +23"
hp: 360
health:
  - name: "HP"
    desc: "360 , regeneration 40 (deactivated by electricity or fire); __Weaknesses__ electricity 15, fire 15"
abilities_mid:
  - name: "Head Regrowth"
    desc: "A jotund troll's regeneration can regrow severed heads. After regaining Hit Points from regeneration, the jotund troll attempts a DC 8 flat check. On a success, one missing head is fully restored; on a critical success, two missing heads are fully restored. If a jotund troll loses their last remaining head, they die immediately."
  - name: "Reactive Heads"
    desc: "A jotund troll gains an extra reaction per round for each of their heads beyond the first, which they can use only to make Reactive Strikes with their jaws or to Fast Swallow. They can't use more than 1 reaction for the same triggering action, even if a creature leaves several squares within their reach, and must use a different head for each Reactive Strike. Whenever one of the jotund troll's heads is severed, the troll loses 1 of their extra reactions per round."
  - name: "Furious Roar"
    desc: "⬲"
  - name: "Trigger"
    desc: "The jotund troll takes electricity or fire damage"
  - name: "Effect"
    desc: "The jotund troll uses their Cacophonous Roar and, if they're aware of the damage's source, can Stride toward it. If the jotund troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +29 (reach 15 feet) __Damage__ 3d12+14 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +29 (Agile, reach 15 feet) __Damage__ 3d10+14 slashing"
abilities_bot:
  - name: "Cacophonous Roar"
    desc: "⬻ (Auditory, emotion, incapacitation, mental, occult) The jotund troll roars from all their heads mystically distorting the listener's mind. Each nontroll creature in a 100-foot emanation must attempt a DC 34 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is stupefied 1 for 1 round."
  - name: "Failure"
    desc: "The creature is stupefied 2 for 1 round."
  - name: "Critical Failure"
    desc: "The creature is confused for 1 round."
  - name: "Fast Swallow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The jotund troll Grabs a creature with their jaws"
  - name: "Effect"
    desc: "The troll uses Swallow Whole."
  - name: "Ravenous Jaws"
    desc: "⬺ The jotund troll makes a number of jaws Strikes up to their number of heads, each against a different target. These attacks count toward the troll's multiple attack penalty, but the penalty doesn't increase until after the jotund troll makes all of these attacks."
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Swallow Whole"
    desc: "⬻ (attack) Medium, 3d12+8 bludgeoning, Rupture 36 Ravenous Mutants Jotund trolls arise with distressing regularity, particularly in areas like the magic-warped Mana Wastes and the radiation-wracked badlands of Numeria. Although they generally consume other trolls along with everything else, voracious jotund troll families haunt particularly desolate lands. The presence of a single jotund troll can lead an area to blight and ruin, beyond even the damage caused by its terrifying hunger."
sourcebook: "_Monster Core 2_, page 330."
```

```encounter-table
name: Jotund Troll
creatures:
  - 1: Jotund Troll
```
