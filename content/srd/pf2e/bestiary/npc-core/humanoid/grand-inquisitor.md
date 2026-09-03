---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grand Inquisitor"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Grand Inquisitor"
level: 15
source: "NPC Core"
aon_id: "creature-3568"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3568"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Grand Inquisitor"
level: "Creature 15"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; (31 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +25, Deception +27, Diplomacy +30, Intimidation +30, Society +28"
abilityMods: [5, 2, 2, 3, 5, 4]
abilities_top:
  - name: "Items"
    desc: "_+2 resilient full plate_, _+2 striking scimitar_, _+2 striking starknife_"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +26; __Ref__: +20 (+23 vs. damaging effects); __Will__: +28"
hp: 215
health:
  - name: "HP"
    desc: "215"
abilities_mid:
  - name: "Searching Gaze"
    desc: "(aura, emotion, fear, mental, visual) 30 feet. When an opponent ends its turn in the aura, it must attempt a DC 36 Will save or it becomes frightened 1 (frightened 2 on a critical failure), and the grand inquisitor learns its surface thoughts (and underlying motive on a critical failure)."
  - name: "Symbol of Loyalty"
    desc: "(aura, emotion, mental, visual) 60 feet. Allies in the aura who are 14th level and lower and are loyal to the grand inquisitor's cause get a +3 status bonus to Will saves."
  - name: "Reactive Strike"
    desc: "⬲ If the grand inquisitor's attack hits and this reaction was triggered by a frightened creature, the triggering action is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +30 (Forceful, Magical, Sweep) __Damage__ 2d6+15 slashing"
  - name: "Melee"
    desc: "⬻ _starknife_ +30 (Agile, deadly d6, Magical, versatile S) __Damage__ 2d4+15 piercing"
  - name: "Melee"
    desc: "⬻ fist +30 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+15 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _starknife_ +27 (Agile, deadly d6, Magical, thrown 20 feet, versatile S) __Damage__ 2d4+15 piercing"
abilities_bot:
  - name: "Condemn"
    desc: "⬻ (Incapacitation, Linguistic) The grand inquisitor Demoralizes. On a success, the target is stunned with a value equal to its frightened condition. __I Am the Law!__ ⬺ (Auditory, Linguistic) The grand inquisitor vows to bring down all the fury of a nation down upon their foes. Up to three lower-level allies within 60 feet of the grand inquisitor can use their reaction to Grapple, Strike, or Trip with a +2 status bonus."
  - name: "Twisting Fear"
    desc: "The grand inquisitor's Strikes deal an extra 3d6 precision damage to frightened creatures."
sourcebook: "_NPC Core_, page 121."
```

```encounter-table
name: Grand Inquisitor
creatures:
  - 1: Grand Inquisitor
```
