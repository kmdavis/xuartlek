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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +26, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +15, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +26"
abilityMods: [2, 4, 2, 4, 2, 5]
abilities_top:
  - name: "Immaculate Instrument"
    desc: "A sublime breath carries a single tool, prop, or instrument related to its chosen craft, such as a mask, sash, or paintbrush. As long as they possess their immaculate instrument, they treat any critical failures on [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] or [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] checks as failures."
  - name: "Artistic Specialist"
    desc: "In a recital, competition, or other measure of artistic skill, a sublime breath is a 12th-level challenge."
  - name: "Thought Slips Away"
    desc: "The sublime breath's ephemeral lightness makes them impossible to grasp. They use their [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] modifier to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumble Through]], [[srd/pf2e/compendium/rules-elements/actions/player-core#High Jump|High Jump]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Long Jump|Long Jump]]. When they [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leap]], High Jump, or Long Jump, the movement does not provoke reactions."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/artifacts/cursed-immaculate-instrument|_immaculate instrument_]]"
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
    desc: "⬻ soft touch +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|Spirit]]) __Damage__ 2d4+8 bludgeoning plus 1d6 mental and 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ feigned strike +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|Spirit]]) __Damage__ 2d6 mental and 2d6 spirit"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Remove a Condition_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The sublime breath removes any one condition currently affecting them."
  - name: "Artistic Creation"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The sublime breath's art is so real that it takes shape in the hearts of those who witness it. The sublime breath crafts, acts, recites a tale or song, or otherwise uses their art to create a work of art in a 10-foot burst within 60 feet. The creation is perceptible and tangible to creatures that don't disbelieve it and it affects them accordingly; for instance a ladder could be climbed, and a campfire would provide heat and even be able to cook food for an affected creature. A hazardous creation deals 4d6 damage to creatures that enter or begin their turn in the area (DC 24 basic Will save), of a type matching the creation, usually a physical damage type or a common energy type such as fire, acid, or cold. The creation lasts until the end of the sublime breath's next turn, though the sublime breath can Sustain it to prolong the effect for up to 1 minute. The sublime breath can Sustain any number of Artistic Creations with a single action."
  - name: "Artistic Destruction"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Requirements"
    desc: "The sublime breath has either used Artistic Creation this turn or Sustained an Artistic Creation this turn"
  - name: "Effect"
    desc: "The sublime breath destroys their creations to make way for new growth. All of their currently sustained Artistic Creations detonate, dealing 8d6 damage to all enemy creatures either within a creation or within a 10-foot burst of it (DC 24 basic Will save). The damage type matches the creation. Creatures in multiple overlapping bursts take damage only once, of the type of their choice. The sublime breath then cannot use Artistic Creation for 1d4 turns."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The sublime breath can take on the appearance of any Medium or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but might change the damage type their Strikes deal. The sublime breath instinctively takes on the appearance an observer finds most inspiring. The first time they become [[srd/pf2e/compendium/rules-elements/conditions#Observed|observed]], they use Change Shape as a free action, even if they were unaware they were being observed, they take on a specific appearance reflecting the hidden desires, hopes, artistic inclinations, or similar deep-seated emotions of a single observer. As long as the sublime breath can be observed by this creature and maintains this shape, the observer gains a +1 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] and [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] checks and takes a –1 circumstance penalty to Will saves against the sublime breath or to any check or DC that would attempt to capture or restrain them, such as attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] or the DC of a [[srd/pf2e/compendium/spells/rank-3/paralyze|_paralyze_]] spell."
  - name: "Hours Go By"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A sublime breath's presence can allow artists and artisans to work almost effortlessly in a state of perfect flow. The sublime breath encourages a single creature within 60 feet, who becomes [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]]. They can spend the extra action only to Sustain a spell or other ability."
sourcebook: "_War of Immortals_, page 201."
```

```encounter-table
name: Sublime Breath
creatures:
  - 1: Sublime Breath
```
