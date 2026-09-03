---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Melomach"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/huge
statblock: inline
name: "Melomach"
level: 13
source: "Rage of Elements"
aon_id: "creature-2654"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2654"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Melomach"
level: "Creature 13"
size: "Huge"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Talican"
skills:
  - name: "Skills"
    desc: "Athletics +30, Crafting +21, Intimidation +28, Performance +26"
abilityMods: [9, 4, 9, 0, 2, 7]
abilities_top:
  - name: "Heavy"
    desc: "As long as it is immobile, the elemental can't be forcibly moved or knocked prone. If it takes a move action, it loses this immunity until the start of its next turn."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +23; __Will__: +23"
hp: 292
health:
  - name: "HP"
    desc: "292; __Immunities__ bleed, paralyzed, poison, sleep, sonic; __Resistances__ electricity 15"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +26 (Agile, reach 15 feet, versatile P, versatile S) __Damage__ 3d12+18 bludgeoning"
  - name: "Ranged"
    desc: "⬻ lightning +21 (Electricity, Magical, range 120 feet) __Damage__ 3d10+16 electricity"
abilities_bot:
  - name: "Lightning Punch"
    desc: "⬺ The melomach makes a fist Strike, then makes a lightning Strike against a different creature within 120 feet of the fist Strike's target. Both Strikes count toward the melomach's multiple attack penalty, but it doesn't increase until after both attacks are made."
  - name: "Rhythmic Stomp"
    desc: "⬻ (Emotion, Mental, Primal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The melomach's footsteps raise a clanging sound through their body to create a brief musical phrase. The melomach Strides, then generates the effect of one of the following bard composition cantrips at 7th rank: _allegro_, _dirge of doom_ (adds the fear trait), or _triple time_."
  - name: "Scream"
    desc: "⬺ (Primal, Sonic) The melomach unleashes a guttural, ear-piercing wail. All creatures in a 120-foot cone take 7d12 sonic damage with a DC 32 Fortitude save. The melomach can't Scream again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage, is stunned 1, and is deafened for 1 minute."
  - name: "Critical Failure"
    desc: "The creature takes double damage, is stunned 3, and is deafened permanently. Music of Mass Destruction A melomach's appetite for carnage is matched only by its love of loud noises, particularly the boom of explosions and the shriek of tearing metal. In addition to the sound of their own voices, melomachs are partial to the rapid, discordant strumming and powerful howls that typify the musical stylings typical of the Plane of Metal. Boisterous performances often draw the attention of melomachs."
sourcebook: "_Rage of Elements_, page 159."
```

```encounter-table
name: Melomach
creatures:
  - 1: Melomach
```
