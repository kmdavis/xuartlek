---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Larabay"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/medium
statblock: inline
name: "Larabay"
level: 11
source: "Monster Core 2"
aon_id: "creature-4460"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4460"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Larabay"
level: "Creature 11"
size: "Medium"
trait_01: "Fey"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +24, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +22, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +19, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +22, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +23"
abilityMods: [2, 6, 3, 4, 4, 7]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/sword/rapier|rapier]]_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +24; __Will__: +21"
hp: 175
health:
  - name: "HP"
    desc: "175; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 10"
speed: "30 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d6+12 piercing, plus mischief"
  - name: "Ranged"
    desc: "⬻ befuddling gaze +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) __Damage__ 2d8+10 mental plus befuddling visions"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The larabay can take on the appearance of a specific Medium or Small humanoid. This removes their fly Speed but doesn't change the attack and damage modifiers with their Strikes."
  - name: "Befuddling Visions"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The larabay's gaze creates disorientation and confusion. A creature hit by befuddling gaze must attempt a Will save."
  - name: "Critical Success"
    desc: "The target is unaffected and temporarily immune to befuddling visions for 1 minute."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] and [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Critical Failure"
    desc: "The target becomes confused for 1 round, and clumsy and dazzled for 1 round afterward."
  - name: "Mischief"
    desc: "⬻"
  - name: "Requirements"
    desc: "The larabay's last action was a successful rapier Strike"
  - name: "Effect"
    desc: "The larabay attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] the creature they hit. They gain a +4 status bonus to the [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check. This attempt neither applies nor counts toward the larabay's multiple attack penalty."
  - name: "Rainbow Flight"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The larabay [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to its [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Fly Speed|fly Speed]], creating a stunning rainbow in its wake. This movement doesn't provoke reactions. Any creature adjacent to the larabay at any point during this movement must attempt a DC 30 Will saving throw to resist staring at the magnificent rainbow. The larabay cannot use Rainbow Flight again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The target is dazzled for 1 round and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1."
  - name: "Critical Failure"
    desc: "The target is dazzled for 1 minute and slowed 2. Feathers Of The Rainbow Larabays love to reward those who entertain them with a gift of a colorful feather. While these feathers are often seen as the calling card of a prankster, the feathers are a worthy gift. When freely given, a larabay's feathers glimmer prismatically, baring colors beyond the spectrum of the rainbow. Other fey recognize the radiant coloration of these feathers and are sometimes willing to exchange great favors for them. However, stealing a larabay's feather, either by plucking it from a larabay or taking it from someone who holds a gifted feather, causes the feather's coloration to fade, reducing it to no more than common down."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]], [[srd/pf2e/compendium/spells/rank-5/illusory-scene|Illusory Scene]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|Cursed Metamorphosis]], [[srd/pf2e/compendium/spells/rank-5/hallucination|Hallucination]]"
sourcebook: "_Monster Core 2_, page 211."
```

```encounter-table
name: Larabay
creatures:
  - 1: Larabay
```
