---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sibyl"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Sibyl"
level: 3
source: "NPC Core"
aon_id: "creature-3443"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3443"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Sibyl"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; lifesense 60 feet"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Diplomacy +9, Occultism +9, Performance +9, Religion +11"
abilityMods: [0, 3, -1, 2, 2, 4]
abilities_top:
  - name: "Induce Awe"
    desc: "The sibyl can use Religion instead of Intimidation to Coerce or Demoralize."
  - name: "Items"
    desc: "bundles of herbs, Dagger"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +8; __Will__: +12"
hp: 40
health:
  - name: "HP"
    desc: "40"
abilities_mid:
  - name: "Foresight"
    desc: "⬲"
  - name: "Trigger"
    desc: "The sibyl becomes the target of a spell with the detection, prediction, revelation, or scrying trait"
  - name: "Effect"
    desc: "The sibyl's oracular awareness alerts them to danger. They gain a +2 circumstance bonus to their saving throw or AC against the spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 (Agile, Finesse, versatile S) __Damage__ 1d4+4 piercing plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning plus 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ dagger +10 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing plus 1d6 spirit"
abilities_bot:
  - name: "Divine Frenzy"
    desc: "⬻ (Concentrate, Divine, Emotion, Mental)"
  - name: "Requirements"
    desc: "The sibyl isn't fatigued or in a frenzy"
  - name: "Effect"
    desc: "The sibyl enters into a divine frenzy that lasts 1 minute. The sibyl can't voluntarily stop frenzying. While in a divine frenzy, the sibyl takes a –2 penalty to Perception checks and Will saves and gains a +2 status bonus to their spell DC and spell attack modifier. During a divine frenzy, the sibyl can't use actions with the concentrate trait unless they're Casting a Spell or Seeking. The frenzy lasts for 1 minute, until the sibyl falls unconscious, or the encounter ends, whichever comes first. The sibyl can't voluntarily end the frenzy."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 19, attack +11 - __Cantrips (2nd)__ Detect Magic, Divine Lance, Guidance, Haunting Hymn, Know the Way - __1st__ Command, Concordant Choir, Fear, Mindlink (4 slots) - __2nd__ Augury, Darkness, Sudden Blight (3 slots) __Oracle Focus Spells 1 Focus Point,__ DC 19 - __2nd__ Brain Drain"
sourcebook: "_NPC Core_, page 30."
```

```encounter-table
name: Sibyl
creatures:
  - 1: Sibyl
```
