---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Conspiracist"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Conspiracist"
level: 0
source: "NPC Core"
aon_id: "creature-3606"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3606"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Conspiracist"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Conspiracy Lore +11, Deception +10, Occultism -1, Performance +10, Society +11"
abilityMods: [0, 2, 0, 3, 0, 4]
abilities_top:
  - name: "Compulsive Liar"
    desc: "The conspiracist can use Deception instead of Diplomacy to Make an Impression or Request. Any creature attempting a Perception check to Sense Motive against the conspiracist gets a result one degree of success worse than they rolled."
  - name: "Social Specialist"
    desc: "For encounters involving deception and social manipulation, the conspiracist is a 4th-level challenge."
  - name: "Items"
    desc: "Signal Whistle, Writing Set"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +4; __Ref__: +6; __Will__: +10"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Evoke Pity"
    desc: "⬲ (auditory, concentrate, emotion, linguistic, mental)"
  - name: "Trigger"
    desc: "An enemy reduces the conspiracist to below half their maximum HP"
  - name: "Effect"
    desc: "The conspiracist begs their assailants to “see reason” and let them live. The conspiracist attempts a single Performance check against the Will DCs of all enemies in a 30-foot emanation. Any creature the attempt succeeds against takes a –2 circumstance penalty to damaging attacks without the nonlethal trait they make against the conspiracist for 10 minutes."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +4 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Sow Doubt"
    desc: "⬺ (Auditory, Concentrate, Emotion, Linguistic, Mental) The conspiracist argues that their enemies have been hoodwinked into attacking them by nefarious powers. The conspiracist attempts a single Deception check against the Will DCs of all enemies that can hear them."
  - name: "Critical Success"
    desc: "The enemy fully believes the conspiracist, becoming stupefied 2 for 1 minute. If the creature was already stupefied 2, they become controlled by the conspiracist until the end of the encounter."
  - name: "Success"
    desc: "The enemy has trouble disbelieving the conspiracist's logic, becoming stupefied 1 for 1 minute. If they're already stupefied 1, they become stupefied 2."
  - name: "Failure"
    desc: "The enemy is unconvinced, but a seed of doubt remains."
  - name: "Critical Failure"
    desc: "The enemy sees through the conspiracist's act, becoming immune to Sow Doubt for 24 hours."
sourcebook: "_NPC Core_, page 152."
```

```encounter-table
name: Conspiracist
creatures:
  - 1: Conspiracist
```
