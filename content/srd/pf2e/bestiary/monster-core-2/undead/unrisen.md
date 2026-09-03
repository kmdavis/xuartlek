---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Unrisen"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Unrisen"
level: 11
source: "Monster Core 2"
aon_id: "creature-4598"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4598"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Unrisen"
level: "Creature 11"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, lifesense 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
abilityMods: [7, 4, 5, -2, 6, 3]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +22; __Ref__: +17; __Will__: +21"
hp: 220
health:
  - name: "HP"
    desc: "220 (meant to live, void healing); __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ resurrection vulnerability"
abilities_mid:
  - name: "Meant to Live"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) Whenever an unrisen would take damage from [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] energy, it instead heals half that number of Hit Points."
  - name: "Resurrection Vulnerability"
    desc: "A creature with a prepared or spontaneous spell that can restore the dead to life (such as [[srd/pf2e/compendium/spells/rank-5/breath-of-life|_breath of life_]] or [[srd/pf2e/compendium/spells/rank-6/raise-dead|_raise dead_]]) can expend an appropriate spell slot as a 2-action activity to destroy an unrisen within 30 feet. The attempt fails if the unrisen succeeds at a Will save against the creature's spell DC."
  - name: "Rise Again"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) If the unrisen is reduced to 0 Hit Points by means other than fire damage, disintegration, or its resurrection vulnerability, it returns to unlife at the start of its next turn. It has 100 Hit Points and is [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] in the space in which it was destroyed. The unrisen can't be returned by this ability again for 1 hour."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 3d8+13 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d8+13 slashing plus Grab"
abilities_bot:
  - name: "Agonized Howl"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The unrisen howls in pain at its cursed existence. Creatures within a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] take 9d8 mental damage with a DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save. The unrisen can't use Agonized Howl again for 1d4 rounds."
  - name: "Awful Approach"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The unrisen reshapes its grotesque form to move swiftly. It Strides twice. Any living creature that can see the unrisen during this movement must succeed at a DC 28 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (or sickened 2 on a critical failure); this is a [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]] effect."
  - name: "Death Grip"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Requirements"
    desc: "The unrisen has a living creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The unrisen attempts to destroy its victim's life force so it shares in the unrisen's fate. The creature must succeed at a DC 30 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1. While the curse lasts, the creature regains only half as many HP from effects with both the [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] traits; if it dies, any attempt to raise it from the dead causes it to return as an unrisen. The curse ends automatically if the creature's doomed value is reduced to 0. Unrisen Salts An unrisen's essential salts, formed from its remaining distilled life essence, can be used for spells and rituals such as create undead or resurrect, replacing 600 gp worth of gemstones. The existence of these essential salts doesn't damage the soul of the unrisen's source creature, but devout Pharasmins still frown on their use."
sourcebook: "_Monster Core 2_, page 335."
```

```encounter-table
name: Unrisen
creatures:
  - 1: Unrisen
```
