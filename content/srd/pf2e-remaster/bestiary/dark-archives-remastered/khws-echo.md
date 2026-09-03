---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "K.H.W.'S Echo"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/medium
statblock: inline
name: "K.H.W.'S Echo"
level: 14
source: "Dark Archives (Remastered)"
aon_id: "creature-4651"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4651"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "DA"
name: "K.H.W.'S Echo"
level: "Creature 14"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unique"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30"
languages: "Common, Tien"
skills:
  - name: "Skills"
    desc: "Acrobatics +28, Arcana +25, Athletics +25, Esoteric Lore +30, Nature +25, Occultism +25, Religion +25"
abilityMods: [4, 5, 4, 5, 5, 8]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +23; __Ref__: +24; __Will__: +28"
hp: 280
health:
  - name: "HP"
    desc: "280"
abilities_mid:
  - name: "Destabilized Form"
    desc: "When the Echo has fewer than 140 Hit Points, his form destabilizes, large chunks disintegrating from his face, limbs, and torso. White moths constantly stream from the missing spaces, creating a 10-foot emanation that deals 6d6 mental damage with a DC 34 basic Will save. As long as the aura persists, he can dissolve into moths and re-form at another location within 15 feet as a free action at the beginning of each of his turns; this has the occult and teleportation traits."
  - name: "Reactive Strike"
    desc: "⬲ The Echo has reach 15 for the purpose of determining when Reactive Strike triggers and when making Reactive Strikes."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rope dart +29 (Disarm, finesse, magical, sweep, tethered, trip) __Damage__ 4d4+13 piercing plus 2d6 mental"
  - name: "Ranged"
    desc: "⬻ rope dart +29 (Disarm, finesse, magical, sweep, tethered, thrown 80 feet, trip) __Damage__ 4d4+13 piercing plus 2d6 mental"
abilities_bot:
  - name: "Astral Spindle Implement"
    desc: "The Echo carries a drop spindle that constantly spins red astral thread, which is both his thaumaturgic implement and weapon. If his rope dart is lost or broken, he can re-form it with an Interact action. If he critically succeeds at a rope dart Strike, overwhelming thoughts and figments flow down the thread into the target's mind. The target becomes confused for 1 round."
  - name: "Astral Thread Control"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The Echo's previous action was a successful thrown rope dart Strike"
  - name: "Effect"
    desc: "The Echo flicks his wrist and makes a follow-up thrown rope dart Strike at a different target within 30 feet of the first target, using the same multiple attack penalty as his previous Strike. Regardless of whether his attack hits, he then retrieves the weapon."
  - name: "Contingency Oathday-Nine-Rova"
    desc: "Frequency__ once per day__ ⭓"
  - name: "Trigger"
    desc: "The Echo's turn begins and he's stunned, slowed, confused, controlled, immobilized, grabbed, paralyzed, restrained, or otherwise can't act"
  - name: "Effect"
    desc: "The Echo has set up numerous contingencies in the event he's compromised. Talismans on his body shatter, counteracting the triggering effect. The Echo can use this free action even if he can't act."
  - name: "Reconstitute from Thought"
    desc: "⬻ (Healing)"
  - name: "Requirements"
    desc: "The Echo is standing on one of the eight large islands of the map, and the island hasn't darkened"
  - name: "Effect"
    desc: "The Echo throws his rope dart into the island and uses it to absorb mental essence from the mindscape, repairing himself. He regains 45 Hit Points and the island turns a desaturated gray for 1 day, preventing future absorption and disabling the call of the void hazard on that island (see text)."
  - name: "Spindle's Web"
    desc: "⬺ The Echo's spindle revolves faster and faster until it's a blur, lashing red threads in every direction. The threads deal 7d6 slashing damage and 7d6 mental damage to all creatures in a 30-foot emanation, with a DC 34 basic Reflex save. If a creature fails its save, the threads awaken the mindscape anchor within it, affecting it differently based on which anchor that creature used to gain access to the center of the mindscape. (If there is a PC who didn't absorb a mindscape anchor, for instance because there are more than four PCs in the party, then use the anchor of the PC closest to them.) The Echo then can't use Spindle's Web for 1d4 rounds. Lantern The lantern outlines the creature with searing revealing light that deals 2d6 persistent fire damage.Mirror The mirror reflects the creature to another location, teleporting them to a clear space within 25 feet of their current location.Chalice The chalice drains life force, granting the Echo temporary HP equal to half the damage dealt.Tome The tome floods the creature's mind with information; the target is slowed 1 for 1 round."
sourcebook: "_Dark Archives (Remastered)_, page 214."
```

```encounter-table
name: K.H.W.'S Echo
creatures:
  - 1: K.H.W.'S Echo
```
