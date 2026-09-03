---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sorvuth-Ka"
tags:
  - pf2e/creature/level/24
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Sorvuth-Ka"
level: 24
source: "Monster Core 2"
aon_id: "creature-4560"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4560"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sorvuth-Ka"
level: "Creature 24"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Unique"
modifier: 42
perception:
  - name: "Perception"
    desc: "Perception +42; darkvision"
languages: "Aklo; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +45, Athletics +45, Intimidation +41, Survival +45"
abilityMods: [12, 9, 12, 10, 7, 5]
abilities_top:
  - name: "Slumbering Armageddon"
    desc: "Sorvuth-ka's slumber accelerates erosion and weathering, timed to always break at the point of maximum harm via rockslides, sinkholes, treefalls, and other collapses."
ac: 52
armorclass:
  - name: "AC"
    desc: "52; __Fort__: +42; __Ref__: +38; __Will__: +36"
hp: 550
health:
  - name: "HP"
    desc: "550 , regeneration absolute 25; __Immunities__ adaptive defenses, clumsy, disease, drained, enfeebled, mental, paralyzed, petrified, poison, polymorph, stupefied, visual"
abilities_mid:
  - name: "Absolute Regeneration"
    desc: "Sorvuth-ka's regeneration can be deactivated by slaying it with a weapon made from the bones of Chemnosit, Kothogaz, Ulunat, Volnagur, and Xotani."
  - name: "Adaptive Defenses"
    desc: "When injured, Sorvuth-ka's body adapts to ensure that the triggering insult can't harm it again. Immediately after it takes damage, it becomes immune to that type of damage. It can become immune to three different types of damage in this way, with newer immunities replacing older ones."
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 300 feet, DC 45"
  - name: "Reactive"
    desc: "Sorvuth-ka gains 3 reactions each round. It can still use only one reaction per trigger"
  - name: "Bleed Destruction"
    desc: "⭓"
  - name: "Trigger"
    desc: "Sorvuth-ka takes physical damage"
  - name: "Effect"
    desc: "Amber blood spurts from Sorvuth-ka's wound, creating a blood pool in a square adjacent to Sorvuth-ka. The blood remains in the area until removed or it dries, which typically takes 1 day."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +44 (Agile, finesse, reach 15 feet) __Damage__ 4d8+27 slashing plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ crystallized blood +44 (Propulsive, range increment 120 feet) __Damage__ 5d6+21 slashing"
abilities_bot:
  - name: "Amber Strikes"
    desc: "⬻"
  - name: "Requirements"
    desc: "Sorvuth-ka's previous action was a successful Strike against the target"
  - name: "Effect"
    desc: "After landing a Strike, Sorvuth-ka commands it blood to continue the assault, choosing one of the three following options: Crystallize, Inject, or Splash. If the previous attack was a critical hit, Amber Strikes is a free action. _Crystallize_ Sorvuth-ka's blood flows around the target's limbs before hardening. The creature must succeed at a DC 48 Reflex save or become immobilized and off-guard until it Escapes. If the creature was flying, it falls._Inject_ Sorvuth-ka's blood invades the target through its wounds. The target must succeed at a DC 48 Fortitude save or become sickened 2 (sickened 3 on a critical failure). As long as the target is sickened, Sorvuth-ka's blood will attempt to counteract any effect that could restore Hit Points to the target (counteract rank 10, counteract modifier +38)._Splash_ Sorvuth-ka's blood splashes violently, dazzling the target until the end of its next turn and creating a blood pool in a square adjacent to the target"
  - name: "Detonate Blood"
    desc: "⬺"
  - name: "Requirements"
    desc: "A pool of Sorvuth-ka's blood is within 500 feet"
  - name: "Effect"
    desc: "Sorvuth-ka's blood detonates into crystalline amber flechettes. Every creature either in the required blood pool's square or in a 10- foot emanation of that pool other than Sorvuth-ka takes 20d8 piercing damage (DC 48 basic Reflex save). On a critical failure, any resistances to physical damage the creature has are reduced by 10 for 1 minute."
  - name: "Rough Rampage"
    desc: "⬻"
  - name: "Requirements"
    desc: "Sorvuth-ka has at least one creature grabbed or restrained"
  - name: "Effect"
    desc: "Sorvuth-ka Strides, dragging any creatures it's grabbed or restrained along with it. Each grabbed or restrained creature takes 11d6 bludgeoning damage (DC 48 basic Fortitude save). On a failure, the creature is also clumsy 2 (or clumsy 3 on a critical failure) until it Escapes."
sourcebook: "_Monster Core 2_, page 300."
```

```encounter-table
name: Sorvuth-Ka
creatures:
  - 1: Sorvuth-Ka
```
