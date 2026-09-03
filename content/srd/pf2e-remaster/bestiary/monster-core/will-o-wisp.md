---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Will-O'-Wisp"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/air
  - pf2e/creature/trait/small
statblock: inline
name: "Will-O'-Wisp"
level: 6
source: "Monster Core"
aon_id: "creature-3240"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3240"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Will-O'-Wisp"
level: "Creature 6"
size: "Small"
trait_01: "Aberration"
trait_02: "Air"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Aklo, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Deception +12, Intimidation +12, Stealth +16"
abilityMods: [-5, 6, 0, 2, 4, 2]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +10; __Ref__: +16; __Will__: +14"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ magic"
abilities_mid:
  - name: "Glow"
    desc: "(aura, light) 20 feet. A will-o'-wisp is itself naturally invisible, but glows with a colored light, casting bright light in the aura and making it visible."
  - name: "Magic Immunity"
    desc: "A will-o'-wisp is immune to all spells except _force barrage_, _quandary_, and _revealing light_."
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shock +17 (Electricity, Magical) __Damage__ 2d8+4 electricity"
abilities_bot:
  - name: "Feed on Fear"
    desc: "⬻ (Concentrate)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "An enemy within 15 feet is under a fear effect or dying"
  - name: "Effect"
    desc: "The will-o'-wisp feeds on the creature's terror. It regains 2d4 Hit Points, and if it has Gone Dark, its glow reignites."
  - name: "Go Dark"
    desc: "⬻ (Concentrate) The will-o'-wisp extinguishes its glow, becoming invisible. It can end this effect with another use of this action. If it uses its shock attack while invisible, the arc of electricity lets any observer determine its location, making the will-o'-wisp only hidden to all observers until it moves. Eyes of the Dead The elder goddess Nhimbaloth, the so-called “Empty Death,” is said by many to be the source of all will-o'-wisps. Cultists of Nhimbaloth claim she has no true form but is merely a presence that can be felt by all in danger of a pointless and futile death. These same cultists maintain that all will-o'-wisps are Nhimbaloth's eyes, and it's through these fear-devouring creatures that she looks upon all worlds from an eldritch realm beyond even the very concept of death."
sourcebook: "_Monster Core_, page 349."
```

```encounter-table
name: Will-O'-Wisp
creatures:
  - 1: Will-O'-Wisp
```
