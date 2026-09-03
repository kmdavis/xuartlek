---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Totenmaske"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Totenmaske"
level: 7
source: "Monster Core 2"
aon_id: "creature-4585"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4585"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Totenmaske"
level: "Creature 7"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +15"
abilityMods: [4, 6, 2, 1, 2, 3]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +17; __Will__: +13"
hp: 130
health:
  - name: "HP"
    desc: "130 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d6+7 piercing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ claw +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d8+7 slashing"
abilities_bot:
  - name: "Drink Flesh"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Requirements"
    desc: "The totenmaske hit the same creature with two claw Strikes this turn and is still adjacent to it"
  - name: "Effect"
    desc: "The totenmaske drains flesh from the creature's body. The creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 2 and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 unless it succeeds at a DC 25 Fortitude save (sickened 2 and drained 2 on a critical failure)."
  - name: "Living Form"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The totenmaske takes the appearance of a Medium or smaller humanoid creature. This is either their form from before they became undead or the form of the last creature they successfully drained with Drink Flesh. This doesn't change the totenmaske's Speed or the attack and damage bonuses for their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Shape Flesh"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) After spending 1 minute in contact with a [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], or willing creature, a totenmaske can reshape the target's face, causing flesh to cover vital features. The target can attempt a DC 25 Fortitude save to resist; a critical success grants temporary immunity to Shape Flesh for 24 hours. Each time the totenmaske Shapes Flesh, they choose one feature: ears (target becomes [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]]), eyes (target becomes [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]]), mouth (target can't speak or eat), or nose (target can't smell). A creature with both its nose and mouth sealed can't breathe and begins to _suffocate_. Changes are permanent until reversed by removing this curse, but the sealed flesh can be surgically opened with a successful DC 25 [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check that takes 1d4 rounds and deals 1d6 slashing damage per round. Flesh Sculptors Some totenmaskes craft macabre “art” by shaping the flesh of their victims, spending hours, days, or even weeks molding a victim's skin or even fusing multiple creatures together into one piece. The horrifying results of this process can take the form of furniture made from flesh that still lives and breathes, “sculptures” that in no way resemble the human form, and even more twisted and depraved things."
sourcebook: "_Monster Core 2_, page 324."
```

```encounter-table
name: Totenmaske
creatures:
  - 1: Totenmaske
```
