---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hellcat"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Hellcat"
level: 7
source: "Monster Core 2"
aon_id: "creature-4437"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4437"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hellcat"
level: "Creature 7"
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]]; (can't speak any language), fiendish telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +14"
abilityMods: [6, 4, 4, 0, 3, 1]
abilities_top:
  - name: "Fiendish Telepathy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) This functions as telepathy, except that the hellcat can speak mentally to any creature, regardless of language. This doesn't grant the hellcat the ability to understand what the other creature is thinking, unless that creature also understands [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]]."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +17; __Will__: +12 +1 status to all saves vs. magic"
hp: 110
health:
  - name: "HP"
    desc: "110; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10, physical 5 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 __Damage__ 2d12+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+8 slashing"
abilities_bot:
  - name: "Elusive Terror"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) A hellcat can live within the fears of others and use their dread to hide from sight. The hellcat can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] in the presence of [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] creatures. If successful, the hellcat becomes [[srd/pf2e/compendium/rules-elements/conditions#Hidden|Hidden]] from frightened creatures as if it moved behind cover or into concealment, but must otherwise Hide normally from non-frightened creatures."
  - name: "Fearful Attack"
    desc: "The hellcat deals an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] creatures."
  - name: "Hell Pack Mindlink"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) The hellcat telepathically links its senses to all other hellcats within 100 feet for 10 minutes. It loses this contact with any hellcat that moves out of a 100-foot radius. While linked to at least one ally, the hellcat can't be flanked and gains a +2 status bonus to Will saving throws."
  - name: "Menacing Growl"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) The hellcat produces a low growl to disorient and frighten foes. The hellcat can cause this vocalization to originate from somewhere else within 30 feet. Non-fiends in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] must attempt a DC 25 Will save. The hellcat can't issue another Menacing Growl for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is frightened 4."
  - name: "Pounce"
    desc: "⬻ The hellcat [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] and makes a Strike at the end of that movement. If the hellcat began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after the ability's Strike. Cats And Dogs If there's one thing more certain to infuriate a hellcat than being treated as a mere animal, it's to compare it in any way to a [[srd/pf2e/bestiary/monster-core/beast/hell-hound|hell hound]]. Hellcats consider hell hounds little more than vermin infesting the hellscapes they call home and enjoy torturing them more than any other creature."
sourcebook: "_Monster Core 2_, page 190."
```

```encounter-table
name: Hellcat
creatures:
  - 1: Hellcat
```
