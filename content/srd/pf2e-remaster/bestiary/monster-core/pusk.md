---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pusk"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/small
statblock: inline
name: "Pusk"
level: 2
source: "Monster Core"
aon_id: "creature-2895"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2895"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pusk"
level: "Creature 2"
size: "Small"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Chthonian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +8, Deception +6, Stealth +6"
abilityMods: [4, 0, 4, -3, 0, 0]
abilities_top:
  - name: "Sloth"
    desc: "When a pusk regains their actions, roll 1d4. The pusk regains that many actions for the turn (to a maximum of 3, or 2 if the pusk is a minion). Effects like the slowed condition can further reduce their number of actions."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +4; __Will__: +8"
hp: 36
health:
  - name: "HP"
    desc: "36; __Weaknesses__ cold iron 3, holy 3"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 (Magical, Unholy) __Damage__ 1d8+4 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 (Agile, Magical, Unholy) __Damage__ 1d6+4 slashing"
abilities_bot:
  - name: "Cower"
    desc: "⬻ The pusk makes itself as small as possible, protecting its vital organs with its limbs. It gains a +4 circumstance bonus to AC but takes a –2 penalty to attack rolls. This lasts until the pusk moves from its current space, falls unconscious, or ends the effect as a free action."
  - name: "Frenzied Slashes"
    desc: "⬽ The pusk makes three claw Strikes, each at a –2 penalty, all targeting the same creature. The pusk's multiple attack penalty doesn't increase until after it has made all three attacks. The pusk gains the clumsy 2 condition until the beginning of its next turn."
  - name: "Vicious Criticals"
    desc: "A pusk makes the most of any weakness it finds. Whenever a pusk scores a critical hit with its claw Strike, the target takes an additional 1d6 persistent bleed damage."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16 - __1st__ Fear - __3rd__ Slow"
  - name: "Rituals"
    desc: "DC 16 - __1st__ Demonic Pact"
sourcebook: "_Monster Core_, page 76."
```

```encounter-table
name: Pusk
creatures:
  - 1: Pusk
```
