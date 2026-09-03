---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "God Caller"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "God Caller"
level: 10
source: "NPC Core"
aon_id: "creature-3542"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3542"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "God Caller"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19"
languages: "Common, Fey; telepathy 100 feet (with eidolon only)"
skills:
  - name: "Skills"
    desc: "Athletics +20, Intimidation +21, Nature +19, Religion +15, Survival +15"
abilityMods: [4, 2, 1, 0, 3, 5]
abilities_top:
  - name: "Bonded Eidolon"
    desc: "The god caller fights alongside a mystical ally called an eidolon, most likely the beast eidolon. The eidolon has the standard number of actions, uses its normal stat block, and counts toward the encounter's XP budget normally. The eidolon must remain within 100 feet of the god caller, or its physical form will dissolve. The god caller can make their eidolon take form or disappear with the Manifest Eidolon action."
  - name: "Items"
    desc: "_+1 explorer's clothing_, _+1 striking war flail_, _wand of environmental endurance_"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +18; __Ref__: +16; __Will__: +19"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _war flail_ +21 (Disarm, Magical, Sweep, Trip) __Damage__ 2d10+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
abilities_bot:
  - name: "Beseech the Spirits"
    desc: "⬻ (Concentrate, Primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The god caller reaches out to local entities for enhanced perception and perspective. The god caller gains lifesense 60 feet and all-around vision for 10 minutes. The god caller can't use this ability again until after propitiating the spirits during their next daily preparation."
  - name: "Manifest Eidolon"
    desc: "⬽ (Concentrate, Manipulate, Primal, Teleportation) The god caller causes their eidolon to manifest in a space adjacent to them if it's unmanifested, or to unmanifest and disappear from physical reality if it was already manifested."
  - name: "Tandem Trick"
    desc: "(Primal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The god caller uses a team tactic with their eidolon, chosen from the following list, with the listed number of actions and traits."
  - name: "Enlarge"
    desc: "⬺ (concentrate, manipulate) The god caller casts _enlarge_ on their eidolon even if the eidolon is beyond range or line of effect. The god caller doesn't need to expend a spell slot, and can choose 2nd or 4th rank."
  - name: "Tandem Strike"
    desc: "⬺ The god caller makes a Strike and their eidolon can Strike as a reaction. Both attacks count toward the god caller's multiple attack penalty, but the penalty doesn't increase until both attacks have been made."
  - name: "Transfer"
    desc: "⬻ The god caller transfers 50 HP from themself to their eidolon or vice versa. If the creature losing HP has 50 HP or fewer, this effect transfers as many HP as possible without reducing that creature below 1 HP."
  - name: "Transpose"
    desc: "⬻ (concentrate, manipulate, teleportation) The god caller and their eidolon teleport to swap places. God Callers And The Divine Some spirits called by god callers of Sarkoris are divine beings capable of granting spells. Consider granting a god caller NPC a cleric focus spell appropriate to one of the god's domains if they worship such a deity (using the same DC and spell attack as their primal spells). For instance, the Stag Mother of the Forest of Stones might grant the _savor the sting_ domain spell from the pain domain."
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 29, attack +21 - __Cantrips (5th)__ Electric Arc, Gouging Claw, Guidance, Light, Tangle Vine - __4th__ Wall of Fire, Weapon Storm (2 slots) - __5th__ Howling Blizzard, Impaling Spike (2 slots)"
sourcebook: "_NPC Core_, page 102."
```

```encounter-table
name: God Caller
creatures:
  - 1: God Caller
```
