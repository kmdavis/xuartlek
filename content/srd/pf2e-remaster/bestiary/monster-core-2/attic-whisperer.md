---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Attic Whisperer"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/small
statblock: inline
name: "Attic Whisperer"
level: 4
source: "Monster Core 2"
aon_id: "creature-4090"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4090"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Attic Whisperer"
level: "Creature 4"
size: "Small"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Deception +11, Society +10, Stealth +13"
abilityMods: [0, 5, 0, 2, 4, 3]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +13; __Will__: +12"
hp: 60
health:
  - name: "HP"
    desc: "60 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Aura of Sobs"
    desc: "(auditory, aura, emotion, mental, occult) 10 feet. An attic whisperer enshrouds itself in a tapestry of stolen voices. Each living creature that enters or starts their turn in the aura must succeed at a DC 19 Will save or the unnerving, bitter sobs render them distraught and they become stupefied 1 for as long as they remain within the aura. A creature that succeeds is temporarily immune for 1 hour. The attic whisperer can activate or deactivate the aura with a single action, which has the concentrate trait."
  - name: "Whispered Despair"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature with an active emotion effect enters an attic whisperer's aura of sobs"
  - name: "Effect"
    desc: "The attic whisperer attempts to counteract the emotion effect, with a counteract modifier of +13."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 (Agile, Finesse) __Damage__ 2d8 piercing plus steal breath"
  - name: "Melee"
    desc: "⬻ bony hand (agile +12) __Damage__ 2d10 void plus steal voice"
abilities_bot:
  - name: "Steal Breath"
    desc: "(Curse, Incapacitation, Occult) The attic whisperer siphons the breath from living creatures, sapping their strength. A living creature hit by a jaws Strike must attempt a DC 21 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is enfeebled 1 for 1 round."
  - name: "Failure"
    desc: "The target is enfeebled 1 for 24 hours and fatigued."
  - name: "Critical Failure"
    desc: "The target is enfeebled 1 for 24 hours, fatigued, and falls unconscious."
  - name: "Steal Voice"
    desc: "(Curse, Occult) When an attic whisperer hits a living creature with a bony hand Strike, it tries to pull the victim's voice into its aura. The victim must attempt a DC 21 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target's voice is weak for 1 minute. Anytime it attempts to Cast a Spell or use an action that has the auditory trait, it must succeed at a DC 5 flat check or the action is lost."
  - name: "Failure"
    desc: "The target loses the ability to speak for 1 hour, until the curse is removed, or until the attic whisperer is destroyed, whichever comes first. During this time, the attic whisperer can perfectly mimic the target's voice, and the target takes a –2 circumstance penalty to saving throws against that attic whisperer's aura of sobs."
  - name: "Critical Failure"
    desc: "As failure, but the effects last until the attic whisperer is destroyed or the curse is removed. Varisian Nursery Rhyme _Is the attic whispering? Are we safe below? Do you think he's listening? Is that his shadow? Do you hear him waking, Up above the stairs? Do you hear him weeping? Is he really there? Can you say “I'm speaking?” Are you saying naught? Is it you who's weeping? Is it you he's caught?_"
sourcebook: "_Monster Core 2_, page 47."
```

```encounter-table
name: Attic Whisperer
creatures:
  - 1: Attic Whisperer
```
