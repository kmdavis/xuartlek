---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Irnakurse"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Irnakurse"
level: 9
source: "Monster Core"
aon_id: "creature-2998"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2998"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Irnakurse"
level: "Creature 9"
size: "Large"
trait_01: "Aberration"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "Chthonian, Elven, Sakvroth; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +20, Stealth +20"
abilityMods: [5, 5, 3, -2, 3, 4]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +20; __Ref__: +18; __Will__: +16"
hp: 152
health:
  - name: "HP"
    desc: "152"
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (reach 10 feet) __Damage__ 2d12+11 piercing"
  - name: "Melee"
    desc: "⬻ tentacle +20 (Agile, reach 20 feet) __Damage__ 2d8+11 slashing plus mind lash"
abilities_bot:
  - name: "Mind Lash"
    desc: "(Emotion, Mental, Occult) A creature hit by an irnakurse's tentacle is overwhelmed with corrupted images of a ruined life and must succeed at a DC 28 Will save or be stunned 2 (or stunned 4 on a critical failure). After attempting this save, the creature is temporarily immune to mind lash for 24 hours."
  - name: "Soul Scream"
    desc: "⬺ (Auditory, Concentrate, Emotion, Mental, Occult)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The irnakurse unleashes an alien shriek of nightmarish horror and pain. All non-aberration creatures within a 10-foot emanation must attempt a DC 28 Will save. The irnakurse can Sustain Soul Scream for up to 6 rounds; each time it does, it repeats the effect without a new save."
  - name: "Critical Success"
    desc: "The creature is unaffected, and it's temporarily immune to Soul Scream for 24 hours."
  - name: "Success"
    desc: "The creature is stupefied 1 for 1 round."
  - name: "Failure"
    desc: "The creature is stupefied 1. Further failed saves against Soul Scream increase the stupefied value by 1, to a maximum of stupefied 4. Each time the character gets a full night's rest, the stupefied condition gained from Soul Scream decreases by 1."
  - name: "Critical Failure"
    desc: "As failure, except the stupefied value increases by 2 instead of by 1."
  - name: "Storm of Tentacles"
    desc: "⬺ The irnakurse makes up to four tentacle Strikes, each against a different target. These attacks count toward the irnakurse's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all of its attacks."
sourcebook: "_Monster Core_, page 153."
```

```encounter-table
name: Irnakurse
creatures:
  - 1: Irnakurse
```
