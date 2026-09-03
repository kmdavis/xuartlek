---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sublime Breath"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/medium
statblock: inline
name: "Sublime Breath"
level: 6
source: "War of Immortals"
aon_id: "creature-3408"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3408"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Sublime Breath"
level: "Creature 6"
size: "Medium"
trait_01: "Fey"
trait_02: "Mythic"
trait_03: "Unique"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common, Fey; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +12, Crafting +26, Deception +18, Diplomacy +16, Nature +15, Performance +26"
abilityMods: [2, 4, 2, 4, 2, 5]
abilities_top:
  - name: "Immaculate Instrument"
    desc: "A sublime breath carries a single tool, prop, or instrument related to its chosen craft, such as a mask, sash, or paintbrush. As long as they possess their immaculate instrument, they treat any critical failures on Crafting or Performance checks as failures."
  - name: "Artistic Specialist"
    desc: "In a recital, competition, or other measure of artistic skill, a sublime breath is a 12th-level challenge."
  - name: "Thought Slips Away"
    desc: "The sublime breath's ephemeral lightness makes them impossible to grasp. They use their Performance modifier to Escape, Tumble Through, High Jump, or Long Jump. When they Leap, High Jump, or Long Jump, the movement does not provoke reactions."
  - name: "Items"
    desc: "_immaculate instrument_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +14; __Will__: +17 mythic resilience (Will)"
hp: 111
health:
  - name: "HP"
    desc: "111"
abilities_mid:
  - name: "Mythic Resilience"
    desc: "The sublime breath treats their Will saving throws as one step better than it actually is (so a critical failure is a failure, a failure is a success, and a success is a critical success)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ soft touch +16 (Mental, Spirit) __Damage__ 2d4+8 bludgeoning plus 1d6 mental and 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ feigned strike +16 (Mental, range 60 feet, Spirit) __Damage__ 2d6 mental and 2d6 spirit"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Remove a Condition_ ⬻ (concentrate)"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The sublime breath removes any one condition currently affecting them."
  - name: "Artistic Creation"
    desc: "⬻ (Illusion, Mental)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The sublime breath's art is so real that it takes shape in the hearts of those who witness it. The sublime breath crafts, acts, recites a tale or song, or otherwise uses their art to create a work of art in a 10-foot burst within 60 feet. The creation is perceptible and tangible to creatures that don't disbelieve it and it affects them accordingly; for instance a ladder could be climbed, and a campfire would provide heat and even be able to cook food for an affected creature. A hazardous creation deals 4d6 damage to creatures that enter or begin their turn in the area (DC 24 basic Will save), of a type matching the creation, usually a physical damage type or a common energy type such as fire, acid, or cold. The creation lasts until the end of the sublime breath's next turn, though the sublime breath can Sustain it to prolong the effect for up to 1 minute. The sublime breath can Sustain any number of Artistic Creations with a single action."
  - name: "Artistic Destruction"
    desc: "⬻ (Illusion, Mental)"
  - name: "Requirements"
    desc: "The sublime breath has either used Artistic Creation this turn or Sustained an Artistic Creation this turn"
  - name: "Effect"
    desc: "The sublime breath destroys their creations to make way for new growth. All of their currently sustained Artistic Creations detonate, dealing 8d6 damage to all enemy creatures either within a creation or within a 10-foot burst of it (DC 24 basic Will save). The damage type matches the creation. Creatures in multiple overlapping bursts take damage only once, of the type of their choice. The sublime breath then cannot use Artistic Creation for 1d4 turns."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The sublime breath can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but might change the damage type their Strikes deal. The sublime breath instinctively takes on the appearance an observer finds most inspiring. The first time they become observed, they use Change Shape as a free action, even if they were unaware they were being observed, they take on a specific appearance reflecting the hidden desires, hopes, artistic inclinations, or similar deep-seated emotions of a single observer. As long as the sublime breath can be observed by this creature and maintains this shape, the observer gains a +1 circumstance bonus to Crafting and Performance checks and takes a –1 circumstance penalty to Will saves against the sublime breath or to any check or DC that would attempt to capture or restrain them, such as attempts to Grapple or the DC of a _paralyze_ spell."
  - name: "Hours Go By"
    desc: "⬻ (Emotion, Mental) A sublime breath's presence can allow artists and artisans to work almost effortlessly in a state of perfect flow. The sublime breath encourages a single creature within 60 feet, who becomes quickened. They can spend the extra action only to Sustain a spell or other ability."
sourcebook: "_War of Immortals_, page 201."
```

```encounter-table
name: Sublime Breath
creatures:
  - 1: Sublime Breath
```
