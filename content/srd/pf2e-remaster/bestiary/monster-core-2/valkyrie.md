---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Valkyrie"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aesir
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Valkyrie"
level: 12
source: "Monster Core 2"
aon_id: "creature-4017"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4017"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Valkyrie"
level: "Creature 12"
size: "Medium"
trait_01: "Aesir"
trait_02: "Monitor"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "Common, Jotun; ravenspeaker, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +25, Diplomacy +23, Intimidation +23, Religion +22"
abilityMods: [7, 5, 5, 3, 4, 5]
abilities_top:
  - name: "Claimer of the Slain"
    desc: "(concentrate, divine) Valkyries can detect the souls of those recently slain in combat. A valkyrie can spend 10 minutes praying over the body of a creature who has been dead for no more than 12 hours, and if that creature is worthy of becoming an einherji, the valkyrie transforms that creature into an einherji."
  - name: "Ravenspeaker"
    desc: "(divine) Valkyries use ravens as servants and spies. They can speak with ravens, and they can have up to three raven servitors who follow their commands. Valkyries can constantly observe whatever their commanded ravens sense."
  - name: "Items"
    desc: "_+1 resilient breastplate_, _+1 striking returning spear_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +23"
hp: 215
health:
  - name: "HP"
    desc: "215; __Resistances__ electricity 15"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Recall the Fallen"
    desc: "⬲ (divine, healing)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "An allied creature within 60 feet who isn't a construct or undead is reduced to 0 Hit Points, and their dying value is 2 or less; Effect The valkyrie restores 5d10 Hit Points to the target."
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +28 (Magical) __Damage__ 2d6+15 piercing plus 1d12 electricity"
  - name: "Ranged"
    desc: "⬻ _spear_ +26 (Magical, thrown 20 feet) __Damage__ 2d6+15 piercing plus 1d12 electricity"
abilities_bot:
  - name: "Storm of Battle"
    desc: "⬺ (Divine, Electricity) The valkyrie hurls their spear into the air, creating a massive storm in a 100-foot emanation. Spears of lightning rain down upon enemies in the area, dealing 4d12 electricity damage (DC 32 basic Reflex save). Boneyard Advocates While praying to claim a slain warrior, a valkyrie fractures their own consciousness into two parts: mind and soul. They send their mind spinning along the River of Souls to collect and advocate on behalf of the slain warrior's soul. When the prayer ends, the valkyrie reunites their mind and body, and they join the warrior's body and soul into a single form as a new einherji."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __2nd__ Augury - __3rd__ Heroism, Safe Passage - __4th__ Status - __5th__ Infuse Vitality - __6th__ Heal, Heroism - __7th__ Interplanar Teleport (self and mount only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 15."
```

```encounter-table
name: Valkyrie
creatures:
  - 1: Valkyrie
```
