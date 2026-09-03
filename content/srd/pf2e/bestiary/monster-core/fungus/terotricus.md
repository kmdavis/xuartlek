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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +37, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +32, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +35, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +31, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +31"
abilityMods: [10, 5, 9, -1, 6, 5]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +34; __Ref__: +28; __Will__: +33 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 370
health:
  - name: "HP"
    desc: "370 , regeneration 25 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15, [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15, slashing 10"
abilities_mid:
  - name: "Spore Cloud"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]) 30 feet. A creature entering the aura or starting its turn there is exposed to spore blight."
speed: "35 feet; burrow 25 feet, climb 25 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d10+18 bludgeoning plus 2d6 spirit and Improved Grab or Improved Push 20 feet"
  - name: "Ranged"
    desc: "⬻ spores +37 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 80 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d8+8 poison plus 2d6 spirit, spore blight, and sticky spores"
abilities_bot:
  - name: "Infest Environs"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The terotricus is in a swamp or forested area"
  - name: "Effect"
    desc: "The terotricus drains nutrients from nearby trees and undergrowth while simultaneously infesting them with fungal growth. All non-magical plant life (though not [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]] creatures) within a 60-foot emanation withers and sprouts foul mold and slimy mushrooms, removing any cover and [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]] provided by trees and undergrowth. In addition, the terotricus regains 200 Hit Points (this is a [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]] [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] effect)."
  - name: "Spore Blight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|Plants]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/fungus|fungi]] are immune"
  - name: "Saving Throw"
    desc: "DC 40 Fortitude"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 2]] (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 4 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 day)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]] by the terotricus (as [[srd/pf2e/compendium/spells/rank-6/dominate|_dominate_]]; 5d8 days)"
  - name: "Stage 4"
    desc: "dead"
  - name: "Sticky Spores"
    desc: "A creature hit by a terotricus's spores takes a –10-foot status penalty to all its Speeds for 1 minute. If the Strike was a critical hit, the creature is also [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 40). Terotricus Myths The Kellids of Sarkoris dealt with their fair share of terotricuses during the era of the Worldwound, and these people developed unique rituals to purify tainted grounds with the help of ancestral spirits and feathers acquired from [[srd/pf2e/compendium/rules-elements/traits/player-core/celestial|celestials]]. Far south of there, in what is now known as the Sodden Lands, wastelanders who learn of the presence of a terotricus—or “swampblight,” as they're called there— carry lanterns blessed by angels in the hopes that these lights will keep the terotricus at bay."
sourcebook: "_Monster Core_, page 326."
```

```encounter-table
name: Terotricus
creatures:
  - 1: Terotricus
```
