---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Golem"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Golem"
level: 8
source: "Monster Core 2"
aon_id: "creature-4417"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4417"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Golem"
level: "Creature 8"
size: "Large"
trait_01: "Construct"
trait_02: "Earth"
trait_03: "Holy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +18"
abilityMods: [6, 2, 5, 1, 4, 0]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +19; __Ref__: +12; __Will__: +16"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/damage-rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]"
abilities_mid:
  - name: "Day of Rest"
    desc: "A golem needs 1 day of rest per week or it becomes uncontrollable. An uncontrollable golem is unable to cast spells, and it takes a –2 circumstance penalty to checks made using Wisdom, including Will saves. While uncontrollable, the golem loses its immunity to [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]. The golem is uncontrollable until it takes a day of rest."
  - name: "Faithful"
    desc: "A golem faithfully serves its creator as long as it's not in an uncontrollable state (see above). While the golem is faithful, it follows the commands of its creator, even to its own detriment. While the golem remains faithful to its creator, the golem can't be confused or controlled by any creature other than its creator."
  - name: "Hefty Helper"
    desc: "The golem can carry 13 Bulk before becoming [[srd/pf2e/compendium/rules-elements/conditions#Encumbered|encumbered]] and can carry a maximum Bulk of 18."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+8 bludgeoning plus consecrated fists"
abilities_bot:
  - name: "Consecrated Fists"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) After the golem casts a [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] spell, their Strikes deal an additional 1d8 [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] damage and gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]] and holy traits. These benefits last until the end of the golem's next turn."
  - name: "Rampage"
    desc: "⬺"
  - name: "Requirements"
    desc: "The golem is uncontrollable"
  - name: "Effect"
    desc: "The golem makes a melee Strike against every creature in its reach, whether that creature is an ally or not. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after all the Strikes are complete. Temple Guardians Golems have been used to guard and assist at temples across the Inner Sea region, though they're said to have originated in northern Garund. Only followers of holy deities can create golems, most of which are given life by priests of Desna or Shelyn, or sometimes Casandalee."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×4) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/calm|Calm]] (×2), [[srd/pf2e/compendium/spells/rank-3/holy-light|Holy Light]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/divine-wrath|Divine Wrath]] (×2)"
sourcebook: "_Monster Core 2_, page 169."
```

```encounter-table
name: Golem
creatures:
  - 1: Golem
```
