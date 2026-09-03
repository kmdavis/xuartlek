---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gosreg"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Gosreg"
level: 11
source: "Monster Core"
aon_id: "creature-2931"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2931"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gosreg"
level: "Creature 11"
size: "Medium"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, thoughtsense 60 feet"
languages: "Aklo, Sakvroth; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Deception +24, Diplomacy +22, Occultism +23, Society +19, Stealth +23"
abilityMods: [3, 6, 3, 6, 5, 7]
abilities_top:
  - name: "Borrow Languages"
    desc: "The gosreg can read and speak all languages known by creatures within range of its telepathy."
  - name: "Thoughtsense"
    desc: "The gosreg senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +18; __Ref__: +23; __Will__: +22 +1 status to all saves vs. magic"
hp: 195
health:
  - name: "HP"
    desc: "195; __Immunities__ confused; __Resistances__ mental 10"
abilities_mid:
  - name: "Unsettled Aura"
    desc: "(aura, mental, occult) 30 feet. Gosregs project a field of discordant energy that unsettles the minds of thinking creatures. Any non-mindless creature within 30 feet of a gosreg takes a –1 status penalty to Will saves."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 (Finesse) __Damage__ 2d10+7 piercing plus 1d10 mental"
  - name: "Melee"
    desc: "⬻ claw +21 (Agile, Finesse) __Damage__ 2d8+7 slashing"
abilities_bot:
  - name: "Broadcast Stance"
    desc: "⬻ (Mental, Occult, Stance)"
  - name: "Requirements"
    desc: "the gosreg is in its natural form"
  - name: "Effect"
    desc: "The gosreg secures its limbs into the ground as its brain-like head crackles with psychic energy. The gosreg's unsettled aura extends to 60 feet, and it blocks all other creatures' telepathy in the aura. Its Mind Bolt can also affect any number of targets in 60 feet. These effects end when the gosreg uses its claw Strike, leaves its space, or is knocked prone."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Occult, Polymorph) The gosreg takes on the appearance of any Small or Medium humanoid. This doesn't change its Speed or attack and damage modifiers with its claw, but it might change the damage type it deals (typically to bludgeoning). It cannot use its jaws Strike while in humanoid form."
  - name: "Mind Bolt"
    desc: "⬺ (Mental, Occult) A gosreg concentrates its field of discordant mental energy and projects it into the mind of one creature within 60 feet. The target takes 6d6 mental damage (DC 30 basic Will save). On a critical failure, the creature is also confused for 1 minute or until it takes damage. Screams in the Void Despite gosregs' years of observation, even they don't know what will happen when they broadcast a psychic beacon. That decision is made by beings far above them. Depending on their superiors' plans, the response may be silence, legions that will arrive in centuries, or a leader of the Dominion teleporting directly to the beacon."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (6th)__ Telekinetic Hand, Telekinetic Projectile - __4th__ Nightmare, Suggestion (×3) - __5th__ Mind Probe, Sending, Subconscious Suggestion, Synaptic Pulse - __6th__ Phantasmal Calamity, Phantom Pain"
sourcebook: "_Monster Core_, page 107."
```

```encounter-table
name: Gosreg
creatures:
  - 1: Gosreg
```
