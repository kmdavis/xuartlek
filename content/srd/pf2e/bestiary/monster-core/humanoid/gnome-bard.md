---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnome Bard"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Gnome Bard"
level: 1
source: "Monster Core"
aon_id: "creature-3020"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3020"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gnome Bard"
level: "Creature 1"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
languages: "Common, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Deception +7, Diplomacy +5, Intimidation +7, Performance +7, Stealth +5"
abilityMods: [1, 3, 1, 1, 2, 4]
abilities_top:
  - name: "Items"
    desc: "Dagger, Musical Instrument (handheld), Sling (20 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +9"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Gnomish Shift"
    desc: "⬲ (primal, teleportation)"
  - name: "Trigger"
    desc: "The gnome bard would take damage"
  - name: "Effect"
    desc: "The gnome bard gains resistance 2 to the triggering damage and teleports to an adjacent space."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +8 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Do a Jig"
    desc: "⬻ (Auditory, Incapacitation, Occult, Mental) the gnome bard plays a ditty that inspires dance. One creature within 30 feet must make a Will saving throw DC 19."
  - name: "Success"
    desc: "the target is unaffected."
  - name: "Failure"
    desc: "The target must waste 1 action on its next turn dancing."
  - name: "Critical Failure"
    desc: "The target must waste 2 actions on its next turn dancing."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 19, attack +11 - __Cantrips (1st)__ Courageous Anthem, Daze, Figment, Message, Prestidigitation, Summon Instrument - __1st__ Charm, Command (4 slots)"
sourcebook: "_Monster Core_, page 172."
```

```encounter-table
name: Gnome Bard
creatures:
  - 1: Gnome Bard
```
