---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nosferatu Overlord"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/vampire
  - pf2e/creature/trait/medium
statblock: inline
name: "Nosferatu Overlord"
level: 15
source: "Monster Core 2"
aon_id: "creature-4603"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4603"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nosferatu Overlord"
level: "Creature 15"
size: "Medium"
trait_01: "Rare"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Vampire"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +29, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +31, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +31"
abilityMods: [6, 8, 4, 8, 6, 4]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +23; __Ref__: +27; __Will__: +29"
hp: 215
health:
  - name: "HP"
    desc: "215 (fast healing 15, void healing, plagued coffin restoration); __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ physical 15 (except magical wood)"
abilities_mid:
  - name: "Air of Sickness"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 30 feet. A creature entering or starting its turn in the aura must attempt a DC 33 Fortitude save. On a failure, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 and takes a –2 status penalty to saves to resist diseases and remove the sickened condition for 1 hour."
  - name: "Nosferatu Vulnerabilities"
    desc: ""
  - name: "Revulsion"
    desc: "A nosferatu can't voluntarily come within 10 feet of brandished garlic or a brandished religious symbol of a deity with a holy sanctification option. To brandish garlic or a religious symbol, a creature must Interact to do so for 1 round (similar to Raising a Shield). If the nosferatu involuntarily comes within 10 feet of an object of their revulsion, they gain the [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] condition, running from the object of their revulsion until they end an action beyond 10 feet. After 1 round of being exposed to the subject of their revulsion, a nosferatu can attempt a DC 25 Will save as a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait. On a success, they overcome their revulsions for 1d6 rounds (or 1 hour on a critical success)."
  - name: "Stake"
    desc: "A magical wooden stake (such as one affected by a weapon potency rune, runic weapon, or similar magic) driven through the nosferatu's heart drops the nosferatu to 0 HP and prevents them from healing above 0 HP, even in their coffin. Staking a nosferatu requires 3 actions and works only if the nosferatu is [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]. If the stake is removed, the nosferatu can heal above 0 HP again, and if they're in their coffin, the 1-hour rest period begins once the stake is removed. If the nosferatu's head is severed and anointed with holy water while the stake is in place, the nosferatu is destroyed."
  - name: "Sunlight"
    desc: "If exposed to direct sunlight, a nosferatu immediately becomes [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1. The slowed value increases by 1 each time the nosferatu ends their turn in sunlight, and the condition ends when they're no longer in sunlight. If the nosferatu loses all their actions in this way, they're destroyed."
speed: "30 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 3d10+12 piercing plus plague of ancients"
  - name: "Melee"
    desc: "⬻ fangs +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 3d12+12 piercing plus Drink Blood"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The nosferatu transforms into a swarm of pale-gray rats. They gain a land Speed of 30 feet and a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Climb Speed|climb Speed]] of 10 feet, and they become Large. In this swarm form, the nosferatu can take an action to deal each enemy in the swarm's space 2d10 piercing damage with a DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. A creature that fails its save is also exposed to plague of ancients (see below)."
  - name: "Command Thrall"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Requirements"
    desc: "One of the nosferatu's thralls is present and can hear the nosferatu"
  - name: "Effect"
    desc: "The nosferatu gives a single command to one of their thralls, which the thrall follows to the best of its ability during its next turn."
  - name: "Dominate"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) DC 36. The nosferatu can cast [[srd/pf2e/compendium/spells/rank-6/dominate|_dominate_]] at will as a divine [[srd/pf2e/books/player-core/chapter-7-spells/innate-spells|innate spell]]. Casting it requires staring into the target's eyes, giving the spell the [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]] trait. A creature that succeeds is temporarily immune to that nosferatu's Dominate for 24 hours. Fully destroying the nosferatu ends the domination, but merely reducing the nosferatu to 0 HP is insufficient to break the spell."
  - name: "Drink Blood"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Requirements"
    desc: "The nosferatu's last action was a successful fangs Strike"
  - name: "Effect"
    desc: "The nosferatu sinks their fangs into the targeted creature to drink its blood. This requires an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the creature's Fortitude DC. On a success, the creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1, and the nosferatu regains 21 HP, gaining any excess HP as [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]]. Drinking Blood from a creature that's already drained doesn't restore any HP to the nosferatu but increases the creature's drained condition value by 1, killing the victim when it reaches drained 5. A nosferatu can also consume blood that's been emptied into a vessel for sustenance, but they gain no HP from doing so. The target creature's drained condition value decreases by 1 per week. A blood transfusion, which requires a successful DC 20 [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check and sufficient blood or a blood donor, reduces the drained value by 1 after 10 minutes."
  - name: "Paralytic Fear"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Requirements"
    desc: "The nosferatu overlord's last action was a successful claw Strike"
  - name: "Effect"
    desc: "The nosferatu drags the target of the Strike close and freezes its mind in terror. The target must attempt a DC 36 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] by fear until the end of the nosferatu's next turn."
  - name: "Failure"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] and takes a –2 circumstance penalty to its Fortitude DC against the nosferatu's Drink Blood ability until the end of the nosferatu's next turn."
  - name: "Critical Failure"
    desc: "As failure, and the target is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2."
  - name: "Plague of Ancients"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/virulent|virulent]])"
  - name: "Saving Throw"
    desc: "DC 36 Fortitude"
  - name: "Onset"
    desc: "1 day"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (1 day)"
  - name: "Stage 2"
    desc: "drained 2 and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 2 (1 day)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1, drained 3, and enfeebled 3 (1 day)"
  - name: "Stage 4"
    desc: "doomed 2, drained 3, and enfeebled 3 (1 day)"
  - name: "Stage 5"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] (1 day)"
  - name: "Stage 6"
    desc: "death"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __8th__ [[srd/pf2e/compendium/spells/rank-5/telekinetic-haul|Telekinetic Haul]] (×3), [[srd/pf2e/compendium/spells/rank-6/vampiric-exsanguination|Vampiric Exsanguination]] (×2)"
sourcebook: "_Monster Core 2_, page 341."
```

```encounter-table
name: Nosferatu Overlord
creatures:
  - 1: Nosferatu Overlord
```
