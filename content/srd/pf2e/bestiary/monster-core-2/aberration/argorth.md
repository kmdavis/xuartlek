---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Argorth"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/huge
statblock: inline
name: "Argorth"
level: 11
source: "Monster Core 2"
aon_id: "creature-4083"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4083"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Argorth"
level: "Creature 11"
size: "Huge"
trait_01: "Aberration"
trait_02: "Mindless"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; bloodsense (precise) 120 feet, no vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +23"
abilityMods: [7, 3, 5, -5, 1, -1]
abilities_top:
  - name: "Bloodsense"
    desc: "The argorth can detect any creature that has a heartbeat, such as most humanoids, or any creature that's consumed blood within 1 week, such as a vampire."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +21; __Will__: +18"
hp: 200
health:
  - name: "HP"
    desc: "200; __Immunities__ mental, visual; __Resistances__ acid 10, cold 10"
abilities_mid:
  - name: "Death Slam"
    desc: "⬲"
  - name: "Trigger"
    desc: "The argorth is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "Before it's knocked out, the argorth makes a tail Strike against a random creature within reach."
speed: "30 feet, burrow 20 feet, climb 20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 (Magical, reach 10 feet) __Damage__ 2d10+13 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +24 (Magical, reach 10 feet) __Damage__ 2d8+13 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ The argorth can only Constrict creatures grabbed by its tail. 2d8+7 bludgeoning, DC 27"
  - name: "Ground Pound"
    desc: "⬺ The argorth rears up its massive bulk and slams it downward with incredible force. Each creature in a 10-foot emanation takes 5d8 bludgeoning damage (DC 27 basic Reflex save). A creature who critically fails this save is also knocked prone."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Large, 2d8+7 bludgeoning, Rupture 24"
  - name: "Unnatural Shriek"
    desc: "⬺ (Auditory, Emotion, Fear, Mental) The argorth emits a terrible howl not of the mortal world. Each non-aberration creature within 120 feet must attempt a DC 30 Will save. Regardless of the result, a creature is temporarily immune to the argorth's Unnatural Shriek for 24 hours."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is stupefied 1 for 1 minute and frightened 2."
  - name: "Critical Failure"
    desc: "The creature is stupefied 2 for 1 minute and frightened 3. Children Of Oblivion Legends of argorths' creation speak of Malcachavka, a dibrasgorth favored of Lamashtu who was unleashed against a city of mortals. Even after every inhabitant was slain and every building razed, Malcachavka continued to rage, chewing and biting her own flesh. Six of her tentacles were severed in the thrashing, each of which continued to writhe of their own accord. In their mindless frenzy and by Lamashtu's blessing, they grew their own maws and legs, becoming the very first argorths."
sourcebook: "_Monster Core 2_, page 40."
```

```encounter-table
name: Argorth
creatures:
  - 1: Argorth
```
