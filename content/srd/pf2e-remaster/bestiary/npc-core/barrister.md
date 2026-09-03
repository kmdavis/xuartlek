---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Barrister"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Barrister"
level: -1
source: "NPC Core"
aon_id: "creature-3546"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3546"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Barrister"
level: "Creature -1"
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
    desc: "Deception +10, Diplomacy +12, Legal Lore +13, Performance +10, Society +9"
abilityMods: [0, 1, 1, 3, 2, 4]
abilities_top:
  - name: "Legal Specialist"
    desc: "In a court case or other legal proceeding, the barrister is a 4thlevel challenge."
  - name: "Sway the Judge and Jury"
    desc: "A barrister gains a +2 circumstance bonus to Diplomacy checks to Make an Impression or Request something of the deciding members within a courtroom. If the barrister successfully Performs against a DC of 20 during the 20 minutes prior to the check, they increase the circumstance bonus to +4."
  - name: "Items"
    desc: "court garb (functions as fine clothing), law book (functions as scholarly journal), Writing Set"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +3; __Ref__: +3; __Will__: +12"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +4 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Cite Precedent"
    desc: "⬻ (Auditory, Linguistic) The barrister uses existing case law to undermine their opposition. If they succeed at a DC 20 Legal Lore check, they impose a –2 circumstance penalty on the next Diplomacy check an opponent attempts in a legal argument. Any further attempts to Cite Precedent fail until a new topic with different precedents is being argued."
sourcebook: "_NPC Core_, page 108."
```

```encounter-table
name: Barrister
creatures:
  - 1: Barrister
```
