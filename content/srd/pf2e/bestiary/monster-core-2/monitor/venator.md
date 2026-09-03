---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Venator"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Venator"
level: 13
source: "Monster Core 2"
aon_id: "creature-4014"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4014"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Venator"
level: "Creature 13"
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, locate target"
languages: "Common, Diabolic, Empyrean, Utopian"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Arcana +23, Athletics +23, Stealth +27, Survival +24"
abilityMods: [6, 8, 4, 4, 5, -2]
abilities_top:
  - name: "Locate Target"
    desc: "(detection, divine) A venator is assigned an individual target or small group of targets when they are created. The venator can sense the direction of their nearest target while on the same plane as it. If there are none, they can sense the plane where most of their targets can be found."
  - name: "Items"
    desc: "_+1 striking crossbow_ (20 bolts)"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +21; __Ref__: +25; __Will__: +24"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ disease, emotion, fear; __Resistances__ electricity 15"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, Magical, versatile S) __Damage__ 3d10+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _crossbow_ +27 (Magical, range increment 120 feet, reload 1) __Damage__ 2d8+12 piercing plus 1d10 electricity and discharging bolt"
abilities_bot:
  - name: "Discharging Bolt"
    desc: "When the venator damages a creature with their crossbow, the bolt embeds in the target, dealing 2d6 persistent electricity damage. The creature can remove the bolt and end the persistent damage with an Interact action but takes 1d6 electricity damage as part of removing the bolt."
  - name: "Mark Target"
    desc: "⬻ (Divine) The venator releases a ball of light at a target within 60 feet, lighting it up with a magical aura that's constantly visible to the venator. The target can avoid becoming marked with a successful DC 30 Reflex save. While marked, the target finds it difficult to deal with the venator and their allies. The target takes a –1 status penalty to all attacks against the venator and other aeons, as well as to saving throws against effects from the venator and other aeons. The venator can Sustain this effect to designate up to 5 other creatures as trusted allies, causing the target to take the same penalties against these allies. The venator can Dismiss the mark. Otherwise, it fades away naturally after 1 day."
  - name: "Overloaded Arc"
    desc: "⬺ (Divine, Electricity) The venator releases lightning from their body in a 120-foot line, dealing 4d10 electricity damage (DC 33 basic Reflex save). The lightning also arcs, damaging any creature embedded with a venator's bolt within 120 feet even if it isn't in the line. The venator is then slowed 1 for 1 round. Censored Secrets Venators kill Norgorber's enemies and clean up his spilled secrets with surprisingly frequency. It seems he's either convinced these aeons of his own importance or directly subverted the axiomites' process from somewhere in his realm beneath the city of Axis."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33 - __2nd__ Invisibility (at will), Revealing Light (at will) - __5th__ Translocate - __7th__ Interplanar Teleport (to plane indicated by locate target only)"
sourcebook: "_Monster Core 2_, page 11."
```

```encounter-table
name: Venator
creatures:
  - 1: Venator
```
