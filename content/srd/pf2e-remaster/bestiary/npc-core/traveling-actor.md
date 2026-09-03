---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Traveling Actor"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Traveling Actor"
level: 3
source: "NPC Core"
aon_id: "creature-3574"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3574"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Traveling Actor"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common; up to 4 other languages"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +7, Deception +10, Performance +10, Society +9, Theater Lore +9"
abilityMods: [2, 3, 0, 1, 1, 4]
abilities_top:
  - name: "Items"
    desc: "Padded Armor, wooden sword (functions as a light mace)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +12; __Will__: +9"
hp: 35
health:
  - name: "HP"
    desc: "35"
abilities_mid:
  - name: "Dramatic Death"
    desc: "⬲"
  - name: "Trigger"
    desc: "The traveling actor takes any damage"
  - name: "Effect"
    desc: "The traveling actor falls prone and dramatically announces their death. They appear to have died. Anyone who is suspicious of this “death” can Seek to attempt a secret Perception check against the traveling actor's Performance DC. On a success, they see through the ruse."
  - name: "Versatile Performance"
    desc: "The traveling actor can use Performance instead of Diplomacy to Make an Impression and instead of Intimidation to Demoralize."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wooden sword +12 (Agile, Finesse, Shove) __Damage__ 1d4+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Overacted Strike"
    desc: "⬺ (Emotion, Fear, Mental, Visual) The traveling actor puts all their expertise into an attack that strikes fear in those who witness it. The traveling actor Strikes. On a success, the traveling actor chooses another creature within 30 feet who can see the attack, who becomes frightened 1 (or frightened 2 on a critical success)."
sourcebook: "_NPC Core_, page 127."
```

```encounter-table
name: Traveling Actor
creatures:
  - 1: Traveling Actor
```
