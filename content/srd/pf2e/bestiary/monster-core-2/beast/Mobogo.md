---
noteType: pf2eMonster
aliases: "Mobogo"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/huge
statblock: inline
name: "Mobogo"
level: 10
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4476"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mobogo"
level: "Creature 10"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Beast"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision"
languages: "Boggard; [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|_speak with animals_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +21, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +19"
abilityMods: [7, 5, 6, -2, 5, 7]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +22; __Ref__: +17; __Will__: +19"
hp: 160
health:
  - name: "HP"
    desc: "160 , regeneration 30 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]]^ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]]^ or [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]])"
speed: "25 feet, fly 20 feet, swim 30 feet; swamp passage"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+13 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tongue +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]]) __Damage__ 2d6+13 bludgeoning plus tongue grab"
abilities_bot:
  - name: "Song of the Swamp"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The mobogo unleashes a booming croak. All boggards and mobogos within 50 feet gain a +2 status bonus to damage rolls and saves against fear for 1 round. Other creatures in the area of effect must attempt a DC 27 Will save."
  - name: "Success"
    desc: "The creature is unaffected and is temporarily immune for 24 hours."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 for 1d4 rounds."
  - name: "Critical Failure"
    desc: "The creature is slowed 2 for 1d4 rounds."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]]) Large, 2d12+6 bludgeoning, Rupture 19"
  - name: "Swamp Passage"
    desc: "A mobogo [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Ignore Difficult Terrain|ignores difficult terrain]] caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "A creature hit by the mobogo's tongue becomes [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] by the mobogo. The creature isn't [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]], but it can't move beyond the reach of the mobogo's tongue. A creature can sever the tongue with a Strike against AC 27 that deals at least 10 slashing damage. This deals no damage to the mobogo but prevents them from using their tongue Strike until they regrow their tongue, which takes 1 round. The mobogo can move without ending the tongue grab as long as the creature remains within the tongue's reach."
  - name: "Tongue Reposition"
    desc: "When a mobogo successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Repositions]] a creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] by their tongue, they increase the distance they can move that creature by 10 feet (a total of 15 feet on a success or 20 feet on a critical success); the creature must remain within the tongue's reach. Alternatively, the mobogo can transfer the grabbed creature to being grabbed by the mobogo's jaws. Children Of Gogunta [[srd/pf2e/compendium/gm/creature-families/Boggard|Boggards]] of Golarion believe mobogos to have hatched from the first clutch of eggs laid by their demon goddess [[srd/pf2e/compendium/deities/demon-lords/Gogunta|Gogunta]], following her awakening at the dawn of creation. Boggards, hatched millennia later from the second clutch, have been charged with serving and aiding their elder siblings in keeping her sacred swamplands untainted by the presence of outsiders."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27 - __4th__ [[srd/pf2e/compendium/spells/rank-1/Create Water|Create Water]] (at will), [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]], [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/Noise Blast|Noise Blast]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]] - __Constant (2nd)__ [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|Speak with Animals]], [[srd/pf2e/compendium/spells/rank-1/Vanishing Tracks|Vanishing Tracks]]"
  - name: "Rituals"
    desc: "DC 27 - __4th__ [[srd/pf2e/compendium/spells/rituals/Plant Growth|Plant Growth]]"
sourcebook: "_Monster Core 2_, page 224."
```

```encounter-table
name: Mobogo
creatures:
  - 1: Mobogo
```
