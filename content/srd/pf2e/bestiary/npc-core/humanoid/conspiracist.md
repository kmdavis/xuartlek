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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Conspiracy Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] -1, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11"
abilityMods: [0, 2, 0, 3, 0, 4]
abilities_top:
  - name: "Compulsive Liar"
    desc: "The conspiracist can use [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] instead of [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]]. Any creature attempting a Perception check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] against the conspiracist gets a result one degree of success worse than they rolled."
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
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "An enemy reduces the conspiracist to below half their maximum HP"
  - name: "Effect"
    desc: "The conspiracist begs their assailants to “see reason” and let them live. The conspiracist attempts a single Performance check against the Will DCs of all enemies in a 30-foot emanation. Any creature the attempt succeeds against takes a –2 circumstance penalty to damaging attacks without the [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] trait they make against the conspiracist for 10 minutes."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Sow Doubt"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The conspiracist argues that their enemies have been hoodwinked into attacking them by nefarious powers. The conspiracist attempts a single [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check against the Will DCs of all enemies that can hear them."
  - name: "Critical Success"
    desc: "The enemy fully believes the conspiracist, becoming [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 2]] for 1 minute. If the creature was already stupefied 2, they become [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]] by the conspiracist until the end of the encounter."
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
