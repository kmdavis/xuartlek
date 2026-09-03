---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Terotricus"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Terotricus"
level: 19
source: "Monster Core"
aon_id: "creature-3215"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3215"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Terotricus"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Fungus"
trait_02: "Rare"
trait_03: "Unholy"
modifier: 31
perception:
  - name: "Perception"
    desc: "Perception +31; darkvision, tremorsense (imprecise) 120 feet"
languages: "Chthonian, Elven, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +37, Deception +32, Intimidation +35, Nature +31, Survival +31"
abilityMods: [10, 5, 9, -1, 6, 5]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +34; __Ref__: +28; __Will__: +33 +1 status to all saves vs. magic"
hp: 370
health:
  - name: "HP"
    desc: "370 , regeneration 25 (deactivated by cold); __Immunities__ controlled, disease, paralyzed, sleep; __Resistances__ fire 15; __Weaknesses__ cold 15, cold iron 15, holy 15, slashing 10"
abilities_mid:
  - name: "Spore Cloud"
    desc: "(aura, disease) 30 feet. A creature entering the aura or starting its turn there is exposed to spore blight."
speed: "35 feet; burrow 25 feet, climb 25 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +37 (Magical, reach 20 feet, Unholy) __Damage__ 4d10+18 bludgeoning plus 2d6 spirit and Improved Grab or Improved Push 20 feet"
  - name: "Ranged"
    desc: "⬻ spores +37 (Brutal, Magical, range increment 80 feet, Unholy) __Damage__ 4d8+8 poison plus 2d6 spirit, spore blight, and sticky spores"
abilities_bot:
  - name: "Infest Environs"
    desc: "⬺ (Primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The terotricus is in a swamp or forested area"
  - name: "Effect"
    desc: "The terotricus drains nutrients from nearby trees and undergrowth while simultaneously infesting them with fungal growth. All non-magical plant life (though not plant creatures) within a 60-foot emanation withers and sprouts foul mold and slimy mushrooms, removing any cover and concealment provided by trees and undergrowth. In addition, the terotricus regains 200 Hit Points (this is a healing vitality effect)."
  - name: "Spore Blight"
    desc: "(Disease) Plants and fungi are immune"
  - name: "Saving Throw"
    desc: "DC 40 Fortitude"
  - name: "Stage 1"
    desc: "enfeebled 2 (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 4 and slowed 1 (1 day)"
  - name: "Stage 3"
    desc: "controlled by the terotricus (as _dominate_; 5d8 days)"
  - name: "Stage 4"
    desc: "dead"
  - name: "Sticky Spores"
    desc: "A creature hit by a terotricus's spores takes a –10-foot status penalty to all its Speeds for 1 minute. If the Strike was a critical hit, the creature is also immobilized until it Escapes (DC 40). Terotricus Myths The Kellids of Sarkoris dealt with their fair share of terotricuses during the era of the Worldwound, and these people developed unique rituals to purify tainted grounds with the help of ancestral spirits and feathers acquired from celestials. Far south of there, in what is now known as the Sodden Lands, wastelanders who learn of the presence of a terotricus—or “swampblight,” as they're called there— carry lanterns blessed by angels in the hopes that these lights will keep the terotricus at bay."
sourcebook: "_Monster Core_, page 326."
```

```encounter-table
name: Terotricus
creatures:
  - 1: Terotricus
```
