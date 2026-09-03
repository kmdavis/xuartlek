---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drunkard"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Drunkard"
level: 2
source: "NPC Core"
aon_id: "creature-3455"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3455"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Drunkard"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Alcohol Lore +3, Athletics +7, Intimidation +8"
abilityMods: [3, 2, 4, -1, 0, 2]
abilities_top:
  - name: "Items"
    desc: "drunkard's outfit (functions as padded armor), pewter mug"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +8; __Will__: +6"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ pewter mug +8 (thrown 10 feet) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Drunken Flailing"
    desc: "⬻"
  - name: "Requirements"
    desc: "The drunkard is raging"
  - name: "Effect"
    desc: "The drunkard attempts two fist Strikes, each against a different creature."
  - name: "Drunken Rage"
    desc: "⬻ (Concentrate, Emotion, Mental)"
  - name: "Requirements"
    desc: "The drunkard is drunk, and isn't fatigued or raging"
  - name: "Effect"
    desc: "The drunkard flies into a drunken rage. They gain 6 temporary Hit Points that last until the drunken rage ends. While raging, they deal 4 additional damage with melee attacks and take a –1 penalty to AC. The drunkard can't use concentrate actions except Seek. The rage lasts for 1 minute, until the drunkard falls unconscious, or until the drunkard sobers up. The drunkard can't voluntarily stop raging. Once the rage ends, the drunkard can't gain temporary HP from this action for 1 minute."
sourcebook: "_NPC Core_, page 41."
```

```encounter-table
name: Drunkard
creatures:
  - 1: Drunkard
```
