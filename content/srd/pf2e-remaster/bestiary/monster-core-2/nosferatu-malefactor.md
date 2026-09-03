---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nosferatu Malefactor"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/vampire
  - pf2e/creature/trait/medium
statblock: inline
name: "Nosferatu Malefactor"
level: 10
source: "Monster Core 2"
aon_id: "creature-4602"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4602"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nosferatu Malefactor"
level: "Creature 10"
size: "Medium"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Vampire"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Aklo, Common, Necril; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Arcana +21, Athletics +19, Deception +17, Intimidation +19, Stealth +23"
abilityMods: [5, 7, 3, 7, 5, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +17; __Ref__: +21; __Will__: +19"
hp: 135
health:
  - name: "HP"
    desc: "135 (fast healing 10, plagued coffin restoration, void healing); __Immunities__ death effects, disease, paralyzed, poison, sleep; __Resistances__ physical 10 (except magical wood)"
abilities_mid:
  - name: "Nosferatu Vulnerabilities"
    desc: ""
  - name: "Revulsion"
    desc: "A nosferatu can't voluntarily come within 10 feet of brandished garlic or a brandished religious symbol of a deity with a holy sanctification option. To brandish garlic or a religious symbol, a creature must Interact to do so for 1 round (similar to Raising a Shield). If the nosferatu involuntarily comes within 10 feet of an object of their revulsion, they gain the fleeing condition, running from the object of their revulsion until they end an action beyond 10 feet. After 1 round of being exposed to the subject of their revulsion, a nosferatu can attempt a DC 25 Will save as a single action, which has the concentrate trait. On a success, they overcome their revulsions for 1d6 rounds (or 1 hour on a critical success)."
  - name: "Stake"
    desc: "A magical wooden stake (such as one affected by a weapon potency rune, runic weapon, or similar magic) driven through the nosferatu's heart drops the nosferatu to 0 HP and prevents them from healing above 0 HP, even in their coffin. Staking a nosferatu requires 3 actions and works only if the nosferatu is unconscious. If the stake is removed, the nosferatu can heal above 0 HP again, and if they're in their coffin, the 1-hour rest period begins once the stake is removed. If the nosferatu's head is severed and anointed with holy water while the stake is in place, the nosferatu is destroyed."
  - name: "Sunlight"
    desc: "If exposed to direct sunlight, a nosferatu immediately becomes slowed 1. The slowed value increases by 1 each time the nosferatu ends their turn in sunlight, and the condition ends when they're no longer in sunlight. If the nosferatu loses all their actions in this way, they're destroyed."
speed: "30 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 (Agile, finesse) __Damage__ 2d10+11 piercing plus plague of ancients"
  - name: "Melee"
    desc: "⬻ fangs +23 (Finesse) __Damage__ 2d12+11 piercing plus Drink Blood"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, divine, polymorph) The nosferatu transforms into a swarm of pale-gray rats. They gain a land Speed of 30 feet and a climb Speed of 10 feet, and they become Large. In this swarm form, the nosferatu can take an action to deal each enemy in the swarm's space 2d10 piercing damage with a DC 29 basic Reflex save. A creature that fails its save is also exposed to plague of ancients (see below)."
  - name: "Command Thrall"
    desc: "⭓ (Auditory, divine, mental)"
  - name: "Requirements"
    desc: "One of the nosferatu's thralls is present and can hear the nosferatu"
  - name: "Effect"
    desc: "The nosferatu gives a single command to one of their thralls, which the thrall follows to the best of its ability during its next turn."
  - name: "Dominate"
    desc: "⬺ (Divine, incapacitation, mental, visual) DC 29. The nosferatu can cast _dominate_ at will as a divine innate spell. Casting it requires staring into the target's eyes, giving the spell the visual trait. A creature that succeeds is temporarily immune to that nosferatu's Dominate for 24 hours. Fully destroying the nosferatu ends the domination, but merely reducing the nosferatu to 0 HP is insufficient to break the spell."
  - name: "Drink Blood"
    desc: "⬻ (Divine)"
  - name: "Requirements"
    desc: "The nosferatu's last action was a successful fangs Strike"
  - name: "Effect"
    desc: "The nosferatu sinks their fangs into the targeted creature to drink its blood. This requires an Athletics check against the creature's Fortitude DC. On a success, the creature becomes drained 1, and the nosferatu regains 13 HP, gaining any excess HP as temporary Hit Points. Drinking Blood from a creature that's already drained doesn't restore any HP to the nosferatu but increases the creature's drained condition value by 1, killing the victim when it reaches drained 5. A nosferatu can also consume blood that's been emptied into a vessel for sustenance, but they gain no HP from doing so. The target creature's drained condition value decreases by 1 per week. A blood transfusion, which requires a successful DC 20 Medicine check and sufficient blood or a blood donor, reduces the drained value by 1 after 10 minutes."
  - name: "Plague of Ancients"
    desc: "(Disease, virulent)"
  - name: "Saving Throw"
    desc: "DC 29 Fortitude"
  - name: "Onset"
    desc: "1 day"
  - name: "Stage 1"
    desc: "drained 1 (1 day)"
  - name: "Stage 2"
    desc: "drained 2 and enfeebled 2 (1 day)"
  - name: "Stage 3"
    desc: "doomed 1, drained 3, and enfeebled 3 (1 day)"
  - name: "Stage 4"
    desc: "doomed 2, drained 3, and enfeebled 3 (1 day)"
  - name: "Stage 5"
    desc: "unconscious (1 day)"
  - name: "Stage 6"
    desc: "death"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __5th__ Telekinetic Haul (×3)"
sourcebook: "_Monster Core 2_, page 341."
```

```encounter-table
name: Nosferatu Malefactor
creatures:
  - 1: Nosferatu Malefactor
```
