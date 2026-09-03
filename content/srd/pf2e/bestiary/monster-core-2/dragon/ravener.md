---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ravener"
tags:
  - pf2e/creature/level/21
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ravener"
level: 21
source: "Monster Core 2"
aon_id: "creature-4529"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4529"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ravener"
level: "Creature 21"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: "Rare"
trait_05: "Undead"
trait_06: "Unholy"
modifier: 37
perception:
  - name: "Perception"
    desc: "Perception +37; darkvision, scent ([[srd/pf2e/books/player-core/chapter-8-playing-the-game/perception-and-detection#Imprecise Senses|imprecise]]) 60 feet, smoke vision, soulsense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +32, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +39, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +38, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +38, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +40, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +32, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +35"
abilityMods: [9, 5, 9, 5, 6, 8]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder ravener's vision; it ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +38; __Ref__: +34; __Will__: +37 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 500
health:
  - name: "HP"
    desc: "500 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 20"
abilities_mid:
  - name: "Cowering Fear"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 42. A ravener's frightful presence causes creatures to cower in fear as well. As long as a creature is at least [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2 or more as a result of the ravener's frightful presence, it's also [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] from the fear."
  - name: "Soul Ward"
    desc: "An intangible field of necromantic energy protects a ravener from total destruction. This soul ward has 200 Hit Points. Whenever a ravener would be reduced below 1 Hit Point, all damage in excess of what would reduce them to 1 Hit Point is instead dealt to their soul ward. If this damage reduces the soul ward to fewer than 0 Hit Points, the ravener is destroyed. A soul ward's Hit Points can be restored only via specific ravener abilities such as Consume Soul, Void Breath, or vicious criticals. A ravener who goes more than a week without successfully using Consume Soul to feed on a dying creature starves, and their soul ward loses 1d4 Hit Points each day until they feed. If the ravener's soul ward loses all its Hit Points while the ravener still has more than 1 HP, they become a ravener husk."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
  - name: "Discorporate"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Trigger"
    desc: "The ravener takes excess damage to their soul ward but still has at least 51 Hit Points in their soul ward"
  - name: "Effect"
    desc: "The ravener draws deeply into their soul ward, discorporating their body into soul energy to escape. They take 50 damage to their soul ward and their physical body vanishes, reappearing 1d4 hours later in a random location within 1 mile from the location where they used Discorporate."
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d12+13 piercing plus 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]] and 2d6 void"
  - name: "Melee"
    desc: "⬻ horn +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d12+17 slashing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ claw +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d10+13 slashing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ tail +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 4d8+13 slashing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ wing +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d8+13 slashing plus 2d6 void"
abilities_bot:
  - name: "All Becomes Flame"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The ravener curses a creature within 60 feet to have their magic replaced with primordial flames. The creature must attempt a DC 42 Will save. Regardless of the result, the target becomes temporarily immune for 1 day."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/traits/gm-core/cursed|cursed]] for 1 round. While cursed, any spells that the creature casts gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] trait and have their damage type changed to fire damage, regardless of the original damage type or types of the spell. Additionally, any magical items that the cursed target holds or wields are affected in the same manner, such as changing the cold damage of a [[srd/pf2e/compendium/equipment/runes/frost-greater|_frost_]] rune to fire damage. The cursed creature can attempt to temporarily suppress the curse as an action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait. If the creature succeeds a DC 42 Will save, the curse is suppressed until the end of their turn."
  - name: "Failure"
    desc: "As success, but the curse's duration is 1 hour."
  - name: "Critical Failure"
    desc: "As success, but the curse's duration is 1 day, and the DC to suppress the curse increases to DC 44."
  - name: "Consume Soul"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Trigger"
    desc: "A living creature within 30 feet of the ravener dies"
  - name: "Effect"
    desc: "The ravener tears the creature's soul from its body with their maw and gulps it down. The dying creature must attempt a DC 44 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The ravener tears off a small chunk of the creature's soul. If the victim is restored to life, they are [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 in addition to any other side effects of returning to life. The ravener adds a number of Hit Points to their soul ward equal to half the creature's level."
  - name: "Failure"
    desc: "As success, but the creature's soul is ravaged. The creature is drained 3 and the ravener adds a number of Hit Points to their soul ward equal to the creature's level."
  - name: "Critical Failure"
    desc: "As failure, but the ravener devours the entire soul. The victim can't be restored to life as long as the ravener exists except via powerful magic such as a [[srd/pf2e/compendium/spells/rituals/wish|_wish_]] ritual, and the ravener adds a number of Hit Points to their soul ward equal to twice the creature's level."
  - name: "Stoke the Flames"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The ravener intensifies nearby fires. Every foe within 60 feet taking [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]] takes 5d6 fire damage."
  - name: "Void Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) The ravener breathes a blast of necrotic flame that deals 20d6 fire damage plus 4d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent void damage]] (DC 44 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature that fails its save is also [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (or drained 2 on a critical failure). If a creature is drained by the ravener's Void Breath, the ravener's soul ward gains 5 HP. The ravener can't use Void Breath again for 1d4 rounds."
  - name: "Vicious Criticals"
    desc: "The ravener treats an attack roll as a critical hit on a roll of 19 or 20, as long as the attack roll was a success. Additionally, whenever the ravener makes a critical hit with one of their Strikes, the target must succeed at a Fortitude save or gain the [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 condition. If the target already has a drained value of greater than 0, their drained value instead increases by 1, to a maximum of drained 4. Whenever the ravener applies drain to a creature in this way, their soul ward gains 5 Hit Points. Ravener Spellcasters Instead of gaining the vicious criticals ability, a ravener spellcaster gains additional spellcasting prowess. When creating your own ravener spellcaster, give it the spellcasting ability of a spellcaster roughly 2 levels higher than a normal spellcasting dragon of its kind. This typically means that if the original dragon had two spells prepared of its highest rank, you should add one more spell of that rank and then two spells of the next highest rank, while if it had three spells prepared of its highest rank, you would add three spells of the next highest rank (if applicable, add only a single 10th-rank spell). Either way, increase its cantrip rank by 1. If the ravener is unusually young, you might be able to use spells from the relevant dragon spellcasters sidebar, but for a typical ancient dragon, consider the following spells to fill in the new slots, depending on which rank of spells you need. As always, a spellcasting ravener's spells should come from the same tradition as the original dragon. __10th__ [[srd/pf2e/compendium/spells/rank-10/manifestation|_ manifestation_]]__9th__ [[srd/pf2e/compendium/spells/rank-9/massacre|_ massacre_]], [[srd/pf2e/compendium/spells/rank-9/seize-soul|_seize soul_]], [[srd/pf2e/compendium/spells/rank-9/telepathic-demand|_telepathic demand_]]__8th__ [[srd/pf2e/compendium/spells/rank-8/disappearance|_ disappearance_]], [[srd/pf2e/compendium/spells/rank-8/hidden-mind|_hidden mind_]], [[srd/pf2e/compendium/spells/rank-8/quandary|_quandary_]]__7th__ [[srd/pf2e/compendium/spells/rank-7/energy-aegis|_ energy aegis_]], [[srd/pf2e/compendium/spells/rank-7/execute|_execute_]], [[srd/pf2e/compendium/spells/rank-7/spell-riposte|_spell riposte_]]"
sourcebook: "_Monster Core 2_, page 270."
```

```encounter-table
name: Ravener
creatures:
  - 1: Ravener
```
