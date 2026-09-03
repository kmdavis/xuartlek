---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rhu-Chalik"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Rhu-Chalik"
level: 6
source: "Monster Core"
aon_id: "creature-2928"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2928"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Rhu-Chalik"
level: "Creature 6"
size: "Small"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; greater darkvision, thoughtsense 60 feet"
languages: "Aklo; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +13, Deception +13, Diplomacy +13, Intimidation +13, Stealth +15"
abilityMods: [3, 3, 4, 2, 5, 3]
abilities_top:
  - name: "Thoughtsense"
    desc: "The rhu-chalik senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +11; __Will__: +17"
hp: 95
health:
  - name: "HP"
    desc: "95"
abilities_mid:
  - name: "No Breath"
    desc: "A rhu-chalik doesn't breathe and is immune to effects that require breathing (such as inhaled poisons)."
speed: "5 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +15 (Agile) __Damage__ 2d4+6 bludgeoning plus 1d6 mental and excruciating enzyme"
abilities_bot:
  - name: "Excruciating Enzyme"
    desc: "(Occult, Poison) A rhu-chalik's tendrils secrete an enzyme that causes intense pain. A living creature hit by a tendril Strike must succeed at a DC 24 Fortitude save or become sickened 1 from the pain."
  - name: "Label Memories"
    desc: "⬺ (Mental, Occult) The rhu-chalik invades the mind of a target within 100 feet, sorting the memories into alien structures for transmission. The target must attempt a DC 24 Will save."
  - name: "Critical Success"
    desc: "The target creature is unaffected and temporarily immune to Label Memories for 1 minute."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target becomes stupefied 2 for 1 minute as its mind is reorganized to fit the rhu-chalik's needs. If it's already stupefied by this effect, the target instead becomes confused for 1 minute or until it recovers due to taking damage."
  - name: "Critical Failure"
    desc: "As failure, but if the target is already stupefied by Label Memories, they become paralyzed for 1 minute instead of confused."
  - name: "Transmit Memories"
    desc: "⬽ (Concentrate, Mental, Occult)"
  - name: "Requirements"
    desc: "The rhu-chalik is adjacent to a creature paralyzed due to Label Memories"
  - name: "Effect"
    desc: "The rhu-chalik copies the creature's consciousness and mentally sends this copied consciousness through the void of space to their waiting masters. The target creature is deeply disoriented by this procedure, becoming stupefied 2 for 1 day afterward. Connoisseurs of Thoughts Rhu-chaliks lack both mouths and digestive systems. Instead, they gain sustenance from the thoughts and emotions of sentient beings. Each emotion has a distinctive flavor to rhu-chaliks and, as this feeding doesn't harm the food source, rhu-chaliks often dine repeatedly upon their favorite minds. Some rhu-chaliks even incite various emotions in their prey to elicit new tastes for their mental palettes."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24 - __2nd__ Invisibility (self only; at will) - __3rd__ Mind Reading (at will) - __4th__ Rewrite Memory - __5th__ Mind Probe"
sourcebook: "_Monster Core_, page 104."
```

```encounter-table
name: Rhu-Chalik
creatures:
  - 1: Rhu-Chalik
```
